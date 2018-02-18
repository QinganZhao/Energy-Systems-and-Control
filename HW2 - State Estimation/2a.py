# State space matrices
A4 = np.matrix([[0, 1, 0, 0], [-k/J_T, -b/J_T, k/J_T, 0], [0, 0, 0, 1], [k/J_B, 0, -k/J_B, -b/J_B]])
B4 = np.matrix([[0], [1/J_T], [0], [0]])
C4 = np.matrix([0, 1, 0, 0])

# Compute observability Matrix for 4-state system and rank
O4 = np.vstack([C4, C4 @ A4, C4 @ A4 @ A4, C4 @ A4 @ A4 @ A4])
print('Rank of Observability Matrix for four-state system:', np.linalg.matrix_rank(O4))