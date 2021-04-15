from django.shortcuts import render ,HttpResponse

# Create your views here.
def index(request):
    return render(request,"index.html")

def analzyed(request):
    djtext = request.GET.get('textarea','default')
    removepunc = request.GET.get('checkbtn','off')
    uppercase = request.GET.get('uppercasebtn','off')
    countLen = request.GET.get('countLengthbtn','off')
    wordscount = request.GET.get('wordscountbtn','off')
    print(djtext)
    print(removepunc)
    print(uppercase)
    print(countLen)
    print(wordscount)
    # define punctuation
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    word = ''
    wordLen = ''
    totalwords = ''
    if removepunc == 'on' :
        for i in djtext:
            if i not in punctuations:
                word = word + i
    else:
        word = djtext   
        
    if uppercase == 'on' :
        word= word.upper()
        
    if countLen == 'on' :
        wordLen = "Total length is : " + str(len(word))
          
    if wordscount == 'on':
        wordslst = word.split(' ')
        print(wordslst)
        totalwords = "Total numbers of words : " + str(len(wordslst))
        print(totalwords)
        
    print(wordLen)
    djdir = {"key_text" : word,
             "key_length":wordLen,
             "key_wordscount":totalwords
             }
    # params = {"key_text",not_punc}
    return render(request,'removepunctuations.html',djdir)
    