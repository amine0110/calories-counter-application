from tkinter import *
import sqlite3 as sq


# Create and configure the window
root = Tk()
root.title("Calories count")
root.configure(bg="#263D42")
root.iconbitmap("icon.ico")

# Connect the data base
data_base = sq.connect("data.db")

# create a cursor
c = data_base.cursor()

def submit(a,b):


    # Connect the data base
    data_base = sq.connect("data.db")

    # create a cursor
    c = data_base.cursor()

    # Insert the things in the table
    c.execute("INSERT INTO food VALUES (:f_name, :f_calorie)",
              {
                  'f_name': a,
                  'f_calorie': b
              }
              )



    # commit all the changes
    data_base.commit()

    # close the data base
    data_base.close()



    #empty the boxes
    food_n.delete(0, END)
    calorie_num.delete(0, END)

def cal(s_food,food_100):
    return (food_100 * s_food)/100

def calculate():
    food_search_name = food_n.get()
    food_search_calorie = int(calorie_num.get())
    # Connect the data base
    data_base = sq.connect("data.db")

    # create a cursor
    c = data_base.cursor()

    c.execute("SELECT *, oid FROM food")

    items = c.fetchall()




    for item in items:
        if food_search_name == item[0]:
            food_calories_100g = int(item[1])
            result = cal(food_search_calorie, food_calories_100g)
        #else:
        #    result = "none"
        #    break





    lab = Label(root, text="You ate " + str(result) + " kCl of " + food_search_name, font="arial 25 bold")
    lab.grid(row=6, column=0, columnspan=2, pady=20)


    # commit all the changes
    data_base.commit()

    # close the data base
    data_base.close()


def newW():
    # Create the new window
    global top
    top = Toplevel()

    # Create the new food entry with the text
    n_f = Label(top, text="Enter the name of your food")
    n_f.grid(row=0, column=0)
    global new_food
    new_food = Entry(top, w=30)
    new_food.grid(row=0, column=1, padx=10, pady=10)


    # Create the new number of calories with the text
    n_n = Label(top, text="How many calories in 100g")
    n_n.grid(row=1, column=0)
    global new_number
    new_number = Entry(top, w=30)
    new_number.grid(row=1, column=1, padx=10, pady=10)

    #a = new_food.get()
    #b = new_number.get()

    # Submit button
    submit_n = Button(top, text="Submit", padx=50, pady=10, command=lambda :submit(new_food.get(),new_number.get()))
    submit_n.grid(row=2, column=0, columnspan=2)

    #outt = Button(top, )


# Add a picture
picture = PhotoImage(file="capture.gif")
Label(root, image=picture, bg="#263D42").grid(row=0, column=0, columnspan=3, padx=50, pady=10)

# Add a text
text1 = Label(root, text="food name", bg="#263D42",fg="black", font="roadrage 25 bold")
text1.grid(row=1, column=0,pady=10,padx=20)

text2 = Label(root, text="How many grammes", bg="#263D42",fg="black", font="roadrage 20 bold")
text2.grid(row=2, column=0,pady=10,padx=20)

# Box of the name of food entered
food_n = Entry(root, w=20, font="none 15")
food_n.grid(row=1, column=1)

# Box of the number of calories of the food entered
calorie_num = Entry(root, w=20, font="none 15")
calorie_num.grid(row=2, column=1)


# Count the calories of the food entered
sub = Button(root, text="Count", width=30, pady=10, font="none 10 bold", command= calculate)
sub.grid(row=3, column=0, columnspan=2, pady=10)

# Submit new food to the data base
new = Button(root, text="New", width=30, pady=10, font="none 10 bold", command= newW)
new.grid(row=4, column=0, columnspan=2, pady=10)


# Create a display
# fr = Frame(bg="white", width=300, height=200).grid(row=5, column=0, columnspan=2, pady=20)

# Save the day is calories
# save_new_meal = Button(root, text="NEW", command=new).grid(row=6, column=0, columnspan=2, pady=10)




# commit all the changes
data_base.commit()

# close the data base
data_base.close()



mainloop()