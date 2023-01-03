weight = 3

#Ground Shipping 
if weight <= 2:
  ground_cost = weight * 1.50 + 20.00
elif weight > 2 and weight <= 6 :
  ground_cost = weight * 3.00 + 20.00
elif weight > 6 and weight <= 10 :
  ground_cost = weight * 4.00 + 20.00
else :
  ground_cost = weight * 4.75 + 20.00

print (ground_cost)

premium_ground_cost = 125.00

print(premium_ground_cost)

if weight <= 2:
  drone_cost = weight * 4.50
elif weight > 2 and weight <= 6 :
  drone_cost = weight * 9.00
elif weight > 6 and weight <= 10 :
  drone_cost = weight * 12.00
else :
  drone_cost = weight * 14.25

print (drone_cost)

a = ground_cost
b = premium_ground_cost
c = drone_cost

def minimum_of_two (a,b):
  if a < b :
     return a 
  else:
    return b

def minimum_of_three (a,b,c):
  ab = minimum_of_two (a,b)
  bc = minimum_of_two(b,c)
  answer = minimum_of_two (ab,bc)
  return answer
      

print ("\nThe minimum cost for delivery is: \n"+ str(minimum_of_three(a,b,c)))
