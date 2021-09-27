from django import forms
from . models import Number,GuestNumber,WishRequest

class NumberForm(forms.ModelForm):
    class Meta:
        model=Number
        fields=["choice", "numbers"]

class GuestNumberForm(forms.ModelForm):
    choice = forms.ChoiceField(required=True, choices=GuestNumber.CHOICEYESNO, widget=forms.RadioSelect())
    guestnumber1 = forms.BooleanField(required=False, widget=forms.CheckboxInput())
    guestnumber2 = forms.BooleanField(required=False, widget=forms.CheckboxInput())
    guestnumber3 = forms.BooleanField(required=False, widget=forms.CheckboxInput())
    guestnumber4 = forms.BooleanField(required=False, widget=forms.CheckboxInput())
    guestnumber5 = forms.BooleanField(required=False, widget=forms.CheckboxInput())
    guestnumber6 = forms.BooleanField(required=False, widget=forms.CheckboxInput())
    guestnumber7 = forms.BooleanField(required=False, widget=forms.CheckboxInput())
    guestnumber8 = forms.BooleanField(required=False, widget=forms.CheckboxInput())
    guestnumber9 = forms.BooleanField(required=False, widget=forms.CheckboxInput())
    guestnumber10 = forms.BooleanField(required=False, widget=forms.CheckboxInput())
    guestnumber11 = forms.BooleanField(required=False, widget=forms.CheckboxInput())
    guestnumber12 = forms.BooleanField(required=False, widget=forms.CheckboxInput())
    guestnumber13 = forms.BooleanField(required=False, widget=forms.CheckboxInput())
    guestnumber14 = forms.BooleanField(required=False, widget=forms.CheckboxInput())
    guestnumber15 = forms.BooleanField(required=False, widget=forms.CheckboxInput())
    guestnumber16 = forms.BooleanField(required=False, widget=forms.CheckboxInput())
    guestnumber17 = forms.BooleanField(required=False, widget=forms.CheckboxInput())
    guestnumber18 = forms.BooleanField(required=False, widget=forms.CheckboxInput())
    guestnumber19 = forms.BooleanField(required=False, widget=forms.CheckboxInput())
    guestnumber20 = forms.BooleanField(required=False, widget=forms.CheckboxInput())
    guestnumber21 = forms.BooleanField(required=False, widget=forms.CheckboxInput())
    guestnumber22 = forms.BooleanField(required=False, widget=forms.CheckboxInput())
    guestnumber23 = forms.BooleanField(required=False, widget=forms.CheckboxInput())
    guestnumber24 = forms.BooleanField(required=False, widget=forms.CheckboxInput())
    guestnumber25 = forms.BooleanField(required=False, widget=forms.CheckboxInput())
    guestnumber26 = forms.BooleanField(required=False, widget=forms.CheckboxInput())
    guestnumber27 = forms.BooleanField(required=False, widget=forms.CheckboxInput())
    guestnumber28 = forms.BooleanField(required=False, widget=forms.CheckboxInput())
    guestnumber29 = forms.BooleanField(required=False, widget=forms.CheckboxInput())
    guestnumber30 = forms.BooleanField(required=False, widget=forms.CheckboxInput())
    guestnumber31 = forms.BooleanField(required=False, widget=forms.CheckboxInput())
    guestnumber32 = forms.BooleanField(required=False, widget=forms.CheckboxInput())
    guestnumber33 = forms.BooleanField(required=False, widget=forms.CheckboxInput())
    guestnumber34 = forms.BooleanField(required=False, widget=forms.CheckboxInput())
    guestnumber35 = forms.BooleanField(required=False, widget=forms.CheckboxInput())
    guestnumber36 = forms.BooleanField(required=False, widget=forms.CheckboxInput())
    guestnumber37 = forms.BooleanField(required=False, widget=forms.CheckboxInput())
    guestnumber38 = forms.BooleanField(required=False, widget=forms.CheckboxInput())
    guestnumber39 = forms.BooleanField(required=False, widget=forms.CheckboxInput())
    guestnumber40 = forms.BooleanField(required=False, widget=forms.CheckboxInput())
    guestnumber41 = forms.BooleanField(required=False, widget=forms.CheckboxInput())
    guestnumber42 = forms.BooleanField(required=False, widget=forms.CheckboxInput())
    guestnumber43 = forms.BooleanField(required=False, widget=forms.CheckboxInput())
    guestnumber44 = forms.BooleanField(required=False, widget=forms.CheckboxInput())
    guestnumber45 = forms.BooleanField(required=False, widget=forms.CheckboxInput())
    guestnumber46 = forms.BooleanField(required=False, widget=forms.CheckboxInput())
    guestnumber47 = forms.BooleanField(required=False, widget=forms.CheckboxInput())
    guestnumber48 = forms.BooleanField(required=False, widget=forms.CheckboxInput())
    guestnumber49 = forms.BooleanField(required=False, widget=forms.CheckboxInput())
    class Meta:
        model = GuestNumber
        fields = ["choice", "guestnumber1", "guestnumber2", "guestnumber3", "guestnumber4", "guestnumber5", "guestnumber6", "guestnumber7",
                  "guestnumber8", "guestnumber9", "guestnumber10", "guestnumber11", "guestnumber12", "guestnumber13", "guestnumber14",
                  "guestnumber15", "guestnumber16", "guestnumber17", "guestnumber18", "guestnumber19", "guestnumber20", "guestnumber21",
                  "guestnumber22", "guestnumber23", "guestnumber24", "guestnumber25", "guestnumber26", "guestnumber27", "guestnumber28",
                  "guestnumber29", "guestnumber30", "guestnumber31", "guestnumber32", "guestnumber33", "guestnumber34", "guestnumber35",
                  "guestnumber36", "guestnumber38", "guestnumber39", "guestnumber40", "guestnumber41", "guestnumber42", "guestnumber43",
                  "guestnumber44", "guestnumber45", "guestnumber46", "guestnumber47", "guestnumber48", "guestnumber49"]

class WishRequestForm(forms.ModelForm):
    message = forms.CharField(required=True, label="Mesajınız", widget=forms.Textarea(attrs={'rows': 2, 'cols': 40, 'style':'resize:none;'}))
    choice = forms.ChoiceField(label="Seçiniz", choices=WishRequest.CHOICE, required=True)
    class Meta:
        model=WishRequest
        fields=["choice", "message"]

