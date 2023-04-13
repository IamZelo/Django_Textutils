import string
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def features(request):
    return render(request, 'features.html')

def aboutus(request):
    return render(request, 'aboutus.html')

def contactus(request):
    return render(request, 'contactus.html')


def analyze(request):
    # Get values
    get_text = request.POST.get('text', 'default')
    remove_punc  = request.POST.get('removepunct', 'off')
    toupper = request.POST.get('toupper', 'off')
    tolower = request.POST.get('tolower', 'off')
    # Print values
    print("Text:", get_text)
    print("Remove punct:", remove_punc)
    print("Upper:", toupper)
    print("Lower", tolower)
    
    # Process the text accordingly 
    
    purpose = dict()
    
    analyze_text = str(get_text)
    if (remove_punc == 'on'):
        purpose['removepunct']= 'on'
        for letter in str(analyze_text):
            if letter in list(string.punctuation):
                analyze_text = analyze_text.replace(letter, '')
    else:
        purpose['removepunct']= 'off'
        
    if (toupper == 'on'):
        purpose['toupper']= 'on'
        analyze_text = analyze_text.upper()
    else:
         purpose['toupper']= 'off'
    
    if (tolower == 'on'):
        purpose['tolower']= 'on'
        analyze_text = analyze_text.lower()
    else:
         purpose['tolower']= 'off'
    
    # Iterate through purpose dict and add each element to params 
        
    # Create parameter dict
    params = {'text_entered': str(get_text), 'analyzed_text': analyze_text}
    
    for each_purpose in purpose:
        params[each_purpose] = purpose[each_purpose]
        
    # Return the params to the django html page
    return render(request, 'analyze.html', params)
