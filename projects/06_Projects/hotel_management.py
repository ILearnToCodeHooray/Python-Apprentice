'''checking in or out, charging guests for rooms, multiple room and multiple night plus one new feature
i'm going to get program working, worry about meeting requirements after'''
from tkinter import Tk, simpledialog, messagebox
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
            number = simpledialog.askinteger("room number", "Hello, what room are you checking into? \nRooms 1-50 are $100 a night and 51-100 are $200 a night. ")
            if number > 50 and number <=100:
                num_of_nights = int(simpledialog.askinteger("night number", "How many nights will you be staying?"))
                cost = 200 * num_of_nights
                price_word = str(cost)
                messagebox.showinfo("Total", "That will add $" + price_word + " to your total.")
                total_price.append(cost)
                done = 1

            elif number <= 50 and number > 0:
                num_of_nights = simpledialog.askinteger("night number", "How many nights will you be staying?")
                cost = 100 * num_of_nights
                price_word = str(cost)
                messagebox.showinfo("Total", "This will add $" + price_word + " to your total.")
                total_price.append(cost)
                done = 1

            else:
                messagebox.showinfo("Valid number", "Please enter a valid room number")

        except ValueError:
                messagebox.showinfo("Valid number", "Please enter a valid room number")

def check_in():
    extra_rooms = simpledialog.askstring("extra rooms", "Will you be checking into any other rooms? (y/n)")
    if extra_rooms == ("y"):
        individual_check_in(done, number, cost)
    elif extra_rooms == ("n"):
        for i in total_price:
            total = total + total_price(i)
        messagebox.showinfo("New total", "your total is " + total)


    
def in_or_out():
    in_question = simpledialog.askstring("extra rooms", "Are you checking in? (y/n)")
    if in_question == ("y"):
        individual_check_in(done, number, cost)
        check_in()
while True:
    in_or_out()