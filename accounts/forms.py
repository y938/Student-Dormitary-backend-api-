from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser




class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + (
                "first_name",
                "last_name",
                "department",
                "year",
                "block",
                "room", 
                "bed",
                )


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields



#how can i change django rest auth default signup form(username, email, password1, password2)
#with the above custome form