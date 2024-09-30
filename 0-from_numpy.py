#!/usr/bin/env python3
import pandas as pd
import numpy as np

def from_numpy(array):
    """
    Creates a pd.DataFrame from a np.ndarray
    The columns should be labeled in alphabetical order and capitalized
    """
    col_labels = [chr(i) for i in range(65, 65 + array.shape[1])]
    df = pd.DataFrame(array, columns=col_labels)
    return df
