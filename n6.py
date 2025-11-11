import turtle as t

t.screensize(2200,2200)
t.up()
t.bk(300)
t.down()


def mink(lenght, quantity):
    if quantity == 0:
        t.fd(lenght)
        return
    mink(lenght/2, quantity - 1)
    t.lt(90)
    mink(lenght/2, quantity - 1)
    t.rt(90)
    mink(lenght/2, quantity - 1)
    t.rt(90)
    mink(lenght, quantity - 1)
    t.lt(90)
    mink(lenght / 2, quantity - 1)
    t.lt(90)
    mink(lenght / 2, quantity - 1)
    t.rt(90)
    mink(lenght / 2, quantity - 1)

mink(200, 2)
t.update()

t.done()