import cv2
import numpy as np
import math
def create_line(x,y,img):
	cv2.line(img,(x,y),(320,240),(255,0,0),2)
def ret_dist(i,j,index):
	
	x = abs(320-i)
	y = abs(240-j)
	
	
	if index == 1:
		return -1*(x) , -1*(y)
	elif index ==2:
		return x , -1*(y)
	elif index ==3:
		return x,y
	elif index ==4:
		return -1*(x) , y 
def check_rect1(x1,y1):
	sum=0
	area=[]
	rect_area = 76800	
	x = [320,640,640,320]
	y = [0,0,240,240]
	for i in range(0,4):
		if i==3:
			j=0
			dist1 = math.trunc(((pow((x[i]-x[j]),2) + pow((y[i]-y[j]),2))**0.5))
			dist2 = math.trunc(((pow((x[i]-x1),2) + pow((y[i]-y1),2))**0.5))
			dist3 = math.trunc(((pow((x1-x[j]),2) + pow((y1-y[j]),2))**0.5))
			s = math.trunc((dist1+dist2+dist3)/2)
			ara = math.trunc(((s*(s-dist1)*(s-dist2)*(s-dist3))**0.5))
			area.append(ara)
			sum+=ara
					 
		else:
			dist1 = math.trunc(((pow((x[i]-x[i+1]),2) + pow((y[i]-y[i+1]),2))**0.5))
			dist2 = math.trunc(((pow((x[i]-x1),2) + pow((y[i]-y1),2))**0.5))
			dist3 = math.trunc(((pow((x1-x[i+1]),2) + pow((y1-y[i+1]),2))**0.5))
			s = math.trunc((dist1+dist2+dist3)/2)
			ara = math.trunc(((s*(s-dist1)*(s-dist2)*(s-dist3))**0.5))
			area.append(ara)
			sum+=ara
	flag=0
	if sum>rect_area:
		return 0
	else:
		for i in range(0,4):	
			if area[i] ==0:
				flag=1
		
		if flag==1:
			return 1
		else:
			return 2
		


def check_rect2(x1,y1):
	sum=0
	area=[]
	rect_area = 76800	
	x = [0,320,320,0]
	y = [0,0,240,240]
	for i in range(0,4):
		if i==3:
			j=0
			dist1 = math.trunc(((pow((x[i]-x[j]),2) + pow((y[i]-y[j]),2))**0.5))
			dist2 = math.trunc(((pow((x[i]-x1),2) + pow((y[i]-y1),2))**0.5))
			dist3 = math.trunc(((pow((x1-x[j]),2) + pow((y1-y[j]),2))**0.5))
			s = math.trunc((dist1+dist2+dist3)/2)
			ara = math.trunc(((s*(s-dist1)*(s-dist2)*(s-dist3))**0.5))
			area.append(ara)
			sum+=ara
					 
		else:
			dist1 = math.trunc(((pow((x[i]-x[i+1]),2) + pow((y[i]-y[i+1]),2))**0.5))
			dist2 = math.trunc(((pow((x[i]-x1),2) + pow((y[i]-y1),2))**0.5))
			dist3 = math.trunc(((pow((x1-x[i+1]),2) + pow((y1-y[i+1]),2))**0.5))
			s = math.trunc((dist1+dist2+dist3)/2)
			ara = math.trunc(((s*(s-dist1)*(s-dist2)*(s-dist3))**0.5))
			area.append(ara)
			sum+=ara
	flag=0	
	if sum>rect_area:
		return 0
	else:
		for i in range(0,4):	
			if area[i] ==0:
				flag=1
		
		if flag==1:
			return 1
		else:
			return 2


def check_rect3(x1,y1):
	sum=0
	area=[]
	rect_area = 76800	
	x = [0,320,320,0]
	y = [240,240,480,480]
	for i in range(0,4):
		if i==3:
			j=0
			dist1 = math.trunc(((pow((x[i]-x[j]),2) + pow((y[i]-y[j]),2))**0.5))
			dist2 = math.trunc(((pow((x[i]-x1),2) + pow((y[i]-y1),2))**0.5))
			dist3 = math.trunc(((pow((x1-x[j]),2) + pow((y1-y[j]),2))**0.5))
			s = math.trunc((dist1+dist2+dist3)/2)
			ara = math.trunc(((s*(s-dist1)*(s-dist2)*(s-dist3))**0.5))
			area.append(ara)
			sum+=ara
					 
		else:
			dist1 = math.trunc(((pow((x[i]-x[i+1]),2) + pow((y[i]-y[i+1]),2))**0.5))
			dist2 = math.trunc(((pow((x[i]-x1),2) + pow((y[i]-y1),2))**0.5))
			dist3 = math.trunc(((pow((x1-x[i+1]),2) + pow((y1-y[i+1]),2))**0.5))
			s = math.trunc((dist1+dist2+dist3)/2)
			ara = math.trunc(((s*(s-dist1)*(s-dist2)*(s-dist3))**0.5))
			area.append(ara)
			sum+=ara
	flag=0	
	if sum>rect_area:
		return 0
	else:
		for i in range(0,4):	
			if area[i] ==0:
				flag=1
		
		if flag==1:
			return 1
		else:
			return 2


