###first open the the file
file=open('running-config.cfg')
file1=open('newconfigfile','w')


def replace_ip():
###looping through the file
 for line in file:
#  for word in line.split():

###now only the subinterfaces have the 172 ip so i can just use replace on all file to replace all 172 by 192 
   file1.write(line.replace('172','192'))
 file1.close() 
 file.close()
replace_ip()
