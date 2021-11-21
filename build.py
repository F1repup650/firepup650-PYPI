def build():
  import os
  import editor as ed
  os.system("pip install --upgrade pip build twine")
  os.system("clear")
  ed.edit()
  os.system("clear")
  print("Run these commands next: \n  cd package\n  python3 -m build\n  python3 -m twine upload -r pypi dist/*")
# __token__
  os.system("bash")