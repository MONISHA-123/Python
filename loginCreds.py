import json
import re
import os
def checkEmailInFile(email):
    if(os.path.exists("cred.json")):
        f=open('cred.json',"r")
        x=f.read()
        lst=json.loads(x)
        credList=lst["credList"].keys()
        if(email in credList):
            pwd=lst["credList"][email]['password']
            f.close()
            return pwd
        else:
            f.close()
            return False
    else:
        f=open('cred.json','a')
        newDict={
            "credList":{}
        }
        f.write(json.dumps(newDict))
        f.close()
    

def storeCredentialsInFile(email,password):
    f=open('cred.json',"r")
    x=f.read()
    lst=json.loads(x)
    f.close()
    if(lst):
        lst["credList"][email]={"password":password}
        f1=open('cred.json','w')
        newDict=json.dumps(lst)
        f1.write(newDict)
        print("Credential saved successfully !")
        f1.close()
    

def validateEmail(email,flag):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if(re.fullmatch(regex,email)):
        val=checkEmailInFile(email)
        if(flag == 'registration'):
            if(val):
                print("Email already Exist, Try Signing in")
                return 'signIn'
            else:
                return True
        else:
            if(val):
                return val
            else:
                print('Email doesnot exist')
                return False
    else:
        print("Email is not valid")
        return False

def validatePass(email):
    print("Enter the Password","Note : Password must have minimum one special character, one digit, one uppercase, one lowercase character and with minimum length of 6 and maximum length of 15",sep="\n")
    password=input()
    regex=r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#\$%\^&\*]).{6,16}$'
    if(re.fullmatch(regex,password)):
        storeCredentialsInFile(email,password)
        #function to store credentials in a file
    else:
        print("Password is InValid")
        validatePass(email)

def registration():
    print("Enter the Email Id for registration")
    email=input()
    val=validateEmail(email,'registration')
    if(val == 'signIn'):
        login()
    elif(val):
        validatePass(email)
    else:
        registration()
    

def signIn():
    print("Enter the registered Email")
    emailId=input()
    pwd=validateEmail(emailId,'signIn')
    if(pwd):
        print('Enter the password and enter "f" for forgot password')
        inputPwd=input()
        if(inputPwd != 'f'):
            if(pwd == inputPwd):
                print("!!!!!!logged in Successfully!!!!!!!!!")
            else:
                print("Incorrect Password")
                signIn()
        else:
            validatePass(emailId)
    else:
        signIn()

def login():
    print("choose 1 for Registration or 2 for sign in")
    option=int(input())
    if(option== 1):
        registration()
    elif(option == 2):
        signIn()
    else:
        print('Please select proper input value')


login()
