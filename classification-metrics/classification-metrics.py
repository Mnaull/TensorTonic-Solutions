import numpy as np

def classification_metrics(y_true, y_pred, average="micro", pos_label=1):
    """
    Compute accuracy, precision, recall, F1 for single-label classification.
    Averages: 'micro' | 'macro' | 'weighted' | 'binary' (uses pos_label).
    Return dict with float values.
    """
    def compute(tp,fp,fn):
    
        prec=tp/(tp+fp)
        recall=tp/(tp+fn)
        f1=2*prec*recall/(prec+recall)
        return prec,recall,f1
        
    dic={}
    
    nb_classes=len(set(y_true+y_pred))
  
    y_true=np.array(y_true)
    y_pred=np.array(y_pred)
    CONF=np.zeros((nb_classes,nb_classes))
    list=np.zeros((nb_classes,3))
    nb_data=len(y_true)

    array_metrics=np.zeros((nb_classes,3))
    for k in range(nb_data):
        i=y_pred[k]
        j=y_true[k]
        CONF[i,j]+=1


    for c in range(nb_classes):
        tp=CONF[c,c]
        fp=np.sum(CONF[c,:])-tp
        fn=np.sum(CONF[:,c])-tp
        

        list[c,0]=tp
        list[c,1]=fp
        list[c,2]=fn
     


    acc=np.sum(list[:,0])/nb_data
    dic["accuracy"]=acc


    if average=="micro":
        tp=np.sum(list[:,0])/nb_data
        fp=np.sum(list[:,1])/nb_data
        fn=np.sum(list[:,2])/nb_data

        
        prec,recall,f1=compute(tp,fp,fn)

        dic["precision"]=prec       
        dic["recall"]=recall
        dic["f1"]=f1
      
        print("fef")
    
    elif average=="macro":
        print(array_metrics)
        for c in range(nb_classes):
            array_metrics[c,0],array_metrics[c,1],array_metrics[c,2]=compute(list[c,0],list[c,1],list[c,2])
        dic["precision"]=np.mean(array_metrics[:,0])       
        dic["recall"]=np.mean(array_metrics[:,1]) 
        dic["f1"]=np.mean(array_metrics[:,2]) 

    elif average=="binary":
        c=pos_label
        array_metrics[c,0],array_metrics[c,1],array_metrics[c,2]=compute(list[c,0],list[c,1],list[c,2])
        
        dic["precision"]=array_metrics[c,0]    
        dic["recall"]=array_metrics[c,1] 
        dic["f1"]=array_metrics[c,2] 
        

    
    elif average=="weighted":
        for c in range(nb_classes):
            w_classe=np.sum(CONF[:,c])/nb_data
            array_metrics[c,0],array_metrics[c,1],array_metrics[c,2]=compute(list[c,0],list[c,1],list[c,2])
            array_metrics[c,0]*=w_classe
            array_metrics[c,1]*=w_classe
            array_metrics[c,2]*=w_classe
            
        dic["precision"]=np.sum(array_metrics[:,0])       
        dic["recall"]=np.sum(array_metrics[:,1]) 
        dic["f1"]=np.sum(array_metrics[:,2]) 



    
    return dic
        
 
    