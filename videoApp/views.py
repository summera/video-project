# Create your views here.
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from videoApp.models import Video

class VideoCreate(CreateView):
    model = Video

class VideoUpdate(UpdateView):
    model = Video

class VideoDelete(DeleteView):
    model = Video
    #success_url = reverse_lazy('author-list')