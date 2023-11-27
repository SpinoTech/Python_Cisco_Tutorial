import subprocess

# 1) for running the sysModulePy.py file from that script and getting output 

#result=subprocess.run(['python','sysModulePy.py'],capture_output=True , text=True)

#print(result.stdout) #for getting the output
#print(result.stderr) #for getting the error




# 2) running shell command using subprocess

#result = subprocess.run(['dir'],shell=True,capture_output=True,text=True) # running a 'dir' command 

#print(result.stdout)


# 3) using very low level method Popen except run :-

#p=subprocess.Popen(['python','--help'],stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)

#output,errors=p.communicate()
#print(output)



# 4) subprocess.call() -> runs a command in a seperate process and wait it to compleate . it return the code of the command as 0 then it's successfull , else failes

#return_code=subprocess.call(['python','--version'])
#if return_code==0:
#    print('command executed succefully')
#else:
#    print('command returns with failed return code ',return_code)



#$NO$ 5) subprocess pipe -> create and interact with child process . creating pipe , allow to communicate between parent and child process .

ls_process=subprocess.Popen(['ls'],stdout=subprocess.PIPE,text=True,shell=True)
grap_process=subprocess.Popen(['grep','sample'],stdin=ls_process.stdout,text=True)

output,errors=grap_process.communicate()
print(output)
print(errors)

