from django.shortcuts import render
from .forms import ContactForm
from .models import ContactMessage

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the data (e.g., save to a database or send an email)
            cleaned_data = form.cleaned_data
            
            if form.is_valid():
                ContactMessage.objects.create(**form.cleaned_data)
    
            print(cleaned_data)  # Example processing
            return render(request, 'contact/thank_you.html', {'name': cleaned_data["name"]})  # Redirect to a thank-you page
    else:
        form = ContactForm()
        return render(request, 'contact/contact.html', {'form': form})
