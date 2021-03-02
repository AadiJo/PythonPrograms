print("Welcome to the Statistics Program!\n")
Numbers = []
i = 1
NumOfNum = int(input("How many numbers do you want to enter: "))
while i <= NumOfNum:
    Number = float(input("Please enter number: "))
    Numbers.append(Number)
    i += 1
options = input(
        "Now, What do you want to do with those numbers? Do you want to\n 1) ""Get the median\n 2) "
        "Get the average\n ""3) ""Get the range\n 4) Get the mean\n 5) Get the mode\n 6) Exit\n "
        " \nPlease enter the number beside ""the action you want to do: ")
while options != "6":
    if options == "1":  
        Numbers.sort()
        length = len(Numbers)
        remainder = length % 2
        if length == 1:
            median = Numbers[0]
        if remainder == 1:
            length += 1
            i = length / 2
            i -= 1
            i = int(i)
            median = Numbers[i]
        if remainder == 0:
            m1 = int((length / 2) - 1)
            m2 = int((m1 + 1))
            median1 = (Numbers[m2] + Numbers[m1]) / 2
            median = float(median1)
        print('\nThe median is', median, "\n")
    if options == "2":
        sum1 = sum(Numbers)
        length = len(Numbers)
        Avg = float(sum1 / length)
        print("\nThe average is", Avg, "\n")
    if options == "3":
        length = len(Numbers)
        if length == 1:
            range1 = Numbers[0]
        else:
            Numbers.sort()
            range1 = Numbers[-1] - Numbers[0]
        print("\nThe range is", range1, "\n")
    if options == "4":
        length = len(Numbers)
        if length == 1:
            mean = Numbers[0]
            print("\nThe mean is", mean, "\n")
        else:
            Numbers.sort()
            mean1 = Numbers[-1] + Numbers[0]
            MeanReal = float(mean1 / 2)
            print("\nThe mean is", MeanReal, "\n")
    if options == "5":
        length = len(Numbers)
        i = 0
        if length == 1:
            Mode = Numbers[0]
        else:
            Numbers.sort()
            ModeVal = {}
            for x in Numbers:
                if Numbers[i] in ModeVal:
                    ModeVal[Numbers[i]] += 1
                else:
                    ModeVal.update({Numbers[i]: 1})
                i += 1
            import operator
            ModeList = sorted(ModeVal.items(), key=operator.itemgetter(1))
            Mode1 = str(ModeList[-1])
            x = Mode1.rsplit(",")
            y = str(x[0])
            z = y.rsplit("(")
            Mode = z[1]
        print("\nThe mode is", Mode, "\n")
    options = input(
        "Now, What else do you want to do with those numbers? Do you want to\n 1) ""Get the median\n 2) "
        "Get the average\n ""3) ""Get the range\n 4) Get the mean\n 5) Get the mode\n 6) Exit\n "
        " \nPlease enter the number beside ""the action you want to do: ")
print("\nThank you for using the Statistics Program")
