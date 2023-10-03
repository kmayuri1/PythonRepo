#19. What does passing re.VERBOSE as the second argument to re.compile() allow you to do?
import re
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?            # area code
    (\s|-|\.)?                    # separator
    \d{3}                         # first 3 digits
    (\s|-|\.)                     # separator
    \d{4}                         # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})?  # extension
    )''', re.VERBOSE)

print(phoneRegex)
print('''to write regular expressions that look nicer and are more readable by allowing you to visually separate
logical sections of the pattern and add comments.''')