# *********************************************************
# Program: menu.py
# Course: PSP0101 PROBLEM SOLVING AND PROGRAM DESIGN
# Class: TL1-TL4
# Trimester: 2110
# Year: 2021/22 Trimester 1
# Member_1: 1211103154 | Wan Muhammad Atif bin Taram Satiraksa | 1211103154@student.mmu.edu.my | 011-10255127
# Member_2: 1211103194 | Nur Farahiya Aida binti Abd Razak | 1211103194@student.mmu.edu.my | 011-51121620
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
from types import DynamicClassAttribute
import uuid


#Open and save user data to userdata.json 
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
#Open and save vaccination center data to vac_center.json 
def savevac_centerdata(data, filename="vac_center.json"):
    if os.path.exists("vac_center.json"):
        os.remove("vac_center.json")   
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
 
#Open and load vaccination center data to vac_center.json
def openvac_centerdata(filename="vac_center.json"):
    if not os.path.exists("vac_center.json"):
        vaca = []
        saveuserdata(vaca) 

    with open(filename, "r") as f:
        data = json.load(f)
        return data
#Open and save vaccine center/assigned user data to draftvacuser.json
def savevac_userdata(data, filename=f"draftvacusers.json"):
    if os.path.exists("draftvacusers.json"):
        os.remove("draftvacusers.json")   
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
#Open and load vaccine center/assigned user data to draftvacuser.json
def openvac_userdata(filename="draftvacusers.json"):
    if not os.path.exists("draftvacusers.json"):
        vacusers = []
        saveuserdata(vacusers) 

    with open(filename, "r") as f:
        data = json.load(f)
        return data
#Open and save admin data to admindata.json 
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


#Main menu Interface, with 4 options to choose.
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

#Sign Up function. Request inputs and append all inputted info to userdata.json.
def option_1():
    userp = openuserdata()
    print("""Create account: 
    """)

    name=str(input("Enter full name: "))
    try:
        age=int(input("Enter age: "))
    except Exception:
        pass
        option_1()
    id=str(input("Enter MyKad (without \"-\"): "))
    gender=str(input("Enter gender(Male/Female): "))
    phone=str(input("Enter phone number(without \"-\"): "))
    address=str(input("Enter full address: "))
    postcode=str(input("Enter postcode: "))
    city=str(input("Enter city: "))
    state=str(input("Enter state: "))
    email=str(input('Enter your email: '))
    username=str(input("Enter username: "))
    password=str(input("Enter password: "))
    medhistory=str(input('''Enter your medical history(
        1. Have any cardiovascular diseases, diabetes, chronic respiratory disease, chronic lung disease,chronic kidney disease, asthma, obesity, hyper-tension or cancer
        2. None of the above:  
        :'''))
    global medhistoryInterpretation
    if medhistory=="1":
        medhistoryInterpretation = "MEDICAL HISTORY: CHRONIC DISEASES(HIGH RISK)"
    elif medhistory=="2": 
        medhistoryInterpretation = "NO HIGH RISK HEALTH PROBLEMS"
    else :
        medhistory=str(input('''Enter your medical history(
        1. Have any cardiovascular diseases, diabetes, chronic respiratory disease, chronic lung disease,chronic kidney disease, asthma, obesity, hyper-tension or cancer
        2. None of the above  
        :'''))

    occupation=str(input('Enter your occupation: '))
    uniqueUserID=uuid.uuid4().hex #hex change uuid to string form, eliminate "-"
    confirm = input('Confirm all details? (y/n/x to return to main menu): ')


    if confirm == 'y':
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
            'email' : email,
            'username' : username,
            'password' : password,
            "cv19_status": '-' ,
            "apptment_date" : '-' ,
            "apptment_time" : '-' ,
            "apptment_location" : '-',
            "apptment_location_code" : '-',
            "vaccine_type": '-',
            "priority_ranking": '-', 
            "risk_lvl" : '-',
            "occupation" : occupation,
            "med_history": medhistoryInterpretation,
            "uniqueUserID": uniqueUserID,
            "assignstatus" : False
        } 
        
        userp.append(userinfo)
        saveuserdata(userp)
        print('User has been registered.')
        print('Returning to menu....')
        main()
    elif confirm == 'n':
        option_1()
    elif confirm == 'x':
        main()
    else:
        print('Invalid input, please choose between y, n, or x.')
        option_1()

