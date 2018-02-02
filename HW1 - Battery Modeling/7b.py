## Part(b): Simulate

# Assemble (A,B) state-space matrices
A = [[0, 0], [0, -1/(R2 * C)]]
B = [[1/Q], [1/C]]
print(A)
print(B)
C_dummy = [1, 1]
D_dummy = R1
print(C_dummy)
print(D_dummy)

# Create state-space model
sys = signal.lti(A, B, C_dummy, D_dummy)

# Create time vector
DeltaT = 1 # Time step size [sec]
t = np.arange(0,10*60,DeltaT)   # Total Simulation time (min*sec/min)
#print('time')
#print(t)

# Input current signals
#print(np.shape(t))
Current = np.zeros_like(t)*0
for k in range(0, len(Current)):
    if (t[k] % 40) < 20:
        Current[k] = -5

# Initial Conditions
z0 = 0.5 # state-of-charge
V_c0 = 0 # capacitor voltage
x0 = [z0,V_c0] # np.array([[z0],[V_c0]])   # Vectorize initial conditions
print('x0')
print(x0)

print(np.shape(x0))
print(np.shape(Current))
print(np.shape(t))

# Simulate linear dynamics (Read documentation on scipy.signal.lsim)
tsim, y, x = signal.lsim2(sys, Current, t, x0)

# Parse out states
z = x[:,0]
V_c = x[:,1]

# Compute nonlinear output function
V_nl = p_0 + p_1 * z + p_2 * (z ** 2) + p_3 * (z ** 3) + V_c + R1 * Current

### Compute linearized output function
# Linearization Points
zeq = 0.5   # state-of-charge
V_ceq = 0 # capacitor voltage
Ieq = 0 # Current

V_lin = V_c + (p_1 + p_2 + 0.75 * p_3) * z + R1 * Current + p_0 - 0.25 * p_2 - 0.25 * p_3 

## Part(b): Plot results

# Current
plt.figure(num=2, figsize=(8, 8), dpi=80, facecolor='w', edgecolor='k')
plt.subplot(3, 1, 1)
plt.plot(t, Current)
plt.ylabel('Current (A)')

# State-of-charge
plt.subplot(3, 1, 2)
plt.plot(t, z)
plt.ylabel('SOC')

# Nonlinear and linearized voltage
plt.subplot(3, 1, 3)
plt.plot(t, V_nl,label="Nonlinear")
plt.plot(t, V_lin, 'r--', label="Linearized")
plt.ylabel('Voltage (V)')
plt.xlabel('Time (s)')
plt.legend()

plt.show()