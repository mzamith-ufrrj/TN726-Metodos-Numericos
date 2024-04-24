import numpy as np
import matplotlib.pyplot as plt

#Exemplo de uma reta ax+b
if __name__ == '__main__':

    print('Exemplo 01 de MMQ')
    Xi = np.array([1.3, 3.4, 5.1, 6.8, 8.0])
    Yi =  np.array([2, 5.2, 3.8, 6.1, 5.8])
    #É linear
    g1 = Xi
    g2 = np.ones(len(Xi), dtype=float)
    g1g1 = g1 * g1
    g1g2 = g1 * g2
    g2g2 = g2 * g2
    yg1 = Yi * g1
    yg2 = Yi * g2
    sg1g1 = np.sum(g1g1)
    sg1g2 = np.sum(g1g2)
    szpg1 = np.sum(yg1)
    sg2g1 = sg1g2
    sg2g2 = np.sum(g2g2)
    szpg2 = np.sum(yg2)

    m = 2
    A = np.zeros((m, m), dtype=float)
    B = np.zeros(m, dtype=float)
    X = np.zeros(m, dtype=float)
    A[0][0] = sg1g1
    A[0][1] = sg2g1
    A[1][0] = sg1g2
    A[1][1] = sg2g2
    B[0] = szpg1
    B[1] = szpg2

    print(A)
    print(B)
    X = np.linalg.solve(A, B)

    xf = np.linspace(np.min(Xi)-1, np.max(Xi)+1, 1000)
    yf = X[0] * xf + X[1]

    r2, r2ajust =coeficienteDeterminacao(X, Xi, Yi)
    print('R2: ', r2)
    print('R2 ajustado: ', r2ajust)

    #Solução pronta
    #X1 = np.linalg.lstsq(np.vstack([Xi, np.ones(len(Xi))]).T, Yi, rcond=None)[0]
    #print(X1)
    #print(X)
    fig, ax = plt.subplots(figsize=(12, 8))
    #plt.figure(figsize=(12, 8))
    ax.plot(Xi, Yi, 'bo', label='Pontos')
    ax.plot(xf, yf, label="g(x)", c='black')
    txt = r'$g(x) = 0.52241113x + 2.00973725$'
    ax.annotate(txt, xy=(3, 3.57697064),xytext=(3.0, 2.5), fontsize=20 ,arrowprops=dict(facecolor='black',shrink=0.005), )
    #ax.grid()
    ax.legend()
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.xlim([0, 10])
    plt.ylim([0, 10])
    plt.xticks(np.arange(0, 11, 1))
    plt.yticks(np.arange(0, 11, 1))
    plt.show()

