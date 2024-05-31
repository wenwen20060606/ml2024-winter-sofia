import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV

def knn_classifier(X_train,Y_train):
    param_grid = {'n_neignbors': list(range(1,11))}
    knn = KneighborsClassifier()
    grid_search = GridSearchCV(knn, param_grid, cv = 5)
    grid_search.fit(X_train.reshape(-1,1),Y_train)
    best_k = grid_search.best_params_['n_neignbors']
    best_model = grid_search.best_estimator_
        return best_k, best_model

def main():
    #User input a positive integer N (number of training set points)
    N = int(input("Please type a positive integer: \n"))
    
    # Initialize arrays to store training dataset
    X_train = np.zeros((N, 1))
    Y_train = np.zeros(N)
    
    #Read N(x,y) points
    print("Please type in the coordiantes of each points (x,y):")
    for index in range(N):
        x = float(input("Please enter a real number x value for point {index + 1}: \n"))
        y = int(input("please enter a non-negative y value for point {index + 1}: \n"))
        X_train[i] = x
        Y_train[i] = y
    
    #User input a positive integer M(number of testing set points)
    M = int(input('please type a positive integer: \n')
    
    #Initializing arrays to store testing dataset
    X_test = np.zeros((M,1))
    Y_test = np.zeros(M)
    
    #Read M(x,y)points
    Print("Please type in the coordiantes of each points (x,y):")
    for index in range(M): 
        x = float(input("Please enter a real number x value for point {index+1}:\n")
        y = int(input("please enter a non negative y value for point {index+1}:\n")
        X_test[i] = x
        Y_test[i] = y
        
    #find the best k using the GridSearch and Training set
    best_k, best_model = knn_classifier(X_train,Y_train)
    
    #Predict the y value of the testing set using the best k and best model 
    Y_predict =  best_model.predict(X_test.reshape(-1,1))
    
    #Calculate the test accuracy
    test_accuracy  = best_estimator_.score
    
    #print the output
    print('the best k for the knn classifier is {best_k}')
    print('the testing accuracy for the knn classifier is {test_accuracy}')
    
    
    
main()
   

    
