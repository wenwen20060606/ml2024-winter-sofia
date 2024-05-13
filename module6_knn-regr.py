import numpy as np
class knn_regression:
    def _init_(self, k)
        self.k = k
        self.X_train = None
        self.Y_train = None
    def fit(self, X_train, Y_train)
        self.X_train = X_train
        self.Y_train = Y_train
    def predit(self,X_test)
        distances = np.sqrt(np.sum((self.X_train - X_test)**2, axis = 1))
        nearest_indices = np.argsort(distances)[:self.k]
        nearest_neighbors = self.Y_train[nearest_indices]
            return np.mean(nearest_neighbors)
def main()
    #User input a positive integer N (number of points)
    N = int(input("Please type a positive integer: \n"))
        
    #User input a positive integer k (k nearest points for KNN method)
    k = int(input("please type a positive integer: \k"))
        
    #Initialize arrays to store the training points
    X_train = np.zeros((N,2)
    Y_train = np.zeros(N)
        
    #Read N(x,y) points
    print("Please type in the coordiantes of each points (x,y):")
    for index in range(N):
        x = float(input("Please enter x value for point {index + 1}: \n"))
        y = float(input("please enter y value for point {index + 1}: \n"))
        X_train[i] = [x,y]
        Y_train[i] = y
            
    #Initialize KNN object
    knn = knn_regression(k)
        
    #Fit the model with training data
    knn.fit(X_train,Y_train)
        
    #Input X value for KNN prediction 
    X_test = np.array([input("please type X value for prediction: \n")],0)
        
    #Use KNN method to create predicted Y for input X_test
    if k<= N:
        Y_predict = knn.predit(X_test)
        print("The predicted Y value for input X is {Y_predict}")
    else: 
        print("Error: k should be less than or equal to the number of training points (N)")
            
if __name__ == "__main__":
    main()
    
