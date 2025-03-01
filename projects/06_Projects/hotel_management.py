'''checking in or out, charging guests for rooms, multiple room and multiple night plus one new feature'''
def check_in(name):
    done = 0
    while done == 0:
        number = int(input("Hello, " + name + ", what room are you checking into? Rooms 1-50 are $100 a night and 51-100 are $200 a night. "))
        if number > 50 and number <=100:
            num_of_nights = int(input("How many nights will you be staying?"))
            price = 100 * num_of_nights
            print("That will be $" + price)
            done = 1
        elif number <= 50 and number > 0:
            num_of_nights = int(input("How many nights will you be staying?"))
            price = 200 * num_of_nights
            print("that will be $" + price)
            done = 1
        else:
            print("Please enter a valid room number")
    
def in_or_out():
    in_question = input("Are you checking in? (y/n)")
    if in_question == ("y"):
        check_in(name)

while True:
    name = input("What is your name? ")
    in_or_out()