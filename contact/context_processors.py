def newsletter_form(request):
    try:
        # lazy import so broken forms module doesn't crash app import
        from .forms import NewsletterForm
        form = NewsletterForm(prefix="footer_newsletter")
    except Exception:
        # fallback to None so templates can handle missing form gracefully
        form = None
    return {"newsletter_form": form}