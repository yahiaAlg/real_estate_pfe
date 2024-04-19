from typing import Any
from django import forms
from .models import CustomerProfile
from django.contrib.auth.forms import UserChangeForm


class UserForm(UserChangeForm):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        del self.fields["user_permissions"]
        del self.fields["is_superuser"]
        del self.fields["groups"]
        del self.fields["is_staff"]
        del self.fields["is_active"]
        del self.fields["date_joined"]
        del self.fields["last_login"]


class CustomerProfileForm(forms.ModelForm):

    class Meta:
        model = CustomerProfile
        fields = "__all__"
        exclude = ["owner", "is_month_customer", "status"]
