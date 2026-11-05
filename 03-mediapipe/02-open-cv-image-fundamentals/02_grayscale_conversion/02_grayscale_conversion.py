import cv2

imported_image = cv2.imread('zerotwo.jpg')

if imported_image is not None:
    gray_image = cv2.cvtColor(imported_image, cv2.COLOR_BGR2GRAY)

    data_type = str(imported_image.dtype)
    gray_data_type = str(imported_image.dtype)
    height, width, channels = imported_image.shape
    gray_height, gray_width = gray_image.shape

    cv2.putText(imported_image, f"Height: {height}", (20,40), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)
    cv2.putText(imported_image, f"Width: {width}", (20,80), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)
    cv2.putText(imported_image, f"Channels: {channels}", (20,120), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)
    cv2.putText(imported_image, f"Data Type: {data_type}", (20,160), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)

    cv2.imshow('Zero Two: Original Image', imported_image)

    cv2.putText(gray_image, f"Height: {gray_height}", (20,40), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)
    cv2.putText(gray_image, f"Width: {gray_width}", (20,80), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)
    cv2.putText(gray_image, f"Data Type: {gray_data_type}", (20,160), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)

    cv2.imshow('Zero Two: Grayscale', gray_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print(f"Error: Coudln't load image.")
