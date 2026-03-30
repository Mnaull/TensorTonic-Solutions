def bilinear_resize(image, new_h, new_w):
    """
    Resize a 2D grid using bilinear interpolation.
    """
    resized = [[0 for _ in range(new_w)] for _ in range(new_h)]
    H=len(image)
    W=len(image[0])
    print(resized)
    
    for i in range(new_h):
        for j in range(new_w):
            if new_h==1:
                sy=0
            else:
                sy=i*(H-1)/(new_h-1)
            if new_w==1:
                sx=0
            else:
                sx=j*(W-1)/(new_w-1)
                
            y0=int(sy)
            x0=int(sx)
            y1 = min(y0 + 1, H - 1)
            x1 = min(x0 + 1, W - 1)

            dx=sx-x0
            dy=sy-y0
            
            resized[i][j]=image[y0][x0]*(1-dy)*(1-dx)+image[y1][x0]*dy*(1-dx)+image[y0][x1]*(1-dy)*dx+image[y1][x1]*dy*dx
         
    return resized