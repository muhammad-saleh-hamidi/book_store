# userCreationForm -> bra sakhtan user /signUp
# userChangeForm ->bra taghir dar form admin/Admin
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

from.models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        # fields = UserCreationForm.Meta.fields + ('age',)
        fields = ('username','age','email','first_name',)
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        # fields = UserChangeForm.Meta.fields
        fields = ('username', 'age', 'email','first_name',)


"""sakht do ta form """





