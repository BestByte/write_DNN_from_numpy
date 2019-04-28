class Percetion():
    def __init__(self,input_num,activator):
        '''
        '''
        self.activator=activator
        self.weights=[0.0 for _ in range(input_num)]
        self.bias=0.0

    def __str__(self):
        '''
        '''
        return 'weights \t:%s \n bias \t:%f\n' %(self.weights,self.bias)
            
    def predict(self,input_vec):
        '''
        '''
        return self.activator()