# Copyright (C) 2018 The Hunter2 Contributors.
#
# This file is part of Hunter2.
#
# Hunter2 is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option) any later version.
#
# Hunter2 is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
# PARTICULAR PURPOSE.  See the GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License along with Hunter2.  If not, see <http://www.gnu.org/licenses/>.


from allauth.account.forms import ChangePasswordForm, SetPasswordForm
from dal import autocomplete
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse
from django.urls import reverse
from django.views import View

from . import forms, models


class UserProfileAutoComplete(LoginRequiredMixin, autocomplete.Select2QuerySetView):
    raise_exception = True

    def get_queryset(self):
        qs = models.UserProfile.objects.exclude(pk=self.request.user.profile.pk).order_by('user__username')

        if self.q:
            qs = qs.filter(
                Q(user__username__istartswith=self.q) |
                Q(user__email__istartswith=self.q)
            )

        return qs


class EditProfileView(LoginRequiredMixin, View):

    def get(self, request):
        user_form = forms.UserForm(instance=request.user)
        password_form = ChangePasswordForm(user=request.user) if request.user.has_usable_password() else SetPasswordForm(user=request.user)
        profile_formset = forms.UserProfileFormset(instance=request.user)
        attendance_formset = forms.AttendanceFormset(instance=request.user.profile, queryset=request.user.profile.attendance_set.filter(event=request.tenant))
        steam_linked = request.user.socialaccount_set.exists()  # This condition breaks down if we support multiple social accounts.
        context = {
            'user_form': user_form,
            'password_form': password_form,
            'profile_formset': profile_formset,
            'attendance_formset': attendance_formset,
            'steam_linked': steam_linked,
        }
        return TemplateResponse(
            request,
            'teams/profile.html',
            context=context,
        )

    def post(self, request):
        user_form = forms.UserForm(request.POST, instance=request.user)
        if user_form.is_valid():
            created_user = user_form.save(commit=False)
            profile_formset = forms.UserProfileFormset(request.POST, instance=created_user)
            if profile_formset.is_valid():
                created_profile = profile_formset[0].save(commit=False)
                attendance_formset = forms.AttendanceFormset(request.POST, instance=created_profile)
                if attendance_formset.is_valid():
                    created_user.save()
                    profile_formset.save()
                    attendance_formset.save()
                    return HttpResponseRedirect(reverse('edit_profile'))