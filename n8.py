import turtle as t

t.screensize(2200, 2200)

def frac(lenght, quantity):
    if quantity == 0:
        t.fd(lenght)
        return
    frac(lenght, quantity - 1)
    t.lt(120)
    frac(lenght * 0.3, quantity - 1)
    t.lt(180)
    frac(lenght * 0.3, quantity - 1)
    t.lt(120)
    frac(lenght * 0.3, quantity - 1)
    t.lt(180)
    frac(lenght * 0.3, quantity - 1)
    t.lt(120)
    frac(lenght, quantity - 1)

frac(90, 2)
t.update()
t.done()