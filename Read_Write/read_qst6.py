# 6. What are the . and .. folders?

from pathlib import Path
print(Path.cwd().is_absolute())
print(''''.' belongs to current diectory and '..' belongs to parent directory.''')
