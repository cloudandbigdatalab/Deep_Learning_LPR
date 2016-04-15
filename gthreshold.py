###########################################################################################
########################## Global Thresholding Technique ##################################
###########################################################################################

import numpy a s np
def threshold(block , percentage black ):
# Finds a threshold for binarizing an image based on a required perc # of foreground pixels
bin count = 256
height = block . shape [0] width = block.shape[1]
area = height ∗ width
percentage area = np.floor(percentage black ∗ area);
cumulative intensity sum , theshold , found = 0, 0, 0
imhist, bins = np.histogram(block.flatten(), range=[0, bin count], b cumulative intensity sum = np.cumsum(imhist)
# Calculating binarization threshold
for index in range(bin count):
	if cumulative intensity sum [ index ] >= percentage area : threshold = index
break
return threshold