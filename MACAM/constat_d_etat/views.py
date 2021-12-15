from django.contrib.auth.decorators import login_required
from django.core import paginator
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.core.exceptions import *

from . import forms
from .models import *
from .save.constat.save_constat_art_graphique import *
from .save.constat.save_constat_peinture_sur_toile import *
from .save.constat.save_constat_peinture_sur_bois import *
from .save.save_art import *
from .save.photo_significative.save_photo_significative import *

from authentification.models import Agent

from io import BytesIO
from django.template.loader import get_template
from xhtml2pdf import pisa


#returns page after login for constat application
@login_required(login_url='authentification:log_in')
def index(request):    
    
    """
    if not request.user.is_authenticated:
        return redirect('authentification:log_in')   
    """

    form_search = forms.FormSearchArtWork()
    return render(request, 'constat_d_etat/index.html', {'form_search': form_search})
    

#view that looks in the db for an art work according to the title or the inventory number
@login_required(login_url='authentification:log_in')
def search_art_work(request):

    form_search = forms.FormSearchArtWork(request.POST)

    if form_search.is_valid():

        #we set arts to False so that in the gabarit we can test his value
        #if it stays at False it means no art work was found and we can print a message for this
        arts = False
    
        if form_search.cleaned_data['search_by'] == 'inventory_number':

            if form_search.cleaned_data['art_type'] == forms.FormSearchArtWork.ART_GRAPHIQUE:
                arts = ArtGraphique.objects.filter(numero_inventaire=form_search.cleaned_data['query'])
    
            elif form_search.cleaned_data['art_type'] == forms.FormSearchArtWork.PEINTURE_SUR_TOILE:
                arts = PeintureSurToile.objects.filter(numero_inventaire=form_search.cleaned_data['query'])

            elif form_search.cleaned_data['art_type'] == forms.FormSearchArtWork.PEINTURE_SUR_BOIS:
                arts = PeintureSurBois.objects.filter(numero_inventaire=form_search.cleaned_data['query'])        



        elif form_search.cleaned_data['search_by'] == 'title':
            
            if form_search.cleaned_data['art_type'] == forms.FormSearchArtWork.ART_GRAPHIQUE:
                arts = ArtGraphique.objects.filter(titre__icontains=form_search.cleaned_data['query'])

            elif form_search.cleaned_data['art_type'] == forms.FormSearchArtWork.PEINTURE_SUR_TOILE:
                arts = PeintureSurToile.objects.filter(titre__icontains=form_search.cleaned_data['query'])

            elif form_search.cleaned_data['art_type'] == forms.FormSearchArtWork.PEINTURE_SUR_BOIS:
                arts = PeintureSurBois.objects.filter(titre__icontains=form_search.cleaned_data['query'])              

        art_type = form_search.cleaned_data['art_type']
        form_search = forms.FormSearchArtWork()
        context = {
            'arts': arts,
            'form_search': form_search,
            'art_type': art_type,
        }

        return render(request, 'constat_d_etat/list_art/select_art_work.html', context)

    return render(request, 'constat_d_etat/index.html', {'form_search': form_search})


@login_required(login_url='authentification:log_in')
def list_arts(request, art_type, page_number):
    arts = False
        
    if art_type == forms.FormSearchArtWork.ART_GRAPHIQUE:
        arts = ArtGraphique.objects.all()

    elif art_type == forms.FormSearchArtWork.PEINTURE_SUR_TOILE:
        arts = PeintureSurToile.objects.all()

    elif art_type == forms.FormSearchArtWork.PEINTURE_SUR_BOIS:
        arts = PeintureSurBois.objects.all()        

    if arts != False:
        paginator = Paginator(arts, 7)
        try:
            arts = paginator.page(page_number)
        except PageNotAnInteger:
            arts = paginator.page(1)
        except EmptyPage:
            arts = paginator.page(paginator.num_pages)

    form_search = forms.FormSearchArtWork()
    context = {
        'arts': arts,
        'form_search': form_search,
        'art_type': art_type,
    }

    return render(request, 'constat_d_etat/list_art/list_arts.html', context)


