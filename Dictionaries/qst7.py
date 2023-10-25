# 7. What is a shortcut for the following code?

# if 'color' not in spam:
#     spam['color'] = 'black'

spam = {'name': 'Pooka', 'age': 5}
spam.setdefault('color', 'black')
print(spam)