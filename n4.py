# №4
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


direct_Koh(200, 2)
t.update()
