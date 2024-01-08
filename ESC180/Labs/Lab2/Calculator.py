def my_sqrt(x):
    global sqr
    sqr = x**.5
    return sqr

def my_print_square(x):
    print(x**.5)
    return

def memorize():
    global memory
    global curr_value
    memory = curr_value

def recall():
    global memory
    global curr_value
    update_prev_value()
    curr_value = memory

def display_current_value():
    global curr_value
    print("Current value:", curr_value)
    return


def update_prev_value():
    global prev_value, prev_value_2, curr_value
    prev_value_2 = prev_value
    prev_value = curr_value
    return

def add(to_add):
    update_prev_value()
    global curr_value
    curr_value += to_add
    return

def mult(to_mult):
    update_prev_value()
    global curr_value
    curr_value *= to_mult
    return

def div(to_div):
    update_prev_value()
    global curr_value
    #problems occur when to_div = 0
    curr_value /= to_div
    return

def undo():
    global curr_value, prev_value
    temp = curr_value
    curr_value = prev_value
    prev_value = temp
    return

def undo2():
    global curr_value, prev_value, prev_value_2
    temp_prev_2 = prev_value
    prev_value = curr_value
    curr_value = prev_value_2
    prev_value_2 = temp_prev_2
    



if __name__ == "__main__":

    #res = my_sqrt(25)
    #print(res)
    #res = my_print_square(25)
    #print(res)

    curr_value = 0
    prev_value = 0
    prev_value_2 = 0
    memory = 0

    print("Welcome to the calculator program.")
    # display_current_value()
    # add(5)
    # display_current_value()
    # mult(15)
    # display_current_value()
    # memorize()
    # display_current_value()
    # add(20)
    # display_current_value()
    # div(5)
    # display_current_value()
    # recall()
    # display_current_value() #75
    # undo()
    # display_current_value()
    # undo()
    # display_current_value()
    display_current_value()
    add(1)
    display_current_value()
    mult(2)
    display_current_value()
    undo()
    display_current_value()
    add(5)
    display_current_value()
    undo2()
    display_current_value()
