# Gries Chapter 10
# 10.1 filebackup
 
file=input('filename???')
new_file=file+'.bak'

backup=open(file,'w')
for line in file:
    backup.write(line)
backup.close()