
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import NenPoints

@login_required
def Quest(request, Key):
    # Convert Key to integer if possible, or show an error if not
    try:
        Key = int(Key)
    except ValueError:
        return render(request, 'Quest.html', {'Key': Key, 'error': 'This page does not exist'})

    # Valid range check for Key
    if 1 <= Key <= 6:
        # GET Request - Show question page
        nen_points, created = NenPoints.objects.get_or_create(user=request.user)
        Points = get_object_or_404(NenPoints, user= request.user)

        #Solo esta guardando 30 puntos y hay que ver como recorremos los tipos para que se escriban

        Type_Probability = [
        {"type": "Enhancer", "probability": (Points.Enhancer / 50) * 100},
        {"type": "Emitter", "probability": (Points.Emitter / 50) * 100},
        {"type": "Transmutator", "probability": (Points.Transmutator / 50) * 100},
        {"type": "Manipulator", "probability": (Points.Manipulator / 50) * 100},
        {"type": "Conjurer", "probability": (Points.Conjurer / 50) * 100},
        {"type": "Specialist", "probability": (Points.Specialist / 50) * 100},
         ]


        if request.method == 'GET':
            Type_is_know, created = NenPoints.objects.get_or_create(user=request.user)
            if Type_is_know.answered_fiel == False:
                return render(request, 'Quest.html', {'Key': Key, 'error': '', 'List': Type_Probability})
            else:
                return render(request, 'Quest.html', {'Key': Key, 'error': 'Updating quest', 'List': Type_Probability, })
        
        # POST Request - Process answer submission
        elif request.method == 'POST':
            answer = request.POST.get('question')
            if not answer:
                return render(request, 'Quest.html', {'Key': Key, 'error': 'Please select an option'})

            # Retrieve or create NenPoints object for the user
            nen_points, created = NenPoints.objects.get_or_create(user=request.user)

            # gn points based on the answer selected
            if answer == '1':
                nen_points.Enhancer += 10
            elif answer == '2':
                nen_points.Emitter += 10
            elif answer == '3':
                nen_points.Transmutator += 10
            elif answer == '4':
                nen_points.Manipulator += 10
            elif answer == '5':
                nen_points.Conjurer += 10
            elif answer == '6':
                nen_points.Specialist += 10
            else:
                return render(request, 'Quest.html', {'Key': Key, 'error': 'Invalid answer'})
            
           
            Validation = Points.Enhancer + Points.Emitter + Points.Transmutator + Points.Manipulator + Points.Conjurer + Points.Specialist

            if Validation == 50:
                if answer == '1':
                    nen_points.Enhancer = 10
                    nen_points.Emitter = 0
                    nen_points.Transmutator = 0
                    nen_points.Manipulator = 0
                    nen_points.Conjurer = 0
                    nen_points.Specialist = 0
                elif answer == '2':
                    nen_points.Enhancer = 0
                    nen_points.Emitter = 10
                    nen_points.Transmutator = 0
                    nen_points.Manipulator = 0
                    nen_points.Conjurer = 0
                    nen_points.Specialist = 0
                elif answer == '3':
                    nen_points.Enhancer = 0
                    nen_points.Emitter = 0
                    nen_points.Transmutator = 10
                    nen_points.Manipulator = 0
                    nen_points.Conjurer = 0
                    nen_points.Specialist = 0
                elif answer == '4':
                    nen_points.Enhancer = 0
                    nen_points.Emitter = 0
                    nen_points.Transmutator = 0
                    nen_points.Manipulator = 10
                    nen_points.Conjurer = 0
                    nen_points.Specialist = 0
                elif answer == '5':
                    nen_points.Enhancer = 0
                    nen_points.Emitter = 0
                    nen_points.Transmutator = 0
                    nen_points.Manipulator = 0
                    nen_points.Conjurer = 10
                    nen_points.Specialist = 0
                elif answer == '6':
                    nen_points.Enhancer = 0
                    nen_points.Emitter = 0
                    nen_points.Transmutator = 0
                    nen_points.Manipulator = 0
                    nen_points.Conjurer = 0
                    nen_points.Specialist = 10
                nen_points.save()
            else:
                nen_points.save()
                if Validation == 40:
                    nen_points.answered_fiel = True
                    nen_points.save()

            # Redirect to the next question or a final page if Key == 6
            return redirect('Quest', Key)

    # Handle invalid Key range for GET and POST requests
    return render(request, 'Quest.html', {'Key': Key, 'error': 'This page does not exist'})

