import cv2
import mediapipe as mp
import numpy as np

def calculate_angle(a,b,c):
    a = np.array(a) # First
    b = np.array(b) # Mid
    c = np.array(c) # End
    
    radians = np.arctan2(c[1]-b[1], c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0])
    angle = np.abs(radians*180.0/np.pi)
    
    if angle >180.0:
        angle = 360-angle
        
    return angle 

def infer():
    mp_drawing=mp.solutions.drawing_utils
    mp_pose=mp.solutions.pose
    cap = cv2.VideoCapture(0)

    # Pushup counter variables
    counter = 0 
    position = None

    # Setup mediapipe instance
    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
        while cap.isOpened():
            ret, frame = cap.read()
            
            # Recolor image to RGB
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image.flags.writeable = False
        
            # Make detection
            results = pose.process(image)
        
            # Recolor back to BGR
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            
            # Getting landmarks
            try:
                landmarks = results.pose_landmarks.landmark
                
                # Getting coordinates
                left_shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
                left_elbow = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
                left_wrist = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]
                right_shoulder = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
                right_elbow = [landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y]
                right_wrist = [landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y]
                
                # Calculating angle
                angle = (calculate_angle(left_shoulder, left_elbow, left_wrist) + calculate_angle(right_shoulder, right_elbow, right_wrist))/2
                
                # Pushup counter logic
                if angle > 160:
                    position = "UP"
                if angle < 70 and position =='UP':
                    position="DOWN"
                    counter +=1
                    print(counter)
                        
            except:
                pass
            
            # Rep data
            if(counter>0):
                cv2.putText(image, f'Push-ups: {counter}', (25, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2, cv2.LINE_AA)
            
            # Render detections
            mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                    mp_drawing.DrawingSpec(color=(245,114,67), thickness=2, circle_radius=2), 
                                    mp_drawing.DrawingSpec(color=(245,69,222), thickness=2, circle_radius=2) 
                                    )               
            
            cv2.imshow('Mediapipe Feed', image)

            k = cv2.waitKey(30) & 0xff  # Esc for quiting the app
            if k==27:
                break
            elif k==ord('r'):       # Reset the counter on pressing 'r' on the Keyboard
                counter=0

        cap.release()
        cv2.destroyAllWindows()

if __name__=='__main__':
    infer()