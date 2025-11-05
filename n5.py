# №5
import turtle as t

def direct_Koh(lenght, quantity):
    if quantity == 0:
        t.fd(lenght)
        return
    direct_Koh(lenght/3, quantity-1)
    t.lt(60)
    direct_Koh(lenght/3, quantity-1)
    t.rt(120)
    direct_Koh(lenght/3, quantity-1)
    t.lt(60)
    direct_Koh(lenght/3, quantity-1)

for _ in range(3):
    direct_Koh(300, 3)
    t.rt(120)
t.update()
