# sample data
img = np.full((10,10,3), 128, np.uint8)

# sample mask
mask = np.zeros((10,10), np.uint8)
mask[3:6, 3:6] = 1

# color to fill
color = np.array([0,255,0], dtype='uint8')

# equal color where mask, else image
# this would paint your object silhouette entirely with `color`
masked_img = np.where(mask[...,None], color, img)

# use `addWeighted` to blend the two images
# the object will be tinted toward `color`
out = cv2.addWeighted(img, 0.8, masked_img, 0.2,0)
