from django.shortcuts import render
from django.http import HttpResponse

import os
import sys
module_path = os.path.abspath(os.path.join('../'))
if module_path not in sys.path:
    sys.path.append(module_path)
from scrapers.aptoide_scraper import ScrapeAppPage

inst = ScrapeAppPage()
details = [inst.extract(url='https://linkedin-android.en.aptoide.com/app')]


def home(request):

    context = {
        'details': details
    }
    return render(request, 'display_aptoide/home.html', context)



from .forms import ContactUsForm

def contact(request):
  form = ContactUsForm() 
  return render(request, 'display_aptoide/home.html', {'form': form}) 
