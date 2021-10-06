import math

import pandas as pd
import numpy  as np
import matplotlib as plt


def relu(x):
    #! RELU线性整流单元激活函数
    if x < 0:
        return 0
    elif x > 0:
        return x        

def sigmoid(x):
    #! sigmoid函数作为神经元的激活单元函数
    return 1 / (1 + math.exp(-x))

def cost():
    
    