## there are 45 subdirectories in this directory, each of these subdirectories has 5 images. Assert that the number of images in each directory is 5

import os
for celeb in os.listdir("."):
    if os.path.isdir(celeb):
        # print(celeb, len(os.listdir(celeb)))
        assert len(os.listdir(celeb)) == 5
        ## now rename the images inside each directory in the form 1.png, 2.png, 3.png, 4.png, 5.png
        # for i, img in enumerate(os.listdir(celeb)):
        #     os.rename(os.path.join(celeb, img), os.path.join(celeb, str(i+1)+".png"))
        
        ## print the size of 1.png for each celeb in terms of pixels
        from PIL import Image
        img = Image.open(os.path.join(celeb, "1.png"))
        print(celeb, len(os.listdir(celeb)), "images renamed successfully to", os.listdir(celeb), "size of 1.png is", img.size)
    else:
        print(celeb, "is not a directory")