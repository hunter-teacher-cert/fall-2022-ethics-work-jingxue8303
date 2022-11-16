#Collaborators:Elizabeth                                       Jing
#Resource and Reference: https://github.com/ryanhoang15/Python/blob/master/9.22%20Lab%20Ch%209:%20Concert%20seating%20chart(2D).py


price_chart = [[40, 40, 40, 0, 40, 40, 40, 40, 40, 0, 40, 40, 40],
               [20, 20, 30, 0, 30, 20, 20, 20, 30, 0, 30, 20, 20],
               [20, 20, 30, 0, 30, 20, 20, 20, 30, 0, 30, 20, 20],
               [20, 20, 30, 0, 30, 20, 20, 20, 30, 0, 30, 20, 20],
               [20, 20, 30, 0, 30, 20, 20, 20, 30, 0, 30, 20, 20]]
# This is a small scale of airplane seating. The numbers represent the price. 40s are the front rows(discounts can be offered to certain groups by airlines); 30s are by the corridor(the initial 0s); 1st colume and last colume are by the window.

print("Here are the available seats:\n")

for x, row in enumerate(price_chart):
    for col in price_chart[x]:
        print(col, end=" ")
    print()

user_input = input("Pick a (S)eat, a (P)rice or (Q)uit:\n ").lower()

while user_input != "q":
    if user_input == "s":
        row = int(input("Enter the row:\n "))-1
        col = int(input("Enter the column:\n "))-1
        if price_chart[col][row] != 0:
            print("Sold, for $", price_chart[col][row], "!\n")
            price_chart[col][row] = 0
        else:
            print("Sorry, that seat is not available.\n")

    elif user_input == "p": #picking a seat by price
        money = int(input("How much do you want to spend?(20,30,40)\n "))
        found = False
        for x, col in enumerate(price_chart):
            for y, row in enumerate(col):
                if row == money and not found:
                    found = True
                    print("You can have seat", x+1, y+1) #give the first available seat number for the user to type in. We believe this may privide consective seats if needed.)
                    break;
        if not found:
            print("Sorry, no tickets available at that price.\n")
    else:
        print("That wasn't a valid option.\n")
      
    print("Here are the available seats:\n")

  for x, row in enumerate(price_chart):
    for col in price_chart[x]:
      print(col, end=" ")
      print()
      
  user_input = input("Pick a (S)eat, a (P)rice or (Q)uit:\n ").lower()
for x, row in enumerate(price_chart):
    for col in price_chart[x]:
        print(col, end=" ")
    print()