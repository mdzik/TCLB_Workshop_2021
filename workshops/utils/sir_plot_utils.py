import numpy as np               #loading our favorite library
import matplotlib.pyplot as plt   #and the useful plotting library
import matplotlib.pylab as pylab
import os


def make_wsir_plot_1D(s, i, r, x, nt, dt, title, w=None, y_lim=[-0.05, 1.05]):
    params = {'legend.fontsize': 'xx-large',
              'figure.figsize': (14, 8),
             'axes.labelsize': 'xx-large',
             'axes.titlesize':'xx-large',
             'xtick.labelsize':'xx-large',
             'ytick.labelsize':'xx-large'}
    pylab.rcParams.update(params)
    axes = plt.gca()
    plt.plot(x, s, color="green", linewidth=2, marker='', markevery=2, label='Susceptible')
    plt.plot(x, i, color="red", linewidth=2, label='Infected')
    plt.plot(x, r, color="purple", linewidth=2, label='Recovered')
    plt.plot(x, s + i + r, color="black", linewidth=2, label='Total population')

    plt.xlabel(r'$x$')
    plt.ylabel(r'No of people')

    if w is not None:
        plt.plot(x, w, color="blue", linewidth=2, linestyle=":", label='W')

    axes.set_ylim(y_lim)
    
    plt.grid()
    plt.legend()
    plt.title(f'{title} @ nt: {nt} dt {dt}')

    if not os.path.exists('plots'):
        os.makedirs('plots')

    fig_name = f'plots/{title}.png'
    fig = plt.gcf()  # get current figure
    fig.savefig(fig_name, bbox_inches='tight')
    plt.show()
    
    
def compare_sir_vs_wsir_plot(SIR, WSIR, beta_W, xspace, ntimesteps, title, dt, y_lim=[-0.05, 1.05]):
    S, I, R = SIR
    Sw, Iw, Rw, Ww = WSIR

    params = {'legend.fontsize': 'xx-large',
              'figure.figsize': (16, 10),
              'axes.labelsize': 'xx-large',
              'axes.titlesize': 'xx-large',
              'xtick.labelsize': 'xx-large',
              'ytick.labelsize': 'xx-large'}
    pylab.rcParams.update(params)

    axes = plt.gca()
    plt.plot(xspace, S, color="green", linewidth=2, marker='', markevery=2, label='S')
    plt.plot(xspace, I, color="red", linewidth=2, label='I')
    plt.plot(xspace, R, color="purple", linewidth=2, label='R')
    plt.plot(xspace, S + I + R, color="black", linewidth=2, label='N')

    plt.plot(xspace, Sw, color="green", linewidth=2, linestyle="", marker='o', markersize=4, markevery=3, label='S*')
    plt.plot(xspace, Iw, color="red", linewidth=2, linestyle="", marker='o', markersize=4, markevery=3, label='I*')
    plt.plot(xspace, Rw, color="purple", linewidth=2, linestyle="", marker='o', markersize=4, markevery=3, label='R*')
    plt.plot(xspace, Sw + Iw + Rw, color="black", linewidth=2, linestyle="", marker='o', markersize=4, markevery=3, label='N*')
    plt.plot(xspace, Ww, color="blue", linewidth=2, linestyle="", marker='o', markersize=4, markevery=3, label='W*')

    plt.xlabel(r'$x$')
    plt.ylabel(r'No of people')

    axes.set_ylim(y_lim)
    
    plt.grid()
    plt.legend()
    plt.title(f'{title} \n'
              f'@ ntimesteps={ntimesteps:.2e}     dt={dt:.2e}     beta_W={beta_W:.2}')

    if not os.path.exists('plots'):
        os.makedirs('plots')
    fig_name = f'plots/SIRvsWSIR_betaW{beta_W:.2e}.png'
    fig = plt.gcf()  # get current figure
    fig.savefig(fig_name, bbox_inches='tight')
    plt.show()

