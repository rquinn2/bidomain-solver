import natsort
import imageio
import os
import sys

def make_a_gif(directory):
    filenames = os.listdir(directory)
    filenames = natsort.natsorted(filenames)
    images = []
    for filename in filenames[0:-1:1]:
        images.append(imageio.imread(directory+filename))
    
    savename = directory.split('/')[2]
    imageio.mimsave(f'../movies/movie{savename}.gif', images)

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('Usage: python3 make_gif.py <"make_all"|species> [optional]<"test">') 
    elif sys.argv[1] == 'make_all':
        for directory in os.listdir('../img'):
            make_a_gif(f'../img/{directory}/')
    else:
        directory = f'../img/contour_plot_2D_species_{sys.argv[1]}/'
        if len(sys.argv) > 2:
            directory = f'../img/contour_plot_species_{sys.argv[1]}/'
        make_a_gif(directory)
