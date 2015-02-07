from django.db import models
from django.contrib.auth.models import User

class AccountProfile(models.Model):
	user = models.OneToOneField(User)
	website = models.URLField(blank=True)
	remarks = models.TextField(blank=True)

	def __str__(self):
		return self.user.username