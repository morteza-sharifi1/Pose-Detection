import numpy as np 
import cv2 
import mediapipe as mp 
mPose = mp.solutions.pose
mpDraw = mp.solutions.drawing_utils
pose = mPose.Pose()

cap = cv2.VideoCapture('4.mp4')
drawSpec1 = mpDraw.DrawingSpec(thickness=2, circle_radius=3, color=(0,0,255))
drawSpec2 = mpDraw.DrawingSpec(thickness=2, circle_radius=3, color=(0,255,0))
while True:
	success, img = cap.read()
	img = cv2.resize(img, (600,400))
	results = pose.process(img)

	h,w,c = img.shape
	# height, width, channel
	imgBlanck = np.zeros([h,w,c])
	imgBlanck.fill(255)

	mpDraw.draw_landmarks(img, results.pose_landmarks, mPose.POSE_CONNECTIONS,drawSpec1,drawSpec2)
	mpDraw.draw_landmarks(imgBlanck, results.pose_landmarks, mPose.POSE_CONNECTIONS,drawSpec1,drawSpec2)

	cv2.imshow('PoseDetection', img)
	cv2.imshow('extractedPose', imgBlanck)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break