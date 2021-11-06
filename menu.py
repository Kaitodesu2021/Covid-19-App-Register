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

def savevac_userdata(data, filename=f"vac&users.json"):
    if os.path.exists("vac&users.json"):
        os.remove("vac&users.json")   
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
 
def openvac_userdata(filename="vac&users.json"):
    if not os.path.exists("vac&users.json"):
        vacusers = []
        saveuserdata(vacusers) 

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
    global public_user
    userp = openuserdata()
    username=str(input("Enter username: "))
    password=str(input("Enter password: "))
    
    print (userp)
    for f in range(len(userp)):
        if userp[f]['username'] == username and userp[f]['password'] == password:
            print('User logged in successfully')
            #add func for user menu here
            publicListingPage(userp, f)
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
    quit

#admin menu
def admin_menu(admin_user):
    print('-------------------------------------------------------------------------')
    print(f'''
    Welcome, {admin_user}
    Please select an option from below : 
    1. Categorise users
    2. Add vaccination centers
    3. Appointment setup
    4. Assigned appointments
    
    5. Logout
    ''')

    menu = input('Enter number : ')
    
    if menu == '1':
        categorise_users()
    elif menu == '2':
        add_vac_center()
    elif menu == '3':
        appmt_setup()
    #elif menu == 4: 
        #appmt_assgned()
    elif menu == '5':
        main()
    else:
        print('Invalid input, please try again.')
        admin_menu(admin_user)

def categorise_users():
    print('''
        -----------------
        Categorise Users
        -----------------''')
    print('''
    1. Risk Class
    2. Priority Ranking

    3. Return the menu''')

    menu = input('Enter number : ')

    if menu == '1':
        risk_class()
        return
    elif menu == '2':
        prity_rank()
    elif menu == '3':
        admin_menu(admin_user)
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

        choose = input('Enter full user name (or x return to admin menu): ')
        for i in range(len(userp)):
            if userp[i]['names'] == choose:
                print(f'User record for {names} obtained.')
                choose2 = input('Which class do you want to assign the user?(high/low): ')
                if choose2 == 'high':
                    userp[0]['risk_lvl'] = "High"
                    saveuserdata(userp)
                    admin_menu(admin_user)
                elif choose2 == 'low':
                    userp[0]['risk_lvl'] = "Low"
                    saveuserdata(userp)
                    admin_menu(admin_user)
                else:
                    print('Invalid input, please try again.')
                    risk_class()
            elif choose == 'x':
                    print('Returning to admin menu.....')
                    admin_menu(admin_user)
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
    for g in range(len(userp)):
        names = userp[g]['names']
        age = userp[g]['ages']
        occupation = userp[g]['occupation']
        print(f'{names}' + '\t'+ f'{age}' + '\t\t' + f'{occupation}')
        print('--------------------------------------------------------------------------------')
        
        f = input('Input user full name or x to return to admin menu (case-sensitive): ')
        for i in range(len(userp)):
            if f == userp[i]['names']:
                x = input(f'{names}, Set his priority ranking to (1-5): ')
                if x == '1':
                    userp[0]['priority_ranking'] = "1"
                    saveuserdata(userp)
                    admin_menu(admin_user)
                elif x == '2':
                    userp[0]['priority_ranking'] = "2"
                    saveuserdata(userp)
                    admin_menu(admin_user)
                elif x == '3':
                    userp[0]['priority_ranking'] = "3"
                    saveuserdata(userp)
                    admin_menu(admin_user)
                elif x == '4':
                    userp[0]['priority_ranking'] = "4"
                    saveuserdata(userp)
                    admin_menu(admin_user)
                elif x == '5':
                    userp[0]['priority_ranking'] = "5"
                    saveuserdata(userp)
                    admin_menu(admin_user)
                else:
                    print('Invalid input, please try again.')
                    prity_rank()
            elif f == 'x':
                admin_menu(admin_user)
            else:
                print('User does not exist or name have been typed incorrectly, please try again.')
                prity_rank()


def appmt_setup():
    userp = openuserdata()
    print('''
    -----------------
     Unassigned Users
    -----------------''')
    print('Name' + '\t' + 'ID' + '\t\t' + 'Age' + '\t\t\t' + 'Postcode' + '\t\t\t\t' + 'Risk Level' '\t\t\t\t\t' + 'Priority Rank' + '')
    print('-----------------------------------------------------------------------------------------------------------------------------------------')
    for i in range(len(userp)):
        names = userp[i]['names']
        IDs = userp[i]['mykad']
        age = userp[i]['ages']
        postcode = userp[i]['postcode']
        risklvl = userp[i]['risk_lvl']
        prtyrank = userp[i]['priority_ranking']
        print(f'{names}' + '\t' + f'{IDs}' + '\t\t' + f'{age}' + '\t\t\t' + f'{postcode}' + '\t\t\t\t' + f'{risklvl}' '\t\t\t\t\t' + f'{prtyrank}')
        print('-------------------------------------------------------------------------------------------------------------------------------------')

       
        f = input('Please input the name of the user (or type in x to return to admin menu): ')
        print('Available vaccine centers: ')
        with open('newfile', 'w') as z:
            print()
            #placeholder
        

#add new vac center. (open new json file for the vac center containing names of those assigned there)
def add_vac_center():
    vaca = openvac_centerdata()
    print('''
    -----------------------------------------
     Vaccination Centers available currently : 
    -----------------------------------------''')
    print('Name' + '\t' + 'ID' + '\t\t' + 'Age' + '\t\t\t' + 'Postcode' + '\t\t\t\t' + 'Priority Rank')
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
        #if vac_type != 'Moderna' or 'Pfizer' or 'CanSino' or 'J&J' or 'AstraZeneca' or 'Sinopharm' or 'Sinovac':
        #    print('No such vaccine available. Please try again.')

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
    elif q == 'n':
        print('Returning to admin menu....')
        admin_menu(admin_user)
    else:
        print('Invalid input, please try again.')
        add_vac_center()

