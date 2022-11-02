from math import sqrt 
n = int(input())
f = 2
s = ''


while f <= n:
    if n % f == 0:
        t = 0
        
        while n % f == 0:
            n //= f
            t += 1
    
        if s != '':
            s += ' * '
    
        s += str(f)
    
        if t > 1:
         s +=  '^' + str(t)

    if f == 2:
        f -= 1
    f += 2

if s == '':
    s = str(n)

print(s)