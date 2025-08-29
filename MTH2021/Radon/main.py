# -*- coding: utf-8 -*-
"""
Created on Mon Aug  4 14:35:06 2025

@author: 2058162
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy

def sheplog(N):
    #
    # Toft's modified Shepp-Logan picture
    #
    #
    # It is created as a list of ellipses
    # Each entry in Elli describes a separate ellipse
    # Parameters: center x, center y
    #             minor r, major r
    #             angle w.r.t. y, shading value
    #
    # original shading values: 
    # 2 -.98 -0.02 -0.02 remainder 0.01
    #
    # modified:
    # 1 -.8 -.2 -.2 others .1
    #
    Elli=[]
    Elli.append((0,0,0.69,0.92,0,1))
    Elli.append((0,-0.0184,0.6624,0.874,0,-0.8))
    Elli.append((0.22,0,0.11,0.31,-18,-0.2))
    Elli.append((-0.22,0,0.16,0.41,18,-0.2))
    Elli.append((0,0.35,0.21,0.25,0,0.1))
    Elli.append((0,0.1,0.046,0.046,0,0.1))
    Elli.append((0,-0.1,0.046,0.046,0,0.1))
    Elli.append((-0.08,-0.605,0.046,0.023,0,0.1))
    Elli.append((0,-0.605,0.023,0.023,0,0.1))
    Elli.append((0.06,-0.605,0.023,0.046,0,0.1))
    slimg=np.zeros((N,N))
    xcoord = np.linspace(1,-1,N)
    ycoord = np.linspace(-1,1,N)
    for component in Elli:
        xcent=component[0]
        ycent=component[1]
        xlen=component[3]
        ylen=component[2]
        angle= component[4]
        gray = component[5]
        for j in range(N):
            for k in range(N):
                x=(xcoord[j]-ycent)*np.cos(angle/180*np.pi)-(ycoord[k]-xcent)*np.sin(angle/180*np.pi)
                y=(ycoord[k]-xcent)*np.cos(angle/180*np.pi)+(xcoord[j]-ycent)*np.sin(angle/180*np.pi)
                if ((((x)/xlen)**2+((y)/ylen)**2)<=1.):
                    slimg[j,k] += gray
    plt.imshow(slimg,cmap = 'gray', interpolation='none', aspect = 'equal')
    plt.colorbar()
    plt.show()
    return slimg
#
# Define the phantom image
#
N=256
phantom = sheplog(N)
#
# Create a 1-D grid needed for interpolating image data
#  to create the Radon transform
#  Also define the angles used to create the image
#
grid = np.linspace(-1,1,N)
M=30
angles = np.linspace(0,np.pi*(M-1)/M,M)
#
# Create the Radon transform
# - scipy.interpolate.interpn uses linear interpolation.
#   This method can be changed
#
# - Interpolation over a square that is being rotated
#   Out of bounds values are set to 0
#
# - Fit_grid contains the coordinates of each X-ray beam
#   It depends on angle and on displacement
#   Displacement is perpendicular to teh beam direction
#
Radon_image = np.zeros((N,M))                
count_ang=0
fit_grid = np.zeros((N,2))
for angle in angles:
    count_displacement = 0
    for displacement in grid:
       fit_grid[:,0] = np.linspace(-np.cos(angle),np.cos(angle),N)-displacement*np.sin(angle)
       fit_grid[:,1] = np.linspace(-np.sin(angle),np.sin(angle),N)+displacement*np.cos(angle)
       in_data = scipy.interpolate.interpn((grid,grid),phantom,fit_grid, method='linear',bounds_error=False,fill_value=0)
       Radon_image[count_displacement,count_ang]=sum(in_data)*2./N
       count_displacement+=1
    count_ang+=1
#
# Show the Radon transform
#
plt.imshow(Radon_image,interpolation='none',aspect='auto')
plt.show()
#
# Create the wavenumber grid and store it in k_grid
# dk is the wavenumber spacing
# The first half should have positive values
# The second half should have negative values (mostly)
# Element 0 has the value 0
#
dk = np.pi
k_grid = np.zeros(N)
Nmid=int(N/2)
k_grid[N-1]=-dk
for jj in range(1,Nmid+1):
    k_grid[jj]=k_grid[jj-1]+dk
for jj in range(N-2,Nmid,-1):
    k_grid[jj] = k_grid[jj+1]-dk
#
# Store the magnitude of k in abs_k
# Store the k-dependent correction factor for
#   the Fourier transform in phase_k
#
abs_k = np.abs(k_grid)
phase_k = np.exp(-1j*k_grid)

#
# Fourier transform the Radon transform along the displacement
#  axis for each angle and apply the correction factor
#  and a weight factor
#
# Store the result in Radon_Fourier
#
Radon_Fourier = np.zeros((N,M), dtype = complex)                
count_angle=0
for angle in angles:
   Radon_Fourier[:,count_angle] = scipy.fft.fft(Radon_image[:,count_angle])*abs_k*phase_k
   count_angle+=1

Radon_Fourier = Radon_Fourier*2/(N*np.sqrt(2*np.pi))

#
# Reconstruct the original image by carrying out the summation
#  over plane waves (pairs of angle and k) 
#
# Store the plane wave in Recon_comp 
#    and add the real parts to Recon
#
Recon_comp=np.zeros((N,N),dtype=complex)
Recon=np.zeros((N,N))
#
# Use np.meshgrid to generate 2D grids for the x and y coordinates
#
grid_2d = np.meshgrid(grid,grid)
#
# Loop over angles
#   Then combine k_grid with the angle to get kx and ky values
#   Loop over the wavenumbers and create the plane waves
#   The real part of each plane waves is added to the
#     full image, taking into account Fourier coefficient
#     and weight factor
#
count_angle=0
for angle in angles:
    print(count_angle)
    kx = k_grid * np.cos(angle)
    ky = -k_grid * np.sin(angle)
    for j in range(len(k_grid)):
      Recon_comp=np.exp(1j*kx[j]*grid_2d[0])*np.exp(1j*ky[j]*grid_2d[1])*Radon_Fourier[j,count_angle]
      Recon += np.real(Recon_comp)/(N*np.pi)
    count_angle+=1
#
# The image can be improved by rescaling the data to [0,1]
# and setting all data outside a circle with radius 1 to 0.
# Only data within this circle is covered by the full set
#   of spectra
#
# You can amend the code to see the original output
#

plt.imshow(Recon,interpolation='none',cmap='gray')
plt.colorbar()
plt.show()

#
# Set the unreliable part of the figure to some average value
#

innerav = np.mean(Recon[int(N/4):int(3*N/4),int(N/4):int(3*N/4)])

Recon = Recon*(np.sqrt(grid_2d[1]**2+grid_2d[0]**2)<=1.) + \
    innerav*(np.sqrt(grid_2d[1]**2+grid_2d[0]**2)>1.)

#
# We can now rescale the figure to on a 0 - 1 scale using
# relevant data only
# and set the all data outside the area of relevance to 0
#

Reconmx = np.max(Recon)
Reconmin = np.min(Recon)

Recon = (Recon-Reconmin)/(Reconmx-Reconmin) \
    *(np.sqrt(grid_2d[1]**2+grid_2d[0]**2)<=1.)

plt.imshow(Recon,interpolation='none',cmap='gray')
plt.colorbar()
plt.show()
