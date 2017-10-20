###first step opening the books
file1=open('Book1.txt')
file2=open('Book2.txt')
file3=open('Book3.txt')

###creating a function 
def longest_word():

###creating an empty string that would be used to have the biggest word
 l1=""
 l2=""
 l3=""
###looping through the Book1
 for line in file1:
  for word in line.split():
###if any word that is bigger than the prev one will be in l1
   if len(word)>len(l1):
    l1=word
 print(l1) 
 for line1 in file2 







longest_word()
