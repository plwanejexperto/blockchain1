hexa = '0xa5839F87f0cC7409842a238aA28BE2D051D9B948'
deci = str(int(hexa,16))
summ = 0
for i in deci:
    summ += int(i)

print(summ)
