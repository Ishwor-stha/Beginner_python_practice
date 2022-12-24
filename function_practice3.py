# Write a function that computes volume of sphere given its radius
# 4/3 pi r^3

def sphere(radius):
    pi=3.1415
    return (4/3)*(pi*radius*radius*radius)

# print(sphere(radius=int(input("Enter a radius of sphere:")))) 




# Write a function that checks weather a number is in given range or not

def range_cheak(num,low_num,high_num):
    if num>=low_num and num<=high_num:
        return True
    else:
        return False

# print(range_cheak(7,4,6))




# Write a python function that acepts a string and calculates the number of upper case letters and lower case letter

def checks_lower_or_upper(letter):
    ucount=''
    lcount=''
    for i in letter:
        if i.isupper():
            ucount=ucount+i
        elif i.islower():
            lcount=lcount+i
    return f"The number of upper case is {len(ucount)} and the number of lower case is {len(lcount)}"
 
# print(checks_lower_or_upper('HEllo World'))
            




# Write a pyrhon function that takes a list and returns a new list with unique elements of first list
#sample list [1,1,1,2,1,2,3,3,3,2]
# new list [1,2,3]

def unique_list(nums):
    return list(set(nums))

# print(unique_list([1,1,1,2,1,2,3,3,3,2]))
    
    
         #OR
         
def unique_li(num):
    convert=set(num)#set function doesnot repeat data for eg [1,2,1,2,3,3]=[1,2,3]
    li=list(convert)# list function converst to list 
    return li
# print(unique_li([1,1,1,2,1,2,3,3,3,2]))



#pythonfunction to multiply all the numbers in the list

def multiply(number):
    mul=1
    for i in number:
        mul=mul*i
    return mul

# print(multiply([1,2,3,-4]))
# print(multiply([1,2,3,4,5,6,7]))




# Write a funftion that checks whether a word or phrase is palindrome oor not
#Examples of palindrome is 'kayak' reverse the string it becomes same 'kyak'

def palindrome(text):
    text=text.replace(' ','')#this replace space to empty string
    
    text2=text[::-1]# it reverse the string
    if text==text2:
        return f'{text}  is palindrome '
    else:
        return f'{text} is not palindrome'
# print(palindrome('kayak'))
# print(palindrome('nurses run'))    






