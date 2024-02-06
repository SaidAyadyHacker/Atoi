#######################
#                     #
# Coded by saad ayady #
#                     #
#######################
def atoi(nbstr):
    numper = 0
    powr = 1
    if str(nbstr[0]) == '+' :
        if str(nbstr[1]) == '+' :
            return 0
        else :
            powr = 1
    if str(nbstr[0]) == '-':
        if str(nbstr[1]) == '-' :
            return 0
        else :
            powr = -1
    i = 0 
    while i < len(nbstr) :
        if ord(nbstr[i]) >= ord('0') and ord(nbstr[i]) <= ord('9') :
            numper = numper * 10 + int(ord(nbstr[i]) - ord('0'))
        i += 1
    return numper * powr

#### TESTING ####
#print(atoi("12345"))
#print(atoi("+12345"))
#print(atoi("++12345"))
#print(atoi("-12345"))
#print(atoi("--12345"))
#print(atoi("saad12aya34nerjwf5"))
#test = atoi("1392")
#print(type(test))
##################