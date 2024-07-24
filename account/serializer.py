from .models import User
from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed
from django.contrib import auth

# register serializers
class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name','phone_no','email','password','user','admin']
        extra_kwargs = {
            'password' :{'write_only':True}  #  to does not return password in api ## postman
        }
    # convert password to hash key
    def create(self, validated_data):
        email = validated_data.get('email', None)
        password = validated_data.pop('password',None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        if len(password) <6:
            raise serializers.ValidationError("entre strong password")
        instance.save()
        return instance
    
   
# login serializers

class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255, min_length=3)
    password = serializers.CharField(max_length=68, min_length=6, write_only=True)
    tokens = serializers.SerializerMethodField()

    def get_tokens(self, obj):
        user = User.objects.get(email=obj['email'])

        return {
            'refresh': user.tokens()['refresh'],
            'access': user.tokens()['access']
        }

    class Meta:
        model = User
        fields = ['email', 'password', 'tokens','user','admin']

    def validate(self, attrs):
        email = attrs.get('email', '')
        password = attrs.get('password', '')
        filtered_user_by_email = User.objects.filter(email=email)
        user = auth.authenticate(email=email, password=password)

        if filtered_user_by_email.exists() and filtered_user_by_email[0].auth_provider != 'email':
            raise AuthenticationFailed(
                detail='Please continue your login using ' + filtered_user_by_email[0].auth_provider)
        if not user:
            raise AuthenticationFailed('Invalid credentials, try again')
        
        if user.user:
            if user.check_password(password):
                user_type = 'user'
                return {
                    'phone_no': user.phone_no,
                     'email': user.email,
                     'user': user.user,
                    'user_type': user_type,
                    'tokens': user.tokens(),
                    'user': user.user,
                    'id': user.id,
                    'first_name': user.first_name
                }
        elif user.admin:
            user_type = 'admin'
            return {
                'phone_no': user.phone_no,  # Use 'phone_no' instead of 'phone_no'
                'email': user.email,
                'user_type': user_type,
                'user': user.admin,
                'tokens': user.tokens(),
                "id": user.id,
                'first_name': user.first_name,
                # 'frt_team_id': frt_team_id
            }

        else:
            raise AuthenticationFailed('Invalid authentication type')
    
class PasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField()