#%%

from matplotlib import pyplot as plt
from pydicom import dcmread
from pydicom.data import get_testdata_file
import glob
import cv2 as cv
import numpy as np



data_dir = 'data/DICOM/210'
MAX_VAL = 2048

alpha = 25

def callback(val):
    pass


cv.namedWindow("sliders")
cv.createTrackbar("alpha", "sliders", 0, 100, callback)
cv.createTrackbar("low_lim", "sliders", 0, MAX_VAL, callback)
cv.createTrackbar("top_lim", "sliders", 0, MAX_VAL, callback)

for fpath in glob.glob(data_dir + "/1.3.12.2.1107.5.2.30.27329.202310170821*.dcm"):
    ds = dcmread(fpath)
    img = ds.pixel_array
    mask = np.zeros(img.size, dtype=bool)
    max_val = 0

    plt.hist(img)
    plt.show
    cv.imshow(winname = "phote", mat = 20*img)
    
    # use .get() if not sure the item exists, and want a default value if missing
    print(f"Slice location...: {ds.get('SliceLocation', '(missing)')}")

    while(True):
        alpha = cv.getTrackbarPos("alpha", "sliders")
        low_lim = cv.getTrackbarPos("low_lim", "sliders")
        top_lim = cv.getTrackbarPos("top_lim", "sliders")

        mask = np.bitwise_and(ds.pixel_array > low_lim, ds.pixel_array < top_lim)

        
        # plot the image using opencv
        cv.imshow(winname = "phote", mat = 20*img)
        cv.imshow(winname = "mask", mat = mask.astype(float))

        # Wait for 1 ms and check if 'q' key is pressed
        key = cv.waitKey(0)
        if key & 0xFF == ord('q') or key & 0xFF == ord('e') :
            break
        
    if key & 0xFF == ord('e'):
        # Close the window
        cv.destroyAllWindows()    
        break 


    

# %%
