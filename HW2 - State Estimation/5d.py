# Compute eig(A-L(300)C)
Sig = np.matrix((z[-1, 3:]).reshape(3,3))
L = Sig @ C.T / N 
np.linalg.eig(A - L @ C)[0]
