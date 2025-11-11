import turtle as t

t.tracer(0)

def flex(lenght, quantity):
    if quantity == 0:
        t.fd(lenght)
        return
    flex(lenght/2, quantity - 1)
    t.lt(90)
    flex(lenght/2, quantity - 1)
    t.lt(180)
    flex(lenght, quantity - 1)
    t.lt(180)
    flex(lenght/2, quantity - 1)
    t.lt(270)
    flex(lenght/2, quantity - 1)

flex(200, 6)
t.update()

t.done()
