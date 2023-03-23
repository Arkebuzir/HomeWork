'''def show_line():                    #первый пример16
    print("""“Don't let the noise of others' opinions
drown out your own inner voice.”
Steve Jobs""")
show_line()

def unchet(a,b):        #второй пример
    for i in range(a,b):
        if i%2!=0: print(i,end=" ")
unchet(1,10)

def strike(length,side,symbol):     #третий пример
    if side:
        print(symbol*length)
    else:
        for i in range(length):
            print(symbol)
strike(7,False,"*")

def show_max(a,b,c,d):      #четвертый пример
    maximum=max(a,b,c,d)
    print(maximum)
show_max(3,5,7,2)

def show_sum(a,b):          #пятый пример
    summa=0
    for i in range(a,b+1):
        summa+=i
    print(summa)
show_sum(1,10)

def simple(n):              #шестой пример
    for i in range(2, int((n**0.5))+2):
        if n%i==0: return False
    return True
print(simple(7))

def magic(num):
    if int(num[0])+int(num[1])+int(num[2])==int(num[3])+int(num[4])+int(num[5]):
        return True
    else: return False
print(magic("123420"))

def magic(num):
    return int(num[0])+int(num[1])+int(num[2])==int(num[3])+int(num[4])+int(num[5])
print(magic("123420"))
'''