1: Download and Install RobotFramework
   sudo pip install robotframework
   
2: Download and Install pythonautogui
   sudo apt-get install python-tk
   #sudo pip install python-Xlib（不用做）
   sudo pip install pyautogui
(python-tk is required only for Python 2.x, since it does not come with the tkinter module that the message box features use.)

#3: Download and Install xdotool(不用做)
   apt-get install xdotool
3.sudo apt-get install scrot
4: Use command to execute test cases:
   pybot --variable passwd:your pc password ~/checklist/launcher/launcher.txt
   
5: /usr/local/libpython2.7/dist-packages/pyautogui/__init__.py
	1）增加两个方法：
	def assertAndClick(image, **kwargs):
	    x,y = locateCenterOnScreen(image, **kwargs)
	    time.sleep(5)
	    click(x,y)

	def assertAndClickRight(image, **kwargs):
	    x,y = locateCenterOnScreen(image, **kwargs)
	    time.sleep(5)
	    rightClick(x,y)
	2）def click(x=None, y=None, clicks=1, interval=0.0, button='left', duration=0.0, tween=linear, pause=None, _pause=True):的
	_mouseMoveDrag('move', x, y, 0, 0, duration=0, tween=None)注释掉，增加：
	_mouseMoveDrag('move', x, y, 0, 0, duration=01, tween=linear)
	3）def _unpackXY(x, y):的
	if isinstance(x, collections.Sequence):到pass注释掉，增加：
	if type(x) in (tuple, list):
        	x, y = x[0], x[1]
    	x, y = position(x, y)
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
