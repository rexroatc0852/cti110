# A Program to Calculate the Percentages of Males and Females in a Class
# 09/24/18
# CTI-110 P2HW2 - Male Female Percentage
# Christopher Rexroat
#

# Program Announcement
print (" This program will calculate the percentage of " \
       "males and females in a class. " \
       "\nLet's get started! ")

# Request input for total number of males in class
TotalMales = float(input('Enter the total number of males in class: ')) 

# Request input for total number of females in class
TotalFemales = float(input('Enter the total number of females in class: '))

# Calculate total class size
TotalClassSize = (TotalMales + TotalFemales)

# Calculate Percentages
PercentageMale = (TotalMales/TotalClassSize)
PercentageFemale= (TotalFemales/TotalClassSize)

# Display float integer as percentage value
print (" Total Number of students in class is: ", TotalClassSize )
print (format (PercentageMale, '.0%'))
print (format (PercentageFemale, '.0%'))


# Introduce the program
# Request the number of males in the class
# Request the number of females in the class
# Calculate the total Number of class based on requested input
# Calculate the percentages of male/female in relation to total class size
# Display the results
