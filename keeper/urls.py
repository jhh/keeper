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
    path("last_action/", views.get_last_action),
]
