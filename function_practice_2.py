# Write a function that returns the lesser of two given numbers if both numbers are even,but returns 
# the greater if one or both numbers are odd
# EXAMPLE
#  odd_even(2,4)------>2
# odd_even(2,5)------>5

def odd_even(a,b):
    if a%2==0 and b%2==0:
        if a<b:
            print(a)
        else:
            print(b)
    else:
        if a<b:
            print(b)
        else:
            print(a)

# odd_even(9,6)





# Write a function takes a two-word string and returns True if both words begin with same letters 
# else false

def word_check(text):
    lower_text=text.lower()
    list_word=lower_text.split() # split method splits the strings from space and converts into list
                                      #Example ("hello hi")---->["hello","hi"] 
    if list_word[0][0]==list_word[1][0]:
        return True
    else:
        return False

# print(word_check("ishwor Ishan"))
# print(word_check("ishwor Shrestah"))






#Given two integers,return True if the sum of the integer is 20 or if one of the interger is 20 if not return False
# EXAMPLE
# makes_twenty(20,10)------>True
#makes_twenty(8,12)------>True
#makes_twenty(8,10)------>False
def makes_twenty(num1,num2):
    if num1==20 or num2==20:
        return True
    elif num1+num2==20:
        return True
    else:
        return False
# print(makes_twenty(30,10))





# Write a function that capitalizes the first and fourth letters of a name 
# Example happyday=HapPday
def capital_letter(letter):
    first_half=letter[:3]#hap
    rest=letter[3:]#pyday
    return first_half.capitalize() + rest.capitalize()#capitalize method converts first string into capital and rest of in small
    
    
    # print(capital_letter("happyday"))







#Return a sentence with word reverse
# Example  i am home----. home i am

def revese(text):
    text_list=text.split()
    reverse_list=text_list[::-1]
    return " ".join(reverse_list)   #join method returns the data after inserting the user inputted values in between list
                                    #example mylist["a","b","c"]
                                    # "--".join(mylist) 
                                    # output='a--b--c'
                                    #       OR
                                    # " ".join(mylist)
                                    # output= 'a b c'

# print(revese("hello how are you"))







#Given list of ints Return True if  the array contains a 3 next to 3 somewhere
#  Example
#is_3([1,3,3])---->True
#is_3([3,2,3])---->False
#is_3([3,1,2,3])---->False

def is_3(num):
   
    i=0
    j=1
    k=1
    while(k< len(num)):
        if num[i]==num[j]:
            return True
           
        if k==len(num)-1:
            return False
        
        
        k=k+1
        i=i+1
        j=j+1
        
# print(is_3([1,3,3]))
# print(is_3([3,2,3]))





# Given a string, return a string where for every character in the original there are three characters
#   Example
#Hello----->HHHeeellllllooo
#Hi------>HHHiii

def triple_string(text):
    new_word=''
    for i in text:
        word=i*3
        new_word=new_word + word
    return new_word
# print(triple_string(text=input("Enter any strings/words--->")))




# Given three integers between 1 and 11,if their sum is less than or equal to 21,return their sum.
# If their sum exceeds 21 and there's and eleven,reduce the total sum by 10.Finally if,their sum exceeds 21(even after adjustment) return'BUST'
# Example
# (5,6,7)--->18
# (9,9,9)--->BUST
# (9,9,11)--->19

def three_num(a,b,c):
    sum=a+b+c
    if sum <=21:
        return sum
    elif sum<21 and a==11 or b==11 or c==11:
        return sum-10
    else:
        return 'BUST'
    
# print(three_num(a=int(input("Enter first number between 1-11 :")),b=int(input("Enter second number between 1-11 :")),c=int(input("Enter Third number between 1-11 :"))))






# Return the sum of the numbers in the array except ignore sections of numbers starting with 6 and extending to the next 9 ie(6,7,8,9 will be ignored)
# Example [1,3,5]---9
#[4,5,6,7,8,9]-->9
#[2,1,6,9,11]---->14

def sum(numbers_list):
    sum=0
    for i in numbers_list:
        if i<=5 or i>9: #ie 1,2,3,4,5 and greater than 9
            sum=sum+i
    return sum
# result=sum([2,1,6,9,11])
# print(result)






# Write a function that takes in a list of integers and returns True if it contains 007 in order
#Example[1,0,0,7,2]--->True
#Example[1,0,5,0,8,7,2]--->True
#Example[1,7,0,0,2]--->False

def is_007(Num_list):
    check=[0,0,7,'x']
    for i in Num_list:
        if i==check[0]:
            check.pop(0)
    return len(check)==1 #checks whether the length of check array is 1 or not if yes it returns True else False

# check=is_007([1,0,0,4,5,7])
# print(check)
# check=is_007([1,0,4,7,5,0])
# print(check)



# prime number up to user inputed number:

def prime_num(num):
    for i in range(2,num+1):
         if i==2 or i==3 or i==5 or i==7:
             print(i)
         elif i%2!=1 and i%3!=0 and i%5!=0 and i%7!=0:
             print(i)
         
# prime_num(100)


        