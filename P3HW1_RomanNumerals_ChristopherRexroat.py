# A program to Return the Roman Numeral Value of a number 1 - 10
# CTI-110
# P3HW1 - Roman Numerals
# Christopher Rexroat
# 10/07/2018
#

# Prompt User to enter a number 1-10
number = int(input (' Please enter a number from 1-10: '))

# Display Roman Numeral or Error Message
if number == 1:
    print ('The Roman Numeral for the number ',number,'is I')
elif number == 2:
    print ('The Roman Numeral for the number ',number,'is II')
elif number == 3:
    print ('The Roman Numeral for the number ',number,'is III')
elif number == 4:
    print ('The Roman Numeral for the number ',number,'is IV')
elif number == 5:
    print ('The Roman Numeral for the number',number,'is V')
elif number == 6:
    print ('The Roman Numeral for the number',number,'is VI')
elif number == 7:
    print ('The Roman Numeral for the number ',number,'is VII')
elif number == 8:
    print ('The Roman Numeral for the number',number,'is VIII')
elif number == 9:
    print ('The Roman Numeral for the number',number,'is IX')
elif number == 10:
    print ('The Roman Numeral for the number',number,'is X')
else:
    print ('Error: The number entered is outside the acceptable range.' \
           "\nPlease Try again.")