def check_rect4(x1,y1):
	sum=0
	area=[]
	rect_area = 76800	
	x = [320,640,640,320]
	y = [240,240,480,480]
	for i in range(0,4):
		if i==3:
			j=0
			dist1 = math.trunc(((pow((x[i]-x[j]),2) + pow((y[i]-y[j]),2))**0.5))
			dist2 = math.trunc(((pow((x[i]-x1),2) + pow((y[i]-y1),2))**0.5))
			dist3 = math.trunc(((pow((x1-x[j]),2) + pow((y1-y[j]),2))**0.5))
			s = math.trunc((dist1+dist2+dist3)/2)
			ara = math.trunc(((s*(s-dist1)*(s-dist2)*(s-dist3))**0.5))
			area.append(ara)
			sum+=ara
					 
		else:
			dist1 = math.trunc(((pow((x[i]-x[i+1]),2) + pow((y[i]-y[i+1]),2))**0.5))
			dist2 = math.trunc(((pow((x[i]-x1),2) + pow((y[i]-y1),2))**0.5))
			dist3 = math.trunc(((pow((x1-x[i+1]),2) + pow((y1-y[i+1]),2))**0.5))
			s = math.trunc((dist1+dist2+dist3)/2)
			ara = math.trunc(((s*(s-dist1)*(s-dist2)*(s-dist3))**0.5))
			area.append(ara)
			sum+=ara
	
	flag=0
	
	if sum>rect_area:
		return 0
	else:
		for i in range(0,4):	
			if area[i] ==0:
				flag=1
		
		if flag==1:
			return 1
		else:
			return 2


def get_quadrant(m,n):
	quadrant=0
	cv2.circle(img,(m,n),5,(250,0,0),-1)

	rect_val1 = check_rect1(m,n)
	rect_val2 = check_rect2(m,n)
	rect_val3 = check_rect3(m,n)
	rect_val4 = check_rect4(m,n)


	rect_vals=[rect_val1,rect_val2,rect_val3,rect_val4]

	index = 0 
	for i in range(len(rect_vals)):
		if rect_vals[i]==2:
			index=i
	index+=1
	return index




def draw_borders(img):						#Draws rectangles on the screen for the user
	cv2.rectangle(img,(0,0),(320,240),(0,250,0),2)
	cv2.rectangle(img,(320,0),(640,240),(0,250,0),2)
	cv2.rectangle(img,(0,240),(320,480),(0,250,0),2)
	cv2.rectangle(img,(320,240),(640,480),(0,250,0),2)




cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))


while True:
	ret,frame = cap.read()
	frame=cv2.medianBlur(frame,5)
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	lower_blue = np.array([82,80,120])
    	upper_blue = np.array([140,250,250])
	dilate = cv2.inRange(hsv, lower_blue, upper_blue)	
	#erode = cv2.erode(thrImg,None,iterations = 3)
	#ilate = cv2.dilate(erode,None,iterations = 10)
	
	draw_borders(frame)
	
	
	img,cnts,hi = cv2.findContours(dilate,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
	
	max_area=0	
	index=0	
	x_d,y_d=0,0
	if len(cnts)==0:
		pass		
	else:
		for i in range(len(cnts)):
			a = cv2.contourArea(cnts[i])
			if a > max_area:
				cnt = cnts[i] 
	
		cv2.drawContours(frame,cnt,-1,(0,255,0),3)
		M = cv2.moments(cnt)	
		cx = int(M['m10']/M['m00'])
		cy = int(M['m01']/M['m00'])
		cv2.circle(frame,(cx,cy),3,(0,0,255),-1)
		
		ind = get_quadrant(cx,cy)
		x_d,y_d = ret_dist(cx,cy,ind)
		create_line(cx,cy,frame)
		font = cv2.FONT_HERSHEY_SIMPLEX
		X = str(x_d)	
		Y = str(y_d)	
		cv2.putText(frame,X,(10,15), font, 0.5,(255,255,255),2,cv2.LINE_AA)
		cv2.putText(frame,Y,(10,30), font, 0.5,(255,255,255),2,cv2.LINE_AA)
	print "x =", x_d , "    y=" , y_d
	print "   "
	out.write(frame)
#	cv2.imshow('frame',frame)
#    	cv2.imshow('mask',thrImg)
    	k = cv2.waitKey(5) & 0xFF
    	if k == 27:
    	    break

cv2.destroyAllWindows()
cap.release()
out.release()