#returns a page to see the different options we have on the art work selected
@login_required(login_url='authentification:log_in')
def preview_art_work(request, art_type, art_work_id):    
    
    if art_type == forms.FormSearchArtWork.ART_GRAPHIQUE:
        art = get_object_or_404(ArtGraphique, id=int(art_work_id))
        reports = ConstatArtGraphique.objects.filter(art_graphique=art).order_by('-date')

    elif art_type == forms.FormSearchArtWork.PEINTURE_SUR_TOILE:
        art = get_object_or_404(PeintureSurToile, id=int(art_work_id))
        reports = ConstatPeintureSurToile.objects.filter(peinture_sur_toile=art).order_by('-date')

    elif art_type == forms.FormSearchArtWork.PEINTURE_SUR_BOIS:
        art = get_object_or_404(PeintureSurBois, id=int(art_work_id))
        reports = ConstatPeintureSurBois.objects.filter(peinture_sur_bois=art).order_by('-date')    

    form_search = forms.FormSearchArtWork()
    context = {
        'art': art,
        'form_search': form_search,
        'art_type': art_type,
        'reports': reports,
    }

    return render(request, 'constat_d_etat/preview_art_work/preview_art_work.html', context)

    

    
#returns a page to save an art work if the method is GET
#save an art work if the method is POST
@login_required(login_url='authentification:log_in')
def save_art_work(request):
    
    if request.method == 'GET':
        form = forms.FormArt()
        return render(request, 'constat_d_etat/forms/save_art.html', {'form': form})

    else:
        form = forms.FormArt(request.POST, request.FILES)

        if form.is_valid():
            art_saver = SaveArt(form.cleaned_data)
            print(request.FILES)

            if form.cleaned_data['type_oeuvre'] == forms.FormArt.ART_GRAPHIQUE:
                art_saver.save_art_graphique()

            elif form.cleaned_data['type_oeuvre'] == forms.FormArt.PEINTURE_SUR_BOIS:
                art_saver.save_peinture_sur_bois()

            elif form.cleaned_data['type_oeuvre'] == forms.FormArt.PEINTURE_SUR_TOILE:
                art_saver.save_peinture_sur_toile()

            return redirect('constat:index')

        return render(request, 'constat_d_etat/forms/save_art.html', {'form': form})



