# Sumin Ma
# Date: 5th Sep, 2024
# Asking for the user's name, age, and major to complete an introduction message on their behalf

#assign a starting message to a variable
print("To generate your introduction, I will need some information from you...")
#add a newline
print()

#prompt users with a question for their name
u_name = input("What is your name? ")
#prompt users with a question for their age
u_age = input("How old are you? ")
#prompt users with a question for their major
u_major = input("What do you study? ")

#assign the introduction message to a variable
intro_msg = f"Hi, my name is {u_name} and I am {u_age} years old! At Albright College, I study {u_major}."

#add a newline
print()
#print the message
print(intro_msg)