def appmt_assgned():
    vacusers = openvac_userdata()
    print('''
    ---------------------
    Assigned Appointments 
    ---------------------
    ''')
    print('Vaccination Centers: ')
    for i in range(len(vacusers)):
        vac_center = vacusers[i]['vac_name']
        print(f'{vac_center}')
    
    f = input('Select a vaccination center by inputting the number: ')
    #to be finished

def publicUpdate(userp, f): 
    print("""PLEASE CHOOSE WHAT ARE YOU UPDATING=:

        1.NAME
        2.AGE
        3.IDENTITY CARD NUMBER
        4.TELEPHONE NUMBER
        5.USER'S EMAIL
        6.ADDRESS
        7.POSTCODE
        8.STATE
        9.OCCUPATION
        10.MEDICAL HISTORY  
        0. RETURN TO PREVIOUS PAGE
        ---------------------------------------------------------
        THANK YOU FOR CHOOSING, PLEASE WAIT FOR A MOMENT.""")

    z=input("Enter your update number here: ")

    if z=="1".lower(): #to lowercase --> "xxx".lower()
        a=(input("Enter your fullname: " ))
        userp[f]["names"] = a
        publicUpdate(userp, f)

    elif z=="2":
        b=int(input("Enter your age: "))
        userp[f]["ages"] = b
        
        

    elif z=="3":
        c=int(input("Enter your identity card number: "))
        userp[f]["mykad"] = c
        publicUpdate(userp, f)

    elif z=="4":
        d=int(input("Enter your telephone number: "))
        userp[f]["phone"] = d
        publicUpdate(userp, f)

    elif z=="5":
        h=input("Enter your email: ")
        userp[f]["email"] = h
        publicUpdate(userp, f)

    elif z=="6":
        g=input("Enter your current address: ")
        userp[f]["address"] = g
        publicUpdate(userp, f)

    elif z=="7":
        i=int(input("Enter your current postcode: "))
        userp[f]["postcode"] = i
        publicUpdate(userp, f)

    elif z=="8":
        j=input("Enter your current state: ")
        userp[f]["state"] = j
        publicUpdate(userp, f)

    elif z=="9":
        print("""IF YOU ARE A FRONTLINER, PLEASE CHOOSE 1. IF NOT, PLEASE CHOOSE 2):
        1. FRONTLINERS (health-care worker, community services, energy, food and
        transportation, workers, students and etc)
        2. NON-FRONTLINERS 
        """) 

        k=input("Enter your update number here: ")

        if k=="1": 
            userp[f]["occupation"] = "FRONTLINERS"
            print("Occupation: FRONTLINERS")

        elif k=="2":  
            userp[f]["occupation"] = "NON-FRONTLINER"
            print("Occupation: NON-FRONTLINER")

        else:
            print("Invalid input. Please re-enter")   
            publicUpdate(userp, f) 


    elif z=="10":
        print("""PLEASE CHOOSE YOUR MEDICAL HISTORY?
        1.Have any cardiovascular diseases, diabetes, chronic respiratory disease, chronic lung disease,
    chronic kidney disease, asthma, obesity, hyper-tension or cancer
        2. None of the above
        """)
        m=input("Enter your number: ")
        
        if m=="1":
            print("MEDICAL HISTORY: CHRONIC DISEASES(HIGH RISK)")
            userp[f]["med_history"] = "DIAGNOSED WITH CHRONIC DISEASES(HIGH RISK)"

        elif m=="2": 
            print("NO HIGH RISK HEALTH PROBLEMS")
            userp[f]["med_history"] = "NO HIGH RISK HEALTH PROBLEMS"
     
    elif z=="0":
        # publicListing()
        publicListingPage()
    else:
        print("Invalid")
        breakpoint

    saveuserdata(userp) 


def publicListingPage(userp, f): 

    print("""PLEASE SELECT WHAT IS YOUR INTENTION?=:

    1.UPDATE MY INFORMATIONS
    2.VIEW MY APPOINTMENT DETAILS

    ---------------------------------------------------------
    THANK YOU FOR CHOOSING, PLEASE WAIT FOR A MOMENT.""")

    z=input("Enter your intention  number here: ")

    if z=="1".lower(): #to lowercase --> "xxx".lower()
        publicUpdate(userp, f)

    elif z=="2":
        e=[]
        viewAppointment()

    else:
        print("Invalid")
        breakpoint

def viewAppointment(): 

    print("""HI, THIS PAGE IS TO VIEW YOUR APPOINTMENT DETAILS=:

    i.  PLACE : Austin International Convention Center - AICC
    ii. DATE : 25/11/2021
    iii.VACCINE : PFIZER
    iv. TIME : 8:30 a.m.
    v.  PLEASE RESPOND TO OUR RSVP?
        IF YES--> A
        IF NO --> B

    0. RETURN TO PREVIOUS PAGE    
    ---------------------------------------------------------
    THANK YOU FOR CHOOSING, PLEASE WAIT FOR A MOMENT.""")

    z=input("Enter your choice (A/B/0): ")

    if z=="A": 
        e=[]
        print("THANK YOU FOR ACCEPTING THE VACCINE")

    elif z=="B": 
        e=[]
        print("THANK YOU FOR ANSWERING OUR RSVP. PLEASE STATE A REASON WHY ARE YOU NOT ACCEPTING OUR VACCINE") 
        f=input("PLEASE ENTER YOUR REASONS: ")

    elif z=="0":
        publicListingPage()
    else: 
        print("INVALID")  
        publicUpdate()

main()
