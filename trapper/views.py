from django.db import connection
from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
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


SQL = """
SELECT t.time, u.*
FROM trapper_action a, trapper_trace t, unnest(a.measures, t.data) AS u(measure, value)
WHERE a.id = t.action_id AND a.id = %s
"""


@require_http_methods(["GET"])
def get_last_action(request):
    action = Action.objects.latest("created_at")
    action_dict = model_to_dict(action)
    action_dict["created_at"] = action.created_at
    action_dict["traces"] = get_activity_traces(action.id)
    return JsonResponse(action_dict, safe=False)


@require_http_methods(["GET"])
def get_action(request, id):
    action = Action.objects.get(pk=id)
    action_dict = model_to_dict(action)
    action_dict["created_at"] = action.created_at
    action_dict["traces"] = get_activity_traces(action.id)
    return JsonResponse(action_dict, safe=False)


def get_activity_traces(id):
    with connection.cursor() as cursor:
        cursor.execute(SQL, [id])
        rows = cursor.fetchall()
    return rows
