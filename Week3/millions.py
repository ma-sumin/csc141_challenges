#Sumin Ma
#13th Sep 2024
#Make a list that contains every odd number from 1 to 1,000,000 and use the math functions

#make a list that contains every odd number from 1 to 1,000,000
odd_list = []
for num in range(1, 1000000):
    if (num%2 != 0): #check if each number is odd
        odd_list.append(num) #if it is, append it to the list

#use the math functions discussed in class to match the sample output for this lab
min = min(odd_list)
max = max(odd_list)
sum = sum(odd_list)
len = len(odd_list)
mean = sum / len

#print the output
print() #add a new line
print(f"The Min number is: {min}")
print(f"The Max number is: {max}")
print(f"The Sum is:        {sum}")
print(f"The Length is:     {len}")
print(f"The Mean is:       {mean}")
print() #add a new line

