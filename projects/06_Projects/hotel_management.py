'''checking in or out, charging guests for rooms, multiple room and multiple night plus one new feature
i'm going to get program working, worry about meeting requirements after'''
#Variable to check if check in should run again
done = 0
#Room number
number = 0
#Cost of one room
cost = 0
#List for total price
total_price = []
#Variable to display total price
total = 0
def individual_check_in(done, number, price):
    cost = price
    while done == 0:
        try:
            number = int(input("Hello, what room are you checking into? Rooms 1-50 are $100 a night and 51-100 are $200 a night. "))
            if number > 50 and number <=100:
                num_of_nights = int(input("How many nights will you be staying?"))
                cost = 200 * num_of_nights
                price_word = str(cost)
                print("That will add $" + price_word + " to your total.")
                total_price.append(cost)
                done = 1

            elif number <= 50 and number > 0:
                num_of_nights = int(input("How many nights will you be staying?"))
                cost = 100 * num_of_nights
                price_word = str(cost)
                print("This will add $" + price_word + " to your total.")
                total_price.append(cost)
                done = 1

            else:
                print("Please enter a valid room number")

        except ValueError:
                print("Please enter a valid room number")

def check_in():
    individual_check_in(done, number, cost)
    extra_rooms = input("Will you be checking into any other rooms? (y/n)")
    if extra_rooms == ("y"):
        individual_check_in(done, number, cost)
    elif extra_rooms == ("n"):
        for i in total_price:
            total = total + total_price(i)
        print("your total is " + total)


    
def in_or_out():
    if in_question == ("y"):
        check_in()
in_question = input("Are you checking in? (y/n)")
while True:
    in_or_out()