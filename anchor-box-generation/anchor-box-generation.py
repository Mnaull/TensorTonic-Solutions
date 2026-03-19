def generate_anchors(feature_size, image_size, scales, aspect_ratios):
    """
    Generate anchor boxes for object detection.
    """
    stride=image_size//feature_size
    w=[]
    h=[]
    grill=[]
    
    for s in scales:
        for r in aspect_ratios:
            w.append(s*r**(1/2))
            h.append(s/r**(1/2))
    print(w)
    for i in range(feature_size):
        cy=(i+0.5)*stride
        for j in range(feature_size):
            cx=(j+0.5)*stride
            for n in range(len(w)):
                width=w[n]/2
                height=h[n]/2
                grill.append([cx-width,cy-height,cx+width,cy+height])
    return grill
            
    
                
        