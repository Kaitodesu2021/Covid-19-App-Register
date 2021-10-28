#menu

import csv
import json


print("""

Welcome to Covid-19 Vaccination Registration App.

User Menu:

1. Sign up
2. Log in
3. Admin Log in
4. Log Out 

    """)

menu=input("Enter number: ")

if menu=="1":
    print("""Create account: 
    """)
    
    name=str(input("Enter full name: "))
    age=int(input("Enter age: "))
    id=int(input("Enter MyKad (without \"-\" "))
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
    
    with open ('userdata.json',mode='w') as g:
        json.dump(userinfo, g,indent=2)
    
elif menu=="2":
    username=str(input("Enter username: "))
    password=str(input("Enter password: "))
    reset_1=str(input("Forgot password (y/n)?: "))
    if reset_1=="y" or reset_1=="Y":
        reset=str(input("Reset password: "))
    else:
        with open('userdata.json', mode='r') as g:
            userinfo = json.loads('userdata.json',g)
            for item in userinfo['username']['password']:
                if item == username and item == password:
                    print('Logged in.')
        pass
elif menu=="3":
    Admin_user=str(input("Enter username: "))
    Admin_pass=str(input("Enter password: "))
    with open('admin_data.csv','w', newline ='') as f_adm:
        fieldnames = ['admin_usrname','admin_pass']
        write_admin = csv.DictWriter(f_adm, fieldnames=fieldnames)

        write_admin.writeheader()
        write_admin.writerow({
            'admin_usrname' : Admin_user,
            'admin_pass' : Admin_pass
        })
        print(f'Admin Registered. Welcome, {Admin_user}')
#    reset_1=str(input("Forgot password (y/n)?: "))
#    if reset_1=="y" or reset_1=="Y":
#        reset=str(input("Reset password: "))
elif menu=="4":
    print("Logged out.")
else:
    print("Invalid")    
