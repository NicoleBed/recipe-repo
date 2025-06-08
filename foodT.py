import pymysql
import cryptography
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter import filedialog
import tkinter.font as tkFont
from tkinter import ttk
from datetime import datetime
import datetime

'''wanted additions:
1. add option in addmenu() for user to view all valid ingredients
      -dropbox has all valid ingredients
2. add option in valing() to see similar ingredients such as if user entered generic ingredient such as
   onion, program will show all onions (yellow onion, white onion, red onion, onion powder)
      -dropbox updates as user types
'''

'''still needed
1-. ensure no user ingredients are already in their pantry
2-. ensure user does not add the same ingredient twice before commit
'''


def fra():
      global root
      global adder
      global remo
      global edi
      global vie
      global scriptfont20
      global scriptfont16
      global scriptfont14
      root = Tk()
      root.title('HomeDinner')
      root.iconbitmap('c:/Users/nicbe/OneDrive/Desktop/Python/test/images/mixbowl.ico')
      root.geometry("1200x700")
      scriptfont20 = tkFont.Font(family="Monotype Corsiva", size=20, weight=tkFont.NORMAL)
      scriptfont16 = tkFont.Font(family="Monotype Corsiva", size=16, weight=tkFont.NORMAL)
      scriptfont14 = tkFont.Font(family="Monotype Corsiva", size=14, weight=tkFont.NORMAL)
      root.configure(background="#24dc9d")
      adder = LabelFrame(root, text="ADD INGREDIENTS", padx=5, pady=5) #frame for add ingredients function
      remo = LabelFrame(root, text="REMOVE INGREDIENTS", padx=5, pady=5, bg="white") #frame for remov ingredients function
      edi = LabelFrame(root, text="EDIT INGREDIENTS", padx=5, pady=5, bg="white")
      vie = LabelFrame(root, text="VIEW PANTRY", padx=5, pady=5, bg="white")
      return root #try to keep at 36

def des_fra():
      root.destroy()

mydb = pymysql.connect(host="localhost",user="root", passwd="Cheetah36527*",database="testdb")
mycursor = mydb.cursor()
#mycursor.execute("CREATE DATABASE testdb")
#mycursor.execute("CREATE TABLE stock (name VARCHAR(255), type INTEGER(10))")
#mycursor.execute("CREATE TABLE pantry (name VARCHAR(255), amount FLOAT(10), type VARCHAR(10))")
mydb.commit()

liquid = ["apple cider vinegar", "apple juice", "balsamic vingar", "beer", "bourbon", "soy sauce", "honey", "worcestershire sauce", 
          "olive oil", "sesame oil", "canola oil", "vegetable oil", "chicken broth", "beef broth", "vanilla extract",
          "white vinegar","milk", "orange juice", "vodka", "gin", "red wine", "white wine", "cooking wine", "butter",
          "heavy cream", "whole milk"]
    
spice = ["salt", "pepper", "cinnamon", "nutmeg", "oregano", "rosemary", "basil", "garlic powder", "cayenne pepper", "paprika", 
         "bay leaves", "chili powder", "ginger", "brown gravy", "taco seasoning", "sloppy joes", "onion powder", "italian seasoning", 
         "salsa", "scallion", "ranch seasoning"]
    
dry = ["flour", "sugar", "cornstarch", "brown sugar", "baking soda", "baking powder", "bread crumbs", "fettuccine", "crackers", "rice",
       "peanut butter", "jelly", "frozen peas", "frozen corn", "frozen berry medley", "powdered sugar", "parmesan cheese", "elbow macaroni",
       "cheddar cheese", "pepper jack cheese", "blue cheese"]
    
object = ["garlic cloves", "potato", "tomato", "bell pepper", "cucumber", "strawberry", "blueberry", "rasberry", "banana", "orange", 
          "pineapple", "taco shell", "tortilla", "hamburger buns", "hotdog rolls", "sub rolls", "baguette", "loaf of bread", "bagel", 
          "egg", "lettuce", "lemon", "lime", "carrot", "apple", "avocado", "yellow onion", "white onion", "red onion", "celery"]
    
