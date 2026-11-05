# 🖼️ Lab 01 — Loading and Inspecting Images with OpenCV

## 🎯 About This Lab

In this lab, I started exploring **OpenCV** by learning how to load an image, inspect its properties, and display information directly on it.

The goal was to understand how OpenCV reads and represents images, as well as how to access useful information such as image dimensions, colour channels, and data types.

## 🧠 What I Learned

During this exercise, I explored the following concepts:

- 📂 **Loading Images:** Using `cv2.imread()` to import an image from a file.
- 🔍 **Checking Image Data:** Using `cv2` image properties to inspect the loaded image.
- 📏 **Image Dimensions:** Extracting the height, width, and number of colour channels with `.shape`.
- 🔢 **Data Types:** Using `.dtype` to identify the type of data stored in the image array.
- ✍️ **Adding Text:** Using `cv2.putText()` to display image information directly on the image.
- 🖥️ **Displaying Images:** Using `cv2.imshow()` to open an image in a separate window.
- ⌨️ **Keyboard Input:** Using `cv2.waitKey()` to keep the window open until a key is pressed.
- 🧹 **Window Management:** Using `cv2.destroyAllWindows()` to close OpenCV windows properly.

## ⚙️ How It Works

The programme follows a simple workflow:

1. Import the OpenCV library.
2. Load an image using `cv2.imread()`.
3. Check whether the image was loaded successfully.
4. Retrieve its data type and dimensions.
5. Add the information to the image using `cv2.putText()`.
6. Display the modified image.
7. Wait for a keyboard input and close the window.

I also learnt why checking whether an image was loaded successfully is important: it prevents the programme from trying to access properties of an image that doesn't exist or couldn't be found.

## 💡 Key Takeaways

One of the most important things I learnt is that OpenCV represents images as NumPy arrays.

This means that an image is not simply a picture: it is a collection of numerical values that describe its pixels.

Understanding this is an important foundation for future computer vision projects, particularly when working with image processing and MediaPipe.

## 🏁 Result

Successfully loaded an image, retrieved its properties, and displayed its dimensions, colour channels, and data type directly on the image.

This was my first step towards understanding how computers represent and process visual information.
