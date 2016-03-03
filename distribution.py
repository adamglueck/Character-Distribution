"""
distribution.py
Author: Adam Glueck
Credit: All of Glen's work, stack overflow

Assignment:  DIstribution O' Characters

Write and submit a Python program (distribution.py) that computes and displays 
the distribution of characters in a given sample of text.

Output of your program should look like this:

Please enter a string of text (the bigger the better): The rain in Spain stays mainly in the plain.
The distribution of characters in "The rain in Spain stays mainly in the plain." is:
iiiiii
nnnnnn
aaaaa
sss
ttt
ee
hh
ll
pp
yy
m
r

Notice about this example:

* The text: 'The rain ... plain' is provided by the user as input to your program.
* Uppercase characters are converted to lowercase
* Spaces and punctuation marks are ignored completely.
* Characters that are more common appear first in the list.
* Where the same number of characters occur, the lines are ordered alphabetically. 
  For example, in the printout above, the letters e, h, l, p and y both occur twice 
  in the text and they are listed in the output in alphabetical order.
* Letters that do not occur in the text are not listed in the output at all.
"""
import string
letters=list(string.ascii_lowercase)
squirrel=[]
text=input("Please enter a string of text (the bigger the better): ")
print("The distribution of characters in "+'"'+text+'"'+" is:")
text=text.lower()
for i in range (0,26):
    squirrel.append(text.count(letters[i]))
letters2=list(string.ascii_lowercase)
squirrel=zip(squirrel,letters2)
final=sorted(squirrel, key=lambda squirrel: (-squirrel[0], squirrel[1]))  
for z in range (1,26):
    print(final[z][0]*final[z][1])