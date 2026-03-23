file_name = input("Enter a name for a new file:")
Master_pwd = input("create account password password: ")
username = input("Enter a userame for an account:")

def add():
    with open('passwords.txt','a') as f:#opens a file and atomatically close the file
        f.write(username + "|"+ Master_pwd + "\n")#puts user and password inside the file

def info_checker():
    print("To access file enter username and password ")
    name = input('Enter username name: ')
    pwd = input("Password: ")
    if name  == username and pwd == Master_pwd:
        return True
    else:
        print('You have two more trys to enter the right infor')
        for i in range(1,3):
            print("Wrong")
            name = input('Enter username name: ')
            pwd = input("Password: ")
        if name  == username and pwd == Master_pwd:
            return True
        print("You have failed to enter the corret acount info")
        print("The code will now terminate")
        quit()

                  

def view():
    if info_checker():
        with open('passwords.txt','r') as f:
            for line in f.readlines():
                print(line)



def add_new():
    enter_file = input("Enter the file you want to add to: ")
    if enter_file == file_name:
        if info_checker():
            with open('passwords.txt','a') as f:#opens a file and atomatically close the file
                f.write(username + "|"+ Master_pwd + "\n")#puts user and password inside the file


def creation():
    info = input("Do you wish to enter new content y/n: ")
    if info == "y":
       title = input("Enter a content title: ")
       with open('passwords.txt','a') as f:#opens a file and atomatically close the file
                f.write(username + "|"+ Master_pwd + "\n")#puts user and password inside the file
	# code to add this to file being changed
ingredient_count = int(input("Enter the number of ingreditents: "))
for i in range(ingredient_count):
	ingredient = input("Enter an ingredient and its quantity: ")
		# code to add ingredient to file also
		
#def info_check():
    #pswrd_enter = input("Enter the password to acces the file:")#
    #if pasw
    

while True:
    mode = input("would you like to add a new password or look at a exsisting one \
                 (view, add, New content)press q to quit? ")
    if mode =="q":
        break

    if mode == "view":
         
         view()
    elif mode == "add":
        add()
    elif mode == "New content":
        add_new()
    else:
        print("Invalid mode.")
        continue  