import numpy as np


# Tests linear regression model
def linear_regression_test(model, X_test, Y_test):
    pred_labels = model.predict(X_test)

    # Convert real values to class labels
    pred_labels[pred_labels >= 0.5] = 1
    pred_labels[pred_labels < 0.5] = 0

    # Calculate accuracy
    classified = np.sum(pred_labels == Y_test)
    total = Y_test.shape[0]
    accuracy = classified/total * 100

    return accuracy
