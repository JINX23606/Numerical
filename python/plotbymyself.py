import matplotlib.pyplot as plt
import numpy as np
#7.1 Line plot
x = np.linspace(-3,3)
y = x**2
fig , ax = plt.subplots()
ax.plot(x,y,label = '$y= x^2$',color = 'r',linestyle = '--')
ax.legend()
#7.2 Advance Customization and Layout
fig3 , ax3 = plt.subplots(2,1)
L = np.linspace(0,15,100)
tp = 6*L**2- 0.4*L**3
mp = 12*L-3*0.4*L**2
ax3[0].plot(L,tp,label = 'Total Product')
ax3[0].legend()
ax3[0].set_title('Total Product:TP')
ax3[0].set_xlabel('Labor')
ax3[0].set_ylabel('Output')
ax3[0].grid(linestyle='--',color = 'grey',alpha=0.5)

ax3[1].plot(L,mp,label='Marginal Product',linestyle=':',color='red')
ax3[1].legend()
ax3[1].set_title('Marginal Product:MP')
ax3[1].set_xlabel('Labor')
ax3[1].set_ylabel('Marginal Output')
ax3[1].grid(linestyle='--',color = 'grey',alpha=0.5)
plt.tight_layout()
plt.show()

#7.3 Exploring other plot type