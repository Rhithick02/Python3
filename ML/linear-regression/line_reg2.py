import pandas as pd 
import matplotlib.pyplot as plt 

dataframe = pd.read_csv("student_scores.csv")
print(dataframe)
X = dataframe["Hours"].values.reshape(-1, 1)
Y = dataframe["Scores"].values.reshape(-1, 1)
Y_predict = []
m = len(X)
alpha = 0.01
theta = [1, 1]
plt.plot(X, Y, 'o')
for i in range(300):
    error = [0, 0]
    for point in zip(X, Y):
        y_predict = theta[0] + theta[1] * point[0] 
        error[0] += y_predict - point[1]
        error[1] += (y_predict - point[1]) * point[0]
    theta[0] -= alpha * error[0] / m
    theta[1] -= alpha * error[1] / m
for i in range(25):
    Y_predict.append(theta[0] + theta[1] * X[i])
plt.plot(X, Y_predict)
plt.show()
    
