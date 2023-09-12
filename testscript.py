import shutil
import os
import subprocess


def read_command_line():
    from argparse import ArgumentParser as AP

    parser = AP(description="run AutoFeedback on python exercises, using the \
provided solutions (in .lesson/answers.py) to ensure all tests pass")

    parser.add_argument('files', nargs="*",
                        help='list of module directories\
on which to run AutoFeedback')

    args = parser.parse_args()

    if args.files == []:
        moduleList = [x for x in os.listdir(".") if os.path.isdir(x)
                      and not x.startswith(".")]
    else:
        moduleList = args.files
    return moduleList


# Make a directory to run tests in
if os.path.isdir("testing"):
    shutil.rmtree('testing')

moduleList = read_command_line()

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
                if "p-value for the hypothesis test on your" not in ffstring:
                    print(ffstring)
                    raise Exception("FAILED TEST")
                else:
                    for w in ffstring.split() :
                        if w.replace(".","").isnumeric() :
                           startc, endc, err = '\033[91m', '\033[0m', "WARNING: low probability for correct answer. p-value from hypothesis test was " + w
                           print( f"{startc}{err}{endc}")
                           break

            # Change out of the relevant directory
            os.chdir("..")

# Remove the directory that tests were run in
os.chdir("..")
shutil.rmtree('testing')