can = ["cream of chicken soup", "cream of mushroom soup", "chicken broth", "vegetable broth", "tomato paste", "kidney beans",
       "black beans", "diced tomatoes and green chiles", "chunk chicken breast", "corn", "petite diced tomatoes", 
       "green beans", "baked beans", "tomato sauce", "cranberry sauce", "chili", "petite diced tomatoes"]
    
condiments = ["ketchup", "mustard", "relish", "mayonnaise", "ranch", "bbq sauce", "hot sauce"]

meats = ["shrimp", "ground beef", "ground chicken", "ribeye", "sirloin", "flank steak", "pork chops", "boneless skinless chicken thigh",
       "boneless skinless chicken breast", "hamburger patties", "chicken cutlets", "sausage", "salmon", "chicken thighs", "chicken breast",
       "chicken wings"]


sqlFormula = "INSERT INTO stock (name, type) VALUES (%s, %s)"
#1 = oz, 2 = object, 3 = lbs
'''for x in range(0, 26):
      ings = (liquid[x], 1)
      mycursor.execute(sqlFormula, ings)
for x in range(0, 22):
      ings = (spice[x], 1)
      mycursor.execute(sqlFormula, ings)
for x in range(0, 21):
      ings = (dry[x], 1)
      mycursor.execute(sqlFormula, ings)
for x in range(0, 17):
      ings = (can[x], 1)
      mycursor.execute(sqlFormula, ings)
for x in range(0, 7):
      ings = (condiments[x], 1)
      mycursor.execute(sqlFormula, ings)
for x in range(0, 30):
      ings = (object[x], 2)
      mycursor.execute(sqlFormula, ings)
for x in range(0, 16):
      ings = (meats[x], 3)
      mycursor.execute(sqlFormula, ings)'''
#mydb.commit()
#temp ingredient holders
stockitem = []
stocknum = []
stocktype = []
dat = []
'''order of function definitions
      fra(): line 22
      test(): line 115
      addmenu(): line 123
      userin(): line 165
      valing(ing, amo): line 206
      dislist(): line 288
      is_float(sto): line 292
      remov(): line 299
      edit(): line 346
      clea(): line 383
      showall(): line 392
      '''
#test certain parts of functions. changes based on test
def test():
      viewp()


#give test room. keep this comment at line 121

#all functions for adding an ingredient
def addmenu(): #add ingredients to user pantry
      #variables
      global ingredient
      global amount
      global adder
      global alis
      global months
      global days
      global years
      var = IntVar()
      #frame
      adder.grid(row=2, columnspan=3, rowspan=3, sticky="w")

      alis = []
      chemp = "SELECT name FROM stock" #get all pantry
      mycursor.execute(chemp)
      for i in mycursor.fetchall():
            alis.append(i[0])

      #prompt for ingredient name
      inin = Label(adder, text="Enter an ingredient: ", anchor="w", font=scriptfont16)
      inin.grid(row=2, column=0, columnspan=2, sticky="w")
      ingredient = ttk.Combobox(adder, values=alis) #dropdown of all valid ingredients
      ingredient.grid(row=2, column=3, columnspan=3, sticky="w")
      ingredient.bind("<KeyRelease>", upad) #dropdown update as user types

      #prompt for amount
      amin = Label(adder, text="Enter ingredient amount: ", anchor="w", font=scriptfont16)
      amin.grid(row=3, column=0, columnspan=2, sticky="w")
      amount = Entry(adder, width=40)
      amount.grid(row=3, column=3, columnspan=3, sticky="w")

      #ingredient expiration date
      ex = Label(adder, text="Enter expiration date: ", anchor="w", font=scriptfont16)
      ex.grid(row=4, column=0, columnspan=2, sticky="w")

      mon = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
      months = ttk.Combobox(adder, values=mon, width=10)
      months.grid(row=4, column=3, sticky="w")

      d = range(1, 31)
      dli = list(d)
      days = ttk.Combobox(adder, values=dli, width=10)
      days.grid(row=4, column=4, sticky="w")

      y = range(2025, 2050)
      yli = list(y)
      years = ttk.Combobox(adder,values=yli, width=10)
      years.grid(row=4, column=5, sticky="w")

      #confirm button
      ingcon = Button(adder, text="Confirm", command=lambda: valing(ingredient.get(), amount.get()), font=scriptfont16)
      ingcon.grid(row=0, column=3, sticky="w")

      #quit button
      quitb = Button(adder, text="Back", command=lambda: var.set(1), font=scriptfont16)
      quitb.grid(row=0, column=0)

      quitb.wait_variable(var) #wait for quit button to be pressed before ending
      '''add = "INSERT INTO pantry (name, amount, type, expire) VALUES (%s, %s, %s, '%s')" #sql command for adding user input to pantry
      for x in range(len(stocknum)): #execute add
            ip = dat[x]
            print(type(ip))
            ire = (stockitem[x], stocknum[x], stocktype[x])
            mycursor.execute(add, ire)
      #clear temp ingredient holders
      stockitem.clear()
      stocknum.clear()
      stocktype.clear()
      dat.clear()
      mydb.commit()'''
      adder.grid_forget() #hide frame
      return 2 #go back to options menu

