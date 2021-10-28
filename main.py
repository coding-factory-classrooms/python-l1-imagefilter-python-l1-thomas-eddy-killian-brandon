import cli
import sys

args = sys.argv

if args[1] == "--filters":
    cli.f(args[2])
else:
    print("IncorrectArgument : Your argument is trash")

