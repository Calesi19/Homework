import numpy, math
from matplotlib import pyplot

g = 9.8
m = .00048
C = .000025
i_position_y = 50
a = -g
vi = 0
v_terminal = -math.sqrt(m * g / C)
print(f'The terminal velocity is: {v_terminal} m/s')

#F_net = - m * g + C * (v_terminal**2)


delta_t = .05

y = 50
v = 0
t = 0


while y > 0:
    v += a * delta_t
    if v < v_terminal:
        v = v_terminal
    y += v * delta_t
    t += delta_t
    pyplot.figure(1)
    pyplot.plot(t,y,'k.')
    pyplot.plot(t,v,'k.')
pyplot.show()

print("It took{:5.2f} seconds for the particle to hit the ground".format(t))
print("The velocity of the particle as it hit the ground was {:5.2f} meters/seconds".format(v))