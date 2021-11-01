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

def savevac_centerdata(data, filename="vac_center.json"):
    if os.path.exists("vac_center.json"):
        os.remove("vac_center.json")   
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
 
def openvac_centerdata(filename="vac_center.json"):
    if not os.path.exists("vac_center.json"):
        vaca = []
        saveuserdata(vaca) 

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
    medhistory=str(input('Enter your medical history(if not applicable, enter \' - \'): '))
    occupation=str(input('Enter your occupation: '))

    
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
        "cv19_status": '-' ,
        "apptment_data" : '-' ,
        "apptment_time" : '-' ,
        "apptment_location" : '-',
        "priority_ranking": '-', 
        "risk_lvl" : '-',
        "occupation" : occupation,
        "med_history": medhistory
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
    global admin_user
    adminp = openadmindata()
    admin_user=str(input("Enter username: "))
    admin_pass=str(input("Enter password: "))

    
    for f in range(len(adminp)):
        if adminp[f]['adminuser'] == admin_user and adminp[f]['adminpass'] == admin_pass:
            print('Admin logged in successfully')
            admin_menu(admin_user)
            return
    print('Incorrect username/password, please try again.')
    option_3()
    print()

#Exit program
def option_4():
    print("Logged out.")

#admin menu
def admin_menu(admin_user):
    print(f'''Welcome, {admin_user}
    Please select an option from below : 
    1. Categorise users
    2. Add vaccination centers
    3. Appointment setup
    4. Assigned appointments
    
    5. Logout''')

    menu = input('Enter number : ')
    
    if menu == 1:
        categorise_users()
    elif menu == 2:
        add_vac_center()
    elif menu == 3:
        appmt_setup()
    #elif menu == 4: 
        #appmt_assgned()
    else:
        print('Invalid input, please try again.')
        admin_menu()

def categorise_users():
    print('------------------')
    print('Categorise Users')
    print('------------------')

    print('''
    1. Risk Class
    2. Priority Ranking

    3. Return the menu''')

    menu = input('Enter number : ')

    if menu == 1:
        risk_class()
    elif menu == 2:
        prity_rank()
    elif menu == 3:
        admin_menu()
    else:
        print('Invalid input, please try again.')
        categorise_users()
    
def risk_class():
    userp = openuserdata()
    print('''
    ------------------------------
    Assign a user to a risk class
    ------------------------------
    ''')
    print('Name' + '\t\t\t' + 'Age' + '\t\t\t\t' + 'Medical History (if any)')
    print('--------------------------------------------' + '\t\t' + '---------' + '\t\t\t' + '----------------------')
    for i in range(len(userp)):
        names = userp[i]['names']
        age = userp[i]['ages']
        medhistory = userp[i]['med_history']
        print(f'{names}' + '\t\t\t' + f'{age}' + '\t\t\t' + f'{medhistory}')
        print('---------------------------------------------------------------------------------------------------------------------------')

        choose = input('Enter full user name (or x1 return to admin menu): ')
        for i in range(len(userp)):
            if userp[i]['names'] == choose:
                print(f'User record for {names} obtained.')
                choose2 = input('Which class do you want to assign the user?(high/low): ')
                if choose2 == 'high':
                    userp.write() #not sure how to yet
                elif choose2 == 'low':
                    userp.write() #also not sure how to yet
                elif choose2 == 'x1':
                    print('Returning to admin menu.....')
                    admin_menu(admin_user)
                else:
                    print('Invalid input, please try again.')
                    return
            else:
                print('No names matched to said query, please try again.')

def prity_rank():
    userp = openuserdata()
    print('''
    -----------------------------------------
    Assign users to suitable priority ranking
    -----------------------------------------
    ''')
    print('Name' + '\t\t\t' + 'Age' + '\t\t\t\t' + 'Occupation')
    print('-----------------------------------------------------------------------------')
    for i in range(len(userp)):
        names = userp[i]['names']
        age = userp[i]['ages']
        occupation = userp[i]['occupation']
        print(f'{names}' + '\t'+ f'{age}' + '\t\t' + f'{occupation}')
        #to add more


def appmt_setup():
    userp = openuserdata()
    print('''
    -----------------
     Unassigned Users
    -----------------''')
    print('Name' + '\t' + 'ID' + '\t\t' + 'Age' + '\t\t\t' + 'Postcode' + '\t\t\t\t' + 'Risk Level' '\t\t\t\t\t' + 'Priority Rank')
    print('-----------------------------------------------------------------------------------------------------------------------------------------')
    for i in range(len(userp)):
        names = userp[i]['names']
        ID = userp[i]['mykad']
        age = userp[i]['ages']
        postcode = userp[i]['postcode']
        risklvl = userp[i]['risk_lvl']
        prtyrank = userp[i]['priority_ranking']
        print(f'{names}' + '\t' + f'{ID}' + '\t\t' + f'{age}' + '\t\t\t' + f'{postcode}' + '\t\t\t\t' + f'{risklvl}' '\t\t\t\t\t' + f'{prtyrank}')
        #to add more



def add_vac_center():
    vaca = openvac_centerdata()
    print('''
    -----------------------------------------
     Vaccination Centers available currently : 
    -----------------------------------------''')
    print('Name' + '\t' + 'ID' + '\t\t' + 'Age' + '\t\t\t' + 'Postcode' + '\t\t\t\t' + 'Risk Level' '\t\t\t\t\t' + 'Priority Rank')
    print('-----------------------------------------------------------------------------------------------------------------------------------------')
    for i in range(len(vaca)):
        name = vaca[i]['vac_name'] 
        location = vaca[i]['vac_location']
        capacityperhour = vaca[i]['vac_location']
        vaccine = vaca[i]['vac_type']
        print(f'{name}' + '\t' + f'{location}' + '\t\t' + f'{capacityperhour}' + '\t\t\t' + f'{vaccine}')

    q = input('Add new vaccination centre? (y/n): ')
    if q == 'y':
        vac_name=str(input('Enter name of the vaccination center: '))
        vac_location = str(input('Enter address of the vaccination center: '))
        vac_capacity = str(input('Enter capacity/hour of the vaccination center (e.g: 20/hour): '))
        vac_type = str(input('Enter vaccine type (Moderna/Pfizer/CanSino/J&J/AstraZeneca/Sinopharm/Sinovac): '))
        if vac_type != 'Moderna' or 'Pfizer' or 'CanSino' or 'J&J' or 'AstraZeneca' or 'Sinopharm' or 'Sinovac':
            print('No such vaccine available. Please try again.')
            return
        
        add_vacc = {
            "vac_name" : vac_name,
            "vac_location" : vac_location,
            "vac_capacity" : vac_capacity,
            'vac_type' : vac_type
        }

        vaca.append(add_vacc)
        savevac_centerdata(vaca)
        print('New vaccination center has been added.')
        print('Returning to admin menu.....')
        admin_menu(admin_user)

add_vac_center()