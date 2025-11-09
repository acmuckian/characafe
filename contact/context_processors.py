from .forms import NewsletterForm

def newsletter_form(request):
    return {"subscribe_form": NewsletterForm()}