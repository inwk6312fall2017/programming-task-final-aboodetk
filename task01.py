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
 print('longest word in book1 is :',l1) 

###for book 2
 for line in file2:
  for word1 in line.split():
   if len(word1)>len(l2):
    l2=word1
 print('longest word in book2 is :',l2)

#for book 3
 for line in file3:
  for word2 in line.split():

   if len(word2)>len(l3):
    l3=word2
 print('longest word in book3 is :',l3)


longest_word()
