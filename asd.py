A = 3
B = 2
C = 1
D = 0.5
E = 2
F = 1
G = 0.5


liste = [A,B,C,D,E,F,G,]
liste2 = ["a","b","c","d","e","f","g"]
max = 0.59718885
min = 0.59718855
counter = 0

ondalık = (max-min)/10
print(ondalık)
def değer_bul(data,ondalık):
    global min
    sayı = data*ondalık
    min = min + sayı
    return min


for data in liste:
    adana = min
    deger2 = değer_bul(data,ondalık)
    print(f"{liste2[counter]}---------- min degeri = {round(adana,10)} ----index değeri = {round(deger2,10)}")
    counter  = counter + 1

