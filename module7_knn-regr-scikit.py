import numpy as np
from sklearn.neighbors import KNeighborsRegressor

def knn_regression()
    #User input a positive integer N (number of points)
    N = int(input("Please type a positive integer: \n"))
        
    #User input a positive integer k (k nearest points for KNN method)
    k = int(input("please type a positive integer: \k"))
    
    # Initialize arrays to store points
    X_train = np.zeros((N, 1))
    Y_train = np.zeros(N)
    
    #Read N(x,y) points
    print("Please type in the coordiantes of each points (x,y):")
    for index in range(N):
        x = float(input("Please enter x value for point {index + 1}: \n"))
        y = float(input("please enter y value for point {index + 1}: \n"))
        X_train[i] = x
        Y_train[i] = y
    
    # Calculate the variance of labels in the training dataset
    label_variance = np.var(Y_train)
    print("Variance of labels in the training dataset:", label_variance)
        
    #Input X value for KNN prediction 
    X_test = np.array([input("please type X value for prediction: \n")],0)
    
    #Use KNN method to create predicted Y for input X_test
    if k<= N:
        # Initialize the KNN model with K number
        knn_model = KNeighborsRegressor (n_neighbors = K)
        # fit the model with training dataset in N(x,y)
        knn_model.fit(X_train,Y_train)
        # predit the Y for test valur
        Y_predict = knn_model.predit(X_test)
        print("The predicted Y value for input X is {Y_predict}")
    else: 
        print("Error: k should be less than or equal to the number of training points (N)")

 
 knn_regression()

    