def userin(): #no longer used except for text version
      addsto = True
      while (addsto):
            ingredients = input("Enter the ingredient name(enter q to quit): ").lower() 
            if ingredients == "q": #quit
                  add = "INSERT INTO pantry (name, amount, type) VALUES (%s, %s, %s)"
                  for x in range(len(stocknum)):
                        ire = (stockitem[x], stocknum[x], stocktype[x])
                        mycursor.execute(add, ire)
                  stockitem.clear()
                  stocknum.clear()
                  stocktype.clear()
                  mydb.commit()
                  keepstock = False
                  break
            if ingredients.isdigit(): 
                print("- Invalid ingredient -")
                continue
            material = valing(ingredients) #compare to ingredient database
            stockitem.append(ingredients)
            if material == 1:
                  stocktype.append("oz")
            elif material == 2:
                    stocktype.append(ingredients)
            elif material == 3:
                stocktype.append("lb")
            while (material != -1): #starts as invalid to make quit work
                  if material == 1:
                        stock = input("Enter the ingredient amount in ounces (oz): ")
                  elif material == 2:
                        stock = input("Enter the number of ingredients: ")
                  elif material == 3:
                        stock = input("Enter the weight of the ingredient in pounds (lb): ")
                  if is_float(stock) == True:
                        stock = float(stock)
                        stocknum.append(stock)
                        material = -1
                  else:
                        print("- Invalid Amount -")
      return

