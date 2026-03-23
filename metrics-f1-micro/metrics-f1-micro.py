def f1_micro(y_true, y_pred) -> float:
    """
    Compute micro-averaged F1 for multi-class integer labels.
    """
    TP=0
    FPN=0
    
    for i in range(len(y_true)):
        y=y_true[i]
        yp=y_pred[i]
        if y==yp:
            TP+=1
        else:
            FPN+=2
    TP*=2
    return TP/(TP+FPN)
    pass