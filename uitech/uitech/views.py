from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from .forms import CandidateRequirementForm, InternshipForm, ContactForm
from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from .models import CandidateRequirement, InternshipStudents
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib import messages


class Home(TemplateView):
    template_name = 'uitech/index.html'

class Internships(ListView):
    model = InternshipStudents
    template_name = 'uitech/internships.html'
    context_object_name = 'interns_data'

    def get_context_data(self, **kwargs):
        # Fetch data from the model and include it in the context
        context = super().get_context_data(**kwargs)
        context['interns_data'] = InternshipStudents.objects.all()
        context['form'] = InternshipForm()
        context['submitted'] = self.request.GET.get('submitted', False)  # Optional for form feedback
        return context
        
    def post(self, request):
        form = InternshipForm(request.POST)

        if form.is_valid():
            # Extract cleaned data from the form
            context = {
                'name': form.cleaned_data['name'],
                'email': form.cleaned_data['email'],
                'phone': form.cleaned_data['phone'],
                'passout_year': form.cleaned_data['passout_year'],
                'graduation': form.cleaned_data['graduation'],
                'course': form.cleaned_data['course'],
                'duration': form.cleaned_data['duration'],
                'gender': form.cleaned_data['gender'],
                'source': form.cleaned_data['source'],
            }

            # Render email content
            admin_message = render_to_string('uitech/email/email_internships_admin.html', context)
            user_message = render_to_string('uitech/email/email_internships_user.html', context)


            # Send emails
            try:

                # Email settings from settings.py
                smtp_server = settings.EMAIL_HOST
                port = settings.EMAIL_PORT
                login = settings.EMAIL_HOST_USER
                password = settings.EMAIL_HOST_PASSWORD
                from_email = settings.DEFAULT_FROM_EMAIL
                to_email = 'info@uitech.in'
                user_email = context['email']


                # Email to the admin
                admin_msg = MIMEMultipart()
                admin_msg['From'] = from_email
                admin_msg['To'] = to_email
                admin_msg['Subject'] = 'New Internship Registration'
                admin_msg.attach(MIMEText(admin_message, 'html'))

                # Send email to the user
                user_msg = MIMEMultipart()
                user_msg['From'] = to_email
                user_msg['To'] = user_email
                user_msg['Subject'] = 'UIT Internship Registration Confirmation'
                user_msg.attach(MIMEText(user_message, 'html'))


                with smtplib.SMTP_SSL(smtp_server, port) as server:
                    server.login(login, password)
                    # Send the admin email
                    server.sendmail(from_email, to_email, admin_msg.as_string())
                    # Send the user email
                    server.sendmail(from_email, user_email, user_msg.as_string())


                # messages.success(request, "Your registration was successful. Check your email for confirmation.")
                return render(request, 'uitech/internships.html', {'form': InternshipForm(), 'submitted': True})
            except Exception as e:
                messages.error(request, f"An error occurred while sending emails: {e}")
                return render(request, 'uitech/internships.html', {'form': form, 'submitted': False})

        # Return the form with errors to the template
        return render(request, 'uitech/internships.html', {'form': form, 'submitted': False})

    

class FindOpenings(ListView):
    model = CandidateRequirement
    template_name = 'uitech/find_openings.html'
    context_object_name = 'openings_data'
    
    def get_queryset(self):
        return CandidateRequirement.objects.all().order_by('-id')[:8]
        

class OpeningsDetails(ListView):
    model = CandidateRequirement
    template_name = 'uitech/openings_details.html'
    context_object_name = 'openings_data'
    paginate_by = 27

    def get_queryset(self):
        queryset = CandidateRequirement.objects.all().order_by('-id')

        # Get search and filter parameters from the request
        search_query = self.request.GET.get('search', '')
        domain_filter = self.request.GET.get('domain', '')
        experience_filter = self.request.GET.get('experience', '')

        # Apply search filter if a search query exists
        if search_query:
            queryset = queryset.filter(
                Q(full_name__icontains=search_query) |
                Q(domain__icontains=search_query) |
                Q(note__icontains=search_query)
            )

        # Apply domain filter if selected
        if domain_filter:
            queryset = queryset.filter(domain__iexact=domain_filter)

        # Apply experience filter if selected
        if experience_filter:
            queryset = queryset.filter(experience__iexact=experience_filter)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Pass distinct domains and experiences to the context for filtering
        context['distinct_domains'] = CandidateRequirement.objects.values_list('domain', flat=True).distinct()
        context['distinct_experiences'] = CandidateRequirement.objects.values_list('experience', flat=True).distinct()
        return context


