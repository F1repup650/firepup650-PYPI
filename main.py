from os import environ, system
from build import build

system("clear")
joe = system("cat /tmp/updated.txt")
if joe != 0:
    system("./fix.sh")
system("clear")
print("Should be nothing from here")
import package.src.firepup650 as fp

print("Until here")
bob = input("(If owner) Build (Y|*)? ").upper()
system("clear")
if environ["REPL_OWNER"] == "Firepup650" and bob == "Y":
    build()
    exit()
else:
    fp.console.warn("Test Warning")

    fp.e("No demo yet!")
