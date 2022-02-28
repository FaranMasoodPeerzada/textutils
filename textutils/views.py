# Created by Faran Masood Peerzada
from django.http import HttpResponse
'''
code for video 6

def index(request):
    return HttpResponse("<h1>hello</h1><a href ='https://www.facebook.com'>Facebook <a>")
def about(request):
    return HttpResponse("hello faran bhai to about page")

'''
#code for video 7
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
   # params = {'name':'Faran', 'place':'ISB'}
    #return render(request, 'index.html', params)
    return render(request, 'index.html')
   
    
    #return HttpResponse("<a href='./spaceremove'>Back  </a><h1>Home</h1>")


def analyze(request):
    # Get The Text
    djtext= request.POST.get('text','default')
    removepun = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount =  request.POST.get('charcount', 'off')
    #Check Which check box is on
    if removepun == 'on':
        analyzed = ""
        punctuations = '''(/[-[\]{}()*+?.,\\:;^$|#\]/,'"\\$&");'''
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctuation',
        'analyzed_text': analyzed}
        djtext= analyzed
        #return render(request, 'analyze.html', params)
   # elif (fullcaps == 'on'):
    if (fullcaps == 'on'):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
            params = {'purpose':'Changed to uppercase',
        'analyzed_text': analyzed}
        djtext= analyzed
        #return render(request, 'analyze.html', params)
    
    #elif (extraspaceremover =='on'):
    if (extraspaceremover =='on'):
        analyzed=""
        for index, char in enumerate(djtext):
            if djtext[index] == " " and djtext[index + 1]==" ":
                pass
            else:
                analyzed = analyzed + char
        params = {'purpose':'Removed Extra Spaces','analyzed_text': analyzed}
        djtext= analyzed
        #return render(request, 'analyze.html', params)
    #elif (charcount =='on'):
    if (charcount =='on'):
        analyzed=""
        val = len(djtext)
        #for char in djtext:
         #  val = val + 1
            
        params = {'purpose':'Number of Characters  :',
        'analyzed_text': val}
        djtext= analyzed
        #return render(request, 'analyze.html', params)
    #elif (newlineremover =='on'):
    if (newlineremover =='on'):
        analyzed=""
        for char in djtext:
           if char != "\n" and char != "\r":
            analyzed = analyzed + char
        params = {'purpose':'Removed new lines',
        'analyzed_text': analyzed}
        djtext= analyzed
        #return render(request, 'analyze.html', params)
    #else:
     #   return HttpResponse("there is some error")
    
    if (newlineremover !='on' and extraspaceremover != 'on' and  fullcaps != 'on' and removepun !='on'):
        return HttpResponse("Please Select any option and try again..")
    return render(request, 'analyze.html', params)


def contactus(request):
   # params = {'name':'Faran', 'place':'ISB'}
    #return render(request, 'index.html', params)
    return render(request, 'contactus.html')
   
def aboutus(request):
    return render(request, 'aboutus.html')




    """
def ex1(request):
    s ='''<h2>Navigation Bar <br> </h2>
    <a href= "https://www.youtube.com/playlist?list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9" > Django Code With Harry Bhai </a><br>
    <a href="https://www.facebook.com/"> Facebook </a> <br>
    <a href="https://www.flipkart.com/"> Flipkart </a> <br>
    <a href="https://www.hindustantimes.com/"> News </a> <br>
    <a href="https://www.google.com/"> Google </a> <br>'''
    return HttpResponse(s)


def removepunc(request):
    djtext= request.GET.get('text','default')
    print(djtext)
    return HttpResponse("<h1>remove punc</h1>")
def capfirst(request):
    return HttpResponse("<h1>capitalize first</h1>")
def newlineremove(request):
    return HttpResponse("<h1>newlineremove first</h1>")
def spaceremove(request):
    return HttpResponse("<h1>spaceremove first</h1>")
def charcount(request):
    return HttpResponse("<h1>charcount </h1>")

    """