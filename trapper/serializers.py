from rest_framework import serializers

from trapper.models import Action, Activity, Trace


class ActivitySerializer(serializers.HyperlinkedModelSerializer):
    actions = serializers.HyperlinkedRelatedField(
        many=True, view_name="action-detail", read_only=True
    )

    class Meta:
        model = Activity
        fields = (
            "id",
            "name",
            "url",
            "meta",
            "actions",
            "created_at",
        )


class TraceSerializer(serializers.ModelSerializer):
    action = serializers.PrimaryKeyRelatedField(
        write_only=True, queryset=Action.objects.all()
    )

    class Meta:
        model = Trace
        fields = (
            "action",
            "time",
            "data",
        )


class ActionSerializer(serializers.HyperlinkedModelSerializer):
    traces = TraceSerializer(many=True, read_only=True)

    class Meta:
        model = Action
        fields = (
            "id",
            "name",
            "url",
            "activity",
            "measures",
            "meta",
            "traces",
            "created_at",
        )
