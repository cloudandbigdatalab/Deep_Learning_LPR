###########################################################################################
#########Configuration file for CNN to classify characters using grayscale format #########
###########################################################################################


name: ”alprStateNet” layer {
name: ”alpr” type : ”Data” top : ”data” top: ”label”
include { phase: TRAIN
}
transform param {
scale : 0.00390625
}
data param {
source : ”examples/lprNum/lprNumTrainGray2414C1” batch size : 128
backend : LMDB
} }
layer {
name: ”lpr” type : ”Data” top : ”data” top: ”label”
include { phase: TEST
}
transform param {
scale : 0.00390625
}
data param {
source : ”rohith/gdrive/realtime_alpr_examples” batch size : 30
backend : LMDB
 } }
layer {
name: ”conv1”
type: ”Convolution” bottom : ”data”
top : ”conv1”
param {
lrmult:1
}
param {
lrmult:2
}
convolution param {
padh: 3 padw: 2
num output : 74
kernelh:5 kernel w: 5 stride : 1 weight filler {
type: ”xavier” }
bias filler { type: ”constant”
} }
}
layer {
          ”conv2” ”Convolution”
name:
type:
bottom : ”conv1” top : ”conv2”
param { lrmult:1
}
param {
lrmult:2
}
convolution param {
padh: 2
padw: 1
num output : 150
kernelh:5 kernel w: 3 stride : 1 weight filler {
type: ”xavier” }
bias filler { type: ”constant”
} }
}
layer {
          ”relu2” ”ReLU”
name:
type :
bottom : ”conv2”
top :
}
layer {
name: "pool2"
type: "Pooling"
bottom : ”conv2” top : ”pool2” pooling param {
pool: MAX kernel size : 4 stride : 1
”conv2”
”pool2” ”Pooling”
} }
layer {
name : ”norm2” type : ”LRN” bottom: ”pool2” top : ”norm2”
lrn param { local size : 5
alpha : 0.0001
beta : 0.75
} }
layer {
name: ”conv3”
type: ”Convolution” bottom : ”norm2”
top : ”conv3”
param {
lrmult:1
}
param {
lrmult:2
}
convolution param {
num output : 384 padh: 2
padw: 0
stride : 1 kernelh:3 kernel w: 1
weight filler { type: ”xavier”
}
bias filler {
type: ”constant”
} }
}
layer {
”conv4” ”Convolution”
name:
type:
bottom : ”conv3” top : ”conv4” param {
lrmult:1
}
param {
lrmult:2
}
convolution param {
pad: 1
num output : 680
kernel size : 3 stride : 1 weight filler {
type: ”xavier” }
bias filler { type: ”constant”
} }
}
layer {
       top :
}
layer {
name: type:
”conv4”
”pool3” ”Pooling”
”relu3” ”ReLU”
name:
type :
bottom : ”conv4”
bottom : ”conv4” top : ”pool3” pooling param {
pool: MAX kernel size : 4 stride : 1
} }
layer {
name : ”norm3” type : ”LRN” bottom: ”pool3” top : ”norm3”
lrn param { local size : 5
alpha : 0.0001
beta : 0.75
} }
layer {
name: ”conv5”
type: ”Convolution” bottom : ”norm3”
top : ”conv5”
param {
lrmult:1
}
param {
lrmult:2
}
convolution param {
num output : 584 stride : 1
pad: 1 group : 2
kernel size : 3
weight filler { type: ”xavier”
}
bias filler {
type: ”constant” }
”conv6”
  } }
layer { name: type:
”Convolution” bottom : ”conv5”
top : ”conv6” param {
lrmult:1
}
param {
lrmult:2
}
convolution param {
pad: 1
num output : 784
kernel size : 3 stride : 1 weight filler {
type: ”xavier” }
bias filler { type: ”constant”
} }
}
layer {
       ”relu6” ”ReLU”
name:
type :
bottom : ”conv6”
top :
}
layer {
”conv6”
”ip1” ”InnerProduct”
name:
type:
bottom : ”conv6” top: ”ip1” param {
lrmult:1
}
param {
lrmult:2
}
inner product param {
num output : 500 weight filler {
type: ”xavier” }
bias filler { type: ”constant”
} }
}
layer {
name:
type :
bottom: ”ip1” top: ”ip1”
}
layer {
name: ”Drop5” type : ”Dropout” bottom: ”ip1” top: ”ip1” dropout param {
dropout ratio : 0.5
} }
layer {
name: ”ip2”
type: ”InnerProduct” bottom: ”ip1”
top: ”ip2”
param {
lrmult:1
}
param {
lrmult:2
}
inner product param {
num output : 36 weight filler {
type: ”xavier” }
bias filler { type: ”constant”
} }
}
layer {
name:
type:
bottom: ”ip2” bottom: ”label” top : ”accuracy”
include { phase: TEST
       } }
layer { name: type :
”loss” ”SoftmaxWithLoss”
”accuracy” ”Accuracy”
bottom: ”ip2” bottom: ”label” top: ”loss”
}
A.2 Sauvola binarization technique import numpy a s np
def
averagefilter (image , m = window[0]
n = window[1]
i f m % 2 == 0 : m=m−1
if n % 2 == 0: n=n−1
window=[3, 3]):
( rows , columns ) = image . shape
pad width = (((m + 1) / 2, (m − 1) / 2), ((n + 1) / 2, (n − 1) / 2)) imageP = np.pad(image , pad width , ’edge ’)
imageD = np.array(imageP, dtype=np.double)
t = np.cumsum(np.cumsum(imageD, axis=0), axis=1);
imageI = (t[m:rows + m, n: columns + n] + t[0:rows, 0:columns] −
t[m:rows + m, 0:columns] − t[0:rows, n:columns + n])
imageI = imageI / (m ∗ n)
return imageI
  def sauvola(image, window=[3, 3], threshold=0.34): # Convert to double
  A.3
imageD = np.array(image, dtype=np.double)
# Mean value
mean = averagefilter (image , window)
# Standard deviation
meanSquare = averagefilter(np.square(imageD), window) deviation = (meanSquare − np.square(mean)) ∗∗ 0.5
# Sauvola
R = np.max(deviation)
threshold = mean ∗ (1 + threshold ∗ ( deviation / R − 1)) output = imageD > threshold
return output

     