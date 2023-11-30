# Importing the libraries
import cv2
import numpy as np
import mediapipe as mp


def calc_angle(a,b,c): # 3D points
    ''' Arguments:
        a,b,c -- Values (x,y,z, visibility) of the three points a, b and c which will be used to calculate the
                vectors ab and bc where 'b' will be 'elbow', 'a' will be shoulder and 'c' will be wrist.
        
        Returns:
        theta : Angle in degress between the lines joined by coordinates (a,b) and (b,c)
    '''
    a = np.array([a.x, a.y])#, a.z])    # Reduce 3D point to 2D
    b = np.array([b.x, b.y])#, b.z])    # Reduce 3D point to 2D
    c = np.array([c.x, c.y])#, c.z])    # Reduce 3D point to 2D

    ab = np.subtract(a, b)
    bc = np.subtract(b, c)
    
    theta = np.arccos(np.dot(ab, bc) / np.multiply(np.linalg.norm(ab), np.linalg.norm(bc)))     # A.B = |A||B|cos(x) where x is the angle b/w A and B
    theta = 180 - 180 * theta / 3.14    # Convert radians to degrees
    return np.round(theta, 2)


def infer():
    mp_drawing = mp.solutions.drawing_utils     # Connecting Keypoints Visuals
    mp_pose = mp.solutions.pose                 # Keypoint detection model
    left_flag = None     # Flag which stores hand position(Either UP or DOWN)
    left_count = 0       # Storage for count of bicep curls
    right_flag = None
    right_count = 0

    cap = cv2.VideoCapture(0)
    pose = mp_pose.Pose(min_detection_confidence=0.7, min_tracking_confidence=0.5) # Lnadmark detection model instance
    while cap.isOpened():
        _, frame = cap.read()

        # BGR to RGB
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)      # Convert BGR frame to RGB
        image.flags.writeable = False
        
        # Make Detections
        results = pose.process(image)                       # Get landmarks of the object in frame from the model

        # Back to BGR
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)      # Convert RGB back to BGR

        try:
            # Extract Landmarks
            landmarks = results.pose_landmarks.landmark
            left_shoulder = landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER]
            left_elbow = landmarks[mp_pose.PoseLandmark.LEFT_ELBOW]
            left_wrist = landmarks[mp_pose.PoseLandmark.LEFT_WRIST]
            right_shoulder = landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER]
            right_elbow = landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW]
            right_wrist = landmarks[mp_pose.PoseLandmark.RIGHT_WRIST]

            # Calculate angle
            left_angle = calc_angle(left_shoulder, left_elbow, left_wrist)      #  Get angle 
            right_angle = calc_angle(right_shoulder, right_elbow, right_wrist)
            
            # Render Detections
            lineColorW=mp_drawing.DrawingSpec(color=(255,255,255),thickness=2,circle_radius=2)
            lineColorG=mp_drawing.DrawingSpec(color=(0,168,39),thickness=2,circle_radius=2)
            lineColor=lineColorW
            
            # Counter 
            if left_angle > 160:
                left_flag = 'down'
            if left_angle < 50 and left_flag=='down':
                left_count += 1
                lineColor=lineColorG
                left_flag = 'up'

            if right_angle > 160:
                right_flag = 'down'
            if right_angle < 50 and right_flag=='down':
                right_count += 1
                lineColor=lineColorG
                right_flag = 'up'

            mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,mp_drawing.DrawingSpec(color=(0,0,255),thickness=2,circle_radius=2),lineColor)
            
        except:
            pass
        
        if(left_count>0):
            cv2.putText(image, f'Left Bicep Curls: {left_count}', (25, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2, cv2.LINE_AA)
        if(right_count>0):
            cv2.putText(image, f'Right Bicep Curls: {right_count}', (25, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2, cv2.LINE_AA)

        cv2.imshow('MediaPipe feed', image)

        k = cv2.waitKey(30) & 0xff  # Esc for quiting the app
        if k==27:
            break
        elif k==ord('r'):       # Reset the counter on pressing 'r' on the Keyboard
            left_count = 0
            right_count = 0

    cap.release()
    cv2.destroyAllWindows()


if __name__=='__main__':
    infer()