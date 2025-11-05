# №7
import turtle as t

t.tracer()
t.up()
t.bk(300)
t.down()

def ice(lenght, quantity):
    if quantity == 0:
        t.fd(lenght)
        return
    ice(lenght, quantity-1)
    t.lt(90)
    ice(lenght/2, quantity-1)
    t.lt(180)
    ice(lenght/2, quantity-1)
    t.lt(90)
    ice(lenght, quantity-1)

ice(50, 5)
t.update()
