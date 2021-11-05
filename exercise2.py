valid=False
while valid==False:
    email = input("Write your email: ")
    if "@" in email:
        if "." in email:
            valid=True
            print("It is a valid email.")
        else:
            print("Please enter a valid email.")
            valid=False
    else:
        print("Please enter a valid email.")
        valid=False