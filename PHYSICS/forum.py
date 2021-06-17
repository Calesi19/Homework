# Prompt for grade
number = int(input("Please enter a positive number: "))     #A
if number < 0:                                              #B
    print('Error. Number is not a positive value')          #C
    quit()                                      

# Initialize sum
sum = 0                                                     #D
print(f'D - sum = {sum} count = /') 

# Count it up (Had to change the parameter from "number" to "number + 1")
for count in range(1, number + 1):                          #E
    print(f'E - sum = {sum} count = {count}')   
    sum += count                                            #F
    print(f'F - sum = {sum} count = {count}')                   

print(f'G - sum = {sum} Count = /') 
# Report
print("The sum is:", sum)                                   #G