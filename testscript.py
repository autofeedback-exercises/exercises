import shutil
import stat
import os

# Make a directory to run tests in
os.mkdir("testing")
os.chdir("testing")

for modulename in os.listdir("..") :
    if modulename=="README.md" or modulename.startswith(".") or modulename=="testscript.py" or modulename=="testing" : continue

    print("TESTING MODULE", modulename )
    mfile = os.path.join("..",modulename)
    for block in os.listdir(mfile) :
        print(">>TESTING ALL EXERICSES IN BLOCK", block )
        bfile = os.path.join(mfile, block)
        for exercise in os.listdir(bfile) :
            # Profide some information on what we are testing
            print(">>>>Testing", exercise, "from block", block, "in module ", modulename, end=" : " )
            # Now make the path to the test file
            tfile = os.path.join(bfile, exercise, ".lesson/test_main.py" )
            # And the path to the solution
            sfile = os.path.join(bfile, exercise, ".lesson/answers.py" )
            # Make a directory to hold the test
            dirname = modulename + "_" + block + "_" + exercise
            os.mkdir(dirname)
            os.mkdir(dirname + "/.lesson")
            # Copy the answers to the test directory
            shutil.copyfile(sfile, dirname + "/main.py" )
            shutil.copyfile(tfile, dirname + "/.lesson/test_main.py" )
            # Change into the relevant directory
            os.chdir(dirname)
            # Now run diagnostic tests for students for this exercise
            os.system("python3 main.py && python3 -m unittest discover -s .lesson -f > feedback_log 2> test_log")
            # Check the test log for any errors
            efile = open("test_log", "r")
            if "FAILED" in efile.read() : 
               print("FAILED")
               os.system("cat feedback_log")
            else :
               print("PASSED")
            efile.close()
            # Change out of the relevant directory
            os.chdir("..") 

# Remove the directory that tests were run in
os.chdir("..")
shutil.rmtree('testing')
