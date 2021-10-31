#menu


import json
import os

def saveuserdata(data, filename="userdata.json"):
    if os.path.exists("userdata.json"):
        os.remove("userdata.json")   
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)


def openuserdata(filename="userdata.json"):
    if not os.path.exists("userdata.json"):
        userp = []
        saveuserdata(userp) 

    with open(filename, "r") as f:
        data = json.load(f)
        return data

#Main menu interface
def main():
    print("""

    Welcome to Covid-19 Vaccination Registration App.

    User Menu:

    1. Sign up
    2. Log in
    3. Admin Log in
    4. Quit

    """)

    menu=input("Enter number: ")

    if menu == '1':
        option_1()
    elif menu == '2':
        option_2()
    elif menu == '3':
        option_3()
    elif menu == '4':
        option_4()
    else:
        print('Invalid.')
        main()
        return

def option_1():
    userp = openuserdata()
    print("""Create account: 
    """)
    
    name=str(input("Enter full name: "))
    age=int(input("Enter age: "))
    id=int(input("Enter MyKad (without \"-\"): "))
    gender=str(input("Enter gender(Male/Female): "))
    phone=str(input("Enter phone number(without \"-\"): "))
    address=str(input("Enter full address: "))
    postcode=int(input("Enter postcode: "))
    city=str(input("Enter city: "))
    state=str(input("Enter state: "))
    username=str(input("Enter username: "))
    password=str(input("Enter password: "))

    
    userinfo = {
        "names" : name,
        "ages" : age,
        "mykad" : id,
        "gender" : gender,
        "phone" : phone,
        "address" : address,
        'postcode' : postcode,
        'city' : city,
        'state' : state,
        'username' : username,
        'password' : password
    } 
    
    userp.append(userinfo)
    saveuserdata(userp)
    print('User has been registered.')
    print('Returning to menu....')
    main()
    return


def option_2():
    userp = openuserdata()
    username=str(input("Enter username: "))
    password=str(input("Enter password: "))
    
    for f in range(len(userp)):
        if userp[f]['username'] == username and userp[f]['password'] == password:
            print('User logged in successfully')
            return
    print('Incorrect username/password, please try again.')
    option_2()
    print()
            
        

#needs correction
def option_3():
    
    Admin_user=str(input("Enter username: "))
    Admin_pass=str(input("Enter password: "))
    
def option_4():
    print("Logged out.")


main()