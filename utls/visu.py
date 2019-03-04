import matplotlib.pyplot as plt


def visu_p_int(p, vis_int):

    plt.plot(p)
    plt.plot(p.index, vis_int)
    plt.show()
