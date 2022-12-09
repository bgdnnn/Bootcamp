from os.path import exists


#========The beginning of the class==========
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
        '''
        In this function, you must initialise the following attributes:
            ● country,
            ● code,
            ● product,
            ● cost, and
            ● quantity.
        '''
    def get_cost(self):
        return self.cost
 
    def get_quantity(self):
        return self.quantity
        
    def __str__(self, *uniq):

        if not uniq:
            return (f"""
|  {self.country:<17} |  {self.code:<10} | {self.product:<25} | {self.cost:<8} | {self.quantity:<6}  |"""  """
-------------------------------------------------------------------------------------   """)
        else:
            return (f"""
|  {self.code:<10} |  {self.product:<20} |  {self.cost*self.quantity:<12}      |
-----------------------------------------------------------------     
            """)
      


#=============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []

#==========Functions outside the class==============
def read_shoes_data():
    
    if exists("inventory.txt"):
        with open("inventory.txt", "r") as text:
            for count, line in enumerate(text):
                if count == 0:
                    continue
                shoe_list.append(Shoe(line.strip(" ").split(",")[0], 
                        line.strip(" ").split(",")[1], line.strip(" ").split(",")[2], 
                        int(line.strip(" ").split(",")[3]), int(line.strip(" ").split(",")[4])))
                
    else:
        print("The file doesn't exist ")
    
def capture_shoes():
    pass
    '''
    This function will allow a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoe list.
    '''

def view_all():
    print(f"""
-------------------------------------------------------------------------------------
|  Country           |  Code       |  Product                  | Cost     | Quantity| 
-------------------------------------------------------------------------------------""")
    for obj in shoe_list:
        print(obj.__str__().strip())

def re_stock():
    
    smallest_quantity = min(line.quantity for line in shoe_list)
    
    for line in shoe_list:
        new_quantity = 0
        if smallest_quantity == line.quantity:
            while True:
                shoe_update_option = input("Would you like to update shoe quantity? Yes/No ").lower
                if shoe_update_option == "yes":
                    while True:
                        try:
                            new_quantity = int(input("Type the new quantity! "))
                            break
                        except:
                            print("You typed wrong quantity! Try again! ")
                    line.quantity = new_quantity
                    changes = True
                    break
                elif shoe_update_option == "no":
                    return
              
    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Ask the user if they
    want to add this quantity of shoes and then update it.
    This quantity should be updated on the file for this shoe.
    '''

def seach_shoe():
    """ for shoes in shoe_list:
        print (shoes.code.strip()) """
    
    found = False
    while True:
        shoe_code = input("Type shoe code to search for it: ").upper()
        for shoes in shoe_list:
            if shoe_code in shoes.code.strip():
                print("""
-------------------------------------------------------------------------------------                
|  Country           |  Code       |  Product                  |  Cost    | Quantity|
-------------------------------------------------------------------------------------""")
                print(shoes.__str__().strip())
                found = True
                break
                
        if found:
            break
        else:
            print("Shoe code not found! Try again!")
            
    '''
     This function will search for a shoe from the list
     using the shoe code and return this object so that it will be printed.
    '''

def value_per_item():
    print("""
------------------------------------------------------------    
|  Code       |  Product              |  Value pe item     |
------------------------------------------------------------    """)
    for obj in shoe_list:
        print(obj.__str__(True).strip())
    
    '''
    This function will calculate the total value for each item.
    Please keep the formula for value in mind: value = cost * quantity.
    Print this information on the console for all the shoes.
    '''

def highest_qty():
    
    return (max(line.quantity for line in shoe_list))

def update_to_file():
    with open("inventory.txt", "w") as text:
        text.write("Country,Code,Product,Cost,Quantity\n")
        for obj in shoe_list:
            text.write(f"{obj.country.strip()},{obj.code.strip()},{obj.product.strip()},{obj.cost},{obj.quantity}\n")
        changes = False


changes = False
#==========Main Menu=============
def menu():
    menu_option = ""
    while True:
        print("""What whould you whant to do?
        #capture shoes --        ca
        #view al --                     va
        #re- stock--                   rs
        #view max quantity--  vm
        
        



'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''
read_shoes_data()
#view_all()
a = highest_qty()
print(a)
#update_to_file()
#value_per_item()
#re_stock()
seach_shoe()
