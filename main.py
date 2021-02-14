import numpy as np
import matplotlib.pyplot as plt

line_width = 1.0
label_length = 0.25
label_width = 2.0

def solve(x, y):
    x0, y0 = x[0], y[0]
    x1, y1 = x[1], y[1]
    A = np.array([
        [x0**3, x0**2, x0, 1],
        [x1**3, x1**2, x1 , 1],
        [3*x0**2, 2*x0, 1, 0],
        [3*x1**2, 2*x1, 1, 0]])

    b = np.array([y0, y1, 0, 0])
    coe = np.linalg.solve(A, b)
    xlinkc = np.linspace(x0, x1, 101)
    ylinkc = np.polyval(coe, xlinkc)
    return xlinkc, ylinkc

def draw_mep(xx, yy, colors, **kwargs):
    state = np.array(xx)
    energy = np.array(yy)
    state_link = np.array([])
    energy_link = np.array([])
    for i in range(energy.size-1):
        xlinkc, ylinkc = solve(state[i:i+2], energy[i:i+2])
        state_link = np.append(state_link, xlinkc)
        energy_link = np.append(energy_link, ylinkc)
        plt.plot(state_link, energy_link, linewidth=line_width, color=colors, **kwargs)
        for i, coord in enumerate (state):
            label_x = np.array([coord - label_length / 2, coord + label_length /2])
            label_y = np.array([energy[i], energy[i]])
            plt.plot(label_x, label_y, linewidth=label_length, color=colors)

def main():
    state12 = [1,2,3,4,5,6]
    energy1 = [0.0, 28.7, 17.4, 27.8, 28.6, 8.6]
    energy2 = [0.0, 30.4, 15.8, 30.3, 30.4, 7.8]
    energy3 = [0.0, 29.8, 29.0, 31.5, 13.6]
    energy4 = [0.0, 27.8, 26.5, 30.8, 13.7]
    state_label = ["R", "TS1", "IM1","IM2", "TS2", "P"]
    state_link3131131 = [1,2,4,5,6]
    plt.figure(figsize = (10,6))
    draw_mep(state12,energy1,"black", label="cat-1")
    draw_mep(state12, energy2, "red", label="cat-2")
    draw_mep(state_link3131131, energy3, "blue", label="cat-3")
    draw_mep(state_link3131131, energy4, "green", label="cat-4")
    plt.xticks(state12, state_label)
    plt.legend()
    plt.show()

if __name__ == '__main__':
    main()