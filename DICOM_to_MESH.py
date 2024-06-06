#%%

from matplotlib import pyplot as plt
from pydicom import dcmread
from pydicom.data import get_testdata_file
import glob
import cv2 as cv
import numpy as np
from dataclasses import dataclass



data_dir = 'data/DICOM/top_hl'
MAX_VAL = 2048

alpha = 25

kernel = np.ones((3,3),np.uint8)

def callback(val):
    pass

@dataclass
class imageData:
    img: np.array
    slc: float

img_dat_list = []


for fpath in glob.glob(data_dir + "/1.3.12.2.1107.5.2.30.27329.2023*.dcm"):
    ds = dcmread(fpath)
    img_dat_list.append(imageData(ds.pixel_array,ds.get('SliceLocation', 0)))
 
img_dat_list.sort(key = lambda x: x.slc)   
 
cv.namedWindow("sliders", cv.WINDOW_NORMAL)
cv.resizeWindow("sliders",640,300)
cv.createTrackbar("alpha", "sliders", 0, 100, callback)
cv.createTrackbar("low_lim", "sliders", 0, MAX_VAL, callback)
cv.createTrackbar("top_lim", "sliders", 0, MAX_VAL, callback)

for img_dat in img_dat_list:
    
    # histogram, bin_edges = np.histogram(img_dat.img, bins=256) 
    # fig, ax = plt.subplots()
    # ax.plot(histogram) 

    
    while(True):
        alpha = cv.getTrackbarPos("alpha", "sliders")
        low_lim = cv.getTrackbarPos("low_lim", "sliders")
        top_lim = cv.getTrackbarPos("top_lim", "sliders")

        mask = np.bitwise_and(img_dat.img > low_lim, img_dat.img < top_lim)
        mask = mask.astype(float)
        mask = cv.erode(mask, kernel)
        mask = cv.dilate(mask, kernel)

        # plot the image using opencv
        cv.imshow(winname = "photo", mat = 20*img_dat.img)
        cv.imshow(winname = "mask", mat = mask.astype(float))

        # Wait for 0 ms and check if 'q' key is pressed
        key = cv.waitKey(1)
        if key == -1:
            continue
        elif key & 0xFF == ord('q') or key & 0xFF == ord('e') :
            break
        
    if key & 0xFF == ord('e'):
        # Close the window
        
        break 
cv.destroyAllWindows()    

    

# %%
