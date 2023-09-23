from django import forms
from .models import Post, Commentaire, Reponse


class LessonForm(forms.ModelForm):
    class Meta():
        model = Post
        fields = ('title', 'slug', 'author', 'User',
                  'updated_on', 'content', 'created_on', 'status')


class ComForm(forms.ModelForm):
    class Meta:
        model = Commentaire
        fields = {'corps'}
        labels = {'corps': 'Commentaires'}
        widget = {
            'corps': forms.Textarea(attrs={
                'class': 'form-control',
                'row': 4,
                'cols': 70,
                'placeholder': 'Entrez votre commentaire ici'
            })


        }


class repForm(forms.ModelForm):
    class Meta:
        model = Reponse
        fields = {'corps'}
        labels = {'corps': 'reponses'}
        widget = {
            'corps': forms.Textarea(attrs={
                'class': 'form-control',
                'row': 2,
                'cols': 10,
                'placeholder': 'Entrez votre reponse ici'
            })


        }
