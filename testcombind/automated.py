import cv2
import datetime
import os

# Create a directory to store captured images if it doesn't exist
capture_dir = "capture-img"
os.makedirs(capture_dir, exist_ok=True)

# Initialize the webcam (you might need to adjust the camera index)
camera = cv2.VideoCapture(0)

# Check if the camera is opened successfully
if not camera.isOpened():
    print("Error: Could not access the camera.")
    exit()

# Set camera properties (you can adjust these based on your requirements)
camera.set(cv2.CAP_PROP_AUTO_EXPOSURE, 0)  # Disable auto-exposure
camera.set(cv2.CAP_PROP_EXPOSURE, -3)      # Set exposure value (adjust as needed)

# Create a loop for continuous image capture
while True:
    # Capture a frame from the webcam
    ret, frame = camera.read()

    if not ret:
        print("Error: Failed to capture an image.")
        break

    # Add a timestamp to the image
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    cv2.putText(frame, timestamp, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

    # Display the image
    cv2.imshow("Wide-Field Image", frame)

    # Save the image in the 'capture-img' folder
    filename = os.path.join(capture_dir, f"wide_field_image_{timestamp}.jpg")
    cv2.imwrite(filename, frame)

    # Exit the loop when 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close the OpenCV window
camera.release()
cv2.destroyAllWindows()
