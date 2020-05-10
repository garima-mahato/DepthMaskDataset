import os, cv2
  
# Function to rename multiple files 
def rename_files(path, prefix="bg"): 
  
    for count, filename in enumerate(os.listdir(path)): 
        dst = prefix + str(format(count+1, '03d')) + ".jpg"
        src = path+ filename 
        dst = path+ dst 
          
        # rename() function will 
        # rename all the files 
        os.rename(src, dst)

def resize_files(path, width=200, height=200):
	for count, filename in enumerate(os.listdir(path)):
		src = path + filename
		img = cv2.imread(src)
		if img.shape[0] != width and img.shape[1] != height:
			resized_img = cv2.resize(img, (width, height))
			cv2.imwrite(src, resized_img)
		