#returns a page to make a report if the method is GET
#save a report if the method is POST
@login_required(login_url='authentification:log_in')
def form_report(request, art_type, art_work_id):

    agent = False

    try:
        agent = Agent.objects.get(user_id=request.user.id)
    except ObjectDoesNotExist:
        pass
    
    context = {
        'art_type': art_type,
        'agent': agent,
    }

    if request.method == 'GET':        

        if art_type == forms.FormArt.ART_GRAPHIQUE:
            form = forms.FormArtGraphique()
            art = get_object_or_404(ArtGraphique, id=int(art_work_id))
            
            context['art'] = art
            context['form'] = form                
            #context['form_art'] = form_art  

            form = forms.FormArtGraphique()
            return render(request, 'constat_d_etat/forms/form_art_graphique.html', context)
            

        elif art_type == forms.FormArt.PEINTURE_SUR_TOILE:
            form = forms.FormPeintureSurToile()
            art = get_object_or_404(PeintureSurToile, id=int(art_work_id))
            
            context['art'] = art
            context['form'] = form                
            #context['form_art'] = form_art
            
            form = forms.FormPeintureSurToile()
            return render(request, 'constat_d_etat/forms/form_peinture_sur_toile.html', context)


        elif art_type == forms.FormArt.PEINTURE_SUR_BOIS:
            form = forms.FormPeintureSurBois()
            art = get_object_or_404(PeintureSurBois, id=int(art_work_id))
            
            context['art'] = art
            context['form'] = form                
            #context['form_art'] = form_art

            form = forms.FormPeintureSurBois()
            return render(request, 'constat_d_etat/forms/form_peinture_sur_bois.html', context)
   

    else:
        if art_type == forms.FormArt.ART_GRAPHIQUE:
            form = forms.FormArtGraphique(request.POST)            
            art = get_object_or_404(ArtGraphique, id=int(art_work_id))

            if form.is_valid():
                form.cleaned_data['constat_auteur_constat'] = request.POST['report_author']
                if agent != False:
                    form.cleaned_data['signature_auteur_constat'] = agent.signature
                else:
                    form.cleaned_data['signature_auteur_constat'] = None

                constat_saver = SaveConstatArtGraphique(form.cleaned_data, int(art_work_id))
                constat = constat_saver.save_constat_art_graphique()

                photo_significative_saver = SavePhotoSignificative(request.POST, request.FILES, constat)
                photo_significative_saver.save_photo_significative_cadre()
                photo_significative_saver.save_photo_significative_support_art_graphique()

                messages.add_message(request, messages.SUCCESS, 'Constat effectué')
                return redirect('constat:preview_art_work', art_type=art_type, art_work_id=art_work_id)

            context['art'] = art
            context['form'] = form                
            #context['form_art'] = form_art

            return render(request, 'constat_d_etat/forms/form_art_graphique.html', context)

        elif art_type == forms.FormArt.PEINTURE_SUR_TOILE:
            form = forms.FormPeintureSurToile(request.POST)
            art = get_object_or_404(PeintureSurToile, id=int(art_work_id))

            if form.is_valid():
                form.cleaned_data['constat_gauteur_constat'] = request.POST['report_author']
                if agent != False:
                    form.cleaned_data['signature_auteur_constat'] = agent.signature
                else:
                    form.cleaned_data['signature_auteur_constat'] = None
                
                constat_saver = SaveConstatPeintureSurToile(form.cleaned_data, int(art_work_id))
                constat = constat_saver.save_constat_peinture_sur_toile()

                photo_significative_saver = SavePhotoSignificative(request.POST, request.FILES, constat)
                photo_significative_saver.save_photo_significative_cadre()
                photo_significative_saver.save_photo_significative_chassis()
                photo_significative_saver.save_photo_significative_couche_picturale()

                messages.add_message(request, messages.SUCCESS, 'Constat effectué')
                return redirect('constat:preview_art_work', art_type=art_type, art_work_id=art_work_id)

            context['art'] = art
            context['form'] = form                
            #context['form_art'] = form_art

            return render(request, 'constat_d_etat/forms/form_peinture_sur_toile.html', context)

        elif art_type == forms.FormArt.PEINTURE_SUR_BOIS:
            form = forms.FormPeintureSurBois(request.POST)
            art = get_object_or_404(PeintureSurBois, id=int(art_work_id))

            if form.is_valid():
                form.cleaned_data['constat_auteur_constat'] = request.POST['report_author']
                if agent != False:
                    form.cleaned_data['signature_auteur_constat'] = agent.signature
                else:
                    form.cleaned_data['signature_auteur_constat'] = None
                
                constat_saver = SaveConstatPeintureSurBois(form.cleaned_data, int(art_work_id))
                constat = constat_saver.save_constat_peinture_sur_bois()
                
                photo_significative_saver = SavePhotoSignificative(request.POST, request.FILES, constat)
                photo_significative_saver.save_photo_significative_cadre()
                photo_significative_saver.save_photo_significative_support_peinture_sur_bois()
                photo_significative_saver.save_photo_significative_couche_picturale()

                messages.add_message(request, messages.SUCCESS, 'Constat effectué')
                return redirect('constat:preview_art_work', art_type=art_type, art_work_id=art_work_id)

            context['art'] = art
            context['form'] = form                
            #context['form_art'] = form_art

            return render(request, 'constat_d_etat/forms/form_peinture_sur_bois.html', context)            
 


#display an html recap of a report
@login_required(login_url='authentification:log_in')
def show_report(request, art_type, art_work_id, report_id):

    context = {
        'art_type': art_type,
    }

    if art_type == forms.FormArt.ART_GRAPHIQUE:

        form = forms.FormArtGraphique()
        report = get_object_or_404(ConstatArtGraphique, id=report_id)
        pht_signs_cadre = PhotoSignificativeCadreOeuvre.objects.filter(cadre=report.cadre)
        pht_signs_support = PhotoSignificativeSupportArtGraphique.objects.filter(support=report.support)

        context['report'] = report
        context['pht_signs_cadre'] = pht_signs_cadre
        context['pht_signs_support'] = pht_signs_support
        context['form'] = form

        return render(request, 'constat_d_etat/report/preview_report_art_graphique.html', context)

    elif art_type == forms.FormArt.PEINTURE_SUR_TOILE:

        form = forms.FormPeintureSurToile()
        report = get_object_or_404(ConstatPeintureSurToile, id=report_id)
        pht_signs_cadre = PhotoSignificativeCadreOeuvre.objects.filter(cadre=report.cadre)
        pht_signs_chassis = PhotoSignificativeChassisPeintureSurToile.objects.filter(chassis=report.chassis)
        pht_signs_cp = PhotoSignificativeCouchePicturalePeinture.objects.filter(couche_picturale=report.couche_picturale)

        context['report'] = report
        context['pht_signs_cadre'] = pht_signs_cadre
        context['pht_signs_chassis'] = pht_signs_chassis
        context['pht_signs_cp'] = pht_signs_cp
        context['form'] = form

        return render(request, 'constat_d_etat/report/preview_report_peinture_sur_toile.html', context)

    elif art_type == forms.FormArt.PEINTURE_SUR_BOIS:

        form = forms.FormPeintureSurBois()
        report = get_object_or_404(ConstatPeintureSurBois, id=report_id)
        pht_signs_cadre = PhotoSignificativeCadreOeuvre.objects.filter(cadre=report.cadre)
        pht_signs_cp = PhotoSignificativeCouchePicturalePeinture.objects.filter(couche_picturale=report.couche_picturale)
        pht_signs_support = PhotoSignificativeSupportPeintureSurBois.objects.filter(support=report.support_peinture_sur_bois)

        context['report'] = report
        context['pht_signs_cadre'] = pht_signs_cadre
        context['pht_signs_support'] = pht_signs_support
        context['pht_signs_cp'] = pht_signs_cp
        context['form'] = form
        return render(request, 'constat_d_etat/report/preview_report_peinture_sur_bois.html', context)






