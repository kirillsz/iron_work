


from rest_framework import routers


from .views import ProfileView

router = routers.SimpleRouter()

router.register(r'api/v1/profiles', ProfileView)

urlpatterns = router.urls

