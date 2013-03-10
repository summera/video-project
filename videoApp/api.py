from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from videoApp.models import TimeTag


class TimeTagResource(ModelResource):
    class Meta:
        queryset = TimeTag.objects.all()
        resource_name = 'time_tag'
        authorization = Authorization()
