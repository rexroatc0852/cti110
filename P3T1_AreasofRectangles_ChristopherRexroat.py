# A Program to compare the Area of two rectangles
# CTI-110
# P3T1 - Areas of Rectangles
# Christopher Rexroat
# 10/07/2018
#

# Request Dimensions of Rectangle 1
length1 = int (input (' What is the Length of Rectangle 1: '))
width1 = int (input (' What is the Width of Rectangle 1: '))

# Request Dimensions of Rectangle 2
length2 = int (input ('What is the Length of Rectangle 2: '))
width2 = int (input ('What is the Width of Rectangle 2: '))

# Calculate Area of Rectangle 1 and 2
area1 = length1 * width1
area2 = length2 * width2

# Compare Area Results and Output Display
if area1 > area2:
    print ('Rectangle 1 has the greater area.')
elif area2 > area1:
    print ('Rectangle 2 has the greater area.')
else:
    print ('Rectangle 1 and Rectangle 2 have the same area.')
