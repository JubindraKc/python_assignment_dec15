def full_name():
    print("your first name is ", first_name)
    print("your last name is ", last_name)


choice = input("will you include your middle name? y/n\n")
name = input("please enter your full name separated with whitespace\n")

if choice == 'y':
    first_name, last_name, middle_name = name.split(" ")
    full_name()
    print('your middle name is ', middle_name)

elif choice == 'n':
    first_name, last_name = name.split(" ")
    full_name()

else:
    print("error")
