ulist=[]
print("User Login")
print('''1. Sign Up
       2. Log-in
       3. Delete User
       4. Show all users
       5. Exit
    ''')

ch=0

while(ch!=4):
    ch=int(input("Enter your choice : "))
    if ch==1:
        user={}
        user['username']= input("Username : ")
        user['password']= input("Password : ")
        user['email']= input("E-mail : ")
        ulist.append(user)
    

    if ch==2:
        print("Log-in for existing user")
        for user in ulist:
            username=input("Enter your username : ")
            password=input("Enter your password : ")
            if user['username']==username and user['password']==password:
                print("Welcome to the page")
            else:
                print("INVALID USER , TRY AGAIN")
    
    if ch==3:
        print("Delete user")
        for user in ulist:
            username=input("Enter your username : ")
            if user['username']==username:
                ulist.remove(user)
                print("Existing user is deleted")
            else:
                print("INVALID USER , TRY AGAIN")
    
    if ch==4:
        print("Show all Users")
        for user in ulist:
            print (user)


        
           
       