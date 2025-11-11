import turtle as t

t.screensize(2200, 2200)

def lev(lenght, quantity):
    if quantity == 0:
        t.fd(lenght)
        return
    t.lt(45)
    lev(lenght / 2, quantity - 1)
    t.rt(90)
    lev(lenght / 2, quantity - 1)
    t.lt(45)


lev(200, 4)
t.update()

t.done()