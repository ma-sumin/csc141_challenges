#Sumin Ma
#15th Sep 2024
#get scores from users and calculate the average score

print() #add a new line
print("-------------------------")
print("Calculate average score") #title
print("-------------------------")
print() #add a new line
#prompt the user to enter how many scores they would like to average
num = input("How many scores would you like to average? ")
print() #add a new line

scores = [] #to save scores given by users
for i in range(0, int(num)):
    i = input("Enter a score: ") #ask the user to enter a score for each score they want to average
    scores.append(float(i)) #add that score to the list
print() #add a new line

#calculate the average score of the list
sum_num = sum(scores)
len_num = len(scores)
mean_num = sum_num / len_num

#print the result
print(f"Your average score is {mean_num} points.")
print() #add a new line