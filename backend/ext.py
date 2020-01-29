import cv2


# Function to extract frames
def FrameCapture(path):
    # Path to video file
    vidObj = cv2.VideoCapture(path)

    # Used as counter variable
    count = 0

    # checks whether frames were extracted
    success = 1

    while success:
        # vidObj object calls read
        # function extract frames
        success, image = vidObj.read()

        # Saves the frames with frame-count
        cv2.imwrite("E://projectImplementation//projectFiles//frames//testcase//test_frame%d.jpg" % count, image)

        count += 1
    print(count)

# Driver Code
if __name__ == '__main__':
    # Calling the function
    FrameCapture("E://projectImplementation//projectFiles//frames//FYP//test_case2_patch.MOV")