#Sumin Ma
#13th Sep 2024
#Lion Bars production report: calculating the total amount of weight in ounces and pounds

#prompt the user to enter the weight of one Lion bar, in ounces.
weight_each_oz = float(input("Please enter the weight of each Lion Bar (in ounces): "))
#propmt the user again to enter how many Lion Bars were made last month.
num = int(input("How many Lion Bars were produce this month? "))

#the total amount of weight in ounces
weight_whole_oz = weight_each_oz * num
#calculate the conversion from ounces to pounds
weight_whole_pd = weight_whole_oz // 16
#the remainder when converting ounces to pounds
weight_remainder_oz = weight_whole_oz % 16

print()
print("Lion Bars Production Report")
print("-------------------------------")
#print the results
print(f"Monthly production = {num} Lion Bars @ {weight_each_oz} oz per bar.")
print() #add a new line
print(f"Total weight produced = {weight_whole_oz} oz, Which is {weight_whole_pd} lb(s), {weight_remainder_oz} oz. ")
print() #add a new line
