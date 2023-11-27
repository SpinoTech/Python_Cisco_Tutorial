# Password Manager :

class BasePasswordManager(): 
    def __init__(self):
        self.old_password={'Parichay':['password','phaldar98734@67'],
                           'raju':['raju@com','raju234'],
                           'sam':['sam@123','98098'],
                           'haripada':['haripada@12389','990908']}
    def get_password(self,user):
        if self.old_password.get(user)==None:
            return "No user available" 
        else:
            return (self.old_password[user])[-1]
    def is_correct(self,user,password):
        if self.get_password(user) == password:
            return "Your password is Correct!" 
        else:
            return "Your password is Incorrect!"


class PasswordManager(BasePasswordManager): 
    def __init__(self):
        super().__init__()
    def set_password(self,user,password):
        if self.old_password.get(user) == None:
            if len(password)>=6: 
                self.old_password[user]=[password]
            else:
                return "The password length is short"
        else:
            if len(password)>=6: 
                var1=self.get_level(self.get_password(user))
                var2=self.get_level(password) 
            if var2>var1:
                self.old_password[user]=[password]
            else:
                return "Password is weak"
    def get_level(self,password):
        if password.isdigit() or password.isalpha():
            return "Your password is Crackable Weak!"
        elif password.isalnum():
            return " password is Moderate!" 
        else:
            return " password is Strong & Good!"


x=PasswordManager()

while(True):
    checker=int(input("\n Press 1 for Checking Password Strength \n Press 2 for Adding New Entity \n Press 3 for Viewing all the Entities \n Press 0 for Exit \n"));
    
    if checker==1 :
        passToCheck=input("Please Provide A Password To Check : ")
        print(f"\n {passToCheck}",x.get_level(passToCheck))
    elif checker==2 :
        newName=input("Enter Your Id : ")
        newPass=input("Enter A New Password : ")
        x.set_password(newName,newPass)
        print("\n New Entity Added Successfully !!! \n")
    elif checker==3 :
        print(f"All {len(x.old_password)} Entities Are : \n",x.old_password)
    elif checker==0 :
        break
    else :
        print("Invalid Choice . Please Re Check Your Choice. Thank You !")
