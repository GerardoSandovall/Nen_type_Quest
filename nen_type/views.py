from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def Quest(request, Key):
    Num = Key
    try:
        Key = int(Key)
    except ValueError:
        return render(request, 'Quest.html', {'Key': Num, 'error': 'Esta pagina no existe'})

    if 1 <= Key <= 10:
        if request.method == 'GET':
            return render(request, 'Quest.html', {'Key': Num, 'error': ''})
        else:
            answer = request.POST.get('question')
            print(request.path)  #path de donde viene el post
            print("/Quest/"+str(Key)) #Comprobar que la respuesta viene de ahi 
            
            return redirect('Quest', Key)
    else:
        if request.method == 'GET':
            return render(request, 'Quest.html', {'Key': Num, 'error': 'Esta pagina no existe'})
        else:
            return redirect('Main')  # Ensure to return redirect

