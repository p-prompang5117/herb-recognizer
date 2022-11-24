from PIL import Image
import os

parentlist = os.listdir('scraped_images/')
print(parentlist)

for i in parentlist :
    imglist = os.listdir('scraped_images/'+i)
    print(i)
    for j in imglist:
        #print(j)
        try:
            imageObject = Image.open("scraped_images/"+i+"/"+j)

            vert_flipped = imageObject.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
            vert_flipped.save("scraped_images/"+i+"/vert_"+j)

            hori_flipped = imageObject.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
            hori_flipped.save("scraped_images/"+i+"/hori_"+j)

            ninety_flipped = imageObject.rotate(90)
            ninety_flipped.save("scraped_images/"+i+"/deg90_"+j)

            grayscaled = imageObject.convert('L')
            grayscaled.save("scraped_images/"+i+"/grayed_"+j)

        except:
            print("not a pic")


print("finished")
