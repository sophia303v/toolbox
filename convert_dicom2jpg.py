import pydicom
import numpy as np
from PIL import Image

def convert_dcm_jpg(imgpath):
    """
      Using min-max method to convert dicom to jpg (png)
      imgpath : "../../000.dcm"
    """
    dcm = pydicom.dcmread(imgpath)
    img = dcm.pixel_array.astype(float)
    rescaled_image = (np.maximum(img,0)/img.max())*255 # float pixels
    final_image = np.uint8(rescaled_image) # integers pixels    
    
    final_image = Image.fromarray(final_image)

    return final_image    
