from django.shortcuts import render
from .forms import ContactForm1
from formtools.wizard.views import SessionWizardView


class Destination_WizardView(SessionWizardView):
    template_name = "myapp/destination.html"
    form_list = [ContactForm1]

    def done(self, form_list, **kwargs):
        return render(self.request, 'done.html', {
            'form_data': [form.cleaned_data for form in form_list],
        })
    
    def get(self, request, *args, **kwargs):
        try:
            return self.render(self.get_form())
        except KeyError:
            return super().get(request, *args, **kwargs)
