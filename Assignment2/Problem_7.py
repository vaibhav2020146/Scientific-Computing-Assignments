import numpy as np
import matplotlib.pyplot as plt

x_noisy=[]
with open("C://Users//91991//Desktop//SC//hw2_data_denoising.txt") as f:
    for line in f:
        x_noisy.append(float(line))
x_noisy=np.array(x_noisy)

#matrix A
A=np.zeros((len(x_noisy),len(x_noisy)))
for i in range(len(x_noisy)):
    for j in range(len(x_noisy)):
        if i==j:
            A[i][j]=-1
        elif i==j+1:
            A[i][j]=1
        else:
            A[i][j]=0

#(I + λATA) x = x_noisy. Solving for x using the following code
def denoising_matrix(x_noisy, lam):
    x = np.linalg.inv(np.identity(len(x_noisy)) + lam * np.dot(A.T, A)).dot(x_noisy)
    return x

#now plotting the original signal and the denoised signal
differnt_lam=[1,100,10000]
for i in range(len(differnt_lam)):
    x_matrix=denoising_matrix(x_noisy, differnt_lam[i])
    plt.figure()
    #plt.plot(np.arange(1, 1 + len(x_noisy)), x_noisy,
    #color=(0.5, 0.5, 0.5), label="Noisy Signal")
    plt.plot(np.arange(1, 1 + len(x_noisy)), x_matrix,
    color=(0.5, 0.5, 0.5), label="Reconstructed Signal")
    plt.xlabel("$n$", fontsize=14)
    plt.ylabel("$x_{noisy}$", fontsize=14)
    plt.legend(loc="best")
    plt.gcf().tight_layout()
    plt.show()
