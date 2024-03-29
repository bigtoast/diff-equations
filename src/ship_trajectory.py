__author__ = 'andrew'

# PROBLEM 3
#
# Modify the below functions acceleration and
# ship_trajectory to plot the trajectory of a
# spacecraft with the given initial position
# and velocity. Use the Forward Euler Method
# to accomplish this.

import numpy
import matplotlib.pyplot

h = 1.0 # s
earth_mass = 5.97e24 # kg
gravitational_constant = 6.67e-11 # N m2 / kg2

def acceleration(spaceship_position):
###Your code here.
    return (
        gravitational_constant * earth_mass /
        numpy.square( numpy.sqrt( numpy.square(spaceship_position[0]) + numpy.square(spaceship_position[1]) ) ) *
        ( (- spaceship_position ) / numpy.linalg.norm(spaceship_position) )
    )

def ship_trajectory():
    num_steps = 13000
    x = numpy.zeros([num_steps + 1, 2]) # m
    v = numpy.zeros([num_steps + 1, 2]) # m / s

    x[0, 0] = 15e6
    x[0, 1] = 1e6
    v[0, 0] = 2e3
    v[0, 1] = 4e3

    ###Your code here. This code should call the above
    ###acceleration function.
    for step in range(num_steps):
        x[step + 1] = x[step] + h * v[step]
        v[step + 1] = v[step] + h * acceleration(x[step])

    return x, v

x, v = ship_trajectory()

# @show_plot
def plot_me():
    matplotlib.pyplot.plot(x[:, 0], x[:, 1])
    matplotlib.pyplot.scatter(0, 0)
    matplotlib.pyplot.axis('equal')
    axes = matplotlib.pyplot.gca()
    axes.set_xlabel('Longitudinal position in m')
    axes.set_ylabel('Lateral position in m')
    matplotlib.pyplot.show()

plot_me()