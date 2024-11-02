from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def Quest(request, Key):
    Num = Key
    try:
        Key = int(Key)
    except ValueError:
        return render(request, 'Quest.html', {'Key': Num, 'error': 'Esta pagina no existe'})

    if 1 <= Key <= 6:
        if request.method == 'GET':
            return render(request, 'Quest.html', {'Key': Num, 'error': ''})
        else:
            answer = request.POST.get('question')
            print(request.path)  #path de donde viene el post
            Path = "/Quest/"+str(Key) #Comprobar que la respuesta viene de ahi
            
            if request.path == Path:
                if answer == '1':
                    print("Potenciador")
                    print(answer)
                elif answer == '2':
                    print("Emisor")
                    print(answer)
                elif answer == '3':
                    print("Transmutador")
                    print(answer)
                elif answer == '4':
                    print("Manipulador")
                    print(answer)
                elif answer == '5':
                    print("Conjurador")
                    print(answer)
                elif answer == '6':
                    print("Especialista")
                    print(answer)
                else:
                    print("Error")
                    print(Key)
                    print(answer)
            
            return redirect('Quest', Key)
    else:
        if request.method == 'GET':
            return render(request, 'Quest.html', {'Key': Num, 'error': 'Esta pagina no existe'})
        else:
            return redirect('Main')

