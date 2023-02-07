# TODO Create Variables
#   - Create the following variables
#   - my_first_name
#       -set this equal to your first name
#   - my_last_name
#       -set this equal to your last name
#   - my_year_of_birth
#       -set this equal to your birth year (doesn't have to be real should be less then 100 yrs ago)
#   - current_year
#       -set this equal to 2020
MyFirstName = "Talan"
MyLastName = "Bingham"
MyBirthYear = "1998"
CurrentYear = "2023"


# TODO String Indexing
#   - Print the following items (one per line) (print using variables)
#       - first name  
#       - last name
#       - first letter of your first name (use the +index)
#       - second letter of your last name (use the -index)
#       - first two letter of your first name (use the +index)
#       - second two letter of your last name (use the -index)

print(MyFirstName)
print(MyLastName)
print(MyBirthYear)
print(CurrentYear)
print(MyFirstName[0])
print(MyLastName[-6])
print(MyFirstName[0:1])
print(MyLastName[1:2])
print(MyLastName[-2:])


#TODO Combining Strings
#   - Print the following items (one per line) (print using variables)
#       -first name and last name combined
#       -first name six times

print(MyFirstName, MyLastName)
print(MyFirstName * 6)



# TODO Formatting Strings
#   - Print the following items (one per line) (print using variables)
#       - first name last name -was born in- year of birth
#       - first name last name -was born in- year of birth. first name -enjoyed celebrating- current year

print(MyFirstName,MyLastName,"was born in",MyBirthYear)
print (f"{MyFirstName} {MyLastName} was born in {MyBirthYear}. {MyFirstName} enjoyed celebrating {CurrentYear}")

# TODO Escape characters
#   - Print the following items (one per line) (print using variables)
#       - possesive first name -birth year is- year of birth 
#       - tab last name current year

print(MyFirstName + '\'s' + " birth year is " + str(MyBirthYear))
print('\t' + MyLastName, CurrentYear)

# TODO String methods
#   - Print the following items (one per line) (print using variables)
#       - first name and last name in lower case
#       - length of last name
#       - first name and last name all in upper case

print(MyFirstName.lower(), MyLastName.lower()) #.thing is a method
print(len(MyLastName)) #thing(variable) is a function
FirstNCap = MyFirstName.capitalize()
FirstLCap = MyLastName.capitalize()
print(MyFirstName.upper(), MyLastName.upper())
print(FirstLCap, FirstNCap)