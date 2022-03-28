from skimage.measure import label as sk_label
from skimage.measure import regionprops as sk_regions

def segtodet(segmap, _label):
  '''
  extract bbox from segmentation map
  '''
  sk_mask = sk_label(segmap)
  regions = sk_regions(sk_mask)
  bboxs = []
  for region in regions:
    print('[INFO]bbox: ', region.bbox)
    y1, x1, y2, x2 = region.bbox
    bbox = {'x1': x1, 'y1': y1, 'x2': x2, 'y2': y2, 'label': _label}
    bboxs.append(bbox)
  return bboxs
    
