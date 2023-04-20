import os
from build import build
if os.environ["REPL_OWNER"] == "Firepup650":
  build()
  exit()
else:
  import package.src.firepup650 as fp650
  fp650.e("No demo yet!")