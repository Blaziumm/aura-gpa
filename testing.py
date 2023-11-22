scoreRequiredforA = 90
scoreRequiredforB = 80
scoreRequiredforC = 70
scoreRequiredforD = 60

def numbergradetoletter(grade):
    try:
        print(round(grade))
        intgrade = round(grade)
        if intgrade < 101 and intgrade > -1:
            if intgrade > scoreRequiredforA or intgrade == scoreRequiredforA:
                return("A")
            elif intgrade >scoreRequiredforB or intgrade == scoreRequiredforB:
                return("B")
            elif intgrade >scoreRequiredforC or intgrade == scoreRequiredforC:
                return("C")
            elif intgrade >scoreRequiredforD or intgrade == scoreRequiredforD:
                return("D")
            elif intgrade< scoreRequiredforD:
                return("E")
            else: 
                return("NUMOUT OF RANGE")
    except ValueError or TypeError:
        if grade == "A" or grade == "B" or grade == "C" or grade == "D" or grade == "E":
            return(grade)
        else: 
            return("OUT OF RANGE")
        


print(numbergradetoletter(60))