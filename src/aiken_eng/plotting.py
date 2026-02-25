import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np

mpl.rcParams["axes.titlesize"] = "medium"
mpl.rcParams["axes.grid"] = True
mpl.rcParams["axes.formatter.use_mathtext"] = True
mpl.rcParams["xtick.top"] = True
mpl.rcParams["xtick.labelsize"] = "small"
mpl.rcParams["xtick.direction"] = "in"
mpl.rcParams["xtick.minor.visible"] = True
mpl.rcParams["ytick.right"] = True
mpl.rcParams["ytick.labelsize"] = "small"
mpl.rcParams["ytick.direction"] = "in"
mpl.rcParams["ytick.minor.visible"] = True
mpl.rcParams["grid.linewidth"] = 0.5
mpl.rcParams["legend.fontsize"] = "small"
mpl.rcParams["legend.framealpha"] = 1.0

print("aiken_plot_defaults.py imported.")

ansys_colors = [
    (0, 0, 255),
    (0, 160, 255),
    (0, 255, 255),
    (0, 255, 260),
    (0, 255, 0),
    (178, 255, 0),
    (255, 255, 0),
    (255, 145, 0),
    (255, 0, 0),
]


def plot(x, y, x_label=None, y_label=None, title=None, c="black", hline=None):
    plt.plot(x, y, c=c)
    _plot_options(x=x, x_label=x_label, y_label=y_label, title=title, hline=hline)
    plt.show()


def scatter(x, y, x_label=None, y_label=None, title=None, s=1, c="black", hline=None):
    plt.scatter(x, y, s=s, c=c)
    _plot_options(x=x, x_label=x_label, y_label=y_label, title=title, hline=hline)
    plt.show()


def plot_series(x, y: dict, x_label=None, y_label=None, title=None, hline=None):
    for k in y:
        plt.plot(x, y[k], label=k)
    _plot_options(x=x, x_label=x_label, y_label=y_label, title=title, hline=hline)
    plt.legend()
    plt.show()


def _plot_options(x, x_label=None, y_label=None, title=None, hline=None):
    if hline:
        plt.hlines(hline, x.min(), x.max(), linestyles="dashed")
    if x_label:
        plt.xlabel(x_label)
    if y_label:
        plt.ylabel(y_label)
    if title:
        plt.title(title)


def plot_2d_scatter_colorbar(
    data, title, size=(20, 5), color="hsv", s=2.0, colors_rgb=None
):
    """
    Can specify list of colors to plot in discrete mode.
    Example:
    plot_data(data={"Theta (degrees)": nodes["Y"],
                    "Height (inches)": nodes["Z"],
                    "Membrane Stress (psi)": nodes["Pm"]},
              title="Membrane Stress in Shell",
              colors_rgb=ansys_colors)
    """
    x, y, z = data.keys()

    fig = plt.figure(figsize=size)
    ax = fig.add_subplot(111)

    zvals = np.asarray(list(data[z]))

    # DISCRETE mode
    if colors_rgb is not None:
        if len(colors_rgb) < 1:
            raise ValueError("colors_rgb must contain at least 1 (r,g,b) color.")

        # Convert (r,g,b) to 0..1 floats (support 0..255 ints or 0..1 floats)
        cols = np.asarray(colors_rgb, dtype=float)
        if cols.max() > 1.0:
            cols = cols / 255.0
        cols = np.clip(cols, 0.0, 1.0)

        cmap = mcolors.ListedColormap(cols)

        # Auto-scale boundaries from z range into N discrete bins
        zmin = float(np.nanmin(zvals))
        zmax = float(np.nanmax(zvals))
        n = len(cols)

        # Handle constant z gracefully: everything gets the first color
        if np.isclose(zmin, zmax) or not np.isfinite(zmin) or not np.isfinite(zmax):
            boundaries = np.array([zmin - 0.5, zmin + 0.5])
            norm = mcolors.BoundaryNorm(boundaries, cmap.N)
        else:
            boundaries = np.linspace(zmin, zmax, n + 1)
            norm = mcolors.BoundaryNorm(boundaries, cmap.N)

        p = ax.scatter(data[x], data[y], s=s, c=zvals, cmap=cmap, norm=norm)

        cbar = fig.colorbar(p, ax=ax, shrink=0.75, label=z, boundaries=boundaries)
        cbar.ax.set_yticklabels([f"{b:g}" for b in boundaries])

    # CONTINUOUS mode
    else:
        p = ax.scatter(data[x], data[y], s=s, c=data[z], cmap=color)
        fig.colorbar(p, ax=ax, shrink=0.75, label=z)

    ax.set_xlabel(x)
    ax.set_ylabel(y)
    ax.set_title(title)
    plt.show()
