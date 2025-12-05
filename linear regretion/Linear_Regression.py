import numpy as np


n = int(input("How many data points? "))

X = []
Y = []

for i in range(n):
    x_val = float(input(f"Enter X[{i+1}]: "))
    y_val = float(input(f"Enter Y[{i+1}]: "))
    X.append(x_val)
    Y.append(y_val)


X = np.array(X)
Y = np.array(Y)


X_mean = np.mean(X)
Y_mean = np.mean(Y)


numerator = np.sum((X - X_mean) * (Y - Y_mean))
denominator = np.sum((X - X_mean)**2)
a = numerator / denominator   # slope


b = Y_mean - a * X_mean

print("\n===== RESULT =====")
print("Slope (a):", a)
print("Intercept (b):", b)

Y_pred = a * X + b
print("\nPredicted Y values:", Y_pred)
