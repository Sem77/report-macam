from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout

from .forms import AuthenticationForm
from constat_d_etat.forms import FormSearchArtWork

def log_in(request):

    if request.method == 'GET':
        if not request.user.is_authenticated:
            form = AuthenticationForm()
            return render(request, 'authentification/login.html', {'form': form})
        else:
            form_search = FormSearchArtWork()
            return render(request, 'constat_d_etat/index.html', {'form_search': form_search})

    else:
        form = AuthenticationForm(request.POST)

        context = {
            'form': form,
        }

        if form.is_valid():

            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('constat:index')
            else:                
                return render(request, 'authentification/login.html', context)

        return render(request, 'authentification/login.html', context)            


def log_out(request):
    logout(request)
    return redirect('authentification:log_in')
