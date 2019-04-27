print(3)
import numpy as np
from activators import SigmoidActivator,IdentityActivator

class FullConnectedLayer():
    def __init__(self,input_size,output_size,activator):
        '''
        构造函数
        input_size: 本层输入向量的维度
        output_size: 本层输出向量的维度
        activator: 激活函数
        '''
        self.input_size=input_size
        self.output_size=output_size
        self.activator=activator

        self.W=np.random.uniform(-0.1,.1,(output_size,input_size))
        self.b=np.zeros((output_size))