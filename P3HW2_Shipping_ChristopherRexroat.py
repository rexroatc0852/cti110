# A Program to Show Shipping Charges based on entered weight value.
# CTI-110 
# P3HW2 - Shipping 
# Christopher Rexroat
# 10/07/2018
#
 


def main ():
    # Get the Weight of the Item in LBS.
    packageweight = int( input('Please enter the package weight: '))

    # Determine the shipping cost based on entered weight.
    if packageweight <= 2:
        shipping = 1.50
    elif packageweight < 7:
        shipping = 3.00
    elif packageweight < 11:
        shipping = 4.00
    else:
        shipping = 4.75

    #Display the cost
    print ('Shipping your package will cost: $', format( shipping, ",.2f"))

# Call the main function.
main()
    
