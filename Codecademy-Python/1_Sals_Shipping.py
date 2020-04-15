def ground_shipping(weight):
  flat_charge = 20.0
  if weight > 10:
    var = 4.75
  elif weight <= 10 and weight > 6:
    var = 4.0
  elif weight <= 6 and weight > 2:
    var = 3.0
  else:
    var = 1.5
  cost = weight * var + flat_charge
  return cost
#print(ground_shipping(8.4))

premium_cost = 125

def drone_shipping(weight):
  flat_charge = 0.0
  if weight > 10:
    var = 14.25
  elif weight <= 10 and weight > 6:
    var = 12.0
  elif weight <= 6 and weight > 2:
    var = 9.0
  else:
    var = 4.5
  cost = weight * var + flat_charge
  return cost
#print(drone_shipping(1.5))

def cheapest_shipping(weight):
  cost_ground = ground_shipping(weight)
  cost_drone = drone_shipping(weight)
  if cost_ground < cost_drone and cost_ground < premium_cost:
    print("Ground shipping it is: $", cost_ground)
  elif cost_drone < cost_ground and cost_drone < premium_cost:
    print("Drone shipping it is: $", cost_drone)
  else:
    print("Premium shipping by ground: $", premium_cost)
    
#Test case 1
cheapest_shipping(4.8)

#Test case 2
cheapest_shipping(41.5)
