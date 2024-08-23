import json
import pytest
import os


@pytest.fixture(scope="session")
def fname(pytestconfig):
    return pytestconfig.getoption("fname")


def isCodeCell(cell):
    return cell["cell_type"] == "code"


def isTestCell(cell):
    if isinstance(cell["source"], str):
        return ("runtest(" in cell["source"] and
                "def runtest(" not in cell["source"])
    else:
        return any([v for v in cell["source"] if "runtest(" in v and
                    "def runtest(" not in v])


def generateAnswersJSON(fname, notebookname):
    import jupytext
    nb = jupytext.read(fname)
    nb = json.loads(jupytext.writes(nb, fmt="ipynb"))
    separateMainPy = False
    for cell in nb["cells"]:
        if isCodeCell(cell):
            if cell["source"][0].startswith("#NOTEBOOK"):
                separateMainPy = True
    if separateMainPy:
        nb["cells"] = [f for f in nb["cells"]
                       if notebookname in f["source"][0]]
    return nb


def rewriteCodeCell(template, contents, codeCellID):
    for cell in template["cells"]:
        if isCodeCell(cell):
            if cell["metadata"]["id"] == codeCellID:
                cell["source"] = swapCells(cell["source"], contents["source"])
    return template


def extractCodeCellIDs(template):
    targetCells = []
    for ii, cell in enumerate(template["cells"]):
        if isCodeCell(cell):
            if isTestCell(cell):
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
        if current[0].startswith("%%capture"):
            desired = ["%%capture out\n"] + desired
    return desired


def constructNB(fname, answers=False):
    with open(fname, 'r') as f:
        template = json.load(f)

    pltStr = ["import matplotlib.pyplot as plt\nfighand=plt.gca()"]

    codeCellIDs = extractCodeCellIDs(template)
    if answers:
        contents = generateAnswersJSON('main.py', fname)
    else:
        contents = {"cells": [{"source": pltStr} for _ in codeCellIDs]}

    for ID, code in zip(codeCellIDs, contents["cells"]):
        template = rewriteCodeCell(template, code, ID)

    return execute(template)


def checkOutput(contents, ExpectingCorrect=True):
    if ExpectingCorrect:
        we_dont_want = '\x1b[91m'  # red
        we_do_want = '\x1b[92m'    # green
    else:
        we_do_want = '\x1b[91m'    # red
        we_dont_want = '\x1b[92m'  # green

    successes = []
    for cell in contents["cells"]:
        if isCodeCell(cell):
            if isTestCell(cell):
                stdout = cell["outputs"][0]["text"]
                successes.append(we_dont_want not in stdout)
                successes.append(we_do_want in stdout)
    return all(successes)


def writeNB(contents):
    with open('outputDump.ipynb', 'w') as f:
        f.write(json.dumps(contents))


@pytest.mark.skipif(not os.path.isdir('testsrc'), reason="no testing enabled")
def test_correct(fname):
    output = constructNB(fname, answers=True)
    assert checkOutput(output, ExpectingCorrect=True)


@pytest.mark.skipif(not os.path.isdir('testsrc'), reason="no testing enabled")
def test_incorrect(fname):
    output = constructNB(fname, answers=False)
    assert checkOutput(output, ExpectingCorrect=False)


if __name__ == "__main__":
    import sys
    output = constructNB(sys.argv[-1], answers=True)
    writeNB(output)
