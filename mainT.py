import foodT
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter import filedialog
import tkinter.font as tkFont

'''root = Tk()
root.title('HomeDinner')
root.iconbitmap('c:/Users/nicbe/OneDrive/Desktop/Python/test/images/mixbowl.ico')
root.geometry("1800x400")
root.configure(background="#24dc9d")
#root.grid_columnconfigure(0, weight=1)'''

root = foodT.fra()
'''test of notes
    -add just 'bread' as a valid ingredient
    -add more fruit
    -autocorrect
'''

def main():
    num = 0
    if num == 1:
        tester()
    
    #grid()
    global begin
    global op1
    global op2
    global op3
    global op4
    global op5
    global op6
    global op7
    global acon
    #fonts
    #romanfont = tkFont.Font(family="Lucida Handwriting", size=18, weight=tkFont.NORMAL)
    scriptfont20 = tkFont.Font(family="Monotype Corsiva", size=20, weight=tkFont.NORMAL)
    scriptfont16 = tkFont.Font(family="Monotype Corsiva", size=16, weight=tkFont.NORMAL)
    #courierfont = tkFont.Font(family="Script MT Bold", size=18, weight=tkFont.NORMAL)
    bfont = tkFont.Font(family="Terminal", size=18, weight=tkFont.NORMAL)
    #header and name
    head = Label(root, text="+   Header   +", pady=80, bg="red")
    head.grid(row=0, column=0, columnspan=3)
    intro = Label(root, text="Welcome To Home Dinner", anchor="w", font=scriptfont20, bg="#24dc9d")
    intro.grid(row=1, column=0, columnspan=3)
    titlemap = ImageTk.PhotoImage(Image.open('recipetest/food/images/RecipeLogo.png'))
    title = Label(image=titlemap, anchor="center")

    #title.grid(row=0)

    #main menu - - - -
    choice = IntVar()
    choice.set("100")
    var = IntVar()
    begin = Label(root, text="Please Choose an Option:", font=scriptfont20, bg="#24dc9d")
    begin.grid(row=2, column=0, sticky="w")
    op1 = Radiobutton(root, text="Add ingredients to your pantry     ", variable=choice, value=1, font=scriptfont16, anchor="w", bg="#24dc9d")
    op1.grid(row=3, column=0, sticky="w")
    op2 = Radiobutton(root, text="Remove ingredients to your pantry", variable=choice, value=2, font=scriptfont16, anchor="w", bg="#24dc9d")
    op2.grid(row=4, sticky="w")
    op3 = Radiobutton(root, text="Edit ingredients in your pantry", variable=choice, value=3, font=scriptfont16, anchor="w", bg="#24dc9d")
    op3.grid(row=5, sticky="w")
    op4 = Radiobutton(root, text="View your pantry", variable=choice, value=4, font=scriptfont16, anchor="w", bg="#24dc9d")
    op4.grid(row=6, sticky="w")
    op5 = Radiobutton(root, text="View recipes you can make", variable=choice, value=5, font=scriptfont16, anchor="w", bg="#24dc9d")
    op5.grid(row=7, sticky="w")
    op6 = Radiobutton(root, text="View all recipes", variable=choice, value=6, font=scriptfont16, anchor="w", bg="#24dc9d")
    op6.grid(row=8, sticky="w")
    op7 = Radiobutton(root, text="Clear your pantry", variable=choice, value=7, font=scriptfont16, anchor="w", bg="#24dc9d")
    op7.grid(row=9, sticky="w")
    acon = Button(root, text="Confirm", comman=lambda: click(choice.get()), anchor="center", width=20, font=scriptfont16)
    acon.grid(row=10)
    #main menu - - - -

    #exit program - - - -
    ex = Button(root, text="QUIT", command=qui, anchor="center", height=3, width=40, font=scriptfont16)
    ex.grid(row=15, column=0, sticky="w")

    ex.wait_variable(var)
    #exit program - - - -
    type = False
    ingredients = "0"
    stock = "pop"
    inventory = {ingredients : stock}
    ans = 100

    '''while ans != 0:
        print("+ - - - - - - - - - - +")
        print("Type the number of the choice you would like to make: ")
        print("1. Add ingredients")
        print("2. Remove an ingredient")
        print("3. Edit an ingredient")
        print("4. View recipes you can make")
        print("5. View all recipes")
        print("6. Clear your pantry")
        print("+ - - - - - - - - - - +")
        ans = input("Choice: ")
        if not ans.isdigit():
            print("- Invalid Choice -")
            continue
        else:
            ans = int(ans)
        if ans == 1:
            foodT.userin()
        elif ans == 2:
            foodT.remov()
        elif ans == 3:
            foodT.edit()
        elif ans == 4:
            print("view recipes")
        elif ans == 5:
            print("show all recipes")
        elif ans == 6:
            d = 1
            while d == 1:
                con = input("Clear your pantry?(y/n): ").lower()
                if con == "y":
                    foodT.clea()
                    d = 2
                elif con == "n":
                    d = 2
        else:
            print("- Invalid Choice")'''

