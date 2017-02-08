from django.shortcuts import render

# Create your views here.
def index(request):
    # context = {
    #     "todos":
    # }
    return render(request, 'todoapp/index.html')
