
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import NenPoints
import random


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


        if Points.Num_answers == 0:

            answerComplete = 10

        else:

            answerComplete = Points.Num_answers*10

        Type_Probability = [
        {"type": "Enhancer", "probability": (Points.Enhancer / answerComplete ) * 100},
        {"type": "Emitter", "probability": (Points.Emitter / answerComplete ) * 100},
        {"type": "Transmutator", "probability": (Points.Transmutator / answerComplete ) * 100},
        {"type": "Manipulator", "probability": (Points.Manipulator / answerComplete) * 100},
        {"type": "Conjurer", "probability": (Points.Conjurer / answerComplete) * 100},
        {"type": "Specialist", "probability": (Points.Specialist / answerComplete) * 100},
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
            
            nen_points.Num_answers += 1
            Validation = Points.Enhancer + Points.Emitter + Points.Transmutator + Points.Manipulator + Points.Conjurer + Points.Specialist
            print(Validation)

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
                
                nen_points.Num_answers = 1
                nen_points.save()

            else:
                nen_points.save()
                if Validation == 40:
                    nen_points.answered_fiel = True
                    nen_points.save()
                    return redirect('Results')

            # Redirect to the next question or a final page if Key == 6
            return redirect('Quest', Key)

    # Handle invalid Key range for GET and POST requests
    return render(request, 'Quest.html', {'Key': Key, 'error': 'This page does not exist'})

@login_required
def Results(request):
    nen_points, created = NenPoints.objects.get_or_create(user=request.user)

    if request.method == 'GET':
        nen_points.Emitter

        Scores_Names = [('Enchancer', nen_points.Enhancer), ('Emitter', nen_points.Emitter),('Transmutator', nen_points.Transmutator), ('Manipulator', nen_points.Manipulator),('Conjurer', nen_points.Conjurer) ,('Especialist', nen_points.Specialist)] 

        maxPoints = max(Scores for _, Scores in Scores_Names)
    
    # Filtra los puntajes que igualan al puntaje máximo
        sameValue = [Names for Names, Scores in Scores_Names if Scores == maxPoints]
    
    # Selecciona al azar uno de los empatados
        selected = random.choice(sameValue)
    

        
        return render(request, 'Results/Result.html' , { 'Key': selected } )
    else:
       return render(request, 'Results/Result.html' , { 'Error':'Mising post' } ) 

