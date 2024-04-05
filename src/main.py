import numpy as np


def main():
    my_infos = ['Théophile', 'ROMIEU', 'theophile.romieu@etu.u-paris.fr', '22306075', 'IAD']
    arr = np.arange(len(my_infos))
    print([my_infos[x] for x in arr])


if __name__ == '__main__':
    main()
