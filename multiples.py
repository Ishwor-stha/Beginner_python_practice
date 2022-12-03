operand=int(input("Enter any number you want to see multiples of:"))
num=int(input("Enter the range that you want to see multiples  up to:"))
for i in range(1,num+1):   #i variable goes from 1 to (num+1) which means if i put 10 in num the
                            #i goes up to 9 so to make it up to 10 i added 1 in num
    mul=operand*i
    print(mul)