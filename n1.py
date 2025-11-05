# №1
import turtle as t


def sq(lenght, quantity):
    if quantity == 0:
        return
    for i in range(4):
        t.fd(lenght)
        t.rt(90)
    t.up()
    t.rt(9)
    t.fd(lenght/10)
    t.down()
    sq(lenght*9/10, quantity - 1)

sq(200, 20)
t.update()
