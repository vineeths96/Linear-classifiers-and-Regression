from problem_3.load_data import load_data
from problem_3.problem_3 import problem_3


X_train, Y_train, X_test, Y_test = load_data('german.data-numeric')
problem_3(X_train, Y_train, X_test, Y_test)