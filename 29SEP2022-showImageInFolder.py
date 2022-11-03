import cv2

import glob

#put your own folder in the bracket eg. (“myfile/*jpg”)

path = glob.glob("images/4Nov-testMarkerNew/*.png")
#path = glob.glob("images/ColorScaleDemo20oct/*.png")
#path = glob.glob("images/testColorScaleGreen-3/*.png")




for file in path:
    img = cv2.imread(file)
    
    
    cv2.imshow("Image", img)
    #cv2.waitKey(1000) # 1 frameper Second
    cv2.waitKey(125) # 8 frameper Second
    #cv2.waitKey(62) # 16 frameper Second
    #cv2.waitKey(33) # 30 frameper Second
    #cv2.destroyAllWindows()