#User Login. Compare inputted data to saved user data in userdata.json
def option_2(): 
    global public_user
    userp = openuserdata()
    username=str(input("Enter username: "))
    password=str(input("Enter password: "))
    #if password and username match, proceed to public listing page. Userp is the whole data from userdata.json, f is index. 
    for f in range(len(userp)):
        if userp[f]['username'] == username and userp[f]['password'] == password:
            print('User logged in successfully')
            publicListingPage(userp, f)
            return
            
    print('Incorrect username/password, please try again.')
    option_2()
    print()
            
        

#Admin Login. Compare inputted data to saved admin data in admindata.json
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

#Exit program.
def option_4():
    print("Logged out.")
    quit
    return

#Admin menu. Prompts 5 options that admins must choose to proceed.
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
    elif menu == '4': 
        appmt_assgned()
    elif menu == '5':
        main()
    else:
        print('Invalid input, please try again.')
        admin_menu(admin_user)

#Categorise users allow admins to assign users to risk class and priority ranking based on their occupation or health risks.
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

#Assign users to different risk level of high or low based on the users' medical history.
def risk_class():
    userp = openuserdata()
    print('''
    ------------------------------
    Assign a user to a risk class
    ------------------------------
    ''')
    print('Name' + '\t|' + 'Age' + '\t|' + 'Medical History (if any)')
    print('---------------------------------------------------------------------------------------------------------------------------')
    for i in range(len(userp)):
        names = userp[i]['names']
        age = userp[i]['ages']
        medhistory = userp[i]['med_history']
        print(f'{i+1}. '+ f'{names}' + '\t|' + f'{age}' + '\t|' + f'{medhistory}')
    print('---------------------------------------------------------------------------------------------------------------------------')
    try:
        f = int(input('Enter user number (or 0 to return to main menu): '))
    except Exception:
        pass
        print('Please enter a number.')
        risk_class()
    if f == 0:
        print('Returning to main menu....')
        admin_menu(admin_user)
    else:
        pass
    print(f'User record for {userp[f-1]["names"]} obtained.')
    f2 = input('Which class do you want to assign the user?(high/low): ')
    if f2 == 'high':
        userp[f-1]['risk_lvl'] = "High"
        saveuserdata(userp)
        admin_menu(admin_user)
    elif f2 == 'low':
        userp[f-1]['risk_lvl'] = "Low"
        saveuserdata(userp)
        admin_menu(admin_user)
    else:
        print('Invalid input, please try again.')
        risk_class()

#Assign users to different priority rank for vaccination depending on their occupation (Frontliners with the highest while students and children with the lowest priority ranking)       
def prity_rank():
    userp = openuserdata()
    print('''
    -----------------------------------------
    Assign users to suitable priority ranking
    -----------------------------------------
    ''')
    print('Name' + '\t|' + 'Age' + '\t|' + 'Occupation')
    print('-----------------------------------------------------------------------------')
    for g in range(len(userp)):
        names = userp[g]['names']
        age = userp[g]['ages']
        occupation = userp[g]['occupation']
        print(f'{g+1}. ', f'{names}' ,f'{age}' , f'{occupation}')
    print('--------------------------------------------------------------------------------')
    try:
        f = int(input('Input user\'s number: '))
    except Exception:
        pass
        print('Words are not numbers, please try again.')
        prity_rank()
    x = int(input(f'{userp[f-1]["names"]}, Set his priority ranking to (1-5): '))
    if x == 1:
        userp[f-1]['priority_ranking'] = "1"
        saveuserdata(userp)
        admin_menu(admin_user)
    elif x == 2:
        userp[f-1]['priority_ranking'] = "2"
        saveuserdata(userp)
        admin_menu(admin_user)
    elif x == 3:
        userp[f-1]['priority_ranking'] = "3"
        saveuserdata(userp)
        admin_menu(admin_user)
    elif x ==4:
        userp[f-1]['priority_ranking'] = "4"
        saveuserdata(userp)
        admin_menu(admin_user)
    elif x == 5:
        userp[f-1]['priority_ranking'] = "5"
        saveuserdata(userp)
        admin_menu(admin_user)
    else:
        print('Invalid input, please try again.')
        prity_rank()

#Allows admin to setup appointments to users that haven't been assigned to a vaccination centre.
def appmt_setup():
    userp = openuserdata()
    vacusers = openvac_userdata()
    vaca = openvac_centerdata()
    print('''
    -----------------
     Unassigned Users
    -----------------''')
    print('Name' + '\t|' + 'ID' + '\t|' + 'Age' + '\t|' + 'Postcode' + '\t|' + 'Risk Level' '\t|' + 'Priority Rank' + '')
    print('-----------------------------------------------------------------------------------------------------------------------------------------')
    for i in range(len(userp)):
        if userp[i]["assignstatus"] != True:
            names = userp[i]['names']
            IDs = userp[i]['mykad']
            age = userp[i]['ages']
            postcode = userp[i]['postcode']
            risklvl = userp[i]['risk_lvl']
            prtyrank = userp[i]['priority_ranking']
            print(f'{i+1}. ' + f'{names}' + '\t|' + f'{IDs}' + '\t|' + f'{age}' + '\t|' + f'{postcode}' + '\t|' + f'{risklvl}' '\t|' + f'{prtyrank}')
            print('-------------------------------------------------------------------------------------------------------------------------------------')

    try:
        f = int(input('Please input the number of the user (or type in 0 to return to admin menu): '))
    except Exception:
        print('Input is not a number, please try again.')
        appmt_setup()
        pass
    if f == 0:
        print('Returning to main menu....')
        admin_menu(admin_user)
    else:
        pass
    name = userp[f-1]["names"]
    print(f'User record for {name} was obtained.')
    print('-----------------------------------------------------------------------------------------------------------------------------')
    print('Available vaccine centers: ')
    
    
    for i in range(len(vaca)):
        vacnames = vaca[i]['vac_name'] 
        print(f'{i+1}. ' + f'{vacnames}')
    print('-----------------------------------------------------------------------------------------------------------------------------')

    try:
        k = int(input('Enter the number of a vaccine centre: '))
    except Exception:
        pass
        print('Please enter a number.')
        appmt_setup()
    
    vac_center2 = vaca[k-1]["vac_name"]
    for i in range(len(vacusers[k-1][f'vaccine_centre_{vac_center2}'])):
        date = input('Date(DD.MM.YYYY): ')
        time = input('Time(XX:YY(A.M./P.M.)): ')
        vaccine_type = input('Vaccine: ') 
        name = userp[f-1]['names']
        mykad = userp[f-1]['mykad']
        risklvl = userp[f-1]["risk_lvl"]
        thename = f'vaccine_centre_{vac_center2}'
        #Generate unique id for each individual user
        uniqueUserID = userp[f-1]['uniqueUserID']
    

        thename = { 
            "names": name,
            "mykad": mykad,
            "date": date,
            "time": time,
            "risk_lvl": risklvl,
            "rsvp": None,
            "uniqueUserID": uniqueUserID,
            "vaccineCentreCode": k-1,
            "vaccine_type": vaccine_type
        }

        #Assign data to update userdata.json
        userp[f-1]["apptment_date"] = date
        userp[f-1]["apptment_time"] = time
        userp[f-1]["apptment_location"] = vac_center2
        userp[f-1]["apptment_location_code"] = k-1
        userp[f-1]["vaccine_type"] = vaccine_type
        userp[f-1]['assignstatus'] = True

        saveuserdata(userp) 
        vacusers[k-1][f'vaccine_centre_{vac_center2}'].append(thename)
        savevac_userdata(vacusers)
        print('Returning to admin menu......')
        admin_menu(admin_user)

        
#Add new vacccination center. Appends both draftvacusers.json and vac_center.json with appropriate and specific input data from the admin
def add_vac_center():
    vaca = openvac_centerdata()
    vacusers = openvac_userdata()

    print('''
    -----------------------------------------
     Vaccination Centers available currently : 
    -----------------------------------------''')
    print('Name' + '\t|' + 'ID' + '\t|' + 'Age' + '\t|' + 'Postcode' + '\t|' + 'Priority Rank')
    print('-----------------------------------------------------------------------------------------------------------------------------------------')
    for i in range(len(vaca)):
        name = vaca[i]['vac_name'] 
        location = vaca[i]['vac_location']
        capacityperhour = vaca[i]['vac_location']
        vaccine = vaca[i]['vac_type']
        print(f'{name}' + '\t|' + f'{location}' + '\t|' + f'{capacityperhour}' + '\t|' + f'{vaccine}')
    print('-------------------------------------------------------------------------------------------------------------------------------------------')
        

    q = input('Add new vaccination centre? (y/n): ')
    if q == 'y':
        vac_name=str(input('Enter name of the vaccination center: '))
        vac_location = str(input('Enter address of the vaccination center: '))
        vac_capacity = str(input('Enter capacity/hour of the vaccination center (e.g: 20): '))
        vac_type = str(input('Enter vaccine type (Moderna/Pfizer/CanSino/J&J/AstraZeneca/Sinopharm/Sinovac): '))
       

        add_vacc = {
            "vac_name" : vac_name,
            "vac_location" : vac_location,
            "vac_capacity" : vac_capacity,
            'vac_type' : vac_type
        }
        
        add_vacusers = {
            f"vaccine_centre_{vac_name}": [{}]
        }

        vaca.append(add_vacc)
        savevac_centerdata(vaca)
        vacusers.append(add_vacusers)
        savevac_userdata(vacusers)

        print('New vaccination center has been added.')
        print('Returning to admin menu.....')
        admin_menu(admin_user)
    elif q == 'n':
        print('Returning to admin menu....')
        admin_menu(admin_user)
    else:
        print('Invalid input, please try again.')
        add_vac_center()

#Showcase list of assigned users to the admins to check for rsvp 
def appmt_assgned():
    vaca = openvac_centerdata()
    vacusers = openvac_userdata()
    print('''
    ---------------------
    Assigned Appointments 
    ---------------------
    ''')
    print('Vaccination Centers: ')
    for i in range(len(vaca)):
        vac_center =vaca[i]['vac_name']
        print(f'{i+1}. ' + f'{vac_center}')
    print('-------------------------------------------------------------------------------')
    try:
        f = int(input('Select a vaccination center by inputting the number: '))
    except Exception:
        pass
        print('Please enter a number')
        appmt_assgned()

    vac_center2 = vaca[f-1]["vac_name"]
    print(f'Appointments in {vac_center2}')
    print('No.' +'\t|'+ 'Name' +'\t|'+ 'ID' +'\t|'+ 'RSVP' +'\t|'+ 'Risk Level' +'\t|'+ 'Date' +'\t|'+ 'Time')
    print('-------------------------------------------------------------------------------------------------------------------------------------------------')
    w = 0
  
    for test in vacusers[f-1][f'vaccine_centre_{vac_center2}']:
        name = test['names']
        ic = test['mykad']
        rsvp = test['rsvp']
        risk = test['risk_lvl']
        date = test['date']
        time = test['time']
        while True:
            w += 1
            break
        print(f'{w}. ' +'\t|'+ f'{name}' +'\t|'+ f'{ic}' +'\t|'+ f'{rsvp}' +'\t|'+ f'{risk}'+'\t|'+ f'{date}' +'\t|'+ f'{time}' )
    print('----------------------------------------------------------------------------------------------------------------------------------------------')
    print('1. Remove user from assigned list')
    print('2. Return to admin menu')
    print()
    print('-----------------------------------------------------------------------------------------------------------------------------------------------')
    prompt = input('Enter input number: ')
    if prompt == '1':
        print('Remove user from assigned list')
        w=0
        for test in vacusers[f-1][f'vaccine_centre_{vac_center2}']:
            name = test['names']
            while True:
                w += 1
                break
            print(f'{w}. ' + '\t|' + f'{name}' )
        print('-------------------------------------------------')

        try:
            d = int(input('Please input the user number you want to delete: '))
        except Exception:
            pass
            print('Enter a number, please.')
            appmt_assgned()
        
        vacusers[f-1][f'vaccine_centre_{vac_center2}'][d-1].clear()
        savevac_userdata(vacusers)
        print('User has been deleted. Returning to admin menu...')
        admin_menu(admin_user)
        
    elif prompt == "2":
        print('Returning to admin menu.....')
        admin_menu(admin_user)
    else:
        print('Invalid input, please try again.')
        appmt_assgned()

