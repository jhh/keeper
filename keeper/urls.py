from django.contrib import admin
from django.urls import include, path
from trapper import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"activities", views.ActivityViewSet)
router.register(r"actions", views.ActionViewSet)
router.register(r"traces", views.TraceViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path("reports/activity/last/", views.get_last_activity),
    path("reports/action/last/", views.get_last_action),
    path("reports/action/<int:id>/", views.get_action),
]
