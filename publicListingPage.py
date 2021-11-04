
import json
from publicUpdate import publicUpdate
from viewAppointment import viewAppointment

def publicListingPage(): 
    userdata=[]

    print("""PLEASE SELECT WHAT IS YOUR INTENTION?=:

    1.UPDATE MY INFORMATIONS
    2.VIEW MY APPOINTMENT DETAILS

    ---------------------------------------------------------
    THANK YOU FOR CHOOSING, PLEASE WAIT FOR A MOMENT.""")
    import os 
    dir_path = os.path.dirname(os.path.realpath(__file__))

    # Opening JSON file
    # f = open(dir_path + '/' + 'data.json')

    z=input("Enter your intention  number here: ")

    if z=="1".lower(): #to lowercase --> "xxx".lower()
        e=[]
        publicUpdate()

    elif z=="2":
        e=[]
        viewAppointment()

    else:
        print("Invalid")
        breakpoint

publicListingPage()    

    # returns JSON object as
    # a dictionary
    # data = json.load(f)
    
    # Closing file
    # f.close() 



 
# Iterating through the json
# list
#for i in data['emp_details']:
    #print(i)
 
