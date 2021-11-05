def viewAppointment(): 

    print("""HI, THIS PAGE IS TO VIEW YOUR APPOINTMENT DETAILS=:

    1.PLACE : Austin International Convention Center - AICC
    2.DATE : 25/11/2021
    3.VACCINE : PFIZER
    4.TIME : 8:30 a.m.
    5.PLEASE RESPOND TO OUR RSVP?
        IF YES--> A
        IF NO --> B

    ---------------------------------------------------------
    THANK YOU FOR CHOOSING, PLEASE WAIT FOR A MOMENT.""")

    z=input("Enter your choice (A/B): ")

    if z=="A": 
        e=[]
        print("THANK YOU FOR ACCEPTING THE VACCINE")

    elif z=="B": 
        e=[]
        print("THANK YOU FOR ANSWERING OUR RSVP. PLEASE STATE A REASON WHY ARE YOU NOT ACCEPTING OUR VACCINE") 
        f=input("PLEASE ENTER YOUR REASONS: ")

    else: 
        print("INVALID")  
        

        

