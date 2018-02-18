# State-space Matrices for Luenberger Observer
A_lobs = A - L @ C
B_lobs = np.hstack([B, L])
C_lobs = C
D_lobs = np.matrix([0, 0])

sys_lobs = signal.lti(A_lobs, B_lobs, C_lobs, D_lobs)

# Inputs to observer
u = np.vstack([Torq, y_m]).T 

# Initial Conditions
x_hat0 = [0, 0.2, 0.2]

# Simulate Response
tsim, y, x_hat = signal.lsim(sys_lobs, U=u, T=t, X0=x_hat0)

# Parse states
theta_hat = x_hat[:,0]
omega_T_hat = x_hat[:,1]
omega_B_hat = x_hat[:,2]

# Compute RMSE
est_error = omega_B_true - omega_B_hat
RMSE = np.sqrt(np.mean(est_error ** 2))
print('Luenberger Observer RMSE:', RMSE)

# Plot Results
plt.figure(num=1, figsize=(8, 9), dpi=150, facecolor='w', edgecolor='k')

plt.subplot(2,1,1)
# Plot true and estimated bit velocity
plt.plot(t, omega_B_hat, label=r'Estimated velocity $\hat{\omega}_B$')
plt.plot(t, omega_B_true, label=r'True velocity $\omega_B$')
plt.legend()
plt.xlabel('Bit velocity')
plt.ylabel('Time')

plt.subplot(2,1,2)
# Plot error between true and estimated bit velocity
plt.plot(t, omega_B_true - omega_B_hat)
plt.xlabel('Estimation error')
plt.ylabel('Time')
