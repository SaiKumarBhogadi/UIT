from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
#uitech classes
from uitech.models import CandidateRequirement, InternshipStudents
from uitech.forms import CandidateRequirementForm, InternshipStudentsForm
#uitech classes ends
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.views.generic.edit import FormView
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from .forms import LoginForm


class LoginView(FormView):
    template_name = 'adminpanel/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('adminpanel:admin_dashboard')
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('adminpanel:admin_dashboard')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(self.request, username=username, password=password)
        if user is not None:
            login(self.request, user)
            return super().form_valid(form)
        return self.form_invalid(form)


class AdminDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'adminpanel/admin_dashboard.html'



class SmartHiringView(LoginRequiredMixin, ListView):
    model = CandidateRequirement
    template_name = 'adminpanel/smart_hiring.html'
    context_object_name = 'form_data'

    def get_queryset(self):
        return CandidateRequirement.objects.all().order_by('-id')

    '''def get_queryset(self):
        # Filter form data for the logged-in user
        return CandidateRequirement.objects.all()'''

class DetailHiringView(LoginRequiredMixin, DetailView):
    model = CandidateRequirement
    template_name = 'adminpanel/hiring_detail.html'  # Specify the template to use
    context_object_name = 'hiring_data'


class CreateHiringView(LoginRequiredMixin, CreateView):
    model = CandidateRequirement
    fields = '__all__'
    template_name = 'adminpanel/hiring_form.html'
    success_url = reverse_lazy('adminpanel:smart_hiring')

class EditHiringView(LoginRequiredMixin, UpdateView):
    model = CandidateRequirement
    form_class = CandidateRequirementForm
    template_name = 'adminpanel/hiring_form.html'
    success_url = reverse_lazy('adminpanel:smart_hiring')

#Form Validation
    def form_valid(self, form):
        return super().form_valid(form)

    def form_invalid(self, form):
        print("Form is invalid")
        print(form.errors)
        return super().form_invalid(form)

class DeleteHiringView(LoginRequiredMixin, DeleteView):
    model = CandidateRequirement
    template_name = 'adminpanel/confirm_delete.html'
    success_url = reverse_lazy('adminpanel:smart_hiring')
    
    
    
# Internship Students View

class InternsView(LoginRequiredMixin, ListView):
    model = InternshipStudents
    template_name = 'adminpanel/interns_list.html'
    context_object_name = 'intern_form_data'

    def get_queryset(self):
        return InternshipStudents.objects.all().order_by('-id')


class InternsDetailView(LoginRequiredMixin, DetailView):
    model = InternshipStudents
    template_name = 'adminpanel/interns_detail.html'
    context_object_name = 'interns_data'


class CreateInternView(LoginRequiredMixin, CreateView):
    model = InternshipStudents
    fields = '__all__'
    template_name = 'adminpanel/intern_form.html'
    
    def get_success_url(self):
        # Redirect to the details page of the newly created intern
        return reverse('adminpanel:interns_detail', kwargs={'pk': self.object.pk})

class EditInternView(LoginRequiredMixin, UpdateView):
    model = InternshipStudents
    form_class = InternshipStudentsForm
    template_name = 'adminpanel/intern_form.html'
    
    def get_success_url(self):
        # Redirect to the details page of the updated intern
        return reverse('adminpanel:interns_detail', kwargs={'pk': self.object.pk})

    #Form Validation
    def form_valid(self, form):
        return super().form_valid(form)

    def form_invalid(self, form):
        print("Form is invalid")
        print(form.errors)
        return super().form_invalid(form)

class DeleteInternView(LoginRequiredMixin, DeleteView):
    model = InternshipStudents
    template_name = 'adminpanel/confirm_delete_intern.html'
    success_url = reverse_lazy('adminpanel:interns_list')

