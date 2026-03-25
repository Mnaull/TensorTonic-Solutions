import numpy as np

def vector_norm_3d(v):
    """
    Compute the Euclidean norm of 3D vector(s).
    """
    

    if len(np.shape(v))==1:
        return np.sqrt(np.sum([vi**2 for vi in v]))
    else:
        v=np.array(v)
        return np.sqrt(v[:,0]**2+v[:,1]**2+v[:,2]**2)
    pass