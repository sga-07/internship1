from django import forms
from django.contrib.auth.models import User
from .models import Klasa, Lendet, Lesson



class KlasaForm(forms.ModelForm):
    class Meta:
        model = Klasa
        fields = '__all__'
        help_texts = {
            'titulli': 'e.g., Class 11 or Computer Science Class',
            'pershkrimi': 'Enter a brief description of the class.',
            'imazhi': 'You can upload a photo of the class or leave it blank'
        }
        labels = {
            'titulli' : 'Title',
            'pershkrimi' : 'Description',
            'imazhi' : 'Image'
        }

class LendaForm(forms.ModelForm):
    class Meta:
        model = Lendet
        fields = ['krijues','slug', 'titulli', 'klasa', 'pershkrimi', 'imazhi_lendes']
        help_texts = {
            'titulli': 'E.g....., Arduino Kit, Programming, etc',
            'pershkrimi':'Enter a brief description of the subject',
            'klasa':'Choose the class for which you will create the subject',
            'imazhi_lendes':'You can upload a photo of the subject, or it can be left blank'
        }
        labels = {
            'krijues' : 'Creator',
            'titulli':'Subject Title',
            'klasa' : 'Class',
            'pershkrimi' : 'Description',
            'imazhi_lendes' : 'Image-materials'

        }
        # widgets = {'krijues': forms.HiddenInput(), 'slug': forms.HiddenInput()}


class MesimiForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['slug','titulli', 'lenda', 'video_id', 'pozicioni', ]
        help_texts = {
            'titulli':'Enter the lesson title',
            'lenda':'Choose the subject to which this lesson belongs',
            'video_id':'Enter the zoom meeting link here ',
            'pozicioni':'Enter the lesson number or sequence'
        }
        labels = {
            'titulli': 'Lesson Title',
            'lenda' : 'Subject',
            'pozicioni' : 'Position',
            'video_id' : 'Zoom Link'

        }
        # widgets = {
        #     'slug': forms.HiddenInput()
        # }