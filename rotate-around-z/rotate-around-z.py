import numpy as np

def rotate_around_z(points, theta):
    """
    Rotate 3D point(s) around the Z-axis by angle theta (radians).
    """
    cos=np.cos(theta)
    sin=np.sin(theta)
    points=np.array(points,dtype=float)
    R=np.array([[cos,-sin,0],[sin,cos,0],[0,0,1]])
    if len(np.shape(points))==1:
        return R@points

    rotated=points.copy()
    rotated[:,0]=points[:,0]*cos-points[:,1]*sin
    rotated[:,1]=points[:,1]*cos+points[:,0]*sin
    
    return rotated
    
    pass