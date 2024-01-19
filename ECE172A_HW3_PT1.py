import matplotlib.pyplot as plt
import cv2

#Plot Histogram with Bin: https://www.geeksforgeeks.org/bin-size-in-matplotlib-histogram/
#Read img with opencv: https://www.geeksforgeeks.org/python-opencv-getting-and-setting-pixels/


def computeNormGrayHistogram(img, hist_out):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    print(gray)
    return hist_out




img = cv2.imread("beach.png")

def adaptiveHistEq(img, winSize):

    #get img padding amount
    pad_amount = int(winSize/2)
    rank = 0
    output_img = img

    #create padded image
    img_padded = cv2.copyMakeBorder(img, pad_amount, pad_amount, pad_amount, pad_amount, cv2.BORDER_REFLECT)

    #get image and padded image dimensions
    imRow, imCol = np.size(img)[0:2]
    imRow_p, imCol_p = np.size(img_padded)[0:2]

    for y in range(imRow):
        for x in range(imCol):
            rank = 0
            for j in range(winSize):
                for i in range(winSize):
                    if img[y,x] > img_padded[y+j, x+i]:
                        rank = rank + 1
            output_img[y,x] = rank * (255/winSize*winSize)
    return output_img

equalized_img = adaptiveHistEq(img, 11)

cv2.imshow("img equalized", equalized_img)
cv2.waitKey(2000)
cv2.destroyAllWindows()