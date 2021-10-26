#menu

import csv

def main_menu():
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
    with open ('userdata.csv','w', newline='') as g:
        fieldnames = ['Name','Age', 'MyKad','Gender','Phone_num','address','postcode','city','state','username','password']
        write_user = csv.DictWriter(g, fieldnames= fieldnames)
        
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
        print(f'Account registered with username : {username}')

elif menu=="2":
    username=str(input("Enter username: "))
    password=str(input("Enter password: "))
    reset_1=str(input("Forgot password (y/n)?: "))
    if reset_1=="y" or reset_1=="Y":
        reset=str(input("Reset password: "))
    else:
        with open('userdata.csv','r') as f:
            read_userpass = csv.DictReader(f)

            for lines in read_userpass():
                details = lines.split(',')
            if username == f.read[9] and (password+'\n') == f.read[10]:
                print(f'Welcome, {username}')
                f.close()
            else:
                print('Username/Password is incorrect.')
                print(main_menu)

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
