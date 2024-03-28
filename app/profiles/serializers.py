
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from django.contrib.auth.models import User
from profiles.models import Profile
from django.contrib.auth.models import Group


class ProfileSerializer(serializers.ModelSerializer):

	class Meta:
		model = Profile
		fields = ('id',)

class GroupsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ('id', 'name',)

#используется при отображении
class UserViewSerializer(serializers.ModelSerializer):

	username 	= serializers.CharField()
	groups		= GroupsSerializer(read_only=True, many=True)
	profile		= ProfileSerializer()

	class Meta:
		model = User
		fields = ('id', 'username', 'is_superuser', 'groups', 'profile',)


#используется при создании
class UserSerializer(serializers.ModelSerializer):

	username 	= serializers.CharField(max_length=50, error_messages={'blank': '317', 'max_length': '317',},)
	password 	= serializers.CharField(max_length=128, error_messages={'blank': '318', 'max_length': '329',},)
	
	first_name 	= serializers.CharField(default='', allow_blank=True, read_only=True,)
	last_name 	= serializers.CharField(default='', allow_blank=True, read_only=True,)
	email 		= serializers.CharField(default='', allow_blank=True, read_only=True,)


	class Meta:
		model = User
		fields = ('username', 'password', 'first_name', 'last_name', 'email',)
		validators = [
            UniqueTogetherValidator(
                queryset=User.objects.all(),
                fields=['username',],
				message="319",
            ),
        ]