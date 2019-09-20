from pyrca.utils.conversion import *

# Test the MPa to PSI conversion
mpa = 10
psi = mpa_to_psi(mpa)
print(str(mpa) + ' MPa to PSI = ' + str(psi))