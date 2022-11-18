"""
Draw segmentation mask on image.
Ref: https://learnopencv.com/deep-learning-based-object-detection-and-instance-segmentation-using-mask-rcnn-in-opencv-python-c/
"""

def draw_mask(img, mask, color, alpha=0.3, beta=0.7):
    """
    img: numpy array
    mask: 2d numpy array with binary value 0 & 1
    color: ex: [0, 255, 0]
    """
    roi = img[mask==1]
    img[mask==1] = (  [alpha* color[0], alpha*color[1], alpha* color[2]] + beta * roi)

    return img
