#17. What is the difference between copy.copy() and copy.deepcopy()?

print('''copy.copy(), can be used to make a duplicate copy of a mutable value like a list or dictionary,
If the list you need to copy contains lists, then use the copy.deepcopy() function instead of copy.copy(). The deepcopy() function will copy these inner lists as well.''')