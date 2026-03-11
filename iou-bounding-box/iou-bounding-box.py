def iou(box_a, box_b):
    """
    Compute Intersection over Union of two bounding boxes.
    """
    xa1,ya1,xa2,ya2=box_a
    xb1,yb1,xb2,yb2=box_b
    inter=0
    aire_a=(xa2-xa1)*(ya2-ya1)
    aire_b=(xb2-xb1)*(yb2-yb1)
    x=[xa1,xa2,xb1,xb2]
    x.sort()
    y=[ya1,ya2,yb1,yb2]
    y.sort()
    
    if( ya2<yb1 or yb2<ya1 or xa2<xb1 or xb2<xa1 ):
        return 0
    else:
        inter=(x[2]-x[1])*(y[2]-y[1])
   
    return inter/(aire_b+aire_a-inter)
        
    pass