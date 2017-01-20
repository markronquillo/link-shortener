from django.db import models

from .utils import code_generator


class KirrURL(models.Model):
	url 		= models.CharField(max_length=220,)
	shortcode 	= models.CharField(max_length=15, unique=True, blank=True)
	updated 	= models.DateTimeField(auto_now=True)
	timestamp 	= models.DateTimeField(auto_now_add=True)


	def save(self, *args, **kwargs):
		if not self.shortcode or self.shortcode == "":
			self.shortcode = code_generator()

		super(KirrURL, self).save(*args, **kwargs)

	def __str__(self):
		return str(self.url)

	def __unicode__(self):
		return str(self.url)