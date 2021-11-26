from django.shortcuts import render
from googletrans import Translator

# Create your views here.
def translator_view(request):
    if request.method == 'POST':
        original_text = request.POST.get('my_textarea')
        output = Translator().translate(text=original_text, dest="de").text
        # print("original:"+original_text)
        return render(request, 'translator.html', {'my_textarea':original_text,'output_text': output})
    else:
        return render(request, 'translator.html')