class SmartHiring(SuccessMessageMixin, CreateView):
    model = CandidateRequirement
    form_class = CandidateRequirementForm
    template_name = 'uitech/smart_hiring.html'
    success_url = reverse_lazy('uitech:smart_hiring')
    success_message = "Your Candidate requirement has been successfully submitted."

#Form Validation
    def form_valid(self, form):
        return super().form_valid(form)

    def form_invalid(self, form):
        print("Form is invalid")
        print(form.errors)
        return super().form_invalid(form)

class CheckYourSkill(TemplateView):
    template_name = 'uitech/check_your_skill.html'

class AboutUs(TemplateView):
    template_name = 'uitech/about_us.html'
    
    def get(self, request, *args, **kwargs):
        form = ContactForm()
        form_name = "About"
        return render(request, self.template_name, {'form': form, 'form_name': form_name})

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        form_name = "About"
        if form.is_valid():
            # Prepare email context
            context = form.cleaned_data
            context['form_name'] = form_name
                    
            # Render email content
            email_content = render_to_string('uitech/email/email_contact.html', context)

           # Email settings from settings.py
            smtp_server = settings.EMAIL_HOST
            port = settings.EMAIL_PORT
            login = settings.EMAIL_HOST_USER
            password = settings.EMAIL_HOST_PASSWORD
            from_email = settings.DEFAULT_FROM_EMAIL
            to_email = 'info@uitech.in'

            # Create the email
            msg = MIMEMultipart()
            msg['From'] = from_email
            msg['To'] = to_email
            msg['Subject'] = 'New About Form Submission'
            msg.attach(MIMEText(email_content, 'html')) 

            try:
                # Connect to the SMTP server using SSL
                with smtplib.SMTP_SSL(smtp_server, port) as server:
                    server.login(login, password)
                    server.sendmail(from_email, to_email, msg.as_string())
                    print("Email sent successfully!")

                # Display a success message
                success_message = 'Form submitted successfully!'
                return render(request, self.template_name, {'form': form, 'success': success_message, 'form_name': form_name})

            except Exception as e:
                # Handle email sending error
                print(f"Failed to send email: {e}")
                return render(request, self.template_name, {'form': form, 'error': 'Failed to submit form. Please try again later.', 'form_name': form_name})
        
        return render(request, self.template_name, {'form': form, 'form_name': form_name})
    

class ContactUs(TemplateView):
    template_name = 'uitech/contact_us.html'
    
    def get(self, request, *args, **kwargs):
        form = ContactForm()
        form_name = "Contact"
        return render(request, self.template_name, {'form': form, 'form_name': form_name})

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        form_name = "Contact"
        if form.is_valid():
            # Prepare email context
            context = form.cleaned_data
            context['form_name'] = form_name
            
            # Render email content
            email_content = render_to_string('uitech/email/email_contact.html', context)

            # Email settings from settings.py
            smtp_server = settings.EMAIL_HOST
            port = settings.EMAIL_PORT
            login = settings.EMAIL_HOST_USER
            password = settings.EMAIL_HOST_PASSWORD
            from_email = settings.DEFAULT_FROM_EMAIL
            to_email = 'info@uitech.in'

            # Create the email
            msg = MIMEMultipart()
            msg['From'] = from_email
            msg['To'] = to_email
            msg['Subject'] = 'New Contact Form Submission'
            msg.attach(MIMEText(email_content, 'html'))

            try:
                # Connect to the SMTP server using SSL
                with smtplib.SMTP_SSL(smtp_server, port) as server:
                    server.login(login, password)
                    server.sendmail(from_email, to_email, msg.as_string())
                    print("Email sent successfully!")

                # Display a success message
                success_message = 'Form submitted successfully!'
                return render(request, self.template_name, {'form': form, 'success': success_message, 'form_name': form_name})

            except Exception as e:
                # Handle email sending error
                print(f"Failed to send email: {e}")
                return render(request, self.template_name, {'form': form, 'error': 'Failed to submit form. Please try again later.', 'form_name': form_name})
        
        return render(request, self.template_name, {'form': form, 'form_name': form_name})
        
        
        
        
        


class PrivacyPolicy(TemplateView):
    template_name = 'uitech/privacy_policy.html'


class TermsOfUse(TemplateView):
    template_name = 'uitech/terms_of_use.html'


