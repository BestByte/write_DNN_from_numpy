import numpy as np
class ReluActivator():
    def forward(self,weight_input):
        return max(0,weight_input)
    
    def backward(self,output):
        return 1 if output>0 else 0

class IdentityActivator():
    def forwrad(self,weight_input):
        return weight_input

    def backward(self,output):
        return 1

class  SigmoidActivator():
    def forward(self,weight_inoput):
        return 1.0/(1.0 +np.exp(-weight_inoput))
    
    def backward(self,output):
        return output*(1-output)

class TanhActivator():
    def  forward(self,weight_inoput):
        return 2.0/(1.0+np.exp(-2*weight_inoput))-1.0

    def backward(self,output):
        return 1-output*output
        
    