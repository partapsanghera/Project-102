print("Welcome To This Calculator .")
print("Press '1' To Do Addition . Press '2' To Do Subtraction . Press '3' To Multiply . Press '4' To Divide .")

choice =   int(input("Choose What You Want To Do . "))
num1   =   int(input("Enter The First Number - "))
num2   =   int(input("Enter The Second Number - "))

add = float(num1 + num2)
subtract =float(num1 - num2)
multiply = float(num1 * num2)
divide = float(num1 / num2)

if choice == 1:
    print("The Added Number Is: ", add)
elif choice == 2:
    print("The Subtracted Number Is: ",subtract)
elif choice == 3:
    print("The Multiplied Number Is: ",multiply)
elif choice == 4:
    print("The Divided Number Is: ",divide)
else:
    print("The Operation Is Invalid")    