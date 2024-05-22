import numpy as np
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score


def quality_metrics()
    #User input a positive integer N (number of points)
    N = int(input("Please type a positive integer: \n"))
    
    # Initialize arrays to store points
    X_correct = np.zeros(N)
    Y_predict = np.zeros(N)
    
    #Read N(x,y) points
    print("Enter the (x, y) points (0 or 1):")
    for index in range(N):
        try:
            x = int(input("Please enter x value for point {index + 1}: \n"))
            y = int(input("please enter y value for point {index + 1}: \n"))
            if x not in [0,1] or y not in [0,1]:
                raise ValueError ("inputs must be either 0 or 1")
            X_correct[i] = x
            Y_predict[i] = y
        except ValueError as e:
            print (e)
            return
        
    
    # Calculate the Precision based on N(x,y)
    precision = precision_score(X_correct,Y_predict)
    print("the precison for N(x,y)is {precision}")
    
    # Calculate the Recall based on N(x,y)
    recall = recall_score_score(X_correct,Y_predict)
    print("the recall for N(x,y)is {recall}")
    
quality_metrics()

    
