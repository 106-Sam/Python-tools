
n = int(input("No of code: \n"))

ad = []
dc = []

def readText():
    for i in range(n):
        txt = input("Enter ascii codes:\n")
        ad.append(txt)

def decodeText():
    for i in range(n):
        a=chr(int(ad[i]))
        dc.append(a)
    
    for i in dc:
        print(i, end="")



readText()
decodeText()
