#!/usr/bin/env python
# coding: utf-8

# In[83]:


class Square:
    side = 1.0
    
    def __init__(self, side):
        self.side = side
    
    def setSide(self, parameter):
        self.parameter = self.side
        if (self.parameter < 0) :
            self.side = 0
            
    
        
    
    

