
def drink_coffee():
    global last_coffee_time, last_coffee_time2, too_much_coffee, current_time

    #240, 120, 90
    #0, 0
    too_much_coffee = last_coffee_time >= 0 and last_coffee_time2 >= 0 and current_time - last_coffee_time2 <= 2*60

    last_coffee_time2 = last_coffee_time
    last_coffee_time = current_time
    
    print(knols)
    
def study(minutes):
    # global last_coffee_time, last_coffee_time2, current_time, too_much_coffee, knols, too_much_coffee
    print(last_coffee_time)
    if(last_coffee_time != current_time):
        #had no coffee
        knols += minutes * 5
    elif (last_coffee_time == current_time and not too_much_coffee):
        #had a coffee right before
        knols += minutes * 10

    elif (too_much_coffee):
        #drank too much coffee
        pass

    current_time += minutes

    print(knols)





def initialize():
    global too_much_coffee
    global current_time
    global last_coffee_time
    global last_coffee_time2
    global knols
    too_much_coffee = False
    current_time = 0
    knols = 0
    last_coffee_time = -100
    last_coffee_time2 = -100
    
    
if __name__ == '__main__':
    initialize() # start the simulation
    study(60) # knols = 300
    study(20) # knols = 400
    drink_coffee() # knols = 400
    study(10) # knols = 500
    drink_coffee() # knols = 500
    study(10) # knols = 600
    drink_coffee() # knols = 600, 3rd coffee in 20 minutes
    study(10) # knols = 600