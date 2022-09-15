
name = input("Name : ")
surname = input("Surname : ")
gender = input("Gender : ")
accountNo = int(input("Account Number  : "))
password = int(input("Password  : "))

userInfo = {
        "name" : name,
        "surname" : surname,
        "gender" : gender,
        "accountno" : accountNo,
        "password" : password,
        "balance" : 0
    }



def userSigninScreen (accountInfo):
    print("Please Log In")
    while True:
        accountNoCheck = int(input("Please enter your account number : "))
        passwordCheck = int(input("Please enter your password : "))
        
        if accountNoCheck == accountInfo["accountno"] and passwordCheck == accountInfo["password"]:
            print("Log in successful")

            if accountInfo["gender"] == "male" or "Male":
                print(f"Hello Sir {accountInfo['name']}.")
            else : 
                print(f"Hello Lady {accountInfo['name']}")
            break
        else:
            print("Your account number or password is wrong.Please try again!")
            continue


def userMainScreen(balanceInfo):

    while True:
        print("What would you like to do ?Please enter a number : ")
        options = ["1-Withdraw Money","2-Deposit Money","3-Balance Info"]
        print(options)

    
        banking = int(input(" "))
        if banking == 1:
            print(f"You have {balanceInfo['balance']} euro on your balance.")
        
            withdraw = int(input("How much would you like to withdraw ?"))  
            print("Your transaction is pending.Please wait until it finish")
            balanceInfo["balance"]= balanceInfo["balance"] - withdraw
    
            print(f"Your balance at the end of the transaction is {balanceInfo['balance']} euro.")
            
            anotherTrans = int(input("Press 1 to return to the main menu or  press 2 to exit"))
            if anotherTrans == 1 :
                continue
            else:
                print("Have a good day :D")
                break                

           
        elif banking == 2:
            print(f"You have {balanceInfo['balance']} euro on your balance.")
        
            deposit = int(input("How much would you like to deposit ?"))  
            print("Your transaction is pending.Please wait until it finish")
            balanceInfo["balance"] = balanceInfo["balance"] + deposit
        
            print(f"Your balance at the end of the transaction is {balanceInfo['balance']} euro.")
            
            
            anotherTrans = int(input("Press 1 to return to the main menu or  press 2 to exit"))
            if anotherTrans == 1 :
                    continue
            else:
                print("Have a good day :D")
                break  
        
        else:
            print(f"{balanceInfo['name']},You have {balanceInfo['balance']} euro on your balance.")

            anotherTrans = int(input("Press 1 to return to the main menu or  press 2 to exit"))
            if anotherTrans == 1 :
                continue
               
            else:
                print("Have a good day.")
                break

userSigninScreen(userInfo)
userMainScreen(userInfo)
print(userInfo["balance"])



    

