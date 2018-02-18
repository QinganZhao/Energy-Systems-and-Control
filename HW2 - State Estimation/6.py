# New nonlinear spring parameters
k1 = 2
k2 = 0.25

# Noise Covariances
W = np.matrix([[0.0006, 0.005, 0.001], [0.02, 0.003, 0.004], [0.004, 0.001, 0.003]])  #You design this one. 
N = 0.02
Sig0 = np.identity(3)

# Initial Condition
x_hat0 = [0, 0, 0]
states0 = np.r_[x_hat0, np.squeeze(np.asarray(Sig0.reshape(9,1)))]

# Ordinary Differential Equation for Kalman Filter
def ode_ekf(z,it):
    
    # Parse States
    theta_hat = z[0]
    omega_T_hat = z[1]
    omega_B_hat = z[2]
    Sig = np.matrix((z[3:]).reshape(3,3))
    
    # Interpolate input signal data
    iTorq = interp(it, t, Torq)
    iy_m = interp(it, t, y_m)
    
    # Compute Jacobians
    F = np.matrix([[0, -1, -1], [(-k1-3*k2*theta_hat**2)/J_T, -b/J_T, 0], [(k1+3*k2*theta_hat**2)/J_T, 0, -b/J_B]])# YOU DERIVE THESE
    H = C# YOU DERIVE THESE
    
    # Compute Kalman Gain
    L = Sig @ H.T / N
    
    # Compute EKF system matrices
    y_hat = omega_T_hat
    
    f = np.matrix([[omega_T_hat - omega_B_hat], [(-k1 * theta_hat - k2 * theta_hat ** 2 - b * omega_T_hat + iTorq) / J_T], [(k1 * theta_hat + k2 * theta_hat ** 2 - b * omega_B_hat) / J_B]])
    x_dot = f + L * (iy_m - omega_T_hat)
                   
    theta_hat_dot = x_dot[0]
    omega_T_hat_dot = x_dot[1]
    omega_B_hat_dot = x_dot[2]
    
    # Riccati Equation
    Sig_dot = Sig @ F.T + F @ Sig + W - Sig @ H.T / N @ H @ Sig
    
    # Concatenate LHS
    z_dot = np.r_[theta_hat_dot, omega_T_hat_dot, omega_B_hat_dot, Sig_dot.reshape(9,1)]
    
    return(np.squeeze(np.asarray(z_dot)))

# Integrate Extended Kalman Filter ODEs
z = odeint(ode_ekf, states0, t)

# Parse States
theta_hat = z[:,0]
omega_T_hat = z[:, 1]
omega_B_hat = z[:, 2]
Sig33 = z[:, -1]

omega_B_tilde = omega_B_true - omega_B_hat
omega_B_hat_upperbound = omega_B_hat + np.sqrt(Sig33)
omega_B_hat_lowerbound = omega_B_hat - np.sqrt(Sig33)

RMSE = np.sqrt(np.mean(np.power(omega_B_tilde,2)))
print('Extended Kalman Filter RMSE: ' + str(RMSE) + ' rad/s')


# Plot Results
plt.figure(num=2, figsize=(8, 9), dpi=150, facecolor='w', edgecolor='k')

plt.subplot(2,1,1)
#   Plot true and estimated bit velocity
#   Plot estimated bit velocity plus/minus one sigma
plt.plot(t, omega_B_hat, 'r', label=r'Estimated velocity $\hat{\omega}_B$')
plt.plot(t, omega_B_true, 'g', label=r'True velocity $\omega_B$')
plt.plot(t, omega_B_hat_upperbound, 'm--', label=r'Upper bound $\hat{\omega}_B+\sqrt{\Sigma_{33}}$')
plt.plot(t, omega_B_hat_lowerbound, 'b--', label=r'Lower bound $\hat{\omega}_B-\sqrt{\Sigma_{33}}$')
plt.legend()
plt.xlabel('Time')
plt.ylabel('Bit velocity')

plt.subplot(2,1,2)
#   Plot error between true and estimated bit velocity
plt.plot(t, omega_B_tilde)
plt.xlabel('Time')
plt.ylabel('Estimation error')

plt.show()
