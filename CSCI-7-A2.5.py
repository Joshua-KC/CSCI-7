#TODO: Write a program that takes a command line parameter with the name of a file of words (such as words.txt) and finds every line that includes all of the vowels (a, e, i, o, and u)
# Think about a function that could help you find what you are looking for.  What is the simplest matching function that would be powerful enough for this task?
# Turn in your program and the list of words that it finds
# Sample usage: % python3 vowels.py words.txt
file = open("D:\\words.txt", "r")
vowels = ['a', 'e', 'i', 'o', 'u']

#for i in file