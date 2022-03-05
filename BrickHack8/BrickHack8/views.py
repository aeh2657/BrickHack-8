from django.http import HttpResponse
from manage import main

def home(request):
    return HttpResponse("Hello, Django!")

if __name__ == '__main__':
    main()