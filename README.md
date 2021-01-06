# Photos to Video Converter
Takes a directory of image files and converts them into a video using the OpenCV library.

Special features:
 - Can combine multiple image file formats at once. Supported image formats are available in the [OpenCV imread() docs](https://docs.opencv.org/master/d4/da8/group__imgcodecs.html#ga288b8b3da0892bd651fce07b3bbd3a56).
 - Optional dynamic resizing of images allows for images of different sizes to be combined into video (see More Info)
 - DIVX and mp4v codec options (result in .avi or .mp4 video files)
 - Frame rate option allows for easy output video frame rate control

More Info:
Dynamic image resizing can be turned on using the `-var` option. This option resizes all frames to the largest frame size, allowing images of different sizes to be combined into a video.