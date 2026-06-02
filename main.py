# entry point to the app

def main():
    #to collect and save student details
    students =[]
    status = True
    while status:
        print("======MENU======")
        print("1. add student ")
        print("2.add scholarship student ")
        print("3. view all students ")
        print("4. exit ")

        user_choice = input("enter your choice: ")

        if(user_choice == '1'):
            print("student added successfully")
        elif(user_choice == '2'):
            ## methods to add scholarship student
            print("scholarship student added successfully")
        elif(user_choice == '3'):
            ## display entries in students
            print("*********************")
        elif(user_choice == '4'):
            status = False
            break           # used to breake a loop (for or WHILE)
        else:
            print(" please select a valid choice")

# initaialize python project3
if __name__ == "__main__":
    main()





