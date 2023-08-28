import unittest
from main import *

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class UnitTests(unittest.TestCase) :

    def test_output(self):
        tname="test_output"
        errmsg="The text printed to screen is not exactly 'Hello World!'. Ensure you have the correct capitalisation and punctuation, and that nothing else is printed."

        import subprocess
        import sys
 
        def run(cmd):
            proc = subprocess.Popen(cmd,
                stdout = subprocess.PIPE,
                )
            stdout = proc.communicate()
 
            return  stdout

        out= run([sys.executable, 'main.py'])
        screen_out=str(out).split("'")[1].strip("\\n")   

        check = screen_out=='Hello World!'

        if not (check):
            print(f"{bcolors.FAIL}{20*'='}\n{tname} has failed. \n{errmsg}\n{20*'='}\n{bcolors.ENDC}")
        else:
            print(f"{bcolors.OKGREEN}{20*'='}\n{tname} has passed!\n{20*'='}\n{bcolors.ENDC}")

        self.assertTrue(check)
