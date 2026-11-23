"""
Plot the output characteristics for the BC337 NPN transistor
"""

import matplotlib.pyplot as plt
import numpy as np
import ngspyce as ng

# Load netlist
ng.source('npn.cir')

# Sweep both base and collector current
ng.cmd('dc vcc 0 2 .02 vbb .7 1.2 .1')

# Load simulation results into numpy arrays
vb, vc, Ivcc = map(ng.vector, ['Vb', 'Vc', 'I(Vcc)'])

# Correct the sign for collector current
ic = -Ivcc

plt.figure()
# Plot one line per base voltage
series = np.unique(vb)
for _vb in series:
    plt.plot(vc[vb == _vb], ic[vb == _vb], '-',
             label='Vb = {:.1f}'.format(_vb))

plt.legend(loc='center right')
plt.title('Output characteristics for BC337')
plt.xlabel('Collector-emitter voltage in V')
plt.ylabel('Collector current in A')
plt.savefig('bc337.png')
plt.show()
