"""
winter = ['dec','jan','feb']
spring = ['mar', 'apr', 'may']
summer = ['jun', 'jul', 'aug']
fall   = ['sep', 'oct', 'nov']

def getseason():
    month1 = raw_input('Please input the month:')
    month = month1.lower()



    if month in winter:
        return 'winter';
    elif month in spring:
        return 'spring';
    elif month in summer:
        return 'summer';
    elif month in fall:
        return 'fall';
    else:
        return 'Month not found.'

print(getseason())

def getcelsius(F):
    #    F = float(raw_input('Please input the Farenheit:'))
    C = (F-32)/1.8
    C1=round(C,2)
    return C1

#print('Result: '+str(getcelsius()))

def getfahrenheit(C):
    #    C = float(raw_input('Please input the Celsius:'))
    F = (C *1.8) +32
    return F
#print('Result: '+str(getfahrenheit()))

def temperature_converter(num,tem):
    #tem = raw_input('Which temperature would you enter?C for celsius or F for farenheit')
    if tem =='C':
        return getcelsius(num);
    elif tem == 'F':
        return getfahrenheit(num);
    else:
        return "Error: Invalid temperature scale; Must be F or C"

print temperature_converter(55,'C')# 12.7777777778
print temperature_converter(10,'F') # 50.0
print temperature_converter(55, 'X') # Error: Invalid temperature scale; Must be `F` or `C`
"""
def vowelCounter(string):
    counter = 0
    for letter in string:
        if letter in 'aeiou':
            counter +=1
    return counter
print vowelCounter('apples') # Expected: 2
print vowelCounter('aeiou') # Expected: 5
print vowelCounter('why') # Expected: 0
print vowelCounter('mississippi') # Expected: 4
