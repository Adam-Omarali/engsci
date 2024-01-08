# Sample Python code to run the fit_black_box Python code relatively easily

import fit_black_box as bb
import read_data
import numpy as np

# First, define the function you want to fit. Here it's a linear function.
# It is critical that the independant variable ("t") is first in the list of function variables.

def linear(t, m, b):
    return m*t + b

def exp_decay(t, A, d):
    return A*np.e**(-d*t)

def harmonic(t, theta_0, tau, T, phi):
    return theta_0 * np.power(np.e, -t/tau) * np.cos(2*np.pi * t/T + phi)

def quadratic_factored(t, T_0, a, b):
    return T_0 * (a*t**2 + b*t + 1)

def quadratic(t, a, b, c):
    return (a*t**2 + b*t + c)

def even_quadratic(t, T_0, a):
    return T_0 * (a*t**2 + 1)

def avg_frames(x, sample=3):
    return x / sample

def frames_to_sec(frames, fps=60.0):
    return frames / fps

def deg2rad(ang):
    return ang * np.pi / 180

def count_oscillations(amplitudes, k):
    initial_amplitude = amplitudes[0]
    comp = np.e ** (-np.pi / k) * initial_amplitude
    for i in range(len(amplitudes)):
        amp = amplitudes[i]
        if amp <= comp:
            return i // 2
        
    return -1

def calculate_q(amplitudes):
    print("Theoretical Calculation Q = ", np.pi * TAU / PERIOD)
    ks = list(range(2, 9))
    answers = []
    for k in ks:
        ans = count_oscillations(amplitudes, k)
        print("Count Oscillations with k=", k, ":Q = ", k * ans)
        answers.append(k * ans)

    print("Mean:", np.mean(answers))
    print("Std:", np.std(answers))
    print("Uncertainty of Mean:", np.std(answers) / np.sqrt(len(ks)))




angles = [13.5, 21.3, 34.0, 43.9, 60.5, 69.8, 73.8, 81.4, -16.5, -28.4, -42.3, -50.5, -59.8, -65.6, -78.4]
time = [240, 242, 244, 247, 252, 255, 256, 260, 241, 244, 247, 250, 253, 256, 261]


lengths = list(map(lambda x: x/100, [17.6, 24.1, 51.0, 34.3, 60, 75.9, 80.5, 43.5]))

angles = list(map(deg2rad, angles))
time = list(map(frames_to_sec, map(avg_frames, time)))
x = bb.np.array(angles)
y = bb.np.array(time)
xerr = 0.008
yerr = [frames_to_sec(1)] * len(time)
# bb.plot_fit(quadratic_factored, x, y, xerr, yerr, title="Effect of Initial Angle on Period", xlabel="Initial Angle (rad)", ylabel="Period (s)")

angles = [13.5, 21.3, -16.5, -28.4]
time = [240, 242, 241, 244]
angles = list(map(deg2rad, angles))
time = list(map(frames_to_sec, map(avg_frames, time)))
x = bb.np.array(angles)
y = bb.np.array(time)
xerr = 0.008
yerr = [frames_to_sec(1)] * len(x)
# bb.plot_fit(even_quadratic, x, y, xerr, yerr, title="Effect of Small Initial Angle on Period")

# i = 7
file = f"Code/data/13.5.csv"
df = read_data.clean_df(file)
data = read_data.get_amplitudes(df)
# calculate_q(data["amplitudes"])

TAU = 36.3
PERIOD = 1.32489
# L = lengths[i]

#fitting this at different ranges yield different fitting parameters, which one is right?
x = bb.np.array(df['t'][:30 * 60])
y = bb.np.array(df['theta'][:30 * 60])
xerr = 0.05
yerr = bb.np.array([0.005] * 30*60)
# bb.plot_fit(harmonic, x, y, xerr, yerr, init_guess=(df['theta'].iloc[0], 50, 2*np.sqrt(L), 0), title="Angle Over Time -1", xlabel="Time (s)", ylabel="Angle (rad)")


x = bb.np.array(df['t'][:10])
y = bb.np.array(df['theta'][:10])
xerr = 1/120 / 4
yerr = bb.np.array([0.005] * 10)
# bb.plot_fit(harmonic, x, y, xerr, yerr, init_guess=(df['theta'].iloc[0], 50, 1.32, 0), title="Angle Over Time Zoomed In", xlabel="Time (s)", ylabel="Angle (rad)")


x = bb.np.array(data["oscillation_times"])
y = bb.np.array(data["amplitudes"])
xerr = 0.01
yerr = bb.np.array([0.05] * len(data["amplitudes"]))

bb.plot_fit(exp_decay, x, y, xerr, yerr, xlabel="Half Oscillaitions (#)", ylabel="Amplitude (rad)", title="Number of Half Oscillations Effect on Amplitude")

times = [156, 183, 258, 216, 280, 310, 325, 238]
periods = list(map(frames_to_sec, map(avg_frames, times)))

x = bb.np.array(lengths)
y = bb.np.array(periods)
xerr = 0.3 / 100
yerr = [frames_to_sec(1)] * len(x)

def power(L, p, q):
    return p * L ** q

# bb.plot_fit(power, x, y, xerr, yerr, xlabel="Length (m)", ylabel="Period (s)", title="Effect of Length on Period")
# bb.plot_fit(power, x, y, xerr, yerr, xlabel="Log Length (m)", ylabel="Log Period (s)", title="Log-Log Plot: Effect of Length on Period", log=True)

taus = [17.1, 26, 38, 33, 42, 37, 39.6, 36.2]
qs = list(map(lambda x, y: np.pi * x / y, taus, periods))
print(qs)
x = bb.np.array(lengths)
y = bb.np.array(qs)
xerr = 0.3 / 100
yerr = [0.1] * len(x)
# bb.plot_fit(quadratic, x, y, xerr, yerr, xlabel="Length (m)", ylabel="Q Factor", title="Effect of Length on Q Factor")

lengths = list(map(np.log, lengths))
periods = lengths = list(map(np.log, periods))
x = bb.np.array(lengths)
y = bb.np.array(periods)
xerr = 0.3 / 100
yerr = [frames_to_sec(1)] * len(x)
# bb.plot_fit(linear, x, y, xerr, yerr, xlabel="Log Length (m)", ylabel="Log Period (s)", title="Log-Log Plot: Effect of Length on Period")

