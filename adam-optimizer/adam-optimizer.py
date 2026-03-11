import numpy as np

def adam_step(param, grad, m, v, t, lr=1e-3, beta1=0.9, beta2=0.999, eps=1e-8):
    """
    One Adam optimizer update step.
    Return (param_new, m_new, v_new).
    """
    
    m_new=np.multiply(beta1,m)+np.multiply((1-beta1),grad)
    v_new=np.multiply(beta2,v)+np.multiply((1-beta2),np.square(grad))
    
    m_bias=np.divide(m_new,(1-beta1**t))
    v_bias=np.divide(v_new,(1-beta2**t))
    
    param_new=param-np.multiply(lr,np.divide(m_bias,(np.sqrt(v_bias)+eps)))
    return (param_new,m_new,v_new)