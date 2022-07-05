# Name = Vipan Kumar
# user name = @VipanKumar01

import time
year = int(input("Enter the Year : "))

# Making Year Logic

yearDict = {2001:"A", 2002:"B", 2003:"C", 2004:"K", 2005:"F", 2006:"G", 2007:"A", 2008:"I", 2009:"D", 2010:"E",
            2011:"F", 2012:"N", 2013:"B", 2014:"C", 2015:"D", 2016:"L", 2017:"G", 2018:"A", 2019:"B", 2020:"J", 
            2021:"E", 2022:"F", 2023:"G", 2024:"H", 2025:"C", 2026:"D", 2027:"E", 2028:"M", 2029:"A", 2030:"B", 
            2031:"C", 2032:"K", 2033:"F", 2034:"G", 2035:"A", 2036:"I", 2037:"D", 2038:"E", 2039:"F", 2040:"N", 
            2041:"B", 2042:"C", 2043:"D", 2044:"L", 2045:"G", 2046:"A", 2047:"B", 2048:"J", 2049:"E", 2050:"F", 
            2051:"G", 2052:"H", 2053:"C", 2054:"D", 2055:"E", 2056:"M", 2057:"A", 2058:"B", 2059:"C", 2060:"K", 
            2061:"F", 2062:"G", 2063:"A", 2064:"I", 2065:"D", 2066:"E", 2067:"F", 2068:"N", 2069:"B", 2070:"C", 
            2071:"D", 2072:"L", 2073:"G", 2074:"A", 2075:"B", 2076:"J", 2077:"E", 2078:"F", 2079:"G", 2080:"H", 
            2081:"C", 2082:"D", 2083:"E", 2084:"M", 2085:"A", 2086:"B", 2087:"C", 2088:"K", 2089:"F", 2090:"G", 
            2091:"A", 2092:"I", 2093:"D", 2094:"E", 2095:"F", 2096:"N", 2097:"B", 2098:"C", 2099:"D", 2100:"E",
}


if year in yearDict:
    value = yearDict[year]
    

# Making Months Logic
'''
print("""
      -> Enter Only ->
      Jan
      Feb
      Mar
      Apr
      May
      Jun
      Jul
      Aug
      Sep
      Oct
      Nov
      Dec
      
      """)
'''

month = input("Enter the Month : ")

monthList = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
if month in monthList:
    var = monthList.index(month)


anotherDict = {"A":[1,4,4,7,2,5,7,3,6,1,4,6],
               "B":[2,5,5,1,3,6,1,4,7,2,5,7],
               "C":[3,6,6,2,4,7,2,5,1,3,6,1],
               "D":[4,7,7,3,5,1,3,6,2,4,7,2],
               "E":[5,1,1,4,6,2,4,7,3,5,1,3],
               "F":[6,2,2,5,7,3,5,1,4,6,2,4],
               "G":[7,3,3,6,1,4,6,2,5,7,3,5],
               "H":[1,4,5,1,3,6,1,4,7,2,5,7],
               "I":[2,5,6,2,4,7,2,5,1,3,6,1],
               "J":[3,6,7,3,5,1,3,6,2,4,7,2],
               "K":[4,7,1,4,6,2,4,7,3,5,1,3],
               "L":[5,1,2,5,7,3,5,1,4,6,2,4],
               "M":[6,2,3,6,1,4,6,2,5,7,3,5],
               "N":[7,3,4,7,2,5,7,3,6,1,4,6]
               
               }
# main Logic
if month in monthList:
    if value == "A":
        temp = anotherDict["A"][var]
    elif value == "B":
        temp = anotherDict["B"][var]
    elif value == "C":
        temp = anotherDict["C"][var]
    elif value == "D":
        temp = anotherDict["D"][var]
    elif value == "E":
        temp = anotherDict["E"][var]
    elif value == "F":
        temp = anotherDict["F"][var]
    elif value == "G":
        temp = anotherDict["G"][var]
    elif value == "H":
        temp = anotherDict["H"][var]
    elif value == "I":
        temp = anotherDict["I"][var]
    elif value == "J":
        temp = anotherDict["J"][var]
    elif value == "K":
        temp = anotherDict["K"][var]
    elif value == "L":
        temp = anotherDict["L"][var]
    elif value == "M":
        temp = anotherDict["M"][var]
    elif value == "N":
        temp = anotherDict["N"][var]
        
        
date = int(input("Enter the Date : "))

# Weeks With Name of the Day
W1 = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday",
      "Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday",
      "Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday",
      "Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday",
      "Monday","Tuesday","Wednesday"
      ]

W2 = ["Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday",
      "Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday",
      "Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday",
      "Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday",
      "Monday","Tuesday","Wednesday","Thursday"
      ]

W3 = ["Wednesday","Thursday","Friday","Saturday","Sunday",
      "Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday",
      "Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday",
      "Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday",
      "Monday","Tuesday","Wednesday","Thursday","Friday"
      ]

W4 = ["Thursday","Friday","Saturday","Sunday",
      "Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday",
      "Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday",
      "Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday",
      "Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"
      ]

W5 = ["Friday","Saturday","Sunday",
      "Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday",
      "Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday",
      "Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday",
      "Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"
      ]

W6 = ["Saturday","Sunday",
      "Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday",
      "Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday",
      "Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday",
      "Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday",
      "Monday"
      ]

W7 = ["Sunday",
      "Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday",
      "Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday",
      "Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday",
      "Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday",
      "Monday","Tuesday"
      ]

print("--------------------------------------------")
print(f"Your Entered Date is : {date} / {month} / {year} ")
print("The Day is : ",end="")

if temp == 1:
    print(W1[date-1])
    
elif temp == 2:
    print(W2[date-1])
    
elif temp == 3:
    print(W3[date-1])
    
elif temp == 4:
    print(W4[date-1])
    
elif temp == 5:
    print(W5[date-1])
    
elif temp == 6:
    print(W6[date-1])
    
elif temp == 7:
    print(W7[date-1])
    
print("--------------------------------------------")
time.sleep(4)
# The Day is shown to your Screen
# --HappyCode--
