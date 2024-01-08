import lab02

def displayTest(condition):
    global testNo
    testNo += 1
    if condition:
        print("Test", testNo, "passed")
    else:
        print("Test", testNo, "failed")


if __name__ == '__main__':
    testNo = 0

    lab02.initialize()
    lab02.add(42)
    displayTest(lab02.get_current_value() == 42)



    lab02.initialize()
    lab02.add(42)
    lab02.undo()
    displayTest(lab02.get_current_value() == 0)

    lab02.initialize()
    lab02.add(2)
    lab02.multiply(3)
    displayTest(lab02.get_current_value() == 6)
