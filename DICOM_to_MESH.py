#%%

from matplotlib import pyplot as plt
from pydicom import dcmread
from pydicom.data import get_testdata_file
import glob
import cv2 as cv
import numpy as np
from dataclasses import dataclass



data_dir = 'data/DICOM/210'
MAX_VAL = 2048

alpha = 25

def callback(val):
    pass

@dataclass
class imageData:
    img: np.array
    slc: float

img_dat_list = []

# cv.namedWindow("sliders")
# cv.createTrackbar("alpha", "sliders", 0, 100, callback)
# cv.createTrackbar("low_lim", "sliders", 0, MAX_VAL, callback)
# cv.createTrackbar("top_lim", "sliders", 0, MAX_VAL, callback)


for fpath in glob.glob(data_dir + "/1.3.12.2.1107.5.2.30.27329.202310170821*.dcm"):
    ds = dcmread(fpath)
    img_dat_list.append(imageData(ds.pixel_array,ds.get('SliceLocation', 0)))
    # img = ds.pixel_array
    # mask = np.zeros(img.size, dtype=bool)
    # max_val = 0

    # plt.hist(img)
    # plt.show
    # cv.imshow(winname = "photo", mat = 20*img)
 
img_dat_list.sort(key = lambda x: x.slc)   
 
for img_dat in img_dat_list:
    print(img_dat.slc)
    cv.imshow("photo", 20*img_dat.img)
    
    cv.waitKey()
cv.destroyAllWindows()    

    # while(True):
    #     alpha = cv.getTrackbarPos("alpha", "sliders")
    #     low_lim = cv.getTrackbarPos("low_lim", "sliders")
    #     top_lim = cv.getTrackbarPos("top_lim", "sliders")

        # mask = np.bitwise_and(ds.pixel_array > low_lim, ds.pixel_array < top_lim)

        
        # plot the image using opencv
        # cv.imshow(winname = "photo", mat = 20*img)
        # cv.imshow(winname = "mask", mat = mask.astype(float))

        # Wait for 1 ms and check if 'q' key is pressed
        # key = cv.waitKey(0)
        # if key & 0xFF == ord('q') or key & 0xFF == ord('e') :
        #     break
        
#     if key & 0xFF == ord('e'):
#         # Close the window
        
#         break 
# cv.destroyAllWindows()    

    

# %%
