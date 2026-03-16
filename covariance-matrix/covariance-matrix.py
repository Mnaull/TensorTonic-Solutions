import numpy as np

def covariance_matrix(X):
    """
    Compute covariance matrix from dataset X.
    """
    X=np.array(X)
    if len(np.shape(X))<2:
        return None
    N,D=np.shape(X)
    mu=np.zeros(D)
    COV=np.zeros((D,D))
    x0=np.zeros((N,D))

    if N<2:
        return None 

    
    for d in range(D):
        mu[d]=np.mean(X[:,d])
    
    for n in range(N):
        print(X[n]-mu)
        x0[n]=X[n]-mu
    print(mu)
    X=x0
    COV=1/(N-1)*np.transpose(X)@X
    return COV
    pass