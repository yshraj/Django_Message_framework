from django.shortcuts import render, redirect
from django.contrib import messages
def show_messages(request):
    return render(request, 'app/show_messages.html')

def index(request):
    if request.method == 'POST':
        print(request.POST['email'])
        print(request.POST['password'])

        if request.POST['password'] == 'password':
            messages.error(request, "Your password isn't complex enough.")
            return redirect('index')

        messages.info(request, 'This is the info message!')
        messages.error(request, 'ERROR! ERROR!')
        messages.success(request, 'You registered succesfully')
        messages.warning(request, 'Be careful!')
        
        return redirect(show_messages)

    return render(request, 'app/index.html')

