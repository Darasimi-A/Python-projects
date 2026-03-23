print("Welcome to my French Quiz")
playing = input("Do you wana play?: ")

if playing != "yes":
    quit()

print("Great lets play :)")

question1 = input("what does fère mean?: ")
if question1 == "brother":
    print("Good job!")
else:
    print("Wrong!!!!")
    

 
question2 = input("what does mère mean?: ")
if question2 == "mother":
    print("Good job!")
else:
    print("Wrong!!!!")
    

question3 = input("is ma the correct adjective for brother?: ")
if question3 == "no":
    print("Good job!")
else:
    print("Wrong!!!!")

question4 = input("Is a plus tard a goodbye?-yes or no: ")
if question3 == "yes":
    print("Good job!")
else:
    print("Wrong!!!!")

question5 = input("Is comment ca va a greeting?-yes or no: ")
if question3 == "yes":
    print("Good job!")
else:
    print("Wrong!!!!")