def valing(ing, amo): #make sure ingredients are valid
      mon = months.get()
      if mon == 'January':
            mont = 1
      elif mon == 'February':
            mont = 2
      elif mon == 'March':
            mont = 3
      elif mon == 'April':
            mont = 4
      elif mon == 'May':
            mont = 5
      elif mon == 'June':
            mont = 6
      elif mon == 'July':
            mont = 7
      elif mon == 'August':
            mont = 8
      elif mon == 'September':
            mont = 9
      elif mon == 'October':
            mont = 10
      elif mon == 'November':
            mont = 11
      elif mon == 'December':
            mont = 12
      else:
            mont = None

      #liquid, spice, dry, can, condiments (ounces) = 1; object (#) = 2; meats (lbs) = 3
      ing = ing.lower() #user input to lowercase
      sea = "SELECT type FROM stock WHERE name = %s" #search stock for ingredient name
      see = "SELECT type FROM pantry WHERE name = %s" #search pantry for ingredient name
      mycursor.execute(sea, ing) 
      search = mycursor.fetchall()
      mycursor.execute(see, ing)
      seerch = mycursor.fetchall()
      if (is_float(amo) == True): #if amount is invalid
            sto = float(amo)    
      else: #error
            ingredient.delete(0, END)
            amount.delete(0, END)
            response = messagebox.showerror("Warning", "Invalid Amount or Ingredient")
            return
      
      #deprecated method
      '''#ensure no duplicates / - -
      if len(seerch) != 0: #if item already in pantry table (users pantry)
            ingredient.delete(0, END)
            amount.delete(0, END)
            response = messagebox.showerror("Warning", "Ingredient Already in your Pantry")
            return
      for x in range(len(stocknum)): #if item has already been entered but not in pantry yet
            if stockitem[x] == ing:
                  ingredient.delete(0, END)
                  amount.delete(0, END)
                  response = messagebox.showerror("Warning", "Ingredient Already Entered")
                  return
      # - - /'''

      if len(search) == 0: #if ingredient is not in stock #idea 
            ingredient.delete(0, END)
            amount.delete(0, END)
            response = messagebox.showerror("Warning", "Invalid Amount or Ingredient")
            return
      
      else: #search has parenthesis around entries, this just removes them
            pop = search[0]
            pop = str(pop)
            pop = pop[1]
            pop = int(pop)
            if pop == 1: #add ingredient
                  types ="oz"
            elif pop == 2:
                    types = "objects"
            elif pop == 3:
                types = "lb"

            stock = ing
            ingredient.delete(0, END)
            amount.delete(0, END)

            add = "INSERT INTO pantry (name, amount, type, expire) VALUES (%s, %s, %s, %s)" #sql command for adding user input to pantry
            
            yea = int(years.get())
            da = int(days.get())
            ad = datetime.datetime(yea, mont, da)
            str_now = ad.strftime("%Y-%m-%d")

            ire = (stock, amo, types, str_now)
            mycursor.execute(add, ire)

            mydb.commit()
            return
      return 4

      '''check = len(stockitem)
       for i in range(len(liquid)):
             if liquid[i] == ing:
                   return 1
       for i in range(len(spice)):
             if spice[i] == ing:
                   return 1
       for i in range(len(dry)):
             if dry[i] == ing:
                   return 1
       for i in range(len(object)):
             if object[i] == ing:
                   return 2
       for i in range(len(can)):
             if can[i] == ing:
                   return 1
       for i in range(len(condiments)):
             if condiments[i] == ing:
                   return 1
       for i in range(len(meats)):
             if meats[i] == ing:
                   return 3
       if check == len(stockitem):
             print("- Invalid ingredient -")
             return -1'''
      return 4

def is_float(sto):
      try:
            float(sto)
            return True
      except ValueError:
            return False

def upad(event): #update dropbox as user types
      tyte = ingredient.get()
      neop = [option for option in alis if tyte.lower() in option.lower()]
      ingredient['values'] = neop

