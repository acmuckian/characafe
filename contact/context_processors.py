def newsletter_form(request):
    try:
        from .forms import NewsletterForm
        form = NewsletterForm(prefix="newsletter")
    except Exception:
        form = None
    return {"newsletter_form": form}