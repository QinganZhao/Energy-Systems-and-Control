# Desired poles of estimation error system
#   They should have negative real parts
#   Complex conjugate pairs
lam_luen = 2.5 * lam_A

# Compute observer gain
L = control.acker(A.T, C.T, lam_luen).T
print('L:\n', L) 