#all functions for removing an ingredient      
def remov(): #remove an ingredient
      #variable
      global remo
      global shn
      global comdrop
      global rlis
      global exp
      shn = Label(remo, font=scriptfont16)
      exp = Label(remo, font=scriptfont16)
      var = IntVar()

      #frame
      remo.grid(row=2, columnspan=3, sticky="w", rowspan=3)
      
      #check if list is empty (on hold till rest of function is made)
      rlis = []
      chemp = "SELECT name FROM pantry" #get all pantry
      mycursor.execute(chemp) 
      for i in mycursor.fetchall():
            rlis.append(i[0])
 
      if len(rlis) == 0: #error if pantry is empty
            response = messagebox.askyesno("Warning", "Pantry is empty")
            return  
      #spacers
      for i in range(0, 20):
            sp0 = Label(remo, text="+---+", anchor="w")
            sp0.grid(row=15, column=i, sticky="w")
      for i in range(0, 10):
            sp1 = Label(remo, text=" ")
            sp1.grid(row=i, column=0)

      #label
      inrein = Label(remo, text=" What ingredient would you like to remove?: ", anchor="e", font=scriptfont16)
      inrein.grid(row=0, column=0, columnspan=8, sticky="w")

      #dropdown take 2 - still cant figure out the random {} on some entries
      comdrop = ttk.Combobox(remo, values=rlis, height=20, font=scriptfont16)
      comdrop.grid(row=0, column=8, columnspan=4)
      comdrop.bind("<KeyRelease>", rmad) #dropdown update as user types

      #remove label
      promt = Label(remo, text="Remove: ", font=scriptfont16, anchor="w")
      promt.grid(row=2, column=0, columnspan=2, sticky="w")

      #expire date
      expt = Label(remo, text="Expires: ", font=scriptfont16, anchor="w")
      expt.grid(row=3, column=0, columnspan=2, sticky="w")

      #confirm
      rcon = Button(remo, text=" Confirm ", command=lambda: remo1(comdrop.get()), anchor="center", padx=5, pady=0, font=scriptfont14)
      rcon.grid(row=0, column=12, columnspan=4, sticky="w")

      #quit button
      quitb = Button(remo, text=" Back ", command=lambda: var.set(1), anchor="center", padx=5, font=scriptfont16)
      quitb.grid(row=9, column=0, columnspan=3, sticky="w", ipadx=5)

      quitb.wait_variable(var) #wait for quit button to be pressed before ending
      remo.grid_forget() #hide frame
      return -1


      '''amin = Label(adder, text="Enter ingredient amount (oz, #, or lb): ", anchor="w")
      amin.grid(row=3, column=0)
      amount = Entry(adder, width=50)
      amount.grid(row=3, column=1, columnspan=2)'''

      


      '''if (len(stockitem) == 0): #check temp. no longer needed
            print("List is empty. Please add ingredients")
            return
      rem = "pop"
      loo = -1
      c = 1
      d = 2
      while loo != 4: #also check to make sure ingredient is in user stock
            rem = input("What item would you like to remove?: ")
            for x in range(len(stockitem)):
                  if stockitem[x] == rem:
                        loo = 4
                        break
      for x in range(len(stockitem)):
            if stockitem[x] == rem:
                  print(f"{(stockitem[x]):<20}: {(stocknum[x]):<5} {(stocktype[x])}")
                  while c != -1:
                        ans = input("Would you like to remove this ingredient?(y/n): ").lower()
                        if ans == "y":
                              stockitem.pop(x)
                              stocknum.pop(x)
                              stocktype.pop(x)
                              dislist()
                              return
                        elif ans == "n":
                              while d != -1:
                                    anst = input("would you like to remove another entry instead(y/n): ").lower()
                                    if anst == "y":
                                          remov()
                                    elif anst == "n":
                                          return
                                    else:
                                          continue
                        else:
                              print("- Invalid Choice -")
                              continue'''

def remo1(na):
      #check for blank entry or invalid item
      check = []
      for x in range(len(na)):
            check.append(" ")
      checked = ''.join(check)
      che = "SELECT name FROM pantry WHERE name=%s"
      mycursor.execute(che, na)
      fin = mycursor.fetchall()

      if (na == checked) or (len(fin) == 0): #error
            response = messagebox.showerror("Invalid", "Item not in your pantry")
            comdrop.delete(0, END)
            return
      
      #search to get amount and type
      see = "SELECT amount FROM pantry WHERE name=%s"
      sea = "SELECT type FROM pantry WHERE name=%s"
      exps = "SELECT expire FROM pantry WHERE name=%s"

      #search execute
      lis = []
      lis.append(na)
      lis.append(":")
      mycursor.execute(see, na)
      for i in mycursor.fetchall():
            lis.append(i[0])
      #seerch = mycursor.fetchall()
      mycursor.execute(sea, na)
      for i in mycursor.fetchall():
            lis.append(i[0])
      #search = mycursor.fetchall()
      conv = map(str, lis)
      ent = ' '.join(conv)

      mycursor.execute(exps, na)
      axp = mycursor.fetchall()

      #labels
      '''for i in mycursor.fetchall():
            lis.append(i[0])'''
      shn.grid(row=2, column=2, columnspan=5, sticky="w")
      shn.config(text=ent)
      exp.grid(row=3, column=2, sticky="w")
      exp.config(text=axp)
      ye = Button(remo, text="  - Yes -  ", font=scriptfont16, command=lambda: gone(na))
      ye.grid(row=4, column=1, columnspan=2)
      no = Button(remo, text="  - No -  ", font=scriptfont16, command=nope)
      no.grid(row=4, column=4, columnspan=2)
      return

