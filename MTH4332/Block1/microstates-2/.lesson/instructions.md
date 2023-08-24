# Generating microstates II

The assignment for this module involves systems of non-interacting particles that can each be in 3 or more states.  You can store the coordinates of the microstate for a system of N of these particles in a NumPy array as you learned to do in the previous exercise.  Now, however, the coordinates of the particles are no longer -1 and 1.  Instead the coordinate for each particle can be 0, 1, 2,... or M-1, where M is the number of states.

To demonstrate that you can manipulate these arrays that hold the microstate I would like you to write 3 functions.  Each of these functions will take two arguments:

* `N` - the number of particles that the system contains
* `M` - the number of distinct states that each particle can adopt

The three functions will then return a microstate for a system of `N` particles that can each be in 1 of M states.  In particular:

* `rising_states` - should return a microstate in which spin 0 is in state 0, spin 1 is in state 1, spin 2 is in state 2 and so on up to spin M-1, which should be in state M-1. Spin M should then be in state 0 again, Spin M+1 should be in state 1 etc.

* `lowering_states` - should return a microstate in which spin 0 is in state M-1, spin 1 is in state M-2, spin 2 is in state M-3 and so on up to spin M-1, which should be in state 0.  Spin M should then be in state M-1 again, spin M+1 should be in state M-2 etc.

* `updown_states` - should return a microstate in which spin 0 is in state 0, spin 1 is in state 1, spin 2 is in state 2 and so on up to spin M-1, which should be in state M-1.  Spin M should then be in state M-1, spin M+1 shoudl be in state M-2, spin M+2, should be in state M-3 and so on up to spin 2M, which should be in state 0.  Spin 2M + 1 should then be in state 0, spin 2M + 2 should be in state 1 and so on in this raising and lowering pattern.

Hint: You may find the modulo operator (%) useful.  a%b returns the remainder that is obtained when a is divided by b.  5%2 thus returns 2 as 5/2 is 2 remainder 1aWhen writing the function `updown_states` you may also find the NumPy function `np.floor` useful.
