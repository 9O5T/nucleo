program AlphaEnergyChange
    implicit none
    
    ! Constants
    real, parameter :: alpha_mass = 6.64424e-27 ! kg (mass of alpha particle)
    real, parameter :: alpha_energy = 4.0e6     ! eV (energy of alpha particle)
    real, parameter :: proton_mass = 1.675e-27  ! kg (mass of proton)
    real, parameter :: neutron_mass = 1.675e-27 ! kg (mass of neutron)

    ! Variables
    integer :: protons_parent, neutrons_parent, protons_daughter, neutrons_daughter
    real :: initial_energy, final_energy, energy_change
    real :: mass_parent, mass_daughter

    open(unit=150, file='alfa_scattering_variables_var.txt', status='old', action='read')
        read(150,*) protons_parent, neutrons_parent, protons_daughter, neutrons_daughter
    close(150)
    


    ! Calculate masses of parent and daughter nuclei
    mass_parent = protons_parent * proton_mass + neutrons_parent * neutron_mass
    mass_daughter = protons_daughter * proton_mass + neutrons_daughter * neutron_mass
    
    ! Calculate initial and final energies
    initial_energy = alpha_energy
    final_energy = alpha_energy / (1.0 + (mass_daughter / alpha_mass))
    
    ! Calculate energy change
    energy_change = initial_energy - final_energy
    
    open(unit=250, file='alfa_scattering_variables_ans.txt', status='old', action='write')
        write(250,*) "Initial energy of alpha particle:", initial_energy, "eV"
        write(250,*) "Final energy of alpha particle:", final_energy, "eV"
        write(250,*) "Energy change:", energy_change, "eV"
    close(250)
    
    
end program AlphaEnergyChange

