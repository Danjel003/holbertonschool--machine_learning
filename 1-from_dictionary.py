#!/usr/bin/env python3
import pandas as pd

#fjalori
data = {
	'First' : [0.0, 0.5, 1.0, 1.5],
	'Second' : ['one', 'two', 'three', 'four']
}

#DataFrame nga fjalori
df = pd.DataFrame(data, index=['A', 'B', 'C', 'D'])
