my_name = input("Enter your name : ")
my_age = int(input('Enter your age :'))

print(f"My name is {my_name} and I am {my_age} years old" )

############################################################3

first_num = int(input("Enter the first number : ")) 
second_num = int (input("Enter the second number : "))
operation = input("Enter the operation :")

if operation == "+" :
    print(first_num + second_num)

elif operation == "-" :
    print(first_num - second_num)

elif operation == "*" :
    print (first_num*second_num)
elif operation == "/" :
    print (first_num/second_num)
else : 
    print ("This operation is not valid")

#################################################################

bus_capacity = 30
people_inbus = int(input("How many people are in the bus ?"))
want_to_ride = int(input("How many want to take the bus ?"))
empty_seats = bus_capacity - people_inbus

if empty_seats > want_to_ride :
    print (f"There is {empty_seats}  empty seats for people to ride ")
elif empty_seats <= want_to_ride :
    print("The bus is full")























