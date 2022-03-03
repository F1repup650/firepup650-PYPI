def build():
  import os
  from editor import edit
  os.system("rm -rf package/dist")
  os.system("mkdir package/dist")
  os.system("pip install --upgrade pip build twine")
  os.system("clear")
  edit()
  os.system("clear")
  print("Run these commands next: \n  cd package\n  python3 -m build\n  python3 -m twine upload -r pypi dist/*")
# __token__
  os.system("bash")