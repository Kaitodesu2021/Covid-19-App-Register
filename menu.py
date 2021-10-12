#menu

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
    phone=str(input("Enter phone number: "))
    address=str(input("Enter full address: "))
    username=str(input("Enter username: "))
    password=str(input("Enter password: "))
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
    reset_1=str(input("Forgot password (y/n)?: "))
    if reset_1=="y" or reset_1=="Y":
        reset=str(input("Reset password: "))
elif menu=="4":
    print("Logged out.")
else:
    print("Invalid")    