def gone(ing):
      gon = "DELETE FROM pantry WHERE name=%s"
      mycursor.execute(gon, ing)
      mydb.commit()
      shn.config(text=" ")
      lis = []
      chemp = "SELECT name FROM pantry" #get all pantry
      mycursor.execute(chemp) 
      for i in mycursor.fetchall():
            lis.append(i[0])
      comdrop['values'] = lis
      comdrop.delete(0, END)
      return

def nope():
      shn.config(text=" ")
      comdrop.delete(0, END)
      return

def rmad(event): #update dropbox as user types
      tyte = comdrop.get()
      neop = [option for option in rlis if tyte.lower() in option.lower()]
      comdrop['values'] = neop

#edit
def edit():
      #variables
      global elis
      global edidrop
      global shna
      var = IntVar()
      shna = Label(edi, font=scriptfont16)

      for i in range(0, 5):
            s = Label(edi, text="", font=scriptfont16).grid(row=i, column=0)

      #frame
      edi.grid(row=2, columnspan=3, sticky="w", rowspan=3)

      #check if empty
      elis = []
      chemp = "SELECT name FROM pantry" #get all pantry
      mycursor.execute(chemp) 
      for i in mycursor.fetchall():
            elis.append(i[0])

      if len(elis) == 0: #error if pantry is empty
            response = messagebox.askyesno("Warning", "Pantry is empty")
            return
      
      #promt label
      prom = Label(edi, text="What ingredients would you like to edit?: ", anchor="w", font=scriptfont16)
      prom.grid(row=0, column=0, columnspan=5, sticky="w")

      #combobox enter ingredient
      edidrop = ttk.Combobox(edi, values=elis)
      edidrop.grid(row=0, column=5, columnspan=2)
      edidrop.bind("<KeyRelease>", edad)

      #confirm button
      con = Button(edi, text="Confirm", command=lambda: ed(edidrop.get()), anchor="center", font=scriptfont16)
      con.grid(row=0, column=7, columnspan=2)

      #quit button
      quitb = Button(edi, text=" Back ", command=lambda: var.set(1), anchor="center", padx=5, font=scriptfont16)
      quitb.grid(row=4, column=0, columnspan=3, sticky="w", ipadx=5)

      quitb.wait_variable(var) #wait for quit button to be pressed before ending
      edi.grid_forget() #hide frame
      return -1


      '''pseudocode
      ask user for ingredient they want to edit
      show ingredient
      entry box for new amount
      confirmation
      update database
      '''

      '''loo = -1
      material = 0
      while loo != 4: #also check to make sure ingredient is in user stock
            rem = input("What item would you like to edit?: ")
            for x in range(len(stockitem)):
                  if stockitem[x] == rem:
                        loo = 4
      for x in range(len(stockitem)):
            if stockitem[x] == rem:
                  print(f"{(stockitem[x]):<20}: {(stocknum[x]):<5} {(stocktype[x])}")
                  hold = stocknum[x]
                  ans = input("Is this the entry you would like to edit?(y/n): ").lower()
                  if ans == "y":
                        while material != -1:
                              num = input("Enter new amount: ")
                              if is_float(num) == True:
                                    stock = float(num)
                              else:
                                    print("- Invalid Amount -")
                              print(f"Previous amount: {hold}; New amount: {stock}")
                              ansy = input("Are you sure about this change?(y/n): ").lower()
                              if ansy == "y":
                                    stocknum[x] = stock
                                    #dislist()
                                    return
                              elif ansy == "n":
                                    continue     
                  if ans == "n":
                        anst = input("Would you like to edit a different entry?(y/n): ").lower()
                        if anst == "y":
                              edit()
                        elif anst == "n":
                              return
                        else:
                              print("- Invalid Choice -")'''

