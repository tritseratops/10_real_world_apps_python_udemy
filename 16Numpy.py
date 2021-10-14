import numpy

n = numpy.arange(27)
n = n.reshape(3,3,3)
print(n)
print(type(n))

m = numpy.asarray([[1,2,3,4,5,6],[],[]],dtype=object)
print(m)
print(type(m))

import cv2

im_g =cv2.imread("16data/smallgray.png",0)
print(im_g)
print(type(im_g))
im_g =cv2.imread("16data/smallgray.png",1)
print(im_g)
print(type(im_g))

cv2.imwrite("tmp/newgrayimage.png", im_g)

im_g =cv2.imread("16data/smallgray.png",0)
cut_img = im_g[0:2,2:4]
print(cut_img)
cut_img = im_g[:,2:4]
print(cut_img)

cell = im_g[2,4]
print(cell)

for i in im_g.T:
    print(i)


for i in im_g.flat:
    print(i)


ims = numpy.hstack((im_g,im_g,im_g))
print(ims)
ims = numpy.vstack((im_g,im_g,im_g))
print(ims)

hlst = numpy.hsplit(ims, 5)
print(hlst)
print(ims[0])
vlst = numpy.hsplit(ims, 3)
print(vlst)
