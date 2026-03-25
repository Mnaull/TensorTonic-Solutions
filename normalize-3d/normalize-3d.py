import numpy as np

def normalize_3d(v):
    """
    Normalize 3D vector(s) to unit length.
    """
    v=np.array(v)
    if len(np.shape(v))==1:
        norm=np.sqrt(np.sum([vi*vi for vi in v]))
        if norm<10**(-8):
            return v
        return np.array([vi/norm for vi in v])

    else:
        norm=np.sqrt(v[:,0]**2+v[:,1]**2+v[:,2]**2)
        zero=[norm<10**(-10)]
        norm_bis=norm+zero
        print(norm)
        print(norm_bis)
        return v/np.transpose(norm_bis)
        
    pass