import time
import signal
import atexit
import RPi.GPIO as GPIO

atexit.register(GPIO.cleanup)

horizon_servopin=12
vertical_servopin=16
GPIO.setmode(GPIO.BOARD)
GPIO.setup(horizon_servopin,GPIO.OUT,initial=False)
GPIO.setup(vertical_servopin,GPIO.OUT,initial=False)
p_horizon=GPIO.PWM(horizon_servopin,50)
p_vertical=GPIO.PWM(vertical_servopin,50)
p_horizon.start(0)
p_vertical.start(0)

def servodriver(servo,angle):
	i=angle/3.6+25
	servo.ChangeDutyCycle(i/10.0)



Clock = 36
Address = 38
DataOut = 40

def ADC_Read(channel):
	value = 0;
	for i in range(0,4):
		if((channel >> (3 - i)) & 0x01):
			GPIO.output(Address,GPIO.HIGH)
		else:
			GPIO.output(Address,GPIO.LOW)
		GPIO.output(Clock,GPIO.HIGH)
		GPIO.output(Clock,GPIO.LOW)
	for i in range(0,6):
		GPIO.output(Clock,GPIO.HIGH)
		GPIO.output(Clock,GPIO.LOW)
	time.sleep(0.001)
	for i in range(0,10):
		GPIO.output(Clock,GPIO.HIGH)
		value <<= 1
		if(GPIO.input(DataOut)):
			value |= 0x01
		GPIO.output(Clock,GPIO.LOW)
	return value
	
GPIO.setwarnings(False)
GPIO.setup(Clock,GPIO.OUT)
GPIO.setup(Address,GPIO.OUT)
GPIO.setup(DataOut,GPIO.IN,GPIO.PUD_UP)


horizon_light_min_channel=6
horizon_light_max_channel=7
vertical_light_min_channel=8
vertical_light_max_channel=9
light_gap=5
horizon_angle=0
vertical_angle=0

while True:
	horizon_light_min=ADC_Read(horizon_light_min_channel)
	horizon_light_max=ADC_Read(horizon_light_max_channel)
	vertical_light_min=ADC_Read(vertical_light_min_channel)
	vertical_light_max=ADC_Read(vertical_light_max_channel)
	while horizon_light_max-horizon_light_min>light_gap:
		if horizon_angle+1>180:
			horizon_angle=180
		else:
			horizon_angle=horizon_angle+1
		servodriver(p_horizon,horizon_angle)
		time.sleep(0.5)
		horizon_light_min=ADC_Read(horizon_light_min_channel)
		horizon_light_max=ADC_Read(horizon_light_max_channel)
	while horizon_light_min-horizon_light_max>light_gap:
		if horizon_angle-1<0:
			horizon_angle=0
		else:
			horizon_angle=horizon_angle-1
		servodriver(p_horizon,horizon_angle)
		time.sleep(0.5)
		horizon_light_min=ADC_Read(horizon_light_min_channel)
		horizon_light_max=ADC_Read(horizon_light_max_channel)
	while vertical_light_max-vertical_light_min>light_gap:
		if vertical_angle+1>180:
			vertical_angle=180
		else:
			vertical_angle=vertical_angle+1
		servodriver(p_vertical,vertical_angle)
		time.sleep(0.5)
		vertical_light_min=ADC_Read(vertical_light_min_channel)
		vertical_light_max=ADC_Read(vertical_light_max_channel)
	while vertical_light_min-vertical_light_max>light_gap:
		if vertical_angle-1<0:
			vertical_angle=0
		else:
			vertical_angle=vertical_angle-1
		servodriver(p_vertical,vertical_angle)
		time.sleep(0.5)
		vertical_light_min=ADC_Read(vertical_light_min_channel)
		vertical_light_max=ADC_Read(vertical_light_max_channel)

'''
#for i in range(25,125,1):
for i in range(0,181,2):
	servodriver(p_horizon,i)
	servodriver(p_vertical,i/2.0)
	print i
	time.sleep(0.5)
'''
'''
while(True):
  for i in range(0,360,10):
      p.ChangeDutyCycle(12.5-5*i/360)
      time.sleep(1)
  for i in  range(0,360,10):
       p.ChangeDutyCycle(7.5-5*i/360)
       time.sleep(1)
'''
