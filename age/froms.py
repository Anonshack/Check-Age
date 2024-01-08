from django import forms


class TugilganYilForm(forms.Form):
    tugilgan_yil = forms.IntegerField(label='Tug\'ilgan yil')
