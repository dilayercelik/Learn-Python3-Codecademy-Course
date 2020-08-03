train_mass = 22680
train_acceleration = 10
train_distance = 100

bomb_mass = 1

#question 1
def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5/9
  return c_temp

#question 2
f100_in_celsius = f_to_c(100)
print(f100_in_celsius)

#question 3
def c_to_f(c_temp):
  f_temp = c_temp * (9/5) + 32
  return f_temp

#question 4
c0_in_fahrenheit = c_to_f(0)
print(c0_in_fahrenheit)

#question 5
def get_force(mass, acceleration): 
  multi = mass * acceleration
  return multi

#question 6
train_force = get_force(train_mass, train_acceleration)
print(train_force)

#question 7
print("The GE train supplies" + " " + str(train_force) + " " + "Newtons of force.")

#question 8
def get_energy(mass, c = 3*10**8):
  result = mass * (c**2)
  return result
  
#question 9
bomb_energy = get_energy(bomb_mass)
print(bomb_energy)
  
#question 10
print("A 1kg bomb supplies" + " " + str(bomb_energy) + " " + "Joules.")

#"Do the Work" part
#question 11
def get_work(mass, acceleration, distance):
  force = mass * acceleration
  work = force * distance
  return work

#question 12
train_work = get_work(train_mass, train_acceleration, train_distance)
print(train_work)

#question 13
print("The GE train does" + " " + str(train_work) + " " + "Joules of work over" + " " + str(train_distance) + " " + "meters.")

