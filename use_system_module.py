
import sys

sys.stdout.write("Python version: {}\n".format(sys.version) )

sys.stdout.write("Enter anything: ")
sys.stdout.flush()
data_input:str = sys.stdin.readline()

if data_input.strip() == '':
    sys.stderr.write(" - No data entered\n")
    sys.exit(1)

sys.stdout.write("Your input is: {}\n".format(data_input) )

sys.exit(0)