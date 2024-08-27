import json
import pytest
import os
import glob

rootdir = os.getcwd()
fileList = glob.glob('**/*.ipynb', recursive=True)


def isCodeCell(cell):
    return cell["cell_type"] == "code"


def isTestCell(cell):
    if isinstance(cell["source"], str):
        return ("runtest(" in cell["source"] and
                "def runtest(" not in cell["source"])
    else:
        return any([v for v in cell["source"] if "runtest(" in v and
                    "def runtest(" not in v])


def UID():
    """generate a unique 10 digit ID for notebook cells"""
    import random
    import string
    digits = string.digits + string.ascii_letters
    return (''.join(random.choice(digits) for i in range(12)))


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


def reformatNB(NB):
    """given a notebook in json format, ensure that all outputs are cleared and
    that every cell has a unique ID"""

    for cell in NB["cells"]:
        if not cell["metadata"]:
            cell["metadata"]["id"] = UID()
        if isCodeCell(cell):
            cell["outputs"] = []

    return NB


def constructNB(fname, answers=False):
    with open(fname, 'r') as f:
        template = json.load(f)

    template = reformatNB(template)

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
                if ExpectingCorrect and not all(successes[-2:]):
                    print(cell["source"])
                    print(cell["outputs"][0]["text"])
    return all(successes)


def writeNB(contents, filename):
    with open(filename, 'w') as f:
        f.write(json.dumps(contents))


@pytest.fixture()
def setup(fname):
    directory = os.path.dirname(fname)
    if directory:
        os.chdir(directory)
    yield
    os.chdir(rootdir)


def checkTests(fname):
    directory = os.path.dirname(fname)
    filename = os.path.basename(fname)
    if not os.path.isdir('testsrc'):
        pytest.skip(f"no testing in {directory}")
    else:
        return filename


@pytest.mark.parametrize("fname", fileList)
def test_correct(setup, fname):
    filename = checkTests(fname)
    output = constructNB(filename, answers=True)
    assert checkOutput(output, ExpectingCorrect=True)


@pytest.mark.parametrize("fname", fileList)
def test_incorrect(setup, fname):
    filename = checkTests(fname)
    output = constructNB(filename, answers=False)
    assert checkOutput(output, ExpectingCorrect=False)


if __name__ == "__main__":
    import sys
    output = constructNB(sys.argv[-1], answers=True)
    print(checkOutput(output))
    writeNB(output, filename="completed.ipynb")
    output = constructNB(sys.argv[-1], answers=False)
    writeNB(output, filename="empty.ipynb")
