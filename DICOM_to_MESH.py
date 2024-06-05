#%%

from matplotlib import pyplot as plt
from pydicom import dcmread
from pydicom.data import get_testdata_file
import glob
import cv2 as cv
import numpy as np


data_dir = 'data/DICOM'
MAX_VAL = 2048

alpha = 25

def callback(val):
    pass


cv.namedWindow("sliders")
cv.createTrackbar("alpha", "sliders", 0, 100, callback)
cv.createTrackbar("low_lim", "sliders", 0, MAX_VAL, callback)
cv.createTrackbar("top_lim", "sliders", 0, MAX_VAL, callback)

for fpath in glob.glob(data_dir + '/*.dcm'):
    ds = dcmread(fpath)
    img = ds.pixel_array
    mask = np.zeros(img.size, dtype=bool)
    max_val = 0

    plt.hist(img)
    plt.show

    
    # use .get() if not sure the item exists, and want a default value if missing
    print(f"Slice location...: {ds.get('SliceLocation', '(missing)')}")

    while(True):
        alpha = cv.getTrackbarPos("alpha", "sliders")
        low_lim = cv.getTrackbarPos("low_lim", "sliders")
        top_lim = cv.getTrackbarPos("top_lim", "sliders")

        mask = np.bitwise_and(ds.pixel_array > low_lim, ds.pixel_array < top_lim)

        
        # plot the image using opencv
        cv.imshow(winname = "foto", mat = 10*img)
        cv.imshow(winname = "mask", mat = mask.astype(float))

        # Wait for 1 ms and check if 'q' key is pressed
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
        
    if cv.waitKey(100) & 0xFF == ord('e'):
        # Close the window
        cv.destroyAllWindows()    
        break 


    

# %%
