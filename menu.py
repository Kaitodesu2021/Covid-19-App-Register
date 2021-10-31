# *********************************************************
# Program: menu.py
# Course: PSP0101 PROBLEM SOLVING AND PROGRAM DESIGN
# Class: TL1-TL4
# Trimester: 2110
# Year: 2021/22 Trimester 1
# Member_1: 1211103154 | Wan Muhammad Atif bin Taram Satiraksa | 1211103154@student.mmu.edu.my | 011-10255127
# Member_2: 1211103194 | Nur Farahiya Aida binti Abdul Razak | 1211103194@student.mmu.edu.my | 011-51121620
# Member_3: 1211103373 | Muhammad Alif bin Khabali | 1211103373@student.mmu.edu.my | 017-4622108
# Member_4: 1211103097 | Nurul Aqilah binti Mohd Shariff | 1211103097@student.mmu.edu.my | 010-7993211
# *********************************************************
# Task Distribution
# Member_1: Administrator assign appointment, create vaccination center and generate list.
# Member_2: Public user update information and view appointment.
# Member_3: Menu and result display
# Member_4: Account sign up and login authentication.
# *********************************************************


import json
import os

#Open and save user data to userdata.json (if the file doesn't exist, create new one.)
def saveuserdata(data, filename="userdata.json"):
    if os.path.exists("userdata.json"):
        os.remove("userdata.json")   
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

#Open and load information from userdata.json to python 
def openuserdata(filename="userdata.json"):
    if not os.path.exists("userdata.json"):
        userp = []
        saveuserdata(userp) 

    with open(filename, "r") as f:
        data = json.load(f)
        return data

#Open and save admin data to admindata.json (if the file doesn't exist, create new one.)
def saveadmindata(data, filename="admindata.json"):
    if os.path.exists("admindata.json"):
        os.remove("admindata.json")   
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

#Open and load information from admindata.json to python
def openadmindata(filename="admindata.json"):
    if not os.path.exists("admindata.json"):
        adminp = []
        saveuserdata(adminp) 

    with open(filename, "r") as f:
        data = json.load(f)
        return data

#Main menu interface
def main():
    print("""
    ------------------------------------------------------------------------------------
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

#Sign Up function
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
        'password' : password,
        "cv19_status": None ,
        "apptment_data" : None ,
        "apptment_time" : None ,
        "apptment_location" : None,
        "priority_ranking": None, 
        "med_history": None
    } 
    
    userp.append(userinfo)
    saveuserdata(userp)
    print('User has been registered.')
    print('Returning to menu....')
    
    main()
    return

#User Login
def option_2():
    userp = openuserdata()
    username=str(input("Enter username: "))
    password=str(input("Enter password: "))
    
    for f in range(len(userp)):
        if userp[f]['username'] == username and userp[f]['password'] == password:
            print('User logged in successfully')
            #add func for user menu here
            return
    print('Incorrect username/password, please try again.')
    option_2()
    print()
            
        

#Admin Login
def option_3():
    adminp = openadmindata()
    admin_user=str(input("Enter username: "))
    admin_pass=str(input("Enter password: "))
    
    for f in range(len(adminp)):
        if adminp[f]['adminuser'] == admin_user and adminp[f]['adminpass'] == admin_pass:
            print('Admin logged in successfully')
            #add func for admin menu here
            return
    print('Incorrect username/password, please try again.')
    option_3()
    print()

#Exit program
def option_4():
    print("Logged out.")


main()