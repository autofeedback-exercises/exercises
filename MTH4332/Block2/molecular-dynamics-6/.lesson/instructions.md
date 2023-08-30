# Setting the initial velocity

The MD codes you have written thus far can be used to sample from the microcanonical (NVE) ensemble, which is useful.  In general, however, we would like to develop methods to sample from the canonical (NVT) ensemble as it is easier to control the temperature in a lab setting than it is to control the energy and our ultimate goal should surely be to compare the results that we obtain from our simulations with the results that our colleagues obtain from their experiments.

We are thus going to learn how to modify our MD code to make the system sample the canonical ensemble.  Codes for running constant temperature MD will use a thermostat to control the temperature in the simulations.  There are many different ways of implementing a thermostat and we will only have time to introduce one particular method in this exercise.  The basic idea of these thermostats is always the same, however:

* We know, from the derivation of the ideal gas law, that if we are sampling from the canonical (NVT) ensemble the distribution of momentum along each degree of freedom is given by:

![](eq1.png)

In other words, for each degree of freedom, the momentum is a sample from a normal distribution with mean 0 and variance k_B*T*m, where k_B is Boltzmann's constant, T is the temperature and m is the mass of the particle. 

* We also know that classical equipartition (which is like a microscopic version of Gibb's phase rule) will ensure that energy is distributed equally between all the various degrees of freedom in the system if we are sampling from the NVT ensemble.  If we thus set the momentum of the atoms in accordance with the distribution above the distribution of potential energies will thus be set in accordance with the desired temperature.

* We can thus employ a thermostat that exchanges energy between the system and a reservoir.  This thermostat works by ensuring that the momenta of the atoms in the system are set in accordance with the distribution given above.

In the exercises after this one, you are going to learn how to code such a thermostat.  Before getting on to that, however, you first need to complete the function called `gen_vel` in `main.py`.  This function takes a single parameter called `temp`, which gives the temperature at which the simulation is to be run.  `gen_vel` should return a single scalar.  This scalar should be reasonable initial velocity for a particular degree of freedom.  In other words,  `gen_vel` should return a sample from the distribution of velocities given above.

Remember that we are operating with natural units and that as such k_B=1 and m=1.  Furthermore, you may find the following function, which returns a sample from a standard normal random variable with mean 0 and variance 1 useful:

````
random_normal = np.random.normal()
````
