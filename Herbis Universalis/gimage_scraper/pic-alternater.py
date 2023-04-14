from PIL import Image, ImageEnhance
import os

parentlist = os.listdir('scraped_images/')
print(parentlist)

for i in parentlist :
    imglist = os.listdir('scraped_images/'+i)
    print(i)
    for j in imglist:
        try:
            imageObject = Image.open("scraped_images/"+i+"/"+j)

            vert_flipped = imageObject.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
            vert_flipped.save("scraped_images/"+i+"/vert_"+j)

            hori_flipped = imageObject.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
            hori_flipped.save("scraped_images/"+i+"/hori_"+j)

            ninety_flipped = imageObject.rotate(90)
            ninety_flipped.save("scraped_images/"+i+"/deg90_"+j)

            # image brightness
            img_enhancer = ImageEnhance.Brightness(imageObject)

            factor = 1
            enhanced_output = img_enhancer.enhance(factor)
            enhanced_output.save("scraped_images/" + i + "/b1_" + j)

            factor = 0.5
            enhanced_output = img_enhancer.enhance(factor)
            enhanced_output.save("scraped_images/" + i + "/b0.5_" + j)

            factor = 1.5
            enhanced_output = img_enhancer.enhance(factor)
            enhanced_output.save("scraped_images/" + i + "/b1.5_" + j)

            # image constrast
            enhancer = ImageEnhance.Contrast(imageObject)

            factor = 1  # gives original image
            im_output = enhancer.enhance(factor)
            im_output.save("scraped_images/" + i + "/c1_" + j)

            factor = 0.5  # decrease constrast
            im_output = enhancer.enhance(factor)
            im_output.save("scraped_images/" + i + "/c0.5_" + j)

            factor = 1.5  # increase contrast
            im_output = enhancer.enhance(factor)
            im_output.save("scraped_images/" + i + "/c1.5_" + j)

        except:
            print("not a pic")


print("finished")
