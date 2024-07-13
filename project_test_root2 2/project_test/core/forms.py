from django import forms

class CollectionName(forms.Form):
    collectionname = forms.CharField(label = "Flashcard collection name:", max_length = 1000)

class UserInput(forms.Form):
    userinput = forms.CharField(label = "Text to convert:", max_length = 1000)