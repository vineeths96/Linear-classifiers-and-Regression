from problem_4.load_data import load_data
from problem_4.problem_4 import problem_4


X_train, Y_train, X_test, Y_test = load_data('1D_regression_data.txt')
problem_4(X_train, Y_train, X_test, Y_test)