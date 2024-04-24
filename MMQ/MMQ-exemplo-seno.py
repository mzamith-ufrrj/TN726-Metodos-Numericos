
import numpy as np
import matplotlib.pyplot as plt
import sys


if __name__ == '__main__':

    print('Exemplo 01 de MMQ')
    #pontos
    Xi = np.array([0, np.pi/16, np.pi/8, np.pi/4, np.pi/2])
    Yi = np.sin(Xi)

    #função que deu origem aos pontos
    x1 = np.linspace(0, np.pi/2, 1000)
    y1 = np.sin(x1)

    #MMQ
    g1 = np.power(Xi, 2.0)
    g2 = Xi
    g3 = np.ones(len(Xi), dtype=float)

    g1g1 = np.sum(g1 * g1)
    g1g2 = np.sum(g1 * g2)
    g1g3 = np.sum(g1 * g3)

    g2g1 = g1g2
    g2g2 = np.sum(g2 * g2)
    g2g3 = np.sum(g2 * g3)

    g3g1 = g1g3
    g3g2 = g2g3
    g3g3 = np.sum(g3 * g3)

    yg1  = np.sum(g1 * Yi)
    yg2  = np.sum(g2 * Yi)
    yg3  = np.sum(g3 * Yi)

    #Montando a matriz
    m = 3
    A = np.zeros((m, m), dtype=float)
    B = np.zeros(m, dtype=float)
    X = np.zeros(m, dtype=float)

    A[0][0] = g1g1
    A[0][1] = g1g2
    A[0][2] = g1g3

    A[1][0] = g2g1
    A[1][1] = g2g2
    A[1][2] = g2g3

    A[2][0] = g3g1
    A[2][1] = g3g2
    A[2][2] = g3g3



    B[0] = yg1
    B[1] = yg2
    B[2] = yg3

    print(A)
    print(B)
    X = np.linalg.solve(A, B)
    print(X)
    xf = np.linspace(0, np.pi/2, 1000)
    yf = X[0] * np.power(xf, 2.0) + X[1] * xf + X[2]

 
    #exibindo o gráfico
    fig, ax = plt.subplots(figsize=(12, 8))
    #plt.figure(figsize=(12, 8))
    ax.plot(Xi, Yi, 'bo', label='Pontos')
    ax.plot(x1, y1, label="f(x)", c='blue')
    ax.plot(xf, yf, label="g(x)", c='red')

    txt = r'$g(x) = {:.3}x^2 + {:.3}x {:.3}$'.format(X[0], X[1], X[2])
    ax.annotate(txt, xy=(1, X[0] * 1 + X[1] * 1 + X[2]),xytext=(0.15, 0.1), fontsize=14 ,arrowprops=dict(facecolor='black',shrink=0.005), )

    txt = r'$f(x) = sen(x)$'
    ax.annotate(txt, xy=(1, np.sin(1)),xytext=(0.0, 0.7), fontsize=14 ,arrowprops=dict(facecolor='black',shrink=0.005), )

    #ax.grid()
    #ax.legend()
    plt.xlabel('X')
    plt.ylabel('Y')
    #plt.xlim([-0.5, 2])
    #plt.ylim([-0.5, 2])
    plt.xticks(np.arange(0, 1.7, 0.1))
    plt.yticks(np.arange(0, 1.1, 0.1))
    plt.show()


