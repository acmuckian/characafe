from django.shortcuts import redirect, render
from django.contrib import messages
from django.urls import reverse
from .forms import NewsletterForm, ContactForm


def subscribe(request):
    if request.method == "POST":
        form = NewsletterForm(request.POST, prefix="newsletter")
        if form.is_valid():
            form.save()
            return redirect(reverse("contact") + "?subscribed=1")
    return redirect("contact")


def contact_us(request):
    if request.method == "POST":
        form = ContactForm(request.POST, prefix="contact")
        if form.is_valid():
            form.save()
            return redirect(reverse("contact") + "?contacted=1")
    return render(request, "contact/contact.html", {
        "contact_form": ContactForm(prefix="contact"),
        "newsletter_form": NewsletterForm(prefix="newsletter"),
    })
