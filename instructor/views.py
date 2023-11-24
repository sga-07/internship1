from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Lecture
from .forms import LectureForm

def upload_lecture(request):
    if request.method == 'POST':
        form = LectureForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Link and schedule added successfully.')
            # You can add more messages types like messages.info(), messages.warning(), messages.error()
    else:
        form = LectureForm()

    return render(request, 'upload_lecture.html', {'form': form})

# def schedule(request):
#     lectures = Lecture.objects.all()
#     return render(request, 'schedule.html', {'lectures': lectures})

def schedule(request):
    lectures = Lecture.objects.all()

    if request.method == 'POST':
        lecture_id = request.POST.get('lecture_id')
        if lecture_id:
            lecture = get_object_or_404(Lecture, pk=lecture_id)
            lecture.delete()
            messages.success(request, 'Lecture deleted successfully.')

    return render(request, 'schedule.html', {'lectures': lectures})