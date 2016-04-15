###########################################################################################
########################## Edge based binarization #######################################
##########################################################################################

import numpy a s np import c v 2
   def
edge   based   binarization (image ):
# binarizes the image based on threshold determined from edge region
edge image = cv2.Canny(image, 0, 255)
binary image = np.zeros(shape=image.shape) Hblocks = 10
Vblocks = 5
blockH = np.floor(image.shape[0] ∗ 1.0 / Vblocks) blockW = np.floor(image.shape[1] ∗ 1.0 / Hblocks)
debug = False
for r in range(Vblocks):
for c in range(Hblocks):
r0 = r ∗ blockH + 1
c0 = c ∗ blockW + 1
imgblock = image[r0:r0 + blockH, c0:c0 + blockW] edgeblock = edge image[r0:r0 + blockH, c0:c0 + blockW]
t = find threshold (imgblock , edgeblock );
binary image[r0:r0 + blockH, c0:c0 + blockW] = imgblock < t;
binary image = np.array(binary image , dtype=np.uint8) return binary image

def
find   threshold (imgblock , edgeblock ):
# finds the threshold for a block using grayscale values from the # neighbouring pixels of all edges
t1 = []
for r in range(3, imgblock.shape[0] − 2):
for c in range(3, imgblock.shape[1] − 2): if (edgeblock[r, c] == 255 and
edgeblock[r, c − 1] == 0 and
edgeblock[r, c + 1] == 0):
m=min(imgblock[r, c−2], imgblock[r, c+2])
if m< 128:
t2 = np.mean(imgblock[r, c − 2: c + 2]) ∗ 1.0 t1 . append ( t2 )
if (edgeblock[r, c] == 255 and edgeblock[r − 1, c] == 0 and edgeblock[r + 1, c] == 0):
m = min(imgblock[r − 2, c] , imgblock[r + 2, c]) if m< 128:
t2 = np.mean(imgblock[r−2: r+2,c]) ∗ 1.0 t1 . append ( t2 )
if len(t1) == 0: t=0
else :
t = np.mean(t1) − np.std(t1)
return t