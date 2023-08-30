# The kinetic energy

One thing that is particularly important to check whenever we run an MD simulation is whether or not the energy is being conserved.  To check the energy is conserved we need to store the potential that is calculated every time the forces are calculated.  As well as calculating the potential though we also need to calculate the kinetic energy.  The kinetic energy can be computed using a simple function of the velocities of the atoms, which you should know.

Your task in this exercise is thus to write a function called `kinetic` that takes in a list of velocities and that returns a single scalar value for the total kinetic energy of all the particles. For the assignment you will only have one particle and thus one velocity.  To make this exercise more interesting I am asking you to write a function to calculate the total kinetic for a system of N particles moving about on your energy landscape.  

N.B.  In this exercise, we are operating in natural units.  We have thus set the masses of all the atoms equal to one.  
