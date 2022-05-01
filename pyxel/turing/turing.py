# 
# Displaying Turing Patterns using pyxel based on
# https://ipython-books.github.io/124-simulating-a-partial-differential-equation-reaction-diffusion-systems-and-turing-patterns/
#
# May 01, 2022 ver.1 (changed graphics library to pyxel)
#

# -*- coding: utf-8 -*-
import numpy as np
import pyxel

# constants

a = 2.8e-4
b = 5e-3
tau = .1
k = -.005

#size = 100  # size of the 2D grid
size = 100  # size of the 2D grid
dx = 2. / size  # space step

T = 9.0  # total time
dt = .001  # time step
n = int(T / dt)  # number of iterations

# init
pyxel.init(size, size, title="Turing Pattern", fps=1000)

U = np.random.rand(size, size)
V = np.random.rand(size, size)

def laplacian(Z):
    Ztop = Z[0:-2, 1:-1]
    Zleft = Z[1:-1, 0:-2]
    Zbottom = Z[2:, 1:-1]
    Zright = Z[1:-1, 2:]
    Zcenter = Z[1:-1, 1:-1]
    return (Ztop + Zleft + Zbottom + Zright -
            4 * Zcenter) / dx**2

def update():
    # We compute the Laplacian of u and v.
    deltaU = laplacian(U)
    deltaV = laplacian(V)
    # We take the values of u and v inside the grid.
    Uc = U[1:-1, 1:-1]
    Vc = V[1:-1, 1:-1]
    # We update the variables.
    U[1:-1, 1:-1], V[1:-1, 1:-1] = \
        Uc + dt * (a * deltaU + Uc - Uc**3 - Vc + k),\
        Vc + dt * (b * deltaV + Uc - Vc) / tau
    # Neumann conditions: derivatives at the edges
    # are null.
    for Z in (U, V):
        Z[0, :] = Z[1, :]
        Z[-1, :] = Z[-2, :]
        Z[:, 0] = Z[:, 1]
        Z[:, -1] = Z[:, -2]

def draw():
    pyxel.cls(0)
    for x in range(size):
        for y in range(size):
            c = int((U[x, y] - 1.0) * -8.0)
            pyxel.pset(x, y, c)

    # text
    s = ( f"t = {pyxel.frame_count * dt:.2f}\n" )
    pyxel.text(0,0,s,0)

# main    
pyxel.run(update, draw)

# end of turing.py
