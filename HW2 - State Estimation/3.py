# Load Data
data=np.asarray(pd.read_csv("HW2_Data.csv",header=None))

t = data[:,0]      # t   : time vector [sec]
y_m = data[:,1]    # y_m : measured table velocity [radians/sec]
Torq = data[:,2]   # Torq: table torque [N-m]
omega_B_true = data[:,3]    # \omega_B : true rotational speed of bit [radians/sec]

# Plot Data
plt.figure(num=1, figsize=(8, 9), dpi=150, facecolor='w', edgecolor='k')

plt.subplot(2,1,1)
plt.plot(t, Torq)
plt.xlabel('Time')
plt.ylabel('Table torque')
# Plot table torque

plt.subplot(2,1,2)
plt.plot(t, y_m)
plt.xlabel('Time')
plt.ylabel('Measured table velocity')
# Plot measured table velocity

plt.show()
