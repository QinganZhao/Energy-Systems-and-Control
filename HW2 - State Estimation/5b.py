# Noise Covariances
W = np.matrix([[0.0006, 0.005, 0.001], [0.02, 0.003, 0.004], [0.004, 0.001, 0.003]]) #You design this one. 
N = 0.02
Sig0 = np.identity(3)

# Initial Condition
x_hat0 = [0, 0, 0]
states0 = np.r_[x_hat0, np.squeeze(np.asarray(Sig0.reshape(9,1)))]

# Ordinary Differential Equation for Kalman Filter
def ode_kf(z,it):
    
    # Parse States
    x_hat = np.matrix(z[:3]).T
    Sig = np.matrix((z[3:]).reshape(3,3))
    
    # Interpolate input signal data
    iTorq = interp(it, t, Torq)
    iy_m = interp(it, t, y_m)
    
    # Compute Kalman Gain
    L = Sig @ C.T / N 
    
    # Kalman Filter
    x_hat_dot = A @ x_hat + B * iTorq + L @ (iy_m - C @ x_hat)
    
    # Riccati Equation
    Sig_dot = Sig @ A.T + A @ Sig + W - Sig @ C.T / N @ C @ Sig
    
    # Concatenate LHS
    z_dot = np.r_[x_hat_dot, Sig_dot.reshape(9,1)]
    
    return(np.squeeze(np.asarray(z_dot)))


# Integrate Kalman Filter ODEs
z = odeint(ode_kf, states0, t)

# Parse States
theta_hat = z[:,0]
omega_T_hat = z[:, 1]
omega_B_hat = z[:, 2]
Sig33 = z[:, -1]     # Parse out the (3,3) element of Sigma only!

omega_B_tilde = omega_B_true - omega_B_hat
omega_B_hat_upperbound = omega_B_hat + np.sqrt(Sig33)
omega_B_hat_lowerbound = omega_B_hat - np.sqrt(Sig33)

RMSE = np.sqrt(np.mean(np.power(omega_B_tilde,2)))
print('Kalman Filter RMSE: ' + str(RMSE) + ' rad/s')
