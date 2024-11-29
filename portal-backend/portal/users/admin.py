from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError

from .models import User, Student, Professor, Staff


class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('name', 'type', 'email')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    disabled password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('name', 'type', 'email', 'password', 'is_active', 'is_admin')


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('name', 'type', 'email', 'is_verified')
    list_filter = ('is_admin', 'type')
    fieldsets = (
        (None, {'fields': ('name', 'type', 'email', 'password', 'is_verified')}),
        ('OTP Info', {'fields': ('otp', 'otp_valid_till', 'otp_attempts_remaining', 'otp_cooldown')}),
        ('Permissions', {'fields': ('is_admin', 'is_staff', 'is_superuser', 'is_active')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name', 'email', 'password1', 'password2'),
        }),
    )
    search_fields = ('email',)
    ordering = ('type', 'email')
    filter_horizontal = ()


@admin.action(description='Verify selected students')
def verify_student(modeladmin, request, queryset):
    queryset.update(is_verified=True)

class StudentAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'entry_number', 'is_verified')
    search_fields = ('entry_number',)
    ordering = ('is_verified', 'entry_number')
    actions = [verify_student]

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

@admin.action(description='Verify selected professors')
def verify_professor(modeladmin, request, queryset):
    queryset.update(is_verified=True)

class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'university', 'is_verified',)
    search_fields = ('__str__',)
    ordering = ('is_verified',)
    actions = [verify_professor]

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions


admin.site.register(User, UserAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Professor, ProfessorAdmin)
admin.site.register(Staff)
admin.site.unregister(Group)