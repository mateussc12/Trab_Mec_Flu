from sympy import *
import numpy as np
from matplotlib import pyplot as plt


fig1 = plt.figure(figsize=(11, 7), dpi=80)
ax1 = fig1.gca(projection='3d')

fig2 = plt.figure(figsize=(11, 7), dpi=80)
ax2 = fig2.gca(projection='3d')

detalhamento = 100

r_min = 0.00001
phi_min = 0
r_max = 1.0
phi_max = 2 * np.pi

radii = np.linspace(r_min, r_max, detalhamento)
angles = np.linspace(0, 2 * np.pi, detalhamento, endpoint=False)

angles = np.repeat(angles[..., np.newaxis], detalhamento, axis=1)

X = np.append(r_min, (radii * np.cos(angles)).flatten())
Y = np.append(r_min, (radii * np.sin(angles)).flatten())

R = np.sqrt(X ** 2 + Y ** 2)
phi = np.arctan(Y / X)

u = (1 - (R ** 2) / (r_max ** 2))

mi = 1.002 * pow(10, -3)

u_ = symbols('u', cls=Function)
x, y, r = symbols('x y r')

u_ = (1 - (r ** 2) / (r_max ** 2))
tr_ = mi * u_.diff(r)

tr = []
for i in range(len(R)):
    tr.append(tr_.subs([(r, R[i])]))

graf_1 = ax1.plot_trisurf(X, Y, u, cmap='inferno', linewidth=0, antialiased=False)

ax1.set_title('Perfil de velocidades', fontsize=25)
ax1.set_xlabel('x', fontsize=15)
ax1.set_ylabel('y', fontsize=15)
ax1.set_zlabel('u', fontsize=15)

fig1.colorbar(graf_1, shrink=0.7)

graf_2 = ax2.plot_trisurf(X, Y, np.array(tr, dtype=float), cmap='inferno', linewidth=0, antialiased=False)

ax2.set_title('Tensão de cisalhamento', fontsize=25)
ax2.set_xlabel('x', fontsize=15)
ax2.set_ylabel('y', fontsize=15)
ax2.set_zlabel('tau', fontsize=15)

fig2.colorbar(graf_2, shrink=0.7)


plt.tight_layout()
plt.show()
