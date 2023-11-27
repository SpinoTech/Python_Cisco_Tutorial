import os

#get the current working directory

current_dir=os.getcwd()
#print('current working directory is -> ' , current_dir)


files_in_dir=os.listdir()
#print('current list of directory is -> ' , files_in_dir)


# path=r"C:\Users\phaldar\new_os_for_check"
# os.chdir(path)
# print('changed to new dir -> ',os.getcwd)

#creating dir:-
# os.mkdir(r"C:\Users\phaldar\newDir")
# print("directory created")


#removing directory:-
#os.rmdir(r"C:\Users\phaldar\newDir")
#print("directory deleted")

#knowing the size of the file
print(os.name)
size=os.path.getsize("os_module1.py")
print(size)


