import shutil
import os

# Make a directory to run tests in
if os.path.isdir("testing"):
    shutil.rmtree('testing')

moduleList = [x for x in os.listdir(".") if os.path.isdir(x) and not x.startswith(".")]

os.mkdir("testing")
os.chdir("testing")


def setup(testdir, dirname):

    shutil.copytree(testdir, dirname)
    answerfile = os.path.join(testdir, ".lesson/answers.py")
    shutil.copyfile(answerfile, dirname + "/main.py")


for modulename in moduleList:
    print("TESTING MODULE", modulename)
    mfile = os.path.join("..", modulename)
    for block in os.listdir(mfile):
        print(">>TESTING ALL EXERICSES IN BLOCK", block)
        bfile = os.path.join(mfile, block)
        for exercise in os.listdir(bfile):
            # Provide some information on what we are testing
            print(">>>>Testing", exercise, "from block",
                  block, "in module ", modulename, end=" : ")
            # Create a path to the directory that holds the stuff
            tdir = os.path.join(bfile, exercise)
            dirname = modulename + "_" + block + "_" + exercise
            setup(tdir, dirname)

            # Change into the relevant directory
            os.chdir(dirname)
            # Now run diagnostic tests for students for this exercise
            if (os.system("bash .lesson/runtest.sh > feedback_log") == 0):
                print("PASSED")
            else:
                print("FAILED")
                os.system("cat feedback_log")
                raise Exception("FAILED TEST")
            # Change out of the relevant directory
            os.chdir("..")

# Remove the directory that tests were run in
os.chdir("..")
shutil.rmtree('testing')
