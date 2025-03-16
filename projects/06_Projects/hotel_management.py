'''checking in or out, charging guests for rooms, multiple room and multiple night plus one new feature
i'm going to get program working, worry about meeting requirements after'''
from tkinter import Tk, simpledialog, messagebox
#Variable to check if check in should run again
done = 0
#Room number
number = 0
#Cost of one room
cost = 0
#number of nights
num_of_nights = 0
#Variable to display total price
total = 0
#dictionary of transactions made
transactions = {
}
#dictionary showing who is staying in what room and for how long
peoples_purchases = {
}
'''Dictionary showing what people have bought, this is for the rooms left list so that 
people can check into rooms that just got checked out of'''
room_num_person = {
}
#list of rooms left
rooms_left = []
for i in range (100):
    rooms_left.append(i+1)
def individual_check_in(done, number, price):
    num_of_nights = 0
    cost = price
    while done == 0:
        try:
            number = simpledialog.askinteger("room number", "Hello, what room are you checking into?\nRooms 1-50 are $100 a night and 51-100 are $200 a night. ")
            if number > 50 and number <=100:
                num_of_nights = int(simpledialog.askinteger("night number", "How many nights will you be staying?"))
                cost = 200 * num_of_nights
                price_word = str(cost)
                messagebox.showinfo("Total", "That will add $" + price_word + " to your total.")
                done = 1
                rooms_left.remove(number)
                num_and_nights = ("Room number" + str(number), str(num_of_nights) + "nights")
                if name in transactions:
                    transactions[name] += cost
                else:   
                    transactions[name] = cost
                if name in peoples_purchases:
                    peoples_purchases[name] += num_and_nights
                else:
                    peoples_purchases[name] = num_and_nights
            elif number <= 50 and number > 0:
                num_of_nights = simpledialog.askinteger("night number", "How many nights will you be staying?")
                cost = 100 * num_of_nights
                price_word = str(cost)
                messagebox.showinfo("Total", "This will add $" + price_word + " to your total.")
                done = 1
                rooms_left.remove(number)
                num_and_nights = ("Room number " + str(number), str(num_of_nights) + " nights")
                messagebox.showinfo("rooms left", rooms_left)
                if name in transactions:
                    transactions[name] += cost
                else:   
                    transactions[name] = cost
                if name in peoples_purchases:
                    peoples_purchases[name] += num_and_nights
                else:
                    peoples_purchases[name] = num_and_nights
                if name in room_num_person:
                    room_num_person[name] += number
                else:
                    room_num_person[name] = number
            else:
                messagebox.showinfo("Invalid number", "Please enter a valid room number")

        except ValueError:
                messagebox.showinfo("Invalid number", "Please enter a valid room number")

def check_in():
    extra_rooms = simpledialog.askstring("extra rooms", "Will you be checking into any other rooms? (y/n)")
    if extra_rooms == ("y"):
        individual_check_in(done, number, cost)
    elif extra_rooms == ("n"):
        messagebox.showinfo("Find your transaction", transactions)

def check_out():
    if name in transactions:
        confirm = simpledialog.askstring("Confirm", "Are you sure you want to check out from all rooms? (y/n)")
        if confirm == ("y"):
            del transactions[name]
            del peoples_purchases[name]
            rooms_left.append(room_num_person[name])

def in_or_out():
    in_question = simpledialog.askstring("extra rooms", "Are you checking in? (y/n)")
    if in_question == ("y"):
        individual_check_in(done, number, cost)
        check_in()
    elif in_question == ("n"):
        check_out()

while True:
    name = simpledialog.askstring("Home screen", '''If you want to leave, press q, if you want to check transactions, press t
if you want to check what rooms are left press r,  if you want to check who has purchased what 
press ?, and if you want to check in or out enter your name.''')
    if name == ("q"):
        break
    elif name == ("t"):
        messagebox.showinfo("Transactions", transactions)
    elif name == ("r"):
        messagebox.showinfo("Rooms still left", rooms_left)
    elif name == ("?"):
        messagebox.showinfo("Purchases made", peoples_purchases)
    else:
        in_or_out()