from matplotlib.colors import ListedColormap
import numpy as np

def print_rows(x):
    b=''
    for row in x:
        a = ' '.join(map(lambda x: "{:.3f} ".format(x), row)) + "\n"
        b =  b + a
    print(b)
    return b

def cmap_nan(cm, scale=9999):
        ncm = np.zeros((scale, 4))
        pcm = ListedColormap(ncm)
        ncm = np.vstack((pcm(np.linspace(0, 1, 2)), cm(np.linspace(0, 1, 254))))
        return ListedColormap(ncm)
