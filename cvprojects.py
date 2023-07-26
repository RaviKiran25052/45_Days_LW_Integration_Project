import cv2

def background_blur():
    import cv2
    cap = cv2.VideoCapture(0)
    model = cv2.CascadeClassifier("./myhaarcascade_frontalface_default.xml")
    while True:
        status, photo = cap.read()
        gray = cv2.cvtColor(photo,cv2.COLOR_BGR2GRAY)
        face = model.detectMultiScale(gray,1.3,5)
        for (x,y,w,h) in face:
    #to store the clear image face 
            face_clear = photo[y:y+h,x:x+w]
            dst = cv2.GaussianBlur(photo,(19,19),30)
    #to replace the blurred image with clear face image
            dst[y:y+h,x:x+w] = face_clear
            cv2.imshow("My blureed image",dst)
        if cv2.waitKey(1) == 13:
            break
    cv2.destroyAllWindows()
    cap.release()

def face_distance_measure():


# Load the Haar cascade classifier for face detection
    face_cascade = cv2.CascadeClassifier('myhaarcascade_frontalface_default.xml')

    # Get the focal length of the camera (change this value according to your camera)
    focal_length = 600

    # Calculate the distance from the camera to the face
    def calculate_distance(face_width, focal_length, pixel_width):
        return (face_width * focal_length) / pixel_width

    # Open the default camera
    cap = cv2.VideoCapture(0)

    while True:
            # Read a frame from the camera
            ret, frame = cap.read()

            # Convert the frame to grayscale
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Detect faces in the grayscale frame
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)

            for (x, y, w, h) in faces:
                # Draw a rectangle around the face
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

                # Calculate the distance from the camera to the face
                distance = calculate_distance(16, focal_length, w)

                # Display the distance above the rectangle
                cv2.putText(frame, f"Distance: {distance:.2f} cm", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

            # Display the resulting frame
            cv2.imshow("Face Detection", frame)

            # Exit the loop if 'q' is pressed
            if cv2.waitKey(1) == 13:
                break

        # Release the video capture object and close the windows
    cap.release()
    cv2.destroyAllWindows()
