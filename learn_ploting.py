# -*- coding: utf-8 -*-
"""
Script 7 Plotting in Python
Created on Sat Dec 28 06:52:38 2024
@author: HSS
"""
#
# 7.1 Line Plots

# 7.1.1 Understanding the basics of Line Plots
#
# Two important words   -----> Figure
#                       -----> Axes Objects

# 7.1.2 Essential Fns

import numpy as np
import matplotlib.pyplot as plt

# (i)  subplots()
#
# Call Signature ------------------------------------------------------------
# plt.subplots(nrows = 1, ncols = 1)
# --------------------------------------------------------------------------
plt.subplots()
plt.show()
# Note that
type(plt.subplots())  # tuple (  Figure, (a collection of) Axes Object(s)  )
# Unpack
fig , ax  =  plt.subplots()
fig.set_facecolor('lightgrey')
ax.set_facecolor('lightblue')

# The locations of Axes objects
fig , ax  =  plt.subplots()   # fig , ax  =  plt.subplots(1,1)
type(ax)
ax[0]  #error
ax

fig2, ax2 = plt.subplots(1,2)
type(ax2)    # 1d np.array
ax2[0]       # lhs axes
ax2[1]       # rhs axes

fig3, ax3 = plt.subplots(2,1)
type(ax2)    # 1d np.array
ax3[0]       # upper axes
ax3[1]       # lower axes

fig4, ax4 = plt.subplots(2,2)
type(ax4)    # 2d np.array
ax3[0,0]       # upper left axes
ax3[0,1]       # upper right axes
ax3[1,0]       # lower left axes
ax3[1,1]       # lower right axes

# (ii) linspace()
#
# Call Signature ------------------------------------------------------------
# np.linspace(start, stop, num=50, endpoint=True)
# --------------------------------------------------------------------------
np.linspace(0,49)
np.linspace(1,2,3)  # 1  1.5  2
np.linspace(1,5,5)  # 1  2  3  4  5

# (iii) plot()
#
# Call Signature ------------------------------------------------------------
# ax.plot(x, y, options = None)
# --------------------------------------------------------------------------

x = np.linspace(-3,3)
y = x**2
fig_test, ax_test = plt.subplots()
ax_test.plot(x,y)

# Options ---> legend
x = np.linspace(-3,3)
y = x**2
fig_test, ax_test = plt.subplots()
ax_test.plot(x,y, label = '$y = x^2$')  # Latex
ax_test.legend()

# Options ----> linestyle & color
#
#   linestyle	meaning	         color	       meaning
#   -----------------------------------------------
#    '-'	   solid line	     'b'	        blue
#    '--'	   dashed line	     'g'	        green
#    '.'	   point marker	     'r'	       red
#    'o'	   circle marker	 'c'	       cyan
#    's'	   square marker	 'w'	       white
#    '+'	   plus marker	     'm'	       magenta
#    'x'	   x marker	         'y'	       yellow
#    'D'	   diamond marker	 'k'	       black

x = np.linspace(-3,3)
y = x**2
fig_test, ax_test = plt.subplots()
ax_test.plot(x,y, label = '$y = x^2$', color = 'r', linestyle = '--') 
ax_test.legend()


# 7.2 Anvanced Customizations and Layouts

# 7.2.1 Cosmetic Enhancements for Line Plots

fig6, ax6 = plt.subplots()
L = np.linspace(0,15,100)
TP = 6*L**2 - 0.4*L**3
ax6.plot(L,TP, label = 'Total Product')
ax6.legend()

# Additional Fns
#
#  (i) ax.set_title()
#  (ii) ax.grid()
#  (iii) ax.set_xlabel()
#  (iv) ax.set_ylabel()

fig6, ax6 = plt.subplots()
L = np.linspace(0,15,100)
TP = 6*L**2 - 0.4*L**3
ax6.plot(L,TP, label = 'Total Product')
ax6.legend()
ax6.set_title('Short-Run Production Function')
ax6.grid(linestyle ='--', color = 'grey')
ax6.set_xlabel('Labor')
ax6.set_ylabel('Output')

# 7.2.2 Multiple Axes in a Single Figure

fig7, ax7 = plt.subplots(2,1)
L = np.linspace(0,15,100)
TP = 6*L**2 - 0.4*L**3
MP = 12*L - 3*0.4*L**2

ax7[0].plot(L,TP, label = 'Total Product')
ax7[0].legend()
ax7[0].set_title('Total Product:TP')
ax7[0].grid(linestyle ='--', color = 'grey')
ax7[0].set_xlabel('Labor')
ax7[0].set_ylabel('Output')

ax7[1].plot(L,MP, label = 'Marginal Product')
ax7[1].legend()
ax7[1].set_title('Marginal Product: MP')
ax7[1].grid(linestyle ='--', color = 'grey')
ax7[1].set_xlabel('Labor')
ax7[1].set_ylabel('Marginal Output')

plt.tight_layout()

fig7.set_facecolor('lightgrey')
ax7[0].set_facecolor('lightblue')
ax7[1].set_facecolor('lightblue')


# 7.3 Exploring Other Plot Types