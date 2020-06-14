# Project - Basta Fazoolin' (Lesson Module: Classes)


# Question 1-2-7-9
class Menu():

  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time

  def __repr__(self):
    representation =  self.name + ' menu' + ' available from ' + str(self.start_time) + ' to ' + str(self.end_time)

    return representation

  def calculate_bill(self, purchased_items):
    bill = 0
    for item in purchased_items:
      bill += self.items[item]

    return bill



# Question 3
brunch_items = {'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}

brunch = Menu('brunch', brunch_items, 1100, 1600)


# Question 4
early_bird_items = {'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00 }

early_bird = Menu('early bird', early_bird_items, 1500, 1800)


# Question 5
dinner_items = {'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00}

dinner = Menu('dinner', dinner_items, 1700, 2300)

# Question 6
kid_items = {'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}

kid = Menu('kid', kid_items, 1100, 2100)


# Question 8
print(brunch)


# Question 10
purchased_items = ['pancakes', 'home fries', 'coffee']

brunch_bill = brunch.calculate_bill(purchased_items)
print(brunch_bill)


# Question 11
purchased_items = ['salumeria plate', 'mushroom ravioli (vegan)']

early_bird_bill = early_bird.calculate_bill(purchased_items)
print(early_bird_bill)


# Question 12-13-15-16
class Franchise():

  def __init__(self, address, menus):
    self.address = address
    self.menus = menus


  def __repr__(self):
    return self.address


  def available_menus(self, time):
    available = []

    for menu in self.menus:
      if menu.start_time <= time <= menu.end_time:
        available.append(menu)

    return available



# Question 14
all_4_menus = [brunch, early_bird, dinner, kid]

flagship_store = Franchise('1232 West End Road', all_4_menus)

new_installment = Franchise('12 East Mulberry Street', all_4_menus)


# Question 17
var = flagship_store.available_menus(1200)
print(var)

# Question 18
var = flagship_store.available_menus(1700)
print(var)


# Question 19-20
class Business():

  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises


# Question 21
franchises_for_first = [flagship_store, new_installment]
first_business = Business("Basta Fazoolin' with my Heart", franchises_for_first)


# Question 22
items = {'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50}

arepas_menu = Menu('arepa', items, 1000, 2000)


# Question 23
arepas_place = Franchise('189 Fitzgerald Avenue', [arepas_menu])


# Question 24
new_business = Business("Take a' Arepa", [arepas_place])
