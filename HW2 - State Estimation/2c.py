# New A Matrix, for 3-state system
A = np.matrix([[0, 1, -1], [-k/J_T, -b/J_T, 0], [k/J_B, 0, -b/J_B]])
B = np.matrix([[0], [1/J_T], [0]])
C = np.matrix([0, 1, 0])

# Observability Matrix for 3-state system and rank
O = np.vstack([C, C @ A, C @ A @ A])
print('Rank of Observability Matrix for three-state system:', np.linalg.matrix_rank(O))
