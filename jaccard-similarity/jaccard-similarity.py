def jaccard_similarity(set_a, set_b):
    """
    Compute the Jaccard similarity between two item sets.
    """
    set_a=set(set_a)
    set_b=set(set_b)
    inter=0
    
    for a in set_a:
        if a in set_b:
            inter+=1
    union=len(set_a)+len(set_b)-inter
    if union==0:
        return 0
    return inter/union