def ed(ing):
      global neamo
      check = []
      for x in range(len(ing)):
            check.append(" ")
      checked = ''.join(check)
      che = "SELECT * FROM pantry WHERE name=%s"
      mycursor.execute(che, ing)
      fin = mycursor.fetchall()

      if (ing == checked) or (len(fin) == 0): #error
            response = messagebox.showerror("Invalid", "Item not in your pantry")
            edidrop.delete(0, END)
            return
      
      see = "SELECT amount FROM pantry WHERE name=%s"
      sea = "SELECT type FROM pantry WHERE name=%s"

      #search execute
      lis = []
      lis.append(ing)
      lis.append(":")
      mycursor.execute(see, ing) #get amount from pantry
      for i in mycursor.fetchall():
            lis.append(i[0])
            a = i
      mycursor.execute(sea, ing) #get type from pantry
      for i in mycursor.fetchall():
            lis.append(i[0])
      #make database entry to 1 string
      conv = map(str, lis)
      ent = ' '.join(conv)

      #label for old entry
      aed = Label(edi, text="Edit: ", font=scriptfont16)
      aed.grid(row=1, column=0, sticky="w")

      #update with user button
      shna.grid(row=1, column=1, columnspan=4, sticky="w")
      shna.config(text=ent)

      #label and input for new entry amount
      aaed = Label(edi, text="New amount: ", font=scriptfont16)
      aaed.grid(row=2, column=0, sticky="w")

      neamo = Entry(edi, width=15, font=scriptfont16)
      neamo.grid(row=2, column=1, columnspan=2, sticky="w")

      #yes or no
      y = Button(edi, text="- Yes -", command=lambda: yeedi(neamo.get(), ing), font=scriptfont16) #get new amount and ingredient
      y.grid(row=3, column=0)
      n = Button(edi, text="- No -", command=noedi, font=scriptfont16)
      n.grid(row=3, column=1)
      return

def edad(event): #update dropbox as user types
      tyte = edidrop.get()
      neop = [option for option in rlis if tyte.lower() in option.lower()]
      edidrop['values'] = neop

def yeedi(a, ing):
      up = "UPDATE pantry SET amount=%s WHERE name=%s" #command to update entry
      ua = (a, ing) #entry as 1 item
      mycursor.execute(up, ua) #execute
      mydb.commit() #commit
      edidrop.delete(0, END)
      shna.config(text="")
      neamo.delete(0, END)
      return

def noedi():
      edidrop.delete(0, END)
      shna.config(text="")
      neamo.delete(0, END)
      return

#view pantry
def viewp():
      global vie
      var = IntVar()
      vie.grid(row=2, columnspan=3, sticky="w", rowspan=3)
      v = "SELECT * FROM pantry"
      mycursor.execute(v)
      result = mycursor.fetchall()
      i = 1
      for row in result:
            ing1 = Label(vie, text=row[0], font=scriptfont16)
            ing1.grid(row=i, column=0, sticky="w")
            ing2 = Label(vie, text=row[1], font=scriptfont16)
            ing2.grid(row=i, column=1, sticky="w")
            ing3 = Label(vie, text=row[2], font=scriptfont16)
            ing3.grid(row=i, column=2, sticky="w")
            i = i + 1

      

      #quit button
      quitb = Button(vie, text=" Back ", command=lambda: var.set(1), anchor="center", padx=5, font=scriptfont16)
      quitb.grid(row=0, column=0, columnspan=3, sticky="w", ipadx=5)

      quitb.wait_variable(var) #wait for quit button to be pressed before ending
      quitb.grid_forget()
      ing1.grid_forget()
      vie.grid_forget() #hide frame
      return -1

#clear
def clea():
      sql = "DROP TABLE IF EXISTS pantry"
      mycursor.execute(sql)
      mydb.commit()
      mycursor.execute("CREATE TABLE pantry (name VARCHAR(255), amount INTEGER(10), type VARCHAR(10))")
      mydb.commit()
      return

def showall():
      print("show all")
