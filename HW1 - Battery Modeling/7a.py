## Part(a): Model Parameters

# ECM Model Parameters
Q = 3600 # [Coulombs]
R1 = 0.05 # [Ohms]
R2 = 0.005 # [Ohms]
C = 500 # [Farads]

# OCV polynomial coefficients
p_0 = 3.4707
p_1 = 1.6112
p_2 = -2.6287
p_3 = 1.7175

# Plot nonlinear OCV function
z_vec = np.linspace(0,1,25)
OCV = p_0 + p_1*z_vec + p_2 * (z_vec ** 2) + p_3 * (z_vec ** 3)
print(z_vec)
print(OCV)

plt.plot(z_vec, OCV)
plt.xlabel('SOC, $z$ [-]',fontsize=fs)
plt.ylabel('OCV [volts]',fontsize=fs)
plt.tick_params(axis='both', which='major', labelsize=fs)
plt.show()