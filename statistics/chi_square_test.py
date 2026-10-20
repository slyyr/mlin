import numpy as np
import seaborn as sns
from scipy.stats import chi2_contingency
import pandas as pd

# sample dataset provided by seaborn
df = sns.load_dataset("titanic")

### checking connection between sex and survived

# crosstab provides a frequncy table for each item mentioned
contingency_table = pd.crosstab(df['sex'], df["survived"])

chi2, p_value, dof, expected = chi2_contingency(contingency_table)

alpha = 0.05

if p_value < alpha:
    print("reject null hypothesis, there is connection btw them")
else:
    print("accept null hypothesis, there is no connection btw them")