import numpy as np

def angle_between_3d(v, w):
    """
    Compute the angle (in radians) between two 3D vectors.
    """
    def point(a,b):
        return np.sum([a[i]*b[i] for i in range(len(a))])
    
    nv=np.sqrt(point(v,v))
    nw=np.sqrt(point(w,w))
    print(nw)
    if nw<10**(-10) or nv<10**(-10):
        return np.nan

    cos=point(v,w)/(nw*nv)
    return np.arccos(np.clip(cos,-1,1))