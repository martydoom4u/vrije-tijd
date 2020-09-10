from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class UserCreatForm(UserCreationForm):


    class Meta:
        fields = ('username','email','password1','password2')
        model = get_user_model()

        def __int__(self,*args,**Kwargs):
            super().__int__(*args,**Kwargs)
            self.fields['username'].label = 'Display name'
            self.fields['email'].label = 'email address'
