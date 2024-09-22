from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

class CustomUserSerializer(serializers.ModelSerializer):
    # Define password as a CharField with write_only to ensure it is not returned in the response
    password = serializers.CharField(write_only=True)

    class Meta:
        model = get_user_model()  # Using the custom user model
        fields = ['username', 'password', 'bio', 'profile_picture', 'followers']  # Fields to be serialized

    def create(self, validated_data):
        # Extract the password from the validated data
        password = validated_data.pop('password')
        # Create the user without saving the password yet
        user = get_user_model().objects.create(**validated_data)
        # Set the password for the user (handles hashing)
        user.set_password(password)
        user.save()

        # Create a token for the user
        Token.objects.create(user=user)

        return user