def publicUpdate(userp, f): 
    #let user view and update their personal details
    print(f"""PLEASE CHOOSE WHAT ARE YOU UPDATING=:

        1.NAME : "{userp[f]["names"]}"
        2.AGE : "{userp[f]["ages"]}"
        3.IDENTITY CARD NUMBER : "{userp[f]["mykad"]}"
        4.TELEPHONE NUMBER : "{userp[f]["phone"]}"
        5.USER'S EMAIL : "{userp[f]["email"]}"
        6.ADDRESS : "{userp[f]["address"]}"
        7.POSTCODE : "{userp[f]["postcode"]}"
        8.STATE : "{userp[f]["state"]}"
        9.OCCUPATION : "{userp[f]["occupation"]}"
        10.MEDICAL HISTORY   : "{userp[f]["med_history"]}"
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
        publicUpdate(userp, f)
        
    elif z=="3":
        c=str(input("Enter your identity card number: "))
        userp[f]["mykad"] = c
        publicUpdate(userp, f)

    elif z=="4":
        d=str(input("Enter your telephone number: "))
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
            publicUpdate(userp, f)

        elif k=="2":  
            userp[f]["occupation"] = "NON-FRONTLINER"
            print("Occupation: NON-FRONTLINER")
            publicUpdate(userp, f)

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
        #process input and assign the appropriate string to the users
        if m=="1":
            print("MEDICAL HISTORY: CHRONIC DISEASES(HIGH RISK)")
            userp[f]["med_history"] = "DIAGNOSED WITH CHRONIC DISEASES(HIGH RISK)"
            publicUpdate(userp, f)

        elif m=="2": 
            print("NO HIGH RISK HEALTH PROBLEMS")
            userp[f]["med_history"] = "NO HIGH RISK HEALTH PROBLEMS"
            publicUpdate(userp, f)
     
    elif z=="0":
        publicListingPage(userp, f)
    else:
        print("Invalid")
        breakpoint
    #save to userdata.json
    saveuserdata(userp) 


def publicListingPage(userp, f): 
    #List down all available options for public user

    print("PLEASE SELECT WHAT IS YOUR INTENTION?=:")

    print("1. UPDATE MY INFORMATION")
    print('2. VIEW MY APPOINTMENT DETAILS')
    print('0. RETURN TO MAIN MENU')

    print('---------------------------------------------------------')
    print("THANK YOU FOR CHOOSING, PLEASE WAIT FOR A MOMENT.")

    z=input("Enter your intention  number here: ")

    if z=="1".lower(): #to lowercase --> "xxx".lower()
        publicUpdate(userp, f)

    elif z=="2":
        viewAppointment(userp, f)
    
    elif z=="0":
        main()

    else:
        print("Invalid")
        breakpoint

def viewAppointment(userp, f): 
    #let users view appointment details and rsvp

    #open draftvacusers.json for assigned user data to vaccine centre
    vacusers = openvac_userdata()
    #open vac_center data for list of vaccination center
    vaca = openvac_centerdata()
    print(f"""HI, THIS PAGE IS TO VIEW YOUR APPOINTMENT DETAILS=: /n

    i.  PLACE : {userp[f]["apptment_location"]}
    ii. DATE : '{userp[f]["apptment_date"]}'
    iii.VACCINE : '{userp[f]["vaccine_type"]}'
    iv. TIME : '{userp[f]["apptment_time"]}'
    v.  PLEASE RESPOND TO OUR RSVP?
        IF YES--> A
        IF NO --> B

    0. RETURN TO PREVIOUS PAGE    
    ---------------------------------------------------------
    """)
    #get appointment location code based on user
    k = userp[f]["apptment_location_code"]

    if (k == "-"):
        print("You have not been assigned a vaccine appointment date yet. Thank you for your patience")
        publicListingPage(userp, f)
    else:
        vac_center2 = vaca[k]["vac_name"]
        assignedVaccineCenter = vacusers[k][f'vaccine_centre_{vac_center2}']
        #loop to find match between logged in user and draftvacuser.json
        for i in range(len(assignedVaccineCenter)):
            if assignedVaccineCenter[i]["uniqueUserID"] == userp[f]["uniqueUserID"]:
                z=input("Enter your choice (A/B/0): ")

                if z=="A": 
                    vacusers[k][f'vaccine_centre_{vac_center2}'][i]["rsvp"] = "yes"
                    savevac_userdata(vacusers)
                    publicListingPage(userp, f)
                elif z=="B": 
                    vacusers[k][f'vaccine_centre_{vac_center2}'][i]["rsvp"] = "no"
                    savevac_userdata(vacusers)
                    publicListingPage(userp, f)
                elif z=="0":
                    publicListingPage(userp, f)
                else: 
                    print("INVALID")  
                    publicListingPage(userp, f)

main()