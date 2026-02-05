from contact.forms import NewsletterForm

def newsletter_form(request):
    """
    Return a newsletter form for templates. Import forms lazily so importing
    this module won't raise when DJANGO_SETTINGS_MODULE isn't configured.
    """
    try:
        from contact.forms import NewsletterForm
        form = NewsletterForm(prefix="footer_newsletter")
    except Exception:
        form = None
    return {"newsletter_form": form}