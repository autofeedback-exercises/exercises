import numpy as np

def rising_states( nspins, nstates ) :
    spins = np.zeros( nspins )
    for i in range(nspins) : 
        spins[i] = i%nstates
    return spins

def lowering_states( nspins, nstates ) :
    spins = np.zeros( nspins )
    for i in range(nspins) : 
        spins[i] = nstates - 1 - i%nstates
    return spins

def updown_states( nspins, nstates ) :
    spins = np.zeros( nspins )
    for i in range(nspins) :
        base = np.floor( i / nstates )
        if base%2==0 : spins[i] = i%nstates
        else : spins[i] = nstates - 1 - i%nstates
    return spins

