def build():
  from os import system as cmd
  from editor import edit
  cmd("rm -rf package/dist")
  cmd("mkdir package/dist")
  cmd("poetry update")
  cmd("clear")
  useEditor = input("Run Version Editor (Y|*)?").upper()
  if useEditor == "Y":
    edit()
  cmd("clear")
  print("Run these commands next: \n  cd package\n  python3 -m build\n  python3 -m twine upload -r pypi dist/*")
  cmd("bash")