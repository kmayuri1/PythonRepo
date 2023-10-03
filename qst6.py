#6. Parentheses and periods have specific meanings in regular expression syntax. How would youspecify that you want a regex to match actual parentheses and period characters?

import re

regx=re.compile(r'\(\d\d\)-\d\@')
pattern=regx.search('My nbr is (12)-3@')
print('My nbr with parantheses is :'+pattern.group())