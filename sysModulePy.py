import sys

#printing system level versions
# print("python version-> ",sys.version)
# print("python version information -> ",sys.version_info)


#for getting input :-
#for line in sys.stdin:
#    if 'q'==line.rstrip():
#        break
#    print(f"input: {line}")
#
#print(exit)


#for printing the standard output:-
#sys.stdout.write("hello world")


#for printing the standard error:-
#def print_to_stderror(*a):
#    print(*a,file=sys.stderr)
#
#print_to_stderror("hey parichay")
#
#sys.stderr.write("some error happens tere")


#command line argument:-
#n=len(sys.argv)
#print("total number of args are ",n)
#print('name of the program :- ',sys.argv[0])
#print('arguments passed \n')
#
#for i in range(1,n):
#    print(sys.argv[i])
#
#sum=0
#for i in range(1,n):
#    sum+=int(sys.argv[i])
#print("\n Result :",sum)


#for printing all the sys modules
#print(sys.modules)


#for exiting from the script
age=17
if age<18:
    sys.exit('Age is less than 18')
else:
    print('Age is not less than 18')




