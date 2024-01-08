# views.py
import datetime
from django.shortcuts import render
from age.froms import TugilganYilForm
from .models import TugilganYil

def yosh_hisoblash_view(request):
    form = TugilganYilForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        tugilgan_yil_str = form.cleaned_data['tugilgan_yil']

        if tugilgan_yil_str:
            try:
                tugilgan_yil = int(tugilgan_yil_str)
                user = TugilganYil(tugilgan_yil=tugilgan_yil)
                yosh, kun, vaqt = user.yosh_hisoblash()
                return render(request, 'result.html', {'yosh': yosh, 'kun': kun, 'vaqt': vaqt, 'yil': tugilgan_yil})
            except ValueError:
                error_message = "Tug'ilgan yilni to'g'ri kiriting."
                return render(request, 'error.html', {'error_message': error_message})

    return render(request, 'input_form.html', {'form': form})
