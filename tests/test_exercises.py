import json
import pytest
import os


@pytest.fixture(scope="session")
def fname(pytestconfig):
    return pytestconfig.getoption("fname")


def generateAnswersJSON(fname):
    import jupytext
    nb = jupytext.read(fname)
    return json.loads(jupytext.writes(nb, fmt='ipynb'))


def rewriteCodeCell(template, contents, codeCellID):
    for cell in template["cells"]:
        if cell["metadata"]["id"] == codeCellID:
            cell["source"] = swapCells(cell["source"], contents["source"])
    return template


def extractCodeCellIDs(template):
    targetCells = []
    for ii, cell in enumerate(template["cells"]):
        if cell["cell_type"] == "code":
            if any([v for v in cell["source"] if "runtest(" in v and
                    "def runtest(" not in v]):
                targetCells.append(template["cells"][ii-1]["metadata"]["id"])
    return targetCells


def execute(contents):
    import nbformat
    from nbconvert.preprocessors import ExecutePreprocessor
    nb_in = nbformat.reads(json.dumps(contents), as_version=4)
    ep = ExecutePreprocessor(timeout=None, allow_errors=False)
    return ep.preprocess(nb_in)[0]


def swapCells(current, desired):
    if current:
        if current[0].startswith("%%output"):
            desired = ["%%output\n"] + desired
    return desired


def constructNB(fname, answers=False):
    with open(fname, 'r') as f:
        template = json.load(f)

    pltStr = "import matplotlib.pyplot as plt\nfighand=plt.gca()"

    codeCellIDs = extractCodeCellIDs(template)
    if answers:
        contents = generateAnswersJSON('main.py')
    else:
        contents = {"cells": [{"source": pltStr} for _ in codeCellIDs]}

    for ID, code in zip(codeCellIDs, contents["cells"]):
        template = rewriteCodeCell(template, code, ID)

    return execute(template)


def checkOutput(contents, ExpectingCorrect=True):
    if ExpectingCorrect:
        we_dont_want = '\x1b[91m'
        we_do_want = '\x1b[92m'
    else:
        we_do_want = '\x1b[91m'
        we_dont_want = '\x1b[92m'

    successes = []
    for cell in contents["cells"]:
        if cell["cell_type"] == "code":
            if cell["source"].startswith("runtest("):
                stdout = cell["outputs"][0]["text"]
                successes.append(we_dont_want not in stdout)
                successes.append(we_do_want in stdout)
    return all(successes)


def writeNB(contents):
    with open('outputDump.ipynb', 'w') as f:
        f.write(json.dumps(contents))


@pytest.mark.skipif(os.path.isfile('skiptest'), reason="marked for skip")
def test_2correct(fname):
    output = constructNB(fname, answers=True)
    assert checkOutput(output, ExpectingCorrect=True)


def test_1incorrect(fname):
    output = constructNB(fname, answers=False)
    assert checkOutput(output, ExpectingCorrect=False)
