from pyrca.utils.conversion import *

# Test the MPa to PSI conversion
mpa = 10
psi = mpa_to_psi(mpa)
print(str(mpa) + ' MPa to PSI = ' + str(psi))

# Test the PSI to MPa conversion
psi = 10
mpa = psi_to_mpa(psi)
print(str(psi) + ' PSI to MPa = ' + str(mpa))

# Test for mm to inch conversion
mm = 10
inch = mm_to_in(mm)
print(str(mm) + ' mm to inches = ' + str(inch))
