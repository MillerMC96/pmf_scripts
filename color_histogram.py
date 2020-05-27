import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors

def plot_one_dist(ax, bins, this_xlabel, mean_dist, crystal,\
                  starting_point = True,save = False):

    # get standard deviation of the mean_dist's
    mean_dist_std = np.std(mean_dist)
    mean_dist_std_str = f"{mean_dist_std:.2f}"

    # get mean of mean_dist
    mean_dist_mean = np.mean(mean_dist)
    mean_dist_mean_str = f"{mean_dist_mean:.2f}"

    # plotting mean_dist distribution
    #ax.set(title = 'Distribution of movement in one direction')
    if this_xlabel:
        ax.set(xlabel = this_xlabel + ' deviation from fixed point [Å]')
    #ax.set(ylabel = 'Frequency')

    # crystal structure line
    if starting_point:
        ax.axvline(crystal, color = 'k', linestyle = '--', \
        label = 'starting position = ' + str(crystal) + ' Å')
        # mean
        ax.plot([], [], ' ', label = 'mean = ' + mean_dist_mean_str + ' Å')
    else:
        ax.axvline(mean_dist_mean, color = 'k', linestyle = '--', \
        label = 'mean = ' + mean_dist_mean_str + ' Å')

    # standard deviation
    ax.plot([], [], ' ', \
    label = 'standard deviation = ' + mean_dist_std_str + ' Å')

    # histogram with colors
    N, bin_min, patches = ax.hist(mean_dist, bins, density = True)
    fracs = N / N.max()
    norm = colors.Normalize(fracs.min(), fracs.max())
    for thisfrac, thispatch in zip(fracs, patches):
        color = plt.cm.viridis(norm(thisfrac))
        thispatch.set_facecolor(color)

    # best fit line
    y = ((1 / (np.sqrt(2 * np.pi) * mean_dist_std)) * \
         np.exp(-0.5 * (1 / mean_dist_std * (bin_min - mean_dist_mean))**2))
    ax.plot(bin_min, y, '-', color = 'r', label = 'best fit')

    ax.legend(loc = 'best')
    if save:
        plt.savefig('plots/all_pairs_mean_distribution.png', dpi=200)
    # return the plot object
    return ax
