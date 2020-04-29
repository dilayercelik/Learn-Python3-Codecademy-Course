#Module - Python Functions & Logic: Project

#Question 1: create a function for cost of ground shipping
def cost_groundship(weight):
  if (weight <= 2):
    cost = 1.5*weight + 20
    return cost
  elif (weight > 2) and (weight <= 6):
    cost = 3*weight + 20
    return cost
  elif (weight > 6) and (weight <= 10):
    cost = 4*weight + 20
    return cost
  elif (weight > 10):
    cost = 4.75*weight + 20
    return cost
  
#Question 2: Testing the Function above
##should be equal to 53.6
print(cost_groundship(8.4))

#Question 3: Cost of premium ground shipping (independent of weight of package)
cost_premium_groundship = 125.0

#Question 4: create a function for cost of drone shipping
def cost_droneship(weight):
  if (weight <= 2):
    cost = 4.5*weight 
    return cost
  elif (weight > 2) and (weight <= 6):
    cost = 9*weight 
    return cost
  elif (weight > 6) and (weight <= 10):
    cost = 12*weight 
    return cost
  elif (weight > 10):
    cost = 14.25*weight 
    return cost

#Question 5: Testing the Function above
##should be equal to 6.75
print(cost_droneship(1.5))

#Question 6
def cheapest_ship(weight):
  if (cost_groundship(weight) < cost_droneship(weight)) and (cost_groundship(weight) < cost_premium_groundship):
    print("The cheapest shipping method is the ground shipping and the shipping cost is" + " " + str(cost_groundship(weight)) + ".")
  elif (cost_droneship(weight) < cost_groundship(weight)) and (cost_droneship(weight) < cost_premium_groundship):
    print("The cheapest shipping method is the drone shipping and the shipping cost is" + " " + str(cost_droneship(weight)) + ".") 
  elif (cost_premium_groundship < cost_groundship(weight)) and (cost_premium_groundship < cost_droneship(weight)):
    print("The cheapest shipping method is the premium ground shipping and the shipping cost is" + " " + str(cost_premium_groundship) + ".") 
    
#Question 7 Testing the Function above

##for weight = 4.8, answer: ground shipping of cost = 34.4
print(cheapest_ship(4.8))

###for weight = 41.5, answer: premium ground shipping (125)
print(cheapest_ship(41.5))



                                                