def click(ans):
    if ans == 100:
        return
    menhi()
    if ans == 1: #add
        pic = foodT.addmenu()
        if pic == 2:
            mensho()
    elif ans == 2: #remove
        agre = foodT.remov()
        if agre == -1:
            mensho()
    elif ans == 3: #edit
        ed = foodT.edit()
        if ed == -1:
            mensho()
    elif ans == 4: #view pantry+
        vi = foodT.viewp()
        if vi == -1:
            mensho()
        print("view pantry")
    elif ans == 5: #view recipes user can make+
        print("view recipes you can make")
    elif ans == 6: #view all recipes+
        print("view all recipes")
    elif ans == 7: #clear pantry+
        foodT.clea()
    
def menhi():
    begin.grid_forget()
    op1.grid_forget()
    op1.grid_forget()
    op2.grid_forget()
    op3.grid_forget()
    op4.grid_forget()
    op5.grid_forget()
    op6.grid_forget()
    op7.grid_forget()
    acon.grid_forget()
    return

def mensho():
    begin.grid(row=2, sticky="w")
    op1.grid(row=3, sticky="w")
    op2.grid(row=4, sticky="w")
    op3.grid(row=5, sticky="w")
    op4.grid(row=6, sticky="w")
    op5.grid(row=7, sticky="w")
    op6.grid(row=8, sticky="w")
    op7.grid(row=9, sticky="w")
    acon.grid(row=10, sticky="w")
    return

def qui():
    root.destroy()

def grid():
    p1 = Label(root, text="(1,0)")
    p1.grid(row=1, column=0)
    p2 = Label(root, text="(2,0)")
    p2.grid(row=2, column=0)
    p3 = Label(root, text="(3,0)")
    p3.grid(row=3, column=0)
    p4 = Label(root, text="(4,0)")
    p4.grid(row=4, column=0)
    p5 = Label(root, text="(5,0)")
    p5.grid(row=5, column=0)
    p6 = Label(root, text="(6,0)")
    p6.grid(row=6, column=0)
    p7 = Label(root, text="(7,0)")
    p7.grid(row=7, column=0)
    p8 = Label(root, text="(8,0)")
    p8.grid(row=8, column=0)

    p11 = Label(root, text="(1,1)")
    p11.grid(row=1, column=1)
    p21 = Label(root, text="(2,1)")
    p21.grid(row=2, column=1)
    p31 = Label(root, text="(3,1)")
    p31.grid(row=3, column=1)
    p41 = Label(root, text="(4,1)")
    p41.grid(row=4, column=1)
    p51 = Label(root, text="(5,1)")
    p51.grid(row=5, column=1)
    p61 = Label(root, text="(6,1)")
    p61.grid(row=6, column=1)
    p71 = Label(root, text="(7,1)")
    p71.grid(row=7, column=1)
    p81 = Label(root, text="(8,1)")
    p81.grid(row=8, column=1)

def tester():
    foodT.test()

if __name__ == '__main__':
    main()