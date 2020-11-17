#/env/python
#Secret!!! - Can you see it ? by ibaraky
from  PIL import Image
PixelsArray = open('PIXELS.txt').readlines()
PixelsArray = [i.replace('\n','') for i in PixelsArray]
print(len(PixelsArray))
#PixelsArray.reverse()
def newImg():
    img = Image.new('RGB', (317,1438)) # if i add +1 to 288 i can move the angle ...
    N = 0

    for i in range(img.size[0]):
        for j in range(img.size[1]):
                #print(PixelsArray[N])
                #print(eval(PixelsArray[N]))
                #print(N)
                #print(len(PixelsArray))

                img.putpixel((i,j),eval(PixelsArray[N]))
                N+=1


                #print(i,j)


    img.save('sqry.png')


    return img

wallpaper = newImg()
wallpaper.show()