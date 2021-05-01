from django import views
from rest_framework import viewsets

from trapper.models import Action, Activity, Trace
from trapper.serializers import ActionSerializer, ActivitySerializer, TraceSerializer


class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer


class ActionViewSet(viewsets.ModelViewSet):
    queryset = Action.objects.all()
    serializer_class = ActionSerializer


class TraceViewSet(viewsets.ModelViewSet):
    queryset = Trace.objects.all()
    serializer_class = TraceSerializer

    def get_serializer(self, *args, **kwargs):
        if isinstance(kwargs.get("data", {}), list):
            kwargs["many"] = True

        return super().get_serializer(*args, **kwargs)
