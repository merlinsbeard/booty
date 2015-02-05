from django.db import models
from worker.models import Worker
class Biometric(models.Model):
	image					= models.ImageField('biometric/image/')
	left_pinky_finger		= models.ImageField('biometric/left_pinky_finger/')
	left_ring_finger		= models.ImageField('biometric/left_ring_finger/')
	left_middle_finger		= models.ImageField('biometric/left_middle_finger/')
	left_pointing_finger	= models.ImageField('biometric/left_pointing_finger/')
	left_thumb				= models.ImageField('biometric/left_thumb/')
	right_pinky_finger		= models.ImageField('biometric/right_pinky_finger/')
	right_ring_finger		= models.ImageField('biometric/right_ring_finger/')
	right_middle_finger		= models.ImageField('biometric/right_middle_finger/')
	right_pointing_finger	= models.ImageField('biometric/right_pointing_finger/')
	right_thumb				= models.ImageField('biometric/right_thumb/')
	signature				= models.ImageField('biometric/signature/')
	Worker 					= models.OneToOneField(Worker)

