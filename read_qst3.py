# 3. What does Path('C:/Users') / 'Al' evaluate to on Windows?

from pathlib import Path
print(Path('C:/Users') / 'mayur')
print('''Path('C:/Users') / 'mayur'--it belongs to home directory''')