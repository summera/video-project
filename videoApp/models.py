from django.db import models
from django.core.urlresolvers import reverse

#Validates and restricts file types and file size for FileFields
#Use this field instead of File Field. See below models.
class ContentTypeRestrictedFileField(models.FileField):
	"""
	Same as FileField, but you can specify:
	* content_types - list containing allowed content_types. Example: ['application/pdf', 'image/jpeg']
	* max_upload_size - a number indicating the maximum file size allowed for upload.
	2.5MB - 2621440
	5MB - 	5242880
	10MB - 	10485760
	20MB - 	20971520
	50MB - 	5242880
	100MB -	104857600
	250MB - 214958080
	500MB - 429916160
	1GB - 	1073741824
	"""
	def __init__(self, *args, **kwargs):
		self.content_types = kwargs.pop("content_types")
		self.max_upload_size = kwargs.pop("max_upload_size")

		super(ContentTypeRestrictedFileField, self).__init__(*args, **kwargs)

	def clean(self, *args, **kwargs):        
		data = super(ContentTypeRestrictedFileField, self).clean(*args, **kwargs)
		uploadedFile = data.file
		
		try:
			content_type = uploadedFile.content_type
			if content_type in self.content_types:
				if uploadedFile._size > self.max_upload_size:
					raise forms.ValidationError(_('Please keep filesize under %s. Current filesize %s') % (filesizeformat(self.max_upload_size), filesizeformat(fileUpload._size)))
			else:
				raise forms.ValidationError(_('Filetype not supported.'))
		except AttributeError:
			pass        

		return data

# Create your models here.
class Video(models.Model):
	videoUpload = ContentTypeRestrictedFileField(upload_to='videos//%Y/%m/%d',content_types=['video/mp4','video/mpeg', 
		'video/quicktime', 'video/x-flv', 'video/x-ms-wmv', 'video/webm', 'video/ogg', 'video/x-matroska'],
		max_upload_size=1073741824)


	__original_vid = None


	def __init__(self, *args, **kwargs):
		super(Video, self).__init__(*args, **kwargs)
		self.__original_vid = self.videoUpload

	def save(self, force_insert=False, force_update=False):
		if self.videoUpload != self.__original_vid and self.__original_vid != '':
			self.delete_video()
		super(Video, self).save(force_insert, force_update)
		self.__original_vid = self.videoUpload
		print 

	def delete_video(self, empty_doc=False):
		vid_path = os.path.join(settings.MEDIA_ROOT, str(self.__original_vid))
		try:
			os.remove(vid_path)
		except:
			pass

	def get_absolute_url(self):
		return reverse('video_detail', kwargs={'pk': self.id})

class TimeTag(models.Model):
	beginTime = models.FloatField()
	endTime = models.FloatField()
	tag = models.CharField(max_length=30,)