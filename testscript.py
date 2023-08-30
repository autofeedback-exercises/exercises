import shutil
import os
import subprocess

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
            run = subprocess.Popen(["bash", ".lesson/runtest.sh"], text=True,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)
            output, error = run.communicate()
            ffstring = output[7:]
            if run.returncode == 0:
                print("PASSED")
            else:
                print("FAILED")
                # This fix is temporary until we resolve the hypothesis test issues in AutoFeedback
                if "sampled from the wrong distribution" not in ffstring:
                    print(ffstring)
                    raise Exception("FAILED TEST")
                else:
                    print("FAILED test due to hypothesis test issues")

            # Change out of the relevant directory
            os.chdir("..")

# Remove the directory that tests were run in
os.chdir("..")
shutil.rmtree('testing')
