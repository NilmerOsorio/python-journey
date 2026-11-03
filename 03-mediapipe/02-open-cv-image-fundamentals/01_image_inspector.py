import cv2

imported_image = cv2.imread('zero_two.jpg')

if imported_image is not None:
    data_type = str(imported_image.dtype)
    height, width, channels = imported_image.shape

    cv2.putText(imported_image, f"Height: {height}", (20,40), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)
    cv2.putText(imported_image, f"Width: {width}", (20,80), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)
    cv2.putText(imported_image, f"Channels: {channels}", (20,120), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)
    cv2.putText(imported_image, f"Data Type: {data_type}", (20,160), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)
    
    cv2.imshow('Zero Two', imported_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print(f"Error: Couldn't load image. Check the file path")
