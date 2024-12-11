import pandas as pd
import numpy as np

df = pd.read_csv('csvs/unc_profile_plot.csv')
l = df['Length (μm)']
avg_std = 0
for i in range(0, int(df.shape[0] / 3)):
    p1_x = l[3*i]
    p2_x = l[3*i+1]
    p3_x = l[3*i+2]
    mean_x = (p1_x + p2_x + p3_x) / 3
    std_x = np.std([p1_x, p2_x, p3_x])
    avg_std += std_x
    print(f"Mean X: {mean_x:.2f}, Std X: {std_x:.2f}")
    
    
print(avg_std / df.shape[0])