import numpy as np

def apply_homogeneous_transform(T, points):
    """
    Apply 4x4 homogeneous transform T to 3D point(s).
    """
    points = np.asarray(points)
    T=np.asarray(T)
    if points.ndim==1:
        points=np.append(points,1)
        return (points@T.T)[:3]

    N,_=np.shape(points)
    p=np.hstack((points,np.ones((N,1))))
    
    return p@T.T[:,:3]

    
    pass