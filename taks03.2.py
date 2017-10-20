#first u have to open the file to do tasks on
file=open("running-config.cfg") # file opened

#create an empty dictionary 
d=dict()


def conf():
###looping through the file
 for line in file:

###only look for access-list words
  line=list(line.split())
###this will divide the line into to list a is the name and type b is the rest details but i did not figure 
#how to put it in a dict
  if "access-list" in line:
   a=line[1:3]
   b=line[3:]
   print(a)
   print(b)

conf()
