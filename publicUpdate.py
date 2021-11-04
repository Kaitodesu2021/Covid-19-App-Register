# from publicListingPage import publicListingPage

def publicUpdate(): 
    #     print("%d is an integer while %s is a string."%(a,b))
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
        10.CURRENT STATUS
        11.MEDICAL HISTORY  
        0. RETURN TO PREVIOUS PAGE
        ---------------------------------------------------------
        THANK YOU FOR CHOOSING, PLEASE WAIT FOR A MOMENT.""")
    import os 
    # dir_path = os.path.dirname(os.path.realpath(__file__))

    # Opening JSON file
    # f = open(dir_path + '/' + 'data.json')

    z=input("Enter your update number here: ")


    if z=="1".lower(): #to lowercase --> "xxx".lower()
        e=[]
        a=(input("Enter your fullname: " ))
        print(f"Name: {a}")


    elif z=="2":
        e=[]
        b=int(input("Enter your age: "))
        print(f"Age: {b}")

    elif z=="3":
        e=[]
        c=int(input("Enter your identity card number: "))
        print(f"Identity card number:{c} ")

    elif z=="4":
        e=[]
        d=int(input("Enter your telephone number: "))
        print(f"Telephone number:{d}")

    elif z=="5":
        e=[]
        h=input("Enter your email: ")
        print(f"User's email:{h}")

    elif z=="6":
        e=[]
        g=input("Enter your current address: ")
        print(f"Current address: {g}")

    elif z=="7":
        e=[]
        i=int(input("Enter your current postcode: "))
        print(f"Current postcode: {i}")

    elif z=="8":
        e=[]
        j=input("Enter your current state: ")
        print(f"Current state: {j}")

    elif z=="9":
        e=[]
        print("""IF YOU ARE A FROTLINER, PLEASE CHOOSE 1. IF NOT, PLEASE CHOOSE 2):
        1. FRONTLINERS (health-care worker, community services, energy, food and
        transportation, workers, students and etc)
        2. NON-FRONTLINERS 
        """) 

        k=input("Enter your update number here: ")

        if k=="1": 
            e=[]
            print("Occupation: FRONTLINERS")

        elif k=="2":  
            e=[]
            print("Occupation: NON-FRONTLINER")

        else:
            print("Invalid")    


    elif z=="10":
        e=[]
        print("""WHAT IS YOUR CURRENT STATUS AT THE MOMENT?
        1. NORMAL (DID NOT HAVE ANY CONTACT WITH POSITIVE COVID-19 PATIENTS)
        2. BEEN IN CONTACT WITH POSITIVE COVID-19 PATIENT
        3. UNDER QUARANTINE
        """)
        l=input("Enter your number: ")
        
        if l=="1":
            e=[]
            print("CURRENT STATUS: NORMAL(LOW RISK)")

        elif l=="2": 
            e=[]
            print("CURRENT STATUS: BEEN IN CONTACT(MODERATE RISK)")

        elif l=="3": 
            e=[]
            print("CURRENT STATUS: UNDER QUARANTINE(HIGH RISK)")    

        else:
            print("Invalid")


    elif z=="11":
        e=[]
        print("""PLEASE CHOOSE YOUR MEDICAL HISTORY?
        1.Have any cardiovascular diseases, diabetes, chronic respiratory disease, chronic lung disease,
    chronic kidney disease, asthma, obesity, hyper-tension or cancer
        2. Have allergic (seafood,peanuts or etc)
        """)
        m=input("Enter your number: ")
        
        if m=="1":
            e=[]
            print("MEDICAL HISTORY: CHRONIC DISEASES(HIGH RISK)")

        elif m=="2": 
            e=[]
            print("MEDICAL HISTORY: ALLERGIC")
    
        else:
            print("NO HEALTH PROBLEMS")
     
    elif z=="0":
        # publicListing()
        print("test")
        return
    else:
        print("Invalid")
        breakpoint
        #HEYHEYHEY


    # returns JSON object as
    # a dictionary
    # data = json.load(f)

    # Closing file
    # f.close() 
