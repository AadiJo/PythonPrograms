def median(Numbers1):
    Numbers1.sort()
    length1 = len(Numbers1)
    remainder = length1 % 2
    if length1 == 1:
        median2 = Numbers1[0]
    if remainder == 1:
        length1 += 1
        i = length1 / 2
        i -= 1
        i = int(i)
        median2 = Numbers1[i]
    if remainder == 0:
        m1 = int((length1 / 2) - 1)
        m2 = int((m1 + 1))
        median1 = (Numbers1[m2] + Numbers1[m1]) / 2
        median2 = float(median1)
    print('\nThe median is', median2, "\n")


def average(Numbers1):
    sum2 = sum(Numbers1)
    length1 = len(Numbers1)
    Avg = float(sum2 / length1)
    print("\nThe average is", Avg, "\n")


def range_1(Numbers1):
    length1 = len(Numbers1)
    if length1 == 1:
        range1 = Numbers1[0]
    else:
        Numbers1.sort()
        range1 = Numbers1[-1] - Numbers1[0]
    print("\nThe range is", range1, "\n")


def mean(Numbers1):
    length1 = len(Numbers1)
    if length1 == 1:
        mean1 = Numbers1[0]
        print("\nThe mean is", mean1, "\n")
    else:
        Numbers1.sort()
        mean1 = Numbers1[-1] + Numbers1[0]
        MeanReal = float(mean1 / 2)
        print("\nThe mean is", MeanReal, "\n")


def mode(Numbers1):
    length = len(Numbers1)
    i = 0
    if length == 1:
        Mode = Numbers1[0]
    else:
        Numbers1.sort()
        ModeVal = {}
        for x in Numbers1:
            if Numbers1[i] in ModeVal:
                ModeVal[Numbers1[i]] += 1
            else:
                ModeVal.update({Numbers1[i]: 1})
            i += 1
        import operator

        ModeList = sorted(ModeVal.items(), key=operator.itemgetter(1))
        Mode1 = str(ModeList[-1])
        x = Mode1.rsplit(",")
        y = str(x[0])
        z = y.rsplit("(")
        Mode = z[1]
    print("\nThe mode is", Mode, "\n")


File = input("Please give file location: ")
File2 = open(File, "r")
Numbers = []
for x in File2:
    Numbers.append(int(x))
median(Numbers)
average(Numbers)
range_1(Numbers)
mean(Numbers)
mode(Numbers)

print("\nThank you for using the Statistics Program")
