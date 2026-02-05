def newsletter_form(request):
    """
    Context processor that returns the newsletter form under the name
    `newsletter_form`. Import forms lazily so importing this module won't
    raise when DJANGO_SETTINGS_MODULE isn't configured.
    """
    try:
        from contact.forms import NewsletterForm
        form = NewsletterForm(prefix="footer_newsletter")
    except Exception:
        form = None
    return {"newsletter_form": form}