from django.shortcuts import redirect, render
from django.contrib import messages
from django.utils.http import url_has_allowed_host_and_scheme
from django.conf import settings
from django.urls import reverse
from .forms import NewsletterForm, ContactForm


def subscribe(request):
    """
    Handles newsletter subscription from any page.
    """
    if request.method == "POST":
        form = NewsletterForm(request.POST, prefix="newsletter")
        if form.is_valid():
            form.save()
            messages.info(request, "You subscribed to our newsletter!")
            next_url = (
                request.POST.get("next")
                or request.META.get("HTTP_REFERER")
                or reverse("contact")
            )
            if not url_has_allowed_host_and_scheme(
                next_url,
                allowed_hosts=None,
                require_https=request.is_secure()
            ):
                next_url = reverse("contact")
            return redirect(f"{next_url}?subscribed=1")

    return redirect("contact")


def contact_us(request):
    """
    Renders contact page and handles contact form submission.
    """
    contact_form = ContactForm(prefix="contact")
    newsletter_form = NewsletterForm(prefix="newsletter")
    if request.method == "POST":
        contact_form = ContactForm(request.POST, prefix="contact")
        if contact_form.is_valid():
            contact_form.save()
            messages.info(
                request,
                "Thank you for contacting us, we'll be in touch soon!"
            )
            return redirect(reverse("contact") + "?contacted=1")

    return render(request, "contact/contact.html", {
        "contact_form": contact_form,
        "newsletter_form": newsletter_form,
    })
