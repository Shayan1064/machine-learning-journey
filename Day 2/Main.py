print("This is Day 2")

name=input("Enter Name: ")
if(name=='Sara'):
    print("Girl name")
else:
    print("Boy name")
    

name=input("Enter Your Name: ")
age=int(input("Enter Your Age: "))
nation=input("Enter Your Nationality: ")

if(age > 18 and nation=='Pakistan'):
    print("You are eligible for Vote\nCast Vote")
else:
    print("You are not eligible")

print("Hello")

name=input("Enter User Name: ")
password=input("Enter Password: ")

if(name=='Admin'):
    if(password=='Shayan2115'):
        print("Account Login...")
    else:
        print("Password is Incorrect")
else:
    print("Username is Incorrect")

while(True):
    name=input("Enter User Name: ")
    password=input("Enter Password: ")
    if(name=="Shayan" and password=="Shayan2115"):
        print("Account Login...")
    elif(name=="Shayan" and password!="Shayan2115"):
        print("Password is Incorrect")
    elif(name!="Shayan" and password=="Shayan2115"):
        print("Username is Incorrect")
    else:
        print("Both username and password are incorrect")


name=input("Enter User Name: ")
password=input("Enter Password: ")

if(name=="Shayan" and password=="Shayan2115"):
    print("Account Login...")
else:
    if(name!="Shayan"):
        print("Wrong Username")
    else:
        print("Wrong Password")

i=5
while(i>=1):
    print(i)
    i-=1

number=1
table=int(input("Enter table: "))

while(number<=10):
    print(table,"*",number,"=",table*number)
    number+=1


while(True):
    name=input("Enter User Name: ")
    password=input("Enter Password: ")
    if(name=="Shayan" and password=="Shayan2115"):
        print("Account Login...")
    elif(name=="Shayan" and password!="Shayan2115"):
        print("Password is Incorrect")
    elif(name!="Shayan" and password=="Shayan2115"):
        print("Username is Incorrect")
    elif(name=='no'):
        break
    else:
        print("Both username and password are incorrect")

Correct Username and Password

CORRECT_USERNAME = "Shayan"
CORRECT_PASSWORD = "Shayan2115"

while True:
    username = input("Enter Username (or type 'no' to exit): ")

    if username.lower() == "no":
        print("Program terminated.")
        break

    password = input("Enter Password: ")

    if username == CORRECT_USERNAME and password == CORRECT_PASSWORD:
        print("✅ Login successful.")
    elif username == CORRECT_USERNAME:
        print("❌ Incorrect password.")
    elif password == CORRECT_PASSWORD:
        print("❌ Incorrect username.")
    else:
        print("❌ Both username and password are incorrect.")

