# Plot Results
plt.figure(num=3, figsize=(8, 9), dpi=150, facecolor='w', edgecolor='k')

plt.subplot(2,1,1)
#   Plot true and estimated bit velocity
#   Plot estimated bit velocity plus/minus one sigma
plt.plot(t, omega_B_hat, 'r', label=r'Estimated velocity $\hat{\omega}_B$')
plt.plot(t, omega_B_true, 'g', label=r'True velocity $\omega_B$')
plt.plot(t, omega_B_hat_upperbound, 'm--', label=r'Upper bound $\hat{\omega}_B+\sqrt{\Sigma_{33}}$')
plt.plot(t, omega_B_hat_lowerbound, 'b--', label=r'Lower bound $\hat{\omega}_B-\sqrt{\Sigma_{33}}$')
plt.legend()
plt.xlabel('Bit velocity')
plt.ylabel('Time')

plt.subplot(2,1,2)
#   Plot error between true and estimated bit velocity


plt.subplot(2,1,2)
# Plot error between true and estimated bit velocity
plt.plot(t, omega_B_tilde)
plt.xlabel('Estimation error')
plt.ylabel('Time')

plt.show()
