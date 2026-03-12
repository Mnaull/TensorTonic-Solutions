def k_means_centroid_update(points, assignments, k):
    """
    Compute new centroids as the mean of assigned points.
    """
    
    cc=[[0]*len(points[0])]*k
    print(cc)
    ccount=[0]*k
    for i in range(len(points)):
        
        cluster=assignments[i]
        cc[cluster]=[cc[cluster][l]+points[i][l] for l in range(len(points[0]))]
        ccount[cluster]+=1
    print(ccount)
    for i in range(k):
        print(cc[i])
        
        if ccount[i]>0:
            cc[i]= [xi/ccount[i] for xi in cc[i]]    

    return cc
    
        
    