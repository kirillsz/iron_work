from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, status
from rest_framework.response import Response


from .serializers import ProfileSerializer
from .models import Profile

class ProfileView(viewsets.ModelViewSet):

    permission_classes 		= [IsAuthenticated]
    serializer_class 		= ProfileSerializer
    queryset 				= Profile.objects.all()

    def destroy(self, request, pk):

        instance = self.get_object()
		
        if instance.id == request.user.id:

            instance.team = None

            instance.save()
			
        else:

            self.perform_destroy(instance)

        return Response(status=status.HTTP_204_NO_CONTENT)
