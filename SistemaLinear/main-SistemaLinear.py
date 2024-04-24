import numpy as np
import matplotlib.pyplot as plt
import sys


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('Sistema linear')
 
 
    #X = np.zeros(4, dtype=float)
  
    A = np.array([[2.0, 2.0, 1.0, 1.0], [1.0, -1.0, 2.0, -1.0], [3.0, 2.0, -3.0, -2.0], [4.0, 3.0, 2.0, 1.0]])
    #double A[] = {2.0, 2.0, 1.0, 1.0, 1.0, -1.0, 2.0, -1.0, 3.0, 2.0, -3.0, -2.0, 4.0, 3.0, 2, 1};
    B = np.array([7.0, 1.0, 4.0, 12.0])
    #A = np.array ([[1,2],[3,-5]])
    #B = np.array([4,1])
  
    print('------------------------------------------------')
    print('Matriz A: \n', A)
    print('Vetor  B: \n', B)
    X = np.linalg.solve(A, B)
    print('Vetor  X: \n', X)
    print('------------------------------------------------')
    
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
