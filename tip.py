def hotel_tip(amount,tip_percentage):
    
    tip=amount*(tip_percentage/100)
    total=amount+tip
    print('\n\n')
    print("-------------------------------------")
    print('Your tip amount is $ '+str(tip))
    print('Your total amount is $ '+str(total))
    print("-------------------------------------")

    return total
hotel_tip(amount=int(input('Enter your Amount:')),tip_percentage=int(input('IF you want to give tip then enter the percentage:')))