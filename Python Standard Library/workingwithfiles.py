from pathlib import Path
from time import ctime
import shutil

source = Path("E:\Helloworld/app.py")
target = Path() / "app.py"

shutil.copy(source, target)

# path.exists()
# path.rename("init.txt")
# path.unlink()
# print(ctime(path.stat().st_ctime))

# print(path.read_text())
# path.write_text("....")
# path.write_bytes()
