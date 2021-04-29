import time
import datetime

print("3")
time.sleep(0.5)
print("2")
time.sleep(0.5)
print("1")
time.sleep(0.5)

zaman=datetime.datetime.now()

metn=input("metn yazin:")
zaman2=datetime.datetime.now()

yazmasureti = zaman2 - zaman
saniye=round(yazmasureti.total_seconds(),2)
zaman3=round(len(metn)/saniye,1)

print("toplam vaxt : {}".format(saniye))
print("{} saniye bawina".format(zaman3))




print("**********cumlenin tersine cevrilmesi************")
def cevir(metn,say=[]):
    for i in range(len(metn) -1,-1,-1 ):
        say.append(metn[i])
    return "".join(say)

cumle = input("bir cumle yazin:")
print("tersi: {}".format(cevir(cumle)))