#produce a pdf recap of a report
def render_to_pdf(request, template_src, context_dict):

	template = get_template(template_src)
	html  = template.render(context_dict)
	result = BytesIO()
	pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
	if not pdf.err:
		return HttpResponse(result.getvalue(), content_type='application/pdf')
	return None



#display a pdf recap of a report
@login_required(login_url='authentification:log_in')
def generate_pdf_file(request, art_type, art_work_id, report_id):

    context = {
        'art_type': art_type,
    }

    if art_type == forms.FormArt.ART_GRAPHIQUE:

        form = forms.FormArtGraphique()
        report = get_object_or_404(ConstatArtGraphique, id=report_id)
        pht_signs_cadre = PhotoSignificativeCadreOeuvre.objects.filter(cadre=report.cadre)
        pht_signs_support = PhotoSignificativeSupportArtGraphique.objects.filter(support=report.support)

        context['report'] = report
        context['pht_signs_cadre'] = pht_signs_cadre
        context['pht_signs_support'] = pht_signs_support
        context['form'] = form

        pdf = render_to_pdf(request, 'constat_d_etat/pdf_report/pdf_report_art_graphique.html', context)
        return HttpResponse(pdf, content_type='application/pdf')

    elif art_type == forms.FormArt.PEINTURE_SUR_TOILE:

        form = forms.FormPeintureSurToile()
        report = get_object_or_404(ConstatPeintureSurToile, id=report_id)
        pht_signs_cadre = PhotoSignificativeCadreOeuvre.objects.filter(cadre=report.cadre)
        pht_signs_chassis = PhotoSignificativeChassisPeintureSurToile.objects.filter(chassis=report.chassis)
        pht_signs_cp = PhotoSignificativeCouchePicturalePeinture.objects.filter(couche_picturale=report.couche_picturale)

        context['report'] = report
        context['pht_signs_cadre'] = pht_signs_cadre
        context['pht_signs_chassis'] = pht_signs_chassis
        context['pht_signs_cp'] = pht_signs_cp
        context['form'] = form

        pdf = render_to_pdf(request, 'constat_d_etat/pdf_report/pdf_report_peinture_sur_toile.html', context)
        return HttpResponse(pdf, content_type='application/pdf')

    elif art_type == forms.FormArt.PEINTURE_SUR_BOIS:

        form = forms.FormPeintureSurBois()
        report = get_object_or_404(ConstatPeintureSurBois, id=report_id)
        pht_signs_cadre = PhotoSignificativeCadreOeuvre.objects.filter(cadre=report.cadre)
        pht_signs_cp = PhotoSignificativeCouchePicturalePeinture.objects.filter(couche_picturale=report.couche_picturale)
        pht_signs_support = PhotoSignificativeSupportPeintureSurBois.objects.filter(support=report.support_peinture_sur_bois)

        context['report'] = report
        context['pht_signs_cadre'] = pht_signs_cadre
        context['pht_signs_support'] = pht_signs_support
        context['pht_signs_cp'] = pht_signs_cp
        context['form'] = form

        pdf = render_to_pdf(request, 'constat_d_etat/pdf_report/pdf_report_peinture_sur_bois.html', context)
        return HttpResponse(pdf, content_type='application/pdf')



"""
-defend intelligence
-mohamed youssfi
-thibault neuveu
-machine learnia
-docstring
"""