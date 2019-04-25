import numpy as np


def mse(A, B):
    mse = ((A - B)**2).mean()
    return mse
