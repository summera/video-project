# Create your views here.
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from videoApp.models import Video
import mimetypes

class VideoCreate(CreateView):
    model = Video

class VideoUpdate(UpdateView):
    model = Video

class VideoDelete(DeleteView):
    model = Video
    #success_url = reverse_lazy('author-list')

class VideoDetail(DetailView):
	model = Video

	def get_context_data(self, **kwargs):
		context = super(VideoDetail, self).get_context_data(**kwargs)
		mimetype,encoding = mimetypes.guess_type(str(self.object.videoUpload))
		context['mimetype'] = mimetype
		return context
	