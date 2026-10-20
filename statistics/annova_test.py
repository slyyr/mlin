import numpy as np
import seaborn as sns
import pandas as pd
from scipy.stats import f_oneway

df = sns.load_dataset('titanic')
df = df[['age','pclass']].dropna()

df['pclass'].unique()

class_1 = df[df['pclass'] == 1]['age']
class_2 = df[df['pclass'] == 2]['age']
class_3 = df[df['pclass'] == 3]['age']

# annova test
f_stats, p_value = f_oneway(class_1, class_2, class_3)

alpha = 0.05

if p_value < alpha:
    print("reject null hypothesis, there is significant difference in atleast 1 passenger class")
else:
    print("accept null hypothesis, there is no significant difference in passenger class")