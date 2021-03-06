'''
Script of base configuration class.

Written by Luca Derumier.
Version 1.0 - May 2020.
'''

import numpy as np

#########################################################
######################## Configs ########################
#########################################################

class Config():
    '''Base configuration class. For custom configurations, create a
    sub-class that inherits from this one and override properties
    that need to be changed.'''

    # Saves model every n epochs
    EPOCHS = 10

    # Freeze all layers but last
    FREEZE = False

    # Loads pre-trained weights from training on pascal data set
    LOAD_PRETRAINED = False

    # Non best suppression
    NON_BEST_SUP = False

    # Learning rate
    LEARNING_RATE = 0.001

    # Batch size
    BATCH_SIZE = 16

    # Anchors
    '''
    YOLO_ANCHORS = np.array(
        ((0.57273, 0.677385), (1.87446, 2.06253), (3.33843, 5.47434),
         (7.88282, 3.52778), (9.77052, 9.16828)))
    '''

    #K-MEAN-CLUSTERING ANCHORS
    YOLO_ANCHORS = np.array(
        ((2.49031525, 1.99970847), (0.94183062, 1.04296816), (0.5842771 , 0.58763431),
        (1.75105185, 1.49130222), (0.97310534, 2.17019336)))


    # Input/Output ratio size
    INPUT_DIM = (500,500)
    OUTPUT_DIM = (416,416)
