#menu

import csv

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
    name=str(input("Enter name: "))
    age=int(input("Enter age: "))
    id=str(input("Enter MyKad no.: "))
    gender=str(input("Enter gender: "))
    phone=str(input("Enter phone number: "))
    address=str(input("Enter full address: "))
    postcode=str(input("Enter postcode: "))
    city=str(input("Enter city: "))
    state=str(input("Enter state: "))
    username=str(input("Enter username: "))
    password=str(input("Enter password: "))
    with open ('userdata.csv','w', newline='') as f:
        fieldnames = ['Name','Age', 'MyKad','Gender','Phone_num','address','postcode','city','state','username','password']
        write_user = csv.DictWriter(f, fieldnames= fieldnames)
        
        write_user.writeheader()
        write_user.writerow({
            'Name' : name, 
            'Age': age, 
            'MyKad' : id, 
            'Gender' : gender,
            'Phone_num':phone, 
            'address' : address, 
            'postcode':postcode, 
            'city' : city,
            'state' : state, 
            'username' : username, 
            'password': password}
            )
        print(f'Account registered with username : f{username}')
elif menu=="2":
    username=str(input("Enter username: "))
    password=str(input("Enter password: "))
    reset_1=str(input("Forgot password (y/n)?: "))
    if reset_1=="y" or reset_1=="Y":
        reset=str(input("Reset password: "))
    else:
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
        print(f'Admin Registered. Welcome, f{Admin_user}')
#    reset_1=str(input("Forgot password (y/n)?: "))
#    if reset_1=="y" or reset_1=="Y":
#        reset=str(input("Reset password: "))
elif menu=="4":
    print("Logged out.")
else:
    print("Invalid")    
#testagain
#any changes fchcvhvhc dadabjahbdad

#pls test