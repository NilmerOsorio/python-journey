# 🖼️ Lab: Exploring Image Properties with OpenCV

## 🎯 Overview

In this lab, I explored some fundamental image properties using **Python and OpenCV**, working with an image of **Zero Two** from *Darling in the Franxx*.

I practiced loading the image, inspecting its dimensions and data type, converting it to grayscale, and displaying useful information directly on both versions of the image.

## 📚 What I Learned

### 1. 📂 Loading Images

I used `cv2.imread()` to load the Zero Two image into Python.

I also learned to check whether an image was loaded successfully using an `if/else` statement, since OpenCV returns `None` when it cannot find or load the file.

### 2. 🎨 Converting Images to Grayscale

Using `cv2.cvtColor()`, I converted the original BGR image into grayscale.

I learned that:
- OpenCV uses **BGR** as its default color format.
- `cv2.COLOR_BGR2GRAY` converts a color image into grayscale.
- Grayscale images contain only one intensity channel instead of three color channels.

### 3. 🔍 Understanding Image Properties

I explored some important image properties:

- **Height:** The number of pixels vertically.
- **Width:** The number of pixels horizontally.
- **Channels:** The number of color channels in an image.
- **Data type (`dtype`):** Defines the type of values stored in the image.

I used `.shape` to retrieve image dimensions and `.dtype` to inspect the data type.

An important observation was that color images have three channels (BGR), while grayscale images have only one.

### 4. ✏️ Adding Text to Images

I used `cv2.putText()` to display image information directly on both images.

This allowed me to visualize properties such as height, width, channels, and data type without printing them in the terminal.

### 5. 🪟 Displaying Images

I practiced using:

| Function | Purpose |
|---|---|
| `cv2.imshow()` | Displays an image in a window. |
| `cv2.waitKey(0)` | Waits for a keyboard input. |
| `cv2.destroyAllWindows()` | Closes all OpenCV windows. |

## 💡 Key Takeaways

After completing this lab, I have a better understanding of:

- How OpenCV loads images into Python.
- How to inspect image dimensions and data types.
- The difference between BGR and grayscale images.
- How image channels work.
- How to convert color spaces.
- How to display text directly on images.
- How to handle image-loading errors.

## 🚀 Conclusion

This was a small but useful exercise to become more familiar with how OpenCV handles images internally.

Using a Zero Two image made the exercise a little more interesting while helping me understand concepts that will be important in future computer vision projects, especially when working with video streams and MediaPipe.
