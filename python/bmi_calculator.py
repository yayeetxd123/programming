print("Bmi Calculator")
case = 1
running = True
while running:
    try:
        print("Case {}".format(case))
        name = str(input("Enter Name: "))
        height = float(input("Enter Height/m: "))
        weight = int(input("Enter Weight/kg: "))

        bmi_calculation = weight / (height ** 2)
        print("Bmi of {} is {}".format(name,bmi_calculation))
        case += 1

        if bmi_calculation <= 25:
            print("{} is not overweight".format(name))

        elif bmi_calculation > 25:
            print("{} is overweight".format(name))

    except ValueError:
        print("Error! Try using a number")
        running = False

    print()
