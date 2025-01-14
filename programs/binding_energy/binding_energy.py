from __future__ import division, print_function
from math import pi

# define semi-empirical mass formula constanst (MeV)
a1 = 15.67
a2 = 17.23
a3 = 0.75
a4 = 93.2

with open(file="binding_energy_variables_var.txt",encoding='utf-8') as binding_file:
    gettting = binding_file.read()
binding_file.close()
gettting = gettting.split("    ")


Z = float(gettting[0])
A = float(gettting[1])

# determine constant a5 
if A%2 == 1:   
    a5 = 0         # A is odd
elif Z%2 == 0:
    a5 = 12.0      # A & Z are even
else:
    a5 = -12.0     # A is even and Z is odd

#Calculate binding energy
B = a1*A - a2*A**(2/3) - a3*Z**2/A**(1/3) - a4*(A-2*Z)**2/A + a5/A**(1/2)

with open("binding_energy_variables_ans.txt","w",encoding="utf-8") as writed_file:
    writed_file.write("Binding energy is {0:2f} MeV and binding energy per nucleon is {1:2f} MeV.".format(B, B/A))

