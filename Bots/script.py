#print('Hola Mundo')

import turtle as t

t.speed(0)
t.bgcolor('black')
t.pencolor('cyan')
def estrella(lados, longitud):
    for i in range(lados):
        t.forward(longitud)
        t.right(144)
for j in range(36):
    estrella(5, 200)
    t.right(10)
t.done()