import pandas as pd
import numpy as np

ANGLE_THRESHOLD = 5
COUNT_THRESHOLD = 20

def clean_df(src):
    df = pd.read_csv(src)
    df.drop(columns=["Unnamed: 2"], inplace=True)

    #fix columns
    df = df.rename(columns={df.columns[0] : df.iloc[0][0], df.columns[1] : 'theta'})
    df = df.drop(0)

    df = df.astype(float)

    #make angles positive and in rad
    df.iloc[:, 1] = (90 - df.iloc[:, 1] * -1) * np.pi / 180
    return df


#count periods


def get_amplitudes(df):
    #count oscillations, record amplitudes
    prev = (df.iloc[0][1]) #prev
    frame_rate = df.iloc[1][0] - df.iloc[0][0]
    extreme = df.iloc[0][1] #assumes first value is maximum height
    increasing = False
    oscillations = []
    amplitudes = []
    count = 0

    for row in range(1, df.shape[0]):
        theta = (df.iloc[row][1])
        time = df.iloc[row][0]
        if count > COUNT_THRESHOLD:
            #check if theta is within threshold of curr max
            if theta - prev > 0:
                #now increasing
                if not increasing:
                    #previously decreasing
                    oscillations.append(time)
                    amplitudes.append(abs(extreme - theta))
                    increasing = True
                    count = 0
                    extreme = theta
                # else:
                #     #if swapped to increasing, but is still increasing somehow
                #     oscillations[-1] += frame_rate
                #     amplitudes[-1] += abs(prev - theta)
            else:
                # now decreasing
                if increasing:
                    oscillations.append(time)
                    amplitudes.append(abs(extreme - theta))
                    increasing = False
                    count = 0
                    extreme = theta
        
        count += 1
        prev = theta
    
    return {"oscillation_times": oscillations, "amplitudes": amplitudes}