def color_to_grayscale(image):
    """
    Convert an RGB image to grayscale using luminance weights.
    """
    h=len(image)
    w=len(image[0])
    gray=[]
    for i in range(h):
        list=[]
        for j in range(w):
            
            list.append(0.299*image[i][j][0]+0.587*image[i][j][1]+0.114*image[i][j][2] )
        gray.append(list)

    return gray