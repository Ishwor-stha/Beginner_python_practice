#greeting the user
def greeting(name):
    return (f"Hello {name}, how are you?")
#      Note :::
#return is just like a print function
#we cannot call the function on variable if we are using print function.
#While using return statement we can call the function  on variable like down below: 

greet=greeting(input("Enter Your name:"))    
print(greet) 

#Even check 
def even_check(num):
    if num%2==0:
        return "Even"
    else:
        return "Odd"
    
check=even_check(int(input("Enter any number:"))) #the user inputted value always stores as a string so  converted
print(check)                                    #into integer to do above operation on function


#Even check on List

def even_check_list(Numbers):
    for i in Numbers:
       if i%2==0:
        print(f"{i},is even number.") 
       else:
             print(f"{i},is odd number")

even_check_list([1,2,3,4,5])

#Printing even number on list

def even_number(numbers):
 numbers_list=[] #we can create variables and do some operations with it inside function 
 for i in numbers:
     if i%2==0:
         numbers_list.append(i) # data  of i is stored in number_list by using append method
     else:
        pass
 print(numbers_list)
     
even_number([1,2,3,4,6])

#printing odd number of list


def odd_numbers(numbers):
    number_list=[]
    for i in numbers:
        if i%2==0:
            pass
        else:
            number_list.append(i)
    print(number_list)
    
    
    
odd_numbers([1,2,3,4,5])

# Working with tuple/tuple unpacking using function

          #  name           hour    name        hour name      hour name        hour
name_hour=[('Ishwor shrestha',5),('Suman magar',8),('Gopal dahal',10),('Saroj shrestha',7)]# creating a tuple
def emoloyee_of_the_week(details):
    new_hour=0
    new_name=''
    for (name,hour) in details:#tuple unpacking by passig value to name and hour variable ie.name=Ishwor,hour=8
        if hour>new_hour:
            new_hour=hour
            new_name=name
    print(f"The emoloyee of the week with {new_hour}hr is {new_name}")
    
#emoloyee_of_the_week(name_hour)#passing the tuple list to a function


