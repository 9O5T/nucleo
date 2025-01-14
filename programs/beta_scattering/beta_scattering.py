## This code is created by Enes Yıldırım 19.05.2024
AV = 15.76
AS = 17.81
AC = 0.711
ASM = 23.702
ACH = 34.0
VAC = 3.0e+8
# Constants
MEV_PER_AMU = 931.494  # 1 atomic mass unit (u) = 931.494 MeV/c^2
EV_PER_MEV = 1e6       # 1 MeV = 1,000,000 eV

# Masses in atomic mass units (u)
MASS_PROTON = 1.007276466812*MEV_PER_AMU
MASS_NEUTRON = 1.00866491588*MEV_PER_AMU
MASS_ELECTRON = 0.000548579909*MEV_PER_AMU
MASS_POSITRON = MASS_ELECTRON
MASS_HYDROGEN = 1.0078*MEV_PER_AMU

with open("beta_scattering_variables_var.txt","r",encoding="utf-8") as beta_scattering_var_file:
    S = beta_scattering_var_file.read()
beta_scattering_var_file.close()
S = S.split("    ")
name = S[0]
protons = int(S[1])
neutrons = int(S[2])

class Nucleus:
    def __init__(self, name, protons, neutrons):
        self.name = name
        self.protons = protons
        self.neutrons = neutrons
        self.atomic_number = protons + neutrons
        self.decay_type2 = "calculated"
        self.delta = 0.0
        self.kro = 0.0
        if self.protons % 2 == 0:
            self.delta = self.delta + 1.0
        else:
            self.delta = self.delta - 1.0

        if self.neutrons % 2 == 0:
            self.delta = self.delta + 1.0
        else:
            self.delta = self.delta - 1.0

        if self.delta == 0:
            self.kro = 0.0
        elif self.delta == 2 :
            self.kro = ACH*((1)/(self.atomic_number**(3/4)))
        elif self.delta == -2:
            self.kro = - ACH*((1)/(self.atomic_number**(3/4)))

        self.binding = (
            AV*self.atomic_number -
            AS*(self.atomic_number**(2/3)) -
            AC*((self.protons*(self.protons-1))/(self.atomic_number**(1/3))) -
            ASM*(((self.neutrons - self.protons)**2)/(self.atomic_number)) + 
            self.kro
        )
        self.mass = self.protons*MASS_HYDROGEN + self.neutrons*MASS_NEUTRON - self.binding
        


    def beta_decay(self):
        if self.protons > self.neutrons:
            decay_type = 'beta_plus'
        else:
            decay_type = 'beta_minus'  # For Carbon-14, we know it undergoes beta-minus decay
        self.decay_type2 = decay_type
        if decay_type == 'beta_minus':
            # Beta-minus decay: neutron -> proton + electron + antineutrino
            daughter_protons = self.protons + 1
            daughter_neutrons = self.neutrons - 1
            emitted_particle = 'electron'

            self.delta = 0.0
            self.kro = 0.0
            if daughter_protons % 2 == 0:
                self.delta = self.delta + 1.0
            else:
                self.delta = self.delta - 1.0

            if daughter_neutrons % 2 == 0:
                self.delta = self.delta + 1.0
            else:
                self.delta = self.delta - 1.0

            if self.delta == 0:
                self.kro = 0.0
            elif self.delta == 2 :
                self.kro = ACH*((1)/(self.atomic_number**(3/4)))
            elif self.delta == -2:
                self.kro = - ACH*((1)/(self.atomic_number**(3/4)))

            afterdecaybinding = (
                AV*self.atomic_number -
                AS*(self.atomic_number**(2/3)) -
                AC*((daughter_protons*(daughter_protons-1))/(self.atomic_number**(1/3))) -
                ASM*(((daughter_neutrons - daughter_protons)**2)/(self.atomic_number)) + 
                self.kro
            )
            
            daughter_mass = daughter_protons*MASS_HYDROGEN + daughter_neutrons*MASS_NEUTRON - afterdecaybinding

        else:
            # This case won't be used for Carbon-14 but included for completeness
            daughter_protons = self.protons - 1
            daughter_neutrons = self.neutrons + 1
            emitted_particle = 'positron'
            self.delta = 0.0
            self.kro = 0.0

            if daughter_protons % 2 == 0:
                self.delta = self.delta + 1.0
            else:
                self.delta = self.delta - 1.0

            if daughter_neutrons % 2 == 0:
                self.delta = self.delta + 1.0
            else:
                self.delta = self.delta - 1.0

            if self.delta == 0:
                self.kro = 0.0
            elif self.delta == 2 :
                self.kro = ACH*((1)/(self.atomic_number**(3/4)))
            elif self.delta == -2:
                self.kro = - ACH*((1)/(self.atomic_number**(3/4)))

            afterdecaybinding = (
                AV*self.atomic_number -
                AS*(self.atomic_number**(2/3)) -
                AC*((daughter_protons*(daughter_protons-1))/(self.atomic_number**(1/3))) -
                ASM*(((daughter_neutrons - daughter_protons)**2)/(self.atomic_number)) + 
                self.kro
            )
            
            daughter_mass = daughter_protons*MASS_HYDROGEN + daughter_neutrons*MASS_NEUTRON - afterdecaybinding
            
        # Calculate mass defect (mass difference) and energy released
        mass_defect = self.mass - daughter_mass
        energy_released_mev = mass_defect
        energy_released_ev = energy_released_mev * EV_PER_MEV

        # Update the nucleus to the daughter nucleus state
        self.protons = daughter_protons
        self.neutrons = daughter_neutrons
        self.mass = daughter_mass

        return emitted_particle, energy_released_mev, energy_released_ev, self.protons, self.neutrons

    def __str__(self):
        return f"\n\t{self.name}: {self.protons} protons, {self.neutrons} neutrons\n\tprobable decay type = {self.decay_type2}\n\tmass {self.mass} MeV | ({self.mass/MEV_PER_AMU} u)"

def main():

    # Example: Carbon-14 (6 protons, 8 neutrons, mass approximately 14.003241 u)
    nucleus = Nucleus(name, protons, neutrons)
    file_beta = open("beta_scattering_variables_ans.txt",'w')
    file_beta.write("nucleo : Calculation has started.")
    file_beta.write(f"\nInitial state ::{nucleus}")

    # Simulate beta decay
    emitted_particle, energy_released_mev, energy_released_ev, new_protons, new_neutrons = nucleus.beta_decay()

    file_beta.write(f"\nAfter beta decay ::{nucleus}")
    file_beta.write(f"\nEmitted particle: {emitted_particle}")
    file_beta.write(f"\nEnergy released: {energy_released_mev:.6f} MeV ({energy_released_ev:.2f} eV)")
    file_beta.write(f"\nNew state: {new_protons} protons, {new_neutrons} neutrons, mass {nucleus.mass:.6f} MeV")
    file_beta.close()
    
if __name__ == "__main__":
    main()
