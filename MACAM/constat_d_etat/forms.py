from django import forms
from django.utils.regex_helper import Choice
    

class FormArt(forms.Form):

    HORIZONTAL = 'horizontal'
    VERTICAL = 'vertical'
    CARRE = 'carre'  
    RECTANGULAIRE = 'rectangulaire' 
    AUTRE = 'autre' 

    FORMATS = [
        (HORIZONTAL, 'Horizontal'),
        (VERTICAL, 'Vertical'),
        (CARRE, 'Carré'),
        (RECTANGULAIRE, 'Rectangulaire'),
        (AUTRE, 'Autre')
    ]


    ART_GRAPHIQUE = 'art_graphique'
    PEINTURE_SUR_TOILE = 'peinture_sur_toile'
    PEINTURE_SUR_BOIS = 'peinture_sur_bois'

    TYPE_OEUVRE = [
        (ART_GRAPHIQUE, 'Art graphique'),
        (PEINTURE_SUR_TOILE, 'Peinture sur toile'),
        (PEINTURE_SUR_BOIS, 'Peinture sur bois')
    ]    

    photo_oeuvre_face = forms.ImageField(required=False)   

    photo_oeuvre_revers = forms.ImageField(required=False)      
    
    institution = forms.CharField(
        label="Institution : ", 
        max_length=255, 
        required=True)

    numero_inventaire = forms.CharField(
        label="Numéro inventaire : ", 
        max_length=255, 
        required=True)    

    titre_oeuvre = forms.CharField(
        label="Titre : ", 
        max_length=255, 
        required=True
    )

    auteur_oeuvre = forms.CharField(
        label="Auteur : ", 
        max_length=255, 
        required=True
    )

    hauteur_avec_cadre = forms.FloatField(required=False)

    largeur_avec_cadre = forms.FloatField(required=False)

    epaisseur_avec_cadre = forms.FloatField(required=False)

    hauteur_sans_cadre = forms.FloatField(required=True)

    largeur_sans_cadre = forms.FloatField(required=True)

    epaisseur_sans_cadre = forms.FloatField(required=True)

    format_oeuvre = forms.ChoiceField(
        choices=FORMATS, 
        widget=forms.RadioSelect(
            attrs={'label': 'format'}
        ), 
        required=True
    )    

    autre_format = forms.CharField(
        max_length=255, 
        required=False
    )    

    type_oeuvre = forms.ChoiceField(
        choices=TYPE_OEUVRE,
        required=True
    )


class FormReport(forms.Form):

    RESERVE = 'reserve'
    SALLE = 'salle'
    PRETE = 'prete'

    EMPLACEMENTS = [
        (RESERVE, 'En réserve'),
        (SALLE, 'En salle'),
        (PRETE, 'Prêtée')
    ]  

    lieu_de_conservation = forms.CharField(
        label="Lieu de conservation : ", 
        max_length=255, 
        required=True,        
    )    

    ville = forms.CharField(
        label="Ville : ", 
        max_length=255, 
        required=True
    )

    emplacement_oeuvre = forms.ChoiceField(
        choices=EMPLACEMENTS, 
        required=True
    )

    constat_numero_caisse = forms.IntegerField(
        label="N° de caisse : ", 
        widget=forms.NumberInput(
            attrs={
                'size':'4',
            }
        ),
        required=False
    )

    constat_nom_transporteur = forms.CharField(
        label="Nom du transporteur : ", 
        required=False
    )

    constat_autres_oeuvres_meme_caisse = forms.BooleanField(
        label="Autres oeuvres dans la même caisse", 
        widget=forms.CheckboxInput, 
        required=False
    )

    constat_remarques_notes = forms.CharField(
        label="Remarques et notes : ", 
        widget=forms.Textarea, 
        required=False
    )

    constat_photos_numeriques_realisees_au_depart = forms.BooleanField(
        label="Photos numériques réalisées au départ", 
        widget=forms.CheckboxInput, 
        required=False
    )

    constat_original_constat_laisse_emprunteur = forms.BooleanField(
        label="Original du constat laissé à l'emprunteur", 
        widget=forms.CheckboxInput, 
        required=False
    )

    constat_copie_constat_laisse_emprunteur = forms.BooleanField(
        label="Copie du constat laissé à l'emprunteur", 
        widget=forms.CheckboxInput, 
        required=False
    )

    """
    constat_date_constat  = forms.DateField(
        label="Constat établi le : ", 
        required=False
    )"""

    constat_auteur_constat  = forms.CharField(
        label="réalisé par : ", 
        required=False
    )

    constat_nom_convoyeur = forms.CharField(
        label="Nom du convoyeur : ", 
        required=False
    )

    #we will implement signature of convoyeur  

    ##
    #fields of cadre
    ##


    absence_de_cadre = forms.BooleanField(
        label="Absence de cadre",
        widget=forms.CheckboxInput,
        required=False
    )

    #caractéristiques cadre
    cadre_caracteristiques_etat_satisfaisant = forms.BooleanField(
        label="Etat satisfaisant", 
        widget=forms.CheckboxInput, 
        required=False
    )
        
    cadre_caracteristiques_ancien = forms.BooleanField(
        label="Ancien", 
        widget=forms.CheckboxInput, 
        required=False
    )

    cadre_caracteristiques_moderne = forms.BooleanField(
        label="Moderne", 
        widget=forms.CheckboxInput, 
        required=False
    )

    cadre_caracteristiques_cadre_d_origine = forms.BooleanField(
        label="Cadre d'origine", 
        widget=forms.CheckboxInput, 
        required=False
    )

    cadre_caracteristiques_bois_dore = forms.BooleanField(
        label="Bois doré", 
        widget=forms.CheckboxInput, 
        required=False
    )

    cadre_caracteristiques_platre_dore = forms.BooleanField(
        label="Plâtre doré", 
        widget=forms.CheckboxInput, 
        required=False
    )

    cadre_caracteristiques_bois_peint = forms.BooleanField(
        label="Bois peint", 
        widget=forms.CheckboxInput, 
        required=False
    )

    cadre_caracteristiques_feuillure_garnie_de_feutrine = forms.BooleanField(
        label="Feuillure garnie de feutrine", 
        widget=forms.CheckboxInput, 
        required=False
    )

    cadre_caracteristiques_verre_antireflet = forms.BooleanField(
        label="Verre antireflet", 
        widget=forms.CheckboxInput, 
        required=False
    )

    cadre_caracteristiques_tampons_de_calage_cadre_ou_panneau = forms.BooleanField(
        label="Tampons de calage cadre/panneau", 
        widget=forms.CheckboxInput, 
        required=False
    )


    #altérations cadre
    cadre_alterations_disjoint_aux_angles = forms.BooleanField(
        label="Disjoint aux angles", 
        widget=forms.CheckboxInput, 
        required=False
    )

    cadre_alterations_fissure_aux_angles = forms.BooleanField(
        label="Fissure aux angles", 
        widget=forms.CheckboxInput, 
        required=False
    )

    cadre_alterations_fissure_sur_les_bords = forms.BooleanField(
        label="Fissure sur les bords", 
        widget=forms.CheckboxInput, 
        required=False
    )    

    cadre_alterations_cadre_voile = forms.BooleanField(
        label="Cadre voilé", 
        widget=forms.CheckboxInput, 
        required=False
    )

    cadre_alterations_encrassement = forms.BooleanField(
        label="Encrassement", 
        widget=forms.CheckboxInput, 
        required=False
    )

    cadre_alterations_decor_fragilise = forms.BooleanField(
        label="Décor fragilisé", 
        widget=forms.CheckboxInput, 
        required=False
    )

    cadre_alterations_lacunes_de_bois = forms.BooleanField(
        label="Lacunes de bois", 
        widget=forms.CheckboxInput, 
        required=False
    )

    cadre_alterations_lacunes_de_platre = forms.BooleanField(
        label="Lacunes de plâtre", 
        widget=forms.CheckboxInput, 
        required=False
    )

    cadre_alterations_platre_pulverilent = forms.BooleanField(
        label="Plâtre pulvérilent", 
        widget=forms.CheckboxInput, 
        required=False
    )

    cadre_alterations_peinture_ecaillee = forms.BooleanField(
        label="Peinture écaillée", 
        widget=forms.CheckboxInput, 
        required=False
    )

    cadre_alterations_trous_d_envol = forms.BooleanField(
        label="Trous d'envol", 
        widget=forms.CheckboxInput, 
        required=False
    )

    cadre_alterations_galerie_d_insectes = forms.BooleanField(
        label="Galerie d'insectes", 
        widget=forms.CheckboxInput, 
        required=False
    )

    

    #montage cadre
    cadre_montage_trous_de_pitons = forms.BooleanField(
        label="Trous de pitons", 
        widget=forms.CheckboxInput, 
        required=False
    )

    cadre_montage_trous_de_cartels = forms.BooleanField(
        label="Trous de cartels", 
        widget=forms.CheckboxInput, 
        required=False
    )

    cadre_montage_cartel = forms.BooleanField(
        label="Cartel", 
        widget=forms.CheckboxInput, 
        required=False
    )

    cadre_montage_ettiquettes = forms.BooleanField(
        label="Ettiquette(s)", 
        widget=forms.CheckboxInput, 
        required=False
    )

    cadre_montage_encadrement_flottant = forms.BooleanField(
        label="Encadrement flottant", 
        widget=forms.CheckboxInput, 
        required=False
    )

    cadre_montage_fixation_au_cadre = forms.BooleanField(
        label="Fixation au cadre", 
        widget=forms.CheckboxInput, 
        required=False
    )

    cadre_montage_ressorts = forms.BooleanField(
        label="Ressorts", 
        widget=forms.CheckboxInput, 
        required=False
    )

    cadre_montage_clous = forms.BooleanField(
        label="Clous", 
        widget=forms.CheckboxInput, 
        required=False
    )

    cadre_montage_pattes = forms.BooleanField(
        label="Pattes", 
        widget=forms.CheckboxInput, 
        required=False
    )

    cadre_montage_poignee_sur_les_montants = forms.BooleanField(
        label="Poignée sur les montants", 
        widget=forms.CheckboxInput, 
        required=False
    )

    cadre_montage_etat_poignee_sur_les_montants = forms.CharField(
        label="Etat", 
        required=False
    )

    cadre_montage_nombre_poignee_sur_les_montants = forms.IntegerField(
        label="Nombre", 
        required=False
    )



    #dorure cadre
    cadre_dorure_bon_etat = forms.BooleanField(
        label="Bon état", 
        widget=forms.CheckboxInput, 
        required=False
    )

    cadre_dorure_bronzine = forms.BooleanField(
        label="Bronzine", 
        widget=forms.CheckboxInput, 
        required=False
    )

    cadre_dorure_dorure_mixte = forms.BooleanField(
        label="Dorure mixte", 
        widget=forms.CheckboxInput, 
        required=False
    )

    cadre_dorure_piqures = forms.BooleanField(
        label="Piqûres", 
        widget=forms.CheckboxInput, 
        required=False
    )

    cadre_dorure_lacunes = forms.BooleanField(
        label="Lacunes", 
        widget=forms.CheckboxInput, 
        required=False
    )

    cadre_dorure_usures = forms.BooleanField(
        label="Usures", 
        widget=forms.CheckboxInput, 
        required=False
    )

    cadre_dorure_maquillage = forms.BooleanField(
        label="Maquillage", 
        widget=forms.CheckboxInput, 
        required=False
    )

    cadre_dorure_taches = forms.BooleanField(
        label="Taches", 
        widget=forms.CheckboxInput, 
        required=False
    )


    #systeme accrochage cadre
    cadre_systeme_accrochage_attelles = forms.BooleanField(
        label="Attelles", 
        widget=forms.CheckboxInput, 
        required=False
    )

    cadre_systeme_accrochage_pitons = forms.BooleanField(
        label="Pitons", 
        widget=forms.CheckboxInput, 
        required=False
    )

    cadre_systeme_accrochage_systeme_antivol = forms.BooleanField(
        label="Système antivol", 
        widget=forms.CheckboxInput, 
        required=False
    )

    cadre_systeme_accrochage_type_systeme_antivol = forms.CharField(
        label="Type : ", 
        required=False
    )

    cadre_systeme_accrochage_pretee = forms.BooleanField(
        label="Prêté(es)",    
        widget=forms.CheckboxInput, 
        required=False
    )

    cadre_systeme_accrochage_nombre_pretee = forms.IntegerField(
        label="Nombre : ", 
        required=False
    )

    cadre_systeme_accrochage_retirees = forms.BooleanField(
        label="Retiré(es)", 
        widget=forms.CheckboxInput, 
        required=False
    )



    ##
    #fields of emballage
    ##

    #protection simple emballage
    emballage_protection_simple_tamponnage = forms.BooleanField(label="Tamponnage", widget=forms.CheckboxInput, required=False)
    emballage_protection_simple_elastoc = forms.BooleanField(label="Elastoc", widget=forms.CheckboxInput, required=False)
    emballage_protection_simple_fibrenap = forms.BooleanField(label="Fibrenap", widget=forms.CheckboxInput, required=False)
    emballage_protection_simple_papier_kraft = forms.BooleanField(label="Papier kraft", widget=forms.CheckboxInput, required=False)
    emballage_protection_simple_papier_de_soie = forms.BooleanField(label="Papier de soie", widget=forms.CheckboxInput, required=False)
    emballage_protection_simple_film_polyester = forms.BooleanField(label="Film polyester (mylar, mélinex)", widget=forms.CheckboxInput, required=False)
    emballage_protection_simple_papier_cristal = forms.BooleanField(label="Papier cristal", widget=forms.CheckboxInput, required=False)
    emballage_protection_simple_intisse = forms.BooleanField(label="Intissé (tyvek)", widget=forms.CheckboxInput, required=False)
    emballage_protection_simple_carton_cannele = forms.BooleanField(label="Carton cannelé", widget=forms.CheckboxInput, required=False)
    emballage_protection_simple_plaque_de_polypropylene = forms.BooleanField(label="Plaque de polypropylène", widget=forms.CheckboxInput, required=False)
    emballage_protection_simple_bullkraft = forms.BooleanField(label="Bullkraft", widget=forms.CheckboxInput, required=False)
    emballage_protection_simple_bullpack = forms.BooleanField(label="Bullpack", widget=forms.CheckboxInput, required=False)

    #caisse emballage
    emballage_caisse_simple = forms.BooleanField(label="Simple", widget=forms.CheckboxInput, required=False)
    emballage_caisse_double = forms.BooleanField(label="Double", widget=forms.CheckboxInput, required=False)
    emballage_caisse_isotherme = forms.BooleanField(label="Isotherme", widget=forms.CheckboxInput, required=False)
    emballage_caisse_climatique = forms.BooleanField(label="Climatique", widget=forms.CheckboxInput, required=False)
    emballage_caisse_film_par_vapeur = forms.BooleanField(label="Film par-vapeur", widget=forms.CheckboxInput, required=False)
    emballage_caisse_mousses = forms.BooleanField(label="Mousses", widget=forms.CheckboxInput, required=False)
    emballage_caisse_polystylene = forms.BooleanField(label="Polystylène", widget=forms.CheckboxInput, required=False)
    emballage_caisse_tableau_face_dessus = forms.BooleanField(label="Tableau face dessus", widget=forms.CheckboxInput, required=False)
    emballage_caisse_tableau_face_dessous = forms.BooleanField(label="Tableau face dessous", widget=forms.CheckboxInput, required=False)
    emballage_caisse_indicateur_de_renversement = forms.BooleanField(label="Indicateur de renversement", widget=forms.CheckboxInput, required=False)
    emballage_caisse_gel_de_silice = forms.BooleanField(label="Gel de silice", widget=forms.CheckboxInput, required=False)
    emballage_caisse_thermohygrometre = forms.BooleanField(label="Thermohygromètre", widget=forms.CheckboxInput, required=False)
    emballage_caisse_indicateur_de_choc = forms.BooleanField(label="Indicateur de choc", widget=forms.CheckboxInput, required=False)   
        


    """
    def clean_titre_oeuvre(self, *args, **kwargs):
        titre_oeuvre = self.cleaned_data.get('titre_oeuvre')
        if 'Abidjan' not in titre_oeuvre:
            raise forms.ValidationError('Ne contient pas Abidjan')
        return titre_oeuvre
    """


class FormArtGraphique(FormReport):

    ##
    #Fields of Matériaux et support
    ##
    art_graphique_materiaux_support_revers_inacessible = forms.BooleanField(label="Revers inacessible", widget=forms.CheckboxInput, required=False)
    art_graphique_materiaux_support_carton = forms.BooleanField(label="Carton", widget=forms.CheckboxInput, required=False)
    art_graphique_materiaux_support_velin = forms.BooleanField(label="Vélin", widget=forms.CheckboxInput, required=False)
    art_graphique_materiaux_support_papyrus = forms.BooleanField(label="Papyrus", widget=forms.CheckboxInput, required=False)
    art_graphique_materiaux_support_ivoire = forms.BooleanField(label="Ivoire (miniature)", widget=forms.CheckboxInput, required=False)
    art_graphique_materiaux_support_cuir = forms.BooleanField(label="Cuir", widget=forms.CheckboxInput, required=False)
    art_graphique_materiaux_support_parchemin = forms.BooleanField(label="Parchemin", widget=forms.CheckboxInput, required=False)
    art_graphique_materiaux_support_soie = forms.BooleanField(label="Soie", widget=forms.CheckboxInput, required=False)
    art_graphique_materiaux_support_toile = forms.BooleanField(label="Toile (pastel)", widget=forms.CheckboxInput, required=False)
    art_graphique_materiaux_support_papier = forms.BooleanField(label="Papier", widget=forms.CheckboxInput, required=False)
    art_graphique_materiaux_support_papier_machine = forms.BooleanField(label="Papier machine", widget=forms.CheckboxInput, required=False)
    art_graphique_materiaux_support_papier_main = forms.BooleanField(label="Papier main", widget=forms.CheckboxInput, required=False)
    art_graphique_materiaux_support_papier_oriental = forms.BooleanField(label="Papier oriental", widget=forms.CheckboxInput, required=False)
    art_graphique_materiaux_support_papier_occidental = forms.BooleanField(label="Papier occidental", widget=forms.CheckboxInput, required=False)
    art_graphique_materiaux_support_papier_velin = forms.BooleanField(label="Papier vélin", widget=forms.CheckboxInput, required=False)
    art_graphique_materiaux_support_papier_base_fibre_vegetale = forms.BooleanField(label="Papier base fibre végétale", widget=forms.CheckboxInput, required=False)
    art_graphique_materiaux_support_papier_a_base_de_bois = forms.BooleanField(label="Papier à base de bois", widget=forms.CheckboxInput, required=False)
    art_graphique_materiaux_support_filigrane = forms.BooleanField(label="Filigrane", widget=forms.CheckboxInput, required=False)
    art_graphique_materiaux_support_papier_verge = forms.BooleanField(label="Papier vergé", widget=forms.CheckboxInput, required=False)
    art_graphique_materiaux_support_nombre_intervalles_vergeures = forms.IntegerField(label="Intervalles des vergeures : ", required=False)
    art_graphique_materiaux_support_nombre_intervalles_pontuseaux = forms.IntegerField(label="Intervalles des pontuseaux : ", required=False)

    ##
    #field of technique de dessin
    ##
    art_graphique_technique_dessin_stylet_pointe_metal = forms.BooleanField(label="Stylet / pointe de métal", widget=forms.CheckboxInput, required=False)
    art_graphique_technique_dessin_pierre_noire = forms.BooleanField(label="Pierre noire", widget=forms.CheckboxInput, required=False)
    art_graphique_technique_dessin_fusain_crayon_comte = forms.BooleanField(label="Fusain crayon comté", widget=forms.CheckboxInput, required=False)
    art_graphique_technique_dessin_graphite = forms.BooleanField(label="Graphite", widget=forms.CheckboxInput, required=False)
    art_graphique_technique_dessin_sanguine = forms.BooleanField(label="Sanguine", widget=forms.CheckboxInput, required=False)
    art_graphique_technique_dessin_craie_blanche = forms.BooleanField(label="Craie blanche", widget=forms.CheckboxInput, required=False)
    art_graphique_technique_dessin_crayon_de_couleurs = forms.BooleanField(label="Crayon de couleurs", widget=forms.CheckboxInput, required=False)
    art_graphique_technique_dessin_rehauts_blancs = forms.BooleanField(label="Rehauts blancs", widget=forms.CheckboxInput, required=False)
    art_graphique_technique_dessin_pastel = forms.BooleanField(label="Pastel", widget=forms.CheckboxInput, required=False)
    art_graphique_technique_dessin_encre_au_carbone = forms.BooleanField(label="Encre au carbone", widget=forms.CheckboxInput, required=False)
    art_graphique_technique_dessin_encre_brune = forms.BooleanField(label="Encre brune (bistre, sépia)", widget=forms.CheckboxInput, required=False)
    art_graphique_technique_dessin_encre_metallogallique = forms.BooleanField(label="Encre métallogallique", widget=forms.CheckboxInput, required=False)
    art_graphique_technique_dessin_peinture_huile_et_essence_terebenthine_sur_papier = forms.BooleanField(label="Peinture à l'huile et essence térébenthine sur papier", widget=forms.CheckboxInput, required=False)
    art_graphique_technique_dessin_encre_de_couleur = forms.BooleanField(label="Encre de couleur", widget=forms.CheckboxInput, required=False)
    art_graphique_technique_dessin_tempera = forms.BooleanField(label="Tempera", widget=forms.CheckboxInput, required=False)
    art_graphique_technique_dessin_gouache = forms.BooleanField(label="Gouache", widget=forms.CheckboxInput, required=False)
    art_graphique_technique_dessin_aquarelle = forms.BooleanField(label="Aquarelle", widget=forms.CheckboxInput, required=False)
    art_graphique_technique_dessin_autre = forms.BooleanField(label="Autre", widget=forms.CheckboxInput, required=False)
    art_graphique_technique_dessin_autre_technique_dessin = forms.CharField(required=False)
    
    ##
    #field of technique de l'estampe
    ##
    art_graphique_technique_estampe_burin = forms.BooleanField(label="Burin", widget=forms.CheckboxInput, required=False)
    art_graphique_technique_estampe_xylographie = forms.BooleanField(label="Xylographie", widget=forms.CheckboxInput, required=False)
    art_graphique_technique_estampe_taille_epargne = forms.BooleanField(label="Taille d'épargne", widget=forms.CheckboxInput, required=False)
    art_graphique_technique_estampe_eau_forte = forms.BooleanField(label="Eau forte", widget=forms.CheckboxInput, required=False)
    art_graphique_technique_estampe_aquatinte = forms.BooleanField(label="Aquatinte", widget=forms.CheckboxInput, required=False)
    art_graphique_technique_estampe_taille_douce = forms.BooleanField(label="Taille douce", widget=forms.CheckboxInput, required=False)
    art_graphique_technique_estampe_lithographie = forms.BooleanField(label="Lithographie", widget=forms.CheckboxInput, required=False)
    art_graphique_technique_estampe_pointe_seche = forms.BooleanField(label="Pointe sèche", widget=forms.CheckboxInput, required=False)
    art_graphique_technique_estampe_maniere_noire = forms.BooleanField(label="Manière noire", widget=forms.CheckboxInput, required=False)
    art_graphique_technique_estampe_maniere_au_crayon = forms.BooleanField(label="Manière au crayon", widget=forms.CheckboxInput, required=False)
    art_graphique_technique_estampe_procede_au_pochoir = forms.BooleanField(label="Procédé au pochoir", widget=forms.CheckboxInput, required=False)
    art_graphique_technique_estampe_serigraphie = forms.BooleanField(label="Sérigraphie", widget=forms.CheckboxInput, required=False)
    art_graphique_technique_estampe_techniques_combinees = forms.BooleanField(label="Techniques combinées", widget=forms.CheckboxInput, required=False)
    art_graphique_technique_estampe_nom_techniques_combinees = forms.CharField(required=False)

    ##
    #field of Autre technique graphique
    ##
    art_graphique_autre_technique_graphique_encre_a_imprimer_eau = forms.BooleanField(label="Encre à imprimer à l'eau", widget=forms.CheckboxInput, required=False)
    art_graphique_autre_technique_graphique_encre_a_imprimer_huile = forms.BooleanField(label="Encre à imprimer à l'huile", widget=forms.CheckboxInput, required=False)

    ##
    #field of Technique de reproduction
    ##
    art_graphique_technique_reproduction_heliogravure = forms.BooleanField(label="Héliogravure", widget=forms.CheckboxInput, required=False)
    art_graphique_technique_reproduction_quadrichromie_offset = forms.BooleanField(label="Quadrichromie offset", widget=forms.CheckboxInput, required=False)

    ##
    #field of support
    ##
    art_graphique_support_amincissement = forms.BooleanField(label="Amincissement", widget=forms.CheckboxInput, required=False)
    art_graphique_support_fragilite = forms.BooleanField(label="Fragilité", widget=forms.CheckboxInput, required=False)
    art_graphique_support_trou_de_punaises = forms.BooleanField(label="Trou de punaises", widget=forms.CheckboxInput, required=False)
    art_graphique_support_anciennes_restaurations = forms.BooleanField(label="Anciennes restaurations", widget=forms.CheckboxInput, required=False)
    art_graphique_support_gondolement = forms.BooleanField(label="Gondolement", widget=forms.CheckboxInput, required=False)
    art_graphique_support_trace_de_colle = forms.BooleanField(label="Trace de colle", widget=forms.CheckboxInput, required=False)
    art_graphique_support_brulure = forms.BooleanField(label="Brûlure", widget=forms.CheckboxInput, required=False)
    art_graphique_support_pliure = forms.BooleanField(label="Pliure", widget=forms.CheckboxInput, required=False)
    art_graphique_support_residus_adhesifs = forms.BooleanField(label="Résidus d'adhésifs", widget=forms.CheckboxInput, required=False)
    art_graphique_support_cassant = forms.BooleanField(label="Cassant", widget=forms.CheckboxInput, required=False)
    art_graphique_support_piqure = forms.BooleanField(label="Piqûre (foxing)", widget=forms.CheckboxInput, required=False)
    art_graphique_support_rouille = forms.BooleanField(label="Rouille", widget=forms.CheckboxInput, required=False)
    art_graphique_support_coupure = forms.BooleanField(label="Coupure", widget=forms.CheckboxInput, required=False)
    art_graphique_support_papier_froisse = forms.BooleanField(label="Papier froissé", widget=forms.CheckboxInput, required=False)
    art_graphique_support_taches_claires = forms.BooleanField(label="Tâches claires", widget=forms.CheckboxInput, required=False)
    art_graphique_support_dechirure = forms.BooleanField(label="Déchirure", widget=forms.CheckboxInput, required=False)
    art_graphique_support_lacune = forms.BooleanField(label="Lacune", widget=forms.CheckboxInput, required=False)
    art_graphique_support_taches_diverses = forms.BooleanField(label="Tâches diverses", widget=forms.CheckboxInput, required=False)
    art_graphique_support_decoloration = forms.BooleanField(label="Décoloration", widget=forms.CheckboxInput, required=False)
    art_graphique_support_rigidite = forms.BooleanField(label="Rigidité", widget=forms.CheckboxInput, required=False)
    art_graphique_support_zone_brune = forms.BooleanField(label="Zone brune", widget=forms.CheckboxInput, required=False)
    art_graphique_support_deformations = forms.BooleanField(label="Déformations", widget=forms.CheckboxInput, required=False)
    art_graphique_support_peluches = forms.BooleanField(label="Peluches", widget=forms.CheckboxInput, required=False)
    art_graphique_support_poussieres = forms.BooleanField(label="Poussières", widget=forms.CheckboxInput, required=False)
    art_graphique_support_depot_matiere_formant_tache = forms.BooleanField(label="Dépôt matière formant tâche", widget=forms.CheckboxInput, required=False)
    art_graphique_support_perforation = forms.BooleanField(label="Perforation", widget=forms.CheckboxInput, required=False)
    art_graphique_support_insectes = forms.BooleanField(label="Insectes", widget=forms.CheckboxInput, required=False)
    art_graphique_support_dislocation_des_fibres_cellulose = forms.BooleanField(label="Dislocation des fibres cellulose", widget=forms.CheckboxInput, required=False)    
    art_graphique_support_jaunissement_generalise = forms.BooleanField(label="Jaunissement géneralisé", widget=forms.CheckboxInput, required=False)
    art_graphique_support_trou_d_insectes = forms.BooleanField(label="Trou d'insectes", widget=forms.CheckboxInput, required=False)
    art_graphique_support_doublage_defectueux = forms.BooleanField(label="Doublage défectueux", widget=forms.CheckboxInput, required=False)
    art_graphique_support_jaunissement_localise = forms.BooleanField(label="Jaunissement localisé", widget=forms.CheckboxInput, required=False)
    art_graphique_support_micro_organismes = forms.BooleanField(label="Micro-organismes", widget=forms.CheckboxInput, required=False)
    art_graphique_support_epidermages = forms.BooleanField(label="Epidermages", widget=forms.CheckboxInput, required=False)
    art_graphique_support_impregnation_produit_gras = forms.BooleanField(label="Imprégnation d'un produit gras", widget=forms.CheckboxInput, required=False)
    art_graphique_support_moisissures_bacteries = forms.BooleanField(label="Moisissures / bactéries", widget=forms.CheckboxInput, required=False)

    ##
    #field of Technique
    ##
    art_graphique_technique_affaiblissement_des_traits = forms.BooleanField(label="Affaiblissement des traits", widget=forms.CheckboxInput, required=False)
    art_graphique_technique_craquelure = forms.BooleanField(label="Craquelure", widget=forms.CheckboxInput, required=False)
    art_graphique_technique_fixatif_altere = forms.BooleanField(label="Fixatif altéré", widget=forms.CheckboxInput, required=False)
    art_graphique_technique_anciennes_restaurations = forms.BooleanField(label="Anciennes restaurations", widget=forms.CheckboxInput, required=False)
    art_graphique_technique_decapage = forms.BooleanField(label="Décapage", widget=forms.CheckboxInput, required=False)
    art_graphique_technique_jaunissement = forms.BooleanField(label="Jaunissement", widget=forms.CheckboxInput, required=False)
    art_graphique_technique_corrosion_encre = forms.BooleanField(label="Corrosion de l'encre", widget=forms.CheckboxInput, required=False)
    art_graphique_technique_ecaillage_des_gouaches = forms.BooleanField(label="Ecaillage des gouaches", widget=forms.CheckboxInput, required=False)
    art_graphique_technique_vernis_altere = forms.BooleanField(label="Vernis altéré", widget=forms.CheckboxInput, required=False)
    art_graphique_technique_couleurs_qui_ont_fuse = forms.BooleanField(label="Couleurs qui ont fusé (eau)", widget=forms.CheckboxInput, required=False)
    art_graphique_technique_manques = forms.BooleanField(label="Manques", widget=forms.CheckboxInput, required=False)
    art_graphique_technique_traits_degrade = forms.BooleanField(label="Traits dégradé", widget=forms.CheckboxInput, required=False)
    art_graphique_technique_couleurs_eclaircies = forms.BooleanField(label="Couleurs éclaircies (soleil)", widget=forms.CheckboxInput, required=False)
    art_graphique_technique_pulverulence = forms.BooleanField(label="Pulvérulence", widget=forms.CheckboxInput, required=False)
    art_graphique_technique_teintes_palies = forms.BooleanField(label="Teintes pâlies", widget=forms.CheckboxInput, required=False)
    art_graphique_technique_teintes_transformees = forms.BooleanField(label="Teintes transformées", widget=forms.CheckboxInput, required=False)

    ##
    #field of Montage
    ##
    art_graphique_montage_carton_au_verso = forms.BooleanField(label="Carton au verso", widget=forms.CheckboxInput, required=False)
    art_graphique_montage_colle_en_plein = forms.BooleanField(label="Collé en plein", widget=forms.CheckboxInput, required=False)
    art_graphique_montage_anciennes_restaurations = forms.BooleanField(label="Anciennes restaurations", widget=forms.CheckboxInput, required=False)
    art_graphique_montage_fenetre_au_recto = forms.BooleanField(label="Fenêtre au recto", widget=forms.CheckboxInput, required=False)
    art_graphique_montage_colle_par_les_bords = forms.BooleanField(label="Collé par les bords", widget=forms.CheckboxInput, required=False)
    art_graphique_montage_defaut_adherence = forms.BooleanField(label="Défaut d'adhérence", widget=forms.CheckboxInput, required=False)
    art_graphique_montage_passepartout = forms.BooleanField(label="Passepartout", widget=forms.CheckboxInput, required=False)
    art_graphique_montage_fausse_marge = forms.BooleanField(label="Fausse marge", widget=forms.CheckboxInput, required=False)
    art_graphique_montage_charniere_en_japon = forms.BooleanField(label="Charnière en japon", widget=forms.CheckboxInput, required=False)


class FormPeinture(FormReport):

    #Couche picturale

    ##
    #fields of Altérations optiques
    ##
    peinture_alterations_optiques_usures = forms.BooleanField(label="Usures", widget=forms.CheckboxInput, required=False)
    peinture_alterations_optiques_griffures = forms.BooleanField(label="Griffures", widget=forms.CheckboxInput, required=False)
    peinture_alterations_optiques_impression_texture = forms.BooleanField(label="Impression de texture", widget=forms.CheckboxInput, required=False)
    peinture_alterations_optiques_marques_chassis = forms.BooleanField(label="Marques de châssis", widget=forms.CheckboxInput, required=False)
    peinture_alterations_optiques_trous_envol = forms.BooleanField(label="Trous d'envol", widget=forms.CheckboxInput, required=False)
    peinture_alterations_optiques_dejections_insectes = forms.BooleanField(label="Déjections d'insectes", widget=forms.CheckboxInput, required=False)
    peinture_alterations_optiques_transparences_accrues = forms.BooleanField(label="Transparences accrues", widget=forms.CheckboxInput, required=False)
    peinture_alterations_optiques_repeints_alteres = forms.BooleanField(label="Repeints altérés", widget=forms.CheckboxInput, required=False)
    peinture_alterations_optiques_matics_debordants = forms.BooleanField(label="Matics débordants", widget=forms.CheckboxInput, required=False)
    peinture_alterations_optiques_traces_de_dorure = forms.BooleanField(label="Traces de dorure", widget=forms.CheckboxInput, required=False)
    peinture_alterations_optiques_projections = forms.BooleanField(label="Projections", widget=forms.CheckboxInput, required=False)
    peinture_alterations_optiques_ecrasement_de_matiere = forms.BooleanField(label="Ecrasement de matière", widget=forms.CheckboxInput, required=False)

    ##
    #fields of vernis
    ##
    peinture_vernis_homogeneite_satisfaisante = forms.BooleanField(label="Homogénéité satisfaisante", widget=forms.CheckboxInput, required=False)
    peinture_vernis_jaunissement = forms.BooleanField(label="Jaunissement", widget=forms.CheckboxInput, required=False)
    peinture_vernis_encrassement = forms.BooleanField(label="Encrassement", widget=forms.CheckboxInput, required=False)
    peinture_vernis_chancis = forms.BooleanField(label="Chancis", widget=forms.CheckboxInput, required=False)
    peinture_vernis_coulures = forms.BooleanField(label="Coulures", widget=forms.CheckboxInput, required=False)
    peinture_vernis_inegalite_de_surface = forms.BooleanField(label="Inégalité de surface", widget=forms.CheckboxInput, required=False)
    peinture_vernis_lacunes = forms.BooleanField(label="Lacunes", widget=forms.CheckboxInput, required=False)
    peinture_vernis_soulevements = forms.BooleanField(label="Soulèvements", widget=forms.CheckboxInput, required=False)
    peinture_vernis_chevauchement_ecaillement = forms.BooleanField(label="Chevauchement d'écaillement", widget=forms.CheckboxInput, required=False)

    ##
    #fields of Adhesion
    ##
    peinture_adhesion_satisfaisante = forms.BooleanField(label="Satisfaisante", widget=forms.CheckboxInput, required=False)
    peinture_adhesion_deplacage = forms.BooleanField(label="Déplacage", widget=forms.CheckboxInput, required=False)
    peinture_adhesion_epidermage = forms.BooleanField(label="Épidermage", widget=forms.CheckboxInput, required=False)
    peinture_adhesion_cloque = forms.BooleanField(label="Cloque", widget=forms.CheckboxInput, required=False)
    peinture_adhesion_deplacement_ecailles = forms.BooleanField(label="Déplacement d'écailles", widget=forms.CheckboxInput, required=False)
    peinture_adhesion_zones_pulverilentes = forms.BooleanField(label="Zones pulvérilentes", widget=forms.CheckboxInput, required=False)
    peinture_adhesion_transposition = forms.BooleanField(label="Transposition", widget=forms.CheckboxInput, required=False)
    peinture_adhesion_brulures = forms.BooleanField(label="Brûlures", widget=forms.CheckboxInput, required=False)
    peinture_adhesion_lacunes = forms.BooleanField(label="Lacunes", widget=forms.CheckboxInput, required=False)
    peinture_adhesion_soulevement = forms.BooleanField(label="Soulèvement", widget=forms.CheckboxInput, required=False)
    peinture_adhesion_chevauchement_ecailles = forms.BooleanField(label="Chevauchement d'écailles", widget=forms.CheckboxInput, required=False)

    ##
    #fields of Craquelures prématurées
    ##
    peinture_craquelure_prematuree_rides = forms.BooleanField(label="Rides", widget=forms.CheckboxInput, required=False)
    peinture_craquelure_prematuree_gercures = forms.BooleanField(label="Gerçures", widget=forms.CheckboxInput, required=False)
    peinture_craquelure_prematuree_crevasses = forms.BooleanField(label="Crevasses", widget=forms.CheckboxInput, required=False)
    peinture_craquelure_prematuree_craquelures_fermees = forms.BooleanField(label="craquelures fermees", widget=forms.CheckboxInput, required=False)

    ##
    #fields of Craquelures d'âge
    ##
    peinture_craquelure_age_reseau_generalise_fin = forms.BooleanField(label="Réseau généralisé fin", widget=forms.CheckboxInput, required=False)
    peinture_craquelure_age_reseau_generalise_prononce = forms.BooleanField(label="Réseau généralisé prononcé", widget=forms.CheckboxInput, required=False)
    peinture_craquelure_age_limites_a_une_zone = forms.BooleanField(label="Limités à une zone", widget=forms.CheckboxInput, required=False)
    peinture_craquelure_age_circulaire = forms.BooleanField(label="Circulaire", widget=forms.CheckboxInput, required=False)
    peinture_craquelure_age_diagonales = forms.BooleanField(label="Diagonales", widget=forms.CheckboxInput, required=False)
    peinture_craquelure_age_horizontales_verticales = forms.BooleanField(label="Horizontales/verticales", widget=forms.CheckboxInput, required=False)
    peinture_craquelure_age_en_echelle = forms.BooleanField(label="En échelle", widget=forms.CheckboxInput, required=False)
    peinture_craquelure_age_en_escargot = forms.BooleanField(label="En escargot", widget=forms.CheckboxInput, required=False)
    peinture_craquelure_age_faiencage = forms.BooleanField(label="Faïençage", widget=forms.CheckboxInput, required=False)
    peinture_craquelure_age_pavimenteuses = forms.BooleanField(label="Pavimenteuses", widget=forms.CheckboxInput, required=False)


class FormPeintureSurBois(FormPeinture):

    #support

    ##
    #fields of Constitution
    ##
    peinture_sur_bois_constitution_armure_toile = forms.BooleanField(label="Armure toile", widget=forms.CheckboxInput, required=False)
    peinture_sur_bois_constitution_armure_sergee = forms.BooleanField(label="Armure sergée", widget=forms.CheckboxInput, required=False)
    peinture_sur_bois_constitution_armure_satin = forms.BooleanField(label="Armure satin", widget=forms.CheckboxInput, required=False)
    peinture_sur_bois_constitution_papier_maroufle = forms.BooleanField(label="Papier marouflé", widget=forms.CheckboxInput, required=False)
    peinture_sur_bois_constitution_tissage_toile = forms.BooleanField(label="Tissage de la toile", widget=forms.CheckboxInput, required=False)
    peinture_sur_bois_constitution_lache = forms.BooleanField(label="Lâche", widget=forms.CheckboxInput, required=False)
    peinture_sur_bois_constitution_moyen = forms.BooleanField(label="Moyen", widget=forms.CheckboxInput, required=False)
    peinture_sur_bois_constitution_serre = forms.BooleanField(label="Serré", widget=forms.CheckboxInput, required=False)
    peinture_sur_bois_constitution_toile_originale = forms.BooleanField(label="Toile originale", widget=forms.CheckboxInput, required=False)
    peinture_sur_bois_constitution_rentoilage = forms.BooleanField(label="Rentoilage", widget=forms.CheckboxInput, required=False)
    peinture_sur_bois_constitution_doublage = forms.BooleanField(label="Doublage", widget=forms.CheckboxInput, required=False)
    peinture_sur_bois_constitution_doublage_aveugle = forms.BooleanField(label="Doublage aveugle", widget=forms.CheckboxInput, required=False)
    peinture_sur_bois_constitution_agrandissement = forms.BooleanField(label="Agrandissement", widget=forms.CheckboxInput, required=False)
    peinture_sur_bois_constitution_coutures = forms.BooleanField(label="Coutures", widget=forms.CheckboxInput, required=False)
    peinture_sur_bois_constitution_noeuds_toile = forms.BooleanField(label="Noeuds de toile", widget=forms.CheckboxInput, required=False)
    peinture_sur_bois_constitution_bande_tension = forms.BooleanField(label="Bande de tension", widget=forms.CheckboxInput, required=False)
    peinture_sur_bois_constitution_transposition = forms.BooleanField(label="Transposition", widget=forms.CheckboxInput, required=False)
    peinture_sur_bois_constitution_marouflage = forms.BooleanField(label="Marouflage", widget=forms.CheckboxInput, required=False)
    peinture_sur_bois_constitution_pieces = forms.BooleanField(label="Pièces", widget=forms.CheckboxInput, required=False)
    peinture_sur_bois_constitution_nombre_pieces = forms.IntegerField(label="Nombre : ", required=False)
    peinture_sur_bois_constitution_inscriptions = forms.BooleanField(label="Inscriptions", widget=forms.CheckboxInput, required=False)
    peinture_sur_bois_constitution_etiquettes = forms.BooleanField(label="Etiquettes", widget=forms.CheckboxInput, required=False)
    peinture_sur_bois_constitution_marques_cachets = forms.BooleanField(label="Marques ou cachets", widget=forms.CheckboxInput, required=False)

    ##
    #fields of tension
    ##
    peinture_sur_bois_tension_tension_correcte = forms.BooleanField(label="Tension correcte", widget=forms.CheckboxInput, required=False)
    peinture_sur_bois_tension_toile_tres_lache = forms.BooleanField(label="Toile très lâche", widget=forms.CheckboxInput, required=False)
    peinture_sur_bois_tension_toile_lache = forms.BooleanField(label="Toile lâche", widget=forms.CheckboxInput, required=False)
    peinture_sur_bois_tension_toile_trop_tendue = forms.BooleanField(label="Toile trop tendue", widget=forms.CheckboxInput, required=False)

    ##
    #fields of Altérations
    ##
    peinture_sur_bois_alterations_toile_cuite = forms.BooleanField(label="Toile cuite", widget=forms.CheckboxInput, required=False)
    peinture_sur_bois_alterations_toile_impregnee = forms.BooleanField(label="Toile impregnée", widget=forms.CheckboxInput, required=False)
    peinture_sur_bois_alterations_aureoles = forms.BooleanField(label="Auréoles", widget=forms.CheckboxInput, required=False)
    peinture_sur_bois_alterations_coulures = forms.BooleanField(label="Coulures", widget=forms.CheckboxInput, required=False)
    peinture_sur_bois_alterations_dechirures_simples = forms.BooleanField(label="Déchirures simples", widget=forms.CheckboxInput, required=False)
    peinture_sur_bois_alterations_dechirures_complexes = forms.BooleanField(label="Déchirures complexes", widget=forms.CheckboxInput, required=False)
    peinture_sur_bois_alterations_coupure = forms.BooleanField(label="Coupure", widget=forms.CheckboxInput, required=False)
    peinture_sur_bois_alterations_lacerations = forms.BooleanField(label="Lacérations", widget=forms.CheckboxInput, required=False)
    peinture_sur_bois_alterations_percement = forms.BooleanField(label="Percement", widget=forms.CheckboxInput, required=False)
    peinture_sur_bois_alterations_eraflures = forms.BooleanField(label="Eraflures", widget=forms.CheckboxInput, required=False)
    peinture_sur_bois_alterations_cloques = forms.BooleanField(label="Cloques", widget=forms.CheckboxInput, required=False)
    peinture_sur_bois_alterations_poussiere = forms.BooleanField(label="Poussière", widget=forms.CheckboxInput, required=False)
    peinture_sur_bois_alterations_encrassement = forms.BooleanField(label="Encrassement", widget=forms.CheckboxInput, required=False)
    peinture_sur_bois_alterations_trous_envol = forms.BooleanField(label="Trous d'envol", widget=forms.CheckboxInput, required=False)
    peinture_sur_bois_alterations_moisissures = forms.BooleanField(label="Moisissures", widget=forms.CheckboxInput, required=False)
    peinture_sur_bois_alterations_infestation_active = forms.BooleanField(label="Infestation active", widget=forms.CheckboxInput, required=False)

    ##
    #fields of Déformations
    ##
    peinture_sur_bois_deformations_localisees = forms.BooleanField(label="Localisées", widget=forms.CheckboxInput, required=False)
    peinture_sur_bois_deformations_generales = forms.BooleanField(label="Générales", widget=forms.CheckboxInput, required=False)
    peinture_sur_bois_deformations_poche = forms.BooleanField(label="Poche(s)", widget=forms.CheckboxInput, required=False)
    peinture_sur_bois_deformations_en_drapeau = forms.BooleanField(label="En drapeau", widget=forms.CheckboxInput, required=False)
    peinture_sur_bois_deformations_plis = forms.BooleanField(label="Plis", widget=forms.CheckboxInput, required=False)
    peinture_sur_bois_deformations_plis_angles = forms.BooleanField(label="Plis d'angles", widget=forms.CheckboxInput, required=False)
    peinture_sur_bois_deformations_retraits = forms.BooleanField(label="Retraits", widget=forms.CheckboxInput, required=False)
    peinture_sur_bois_deformations_effets_vagues = forms.BooleanField(label="Effets de vagues", widget=forms.CheckboxInput, required=False)
    peinture_sur_bois_deformations_scrupules = forms.BooleanField(label="Scrupules", widget=forms.CheckboxInput, required=False)
    peinture_sur_bois_deformations_enfoncement_par_la_face = forms.BooleanField(label="Enfoncement par la face", widget=forms.CheckboxInput, required=False)
    peinture_sur_bois_deformations_enfoncement_par_le_revers = forms.BooleanField(label="Enfoncement par le revers", widget=forms.CheckboxInput, required=False)




class FormPeintureSurToile(FormPeinture):

    #support

    ##
    #fields of caracteristiques
    ##

    peinture_sur_toile_support_caracteristiques_revers_inaccessible = forms.BooleanField(label="Revers inaccessible", widget=forms.CheckboxInput, required=False)
    peinture_sur_toile_support_caracteristiques_bon_etat = forms.BooleanField(label="Bon état", widget=forms.CheckboxInput, required=False)
    peinture_sur_toile_support_caracteristiques_mauvais_etat = forms.BooleanField(label="Mauvais état", widget=forms.CheckboxInput, required=False)
    peinture_sur_toile_support_caracteristiques_restaure = forms.BooleanField(label="Restauré", widget=forms.CheckboxInput, required=False)
    peinture_sur_toile_support_caracteristiques_fendu = forms.BooleanField(label="Fendu", widget=forms.CheckboxInput, required=False)
    peinture_sur_toile_support_caracteristiques_ouvert = forms.BooleanField(label="Ouvert", widget=forms.CheckboxInput, required=False)
    peinture_sur_toile_support_caracteristiques_vermoulu = forms.BooleanField(label="Vermoulu", widget=forms.CheckboxInput, required=False)
    peinture_sur_toile_support_caracteristiques_inscriptions = forms.BooleanField(label="Inscriptions", widget=forms.CheckboxInput, required=False)
    peinture_sur_toile_support_caracteristiques_etiquettes = forms.BooleanField(label="Etiquettes", widget=forms.CheckboxInput, required=False)
    peinture_sur_toile_support_caracteristiques_marques_cachets = forms.BooleanField(label="Marques ou cachets", widget=forms.CheckboxInput, required=False)
    peinture_sur_toile_support_caracteristiques_caisson_climatique = forms.BooleanField(label="Caisson climatique", widget=forms.CheckboxInput, required=False)
    peinture_sur_toile_support_caracteristiques_protection_arriere = forms.BooleanField(label="Protection arrière", widget=forms.CheckboxInput, required=False)
    peinture_sur_toile_support_caracteristiques_nature_protection_arriere = forms.CharField(label="Nature : ", required=False)
    peinture_sur_toile_support_caracteristiques_trous_de_pitons_dans_les_planches = forms.BooleanField(label="Trous de pitons dans les planches", widget=forms.CheckboxInput, required=False)
    peinture_sur_toile_support_caracteristiques_nombre_trous_de_pitons_dans_les_planches = forms.IntegerField(label="Nombre : ", required=False)
    peinture_sur_toile_support_caracteristiques_trous_de_pitons_dans_les_traverses = forms.BooleanField(label="Trous de pitons dans les traverses", widget=forms.CheckboxInput, required=False)
    peinture_sur_toile_support_caracteristiques_nombre_trous_de_pitons_dans_les_traverses = forms.IntegerField(label="Nombre : ", required=False)
    peinture_sur_toile_support_caracteristiques_chassis_cadre = forms.BooleanField(label="Châssis cadre", widget=forms.CheckboxInput, required=False)
    peinture_sur_toile_support_caracteristiques_poignees_fixees_au_revers = forms.BooleanField(label="Poignées fixées au revers", widget=forms.CheckboxInput, required=False)
    peinture_sur_toile_support_caracteristiques_nature_poignees_fixees_au_revers = forms.CharField(label="Nature : ", required=False)
    peinture_sur_toile_support_caracteristiques_nombre_poignees_fixees_au_revers = forms.IntegerField(label="Nombre : ", required=False)

    ##
    #fields of essence
    ##
    peinture_sur_toile_support_essence_chene = forms.BooleanField(label="Chêne", widget=forms.CheckboxInput, required=False)
    peinture_sur_toile_support_essence_resineux = forms.BooleanField(label="Résineux", widget=forms.CheckboxInput, required=False)
    peinture_sur_toile_support_essence_peuplier = forms.BooleanField(label="Peuplier", widget=forms.CheckboxInput, required=False)
    peinture_sur_toile_support_essence_acajou = forms.BooleanField(label="Acajou", widget=forms.CheckboxInput, required=False)
    peinture_sur_toile_support_essence_autre = forms.BooleanField(label="Autre", widget=forms.CheckboxInput, required=False)
    peinture_sur_toile_support_essence_autre_essence = forms.CharField(required=False)

    ##
    #fields of fil du bois
    ##
    peinture_sur_toile_support_fil_du_bois_horizontal = forms.BooleanField(label="Horizontal", widget=forms.CheckboxInput, required=False)
    peinture_sur_toile_support_fil_du_bois_vertical = forms.BooleanField(label="Vertical", widget=forms.CheckboxInput, required=False)
    peinture_sur_toile_support_fil_du_bois_regulier = forms.BooleanField(label="Régulier", widget=forms.CheckboxInput, required=False)
    peinture_sur_toile_support_fil_du_bois_irregulier = forms.BooleanField(label="Irrégulier", widget=forms.CheckboxInput, required=False)

    ##
    #fields of assemblage
    ##
    peinture_sur_toile_support_assemblage_plats_joints = forms.BooleanField(label="Plats-joints", widget=forms.CheckboxInput, required=False)
    peinture_sur_toile_support_assemblage_rainures_languettes = forms.BooleanField(label="Rainures/languettes", widget=forms.CheckboxInput, required=False)
    peinture_sur_toile_support_assemblage_tenons_mortaises = forms.BooleanField(label="Tenons/mortaises", widget=forms.CheckboxInput, required=False)
    peinture_sur_toile_support_assemblage_queues_arrondes = forms.BooleanField(label="Queues d'arrondes", widget=forms.CheckboxInput, required=False)
    peinture_sur_toile_support_assemblage_correct = forms.BooleanField(label="Correct", widget=forms.CheckboxInput, required=False)
    peinture_sur_toile_support_assemblage_faible = forms.BooleanField(label="Faible", widget=forms.CheckboxInput, required=False)
    peinture_sur_toile_support_assemblage_disjoint = forms.BooleanField(label="Disjoint", widget=forms.CheckboxInput, required=False)
    peinture_sur_toile_support_assemblage_parquettage_mobile = forms.BooleanField(label="Parquettage mobile", widget=forms.CheckboxInput, required=False)
    peinture_sur_toile_support_assemblage_parquettage_bloque = forms.BooleanField(label="Parquettage bloqué", widget=forms.CheckboxInput, required=False)
    peinture_sur_toile_support_assemblage_panneau_contraint = forms.BooleanField(label="Panneau contraint", widget=forms.CheckboxInput, required=False)
    peinture_sur_toile_support_assemblage_traverses_originales = forms.BooleanField(label="Traverses originales", widget=forms.CheckboxInput, required=False)
    peinture_sur_toile_support_assemblage_nombre_de_traverses = forms.IntegerField(label="Nombre de traverses : ", required=False)
    peinture_sur_toile_support_assemblage_nombre_planches = forms.IntegerField(label="Nombre planches : ", required=False)

    ##
    #fields of revers
    ##
    peinture_sur_toile_support_revers_lisse = forms.BooleanField(label="Lisse", widget=forms.CheckboxInput, required=False)
    peinture_sur_toile_support_revers_brut = forms.BooleanField(label="Brut", widget=forms.CheckboxInput, required=False)
    peinture_sur_toile_support_revers_enduit = forms.BooleanField(label="Enduit", widget=forms.CheckboxInput, required=False)

    ##
    #fields of Tranche
    ##
    peinture_sur_toile_support_tranche_invisible = forms.BooleanField(label="Invisible", widget=forms.CheckboxInput, required=False)
    peinture_sur_toile_support_tranche_visible = forms.BooleanField(label="Visible", widget=forms.CheckboxInput, required=False)
    peinture_sur_toile_support_tranche_etat = forms.CharField(label="Etat : ", required=False)

    ##
    #fields of Altérations
    ##
    peinture_sur_toile_support_alterations_percements = forms.BooleanField(label="Percements", widget=forms.CheckboxInput, required=False)
    peinture_sur_toile_support_alterations_eraflures = forms.BooleanField(label="Eraflures", widget=forms.CheckboxInput, required=False)
    peinture_sur_toile_support_alterations_cloques = forms.BooleanField(label="Cloques", widget=forms.CheckboxInput, required=False)
    peinture_sur_toile_support_alterations_coulures = forms.BooleanField(label="Coulures", widget=forms.CheckboxInput, required=False)
    peinture_sur_toile_support_alterations_moisissures = forms.BooleanField(label="Moisissures", widget=forms.CheckboxInput, required=False)
    peinture_sur_toile_support_alterations_poussiere = forms.BooleanField(label="Poussière", widget=forms.CheckboxInput, required=False)
    peinture_sur_toile_support_alterations_encrassement = forms.BooleanField(label="Encrassement", widget=forms.CheckboxInput, required=False)
    peinture_sur_toile_support_alterations_aureoles = forms.BooleanField(label="Auréoles", widget=forms.CheckboxInput, required=False)
    peinture_sur_toile_support_alterations_effritement = forms.BooleanField(label="Effritement", widget=forms.CheckboxInput, required=False)
    peinture_sur_toile_support_alterations_fendillement = forms.BooleanField(label="Fendillement", widget=forms.CheckboxInput, required=False)
    peinture_sur_toile_support_alterations_trous_envol = forms.BooleanField(label="Trous d'envol", widget=forms.CheckboxInput, required=False)
    peinture_sur_toile_support_alterations_galeries_insectes = forms.BooleanField(label="Galeries d'insectes", widget=forms.CheckboxInput, required=False)

    ##
    #fields of Déformations
    ##
    peinture_sur_toile_support_deformations_localisees = forms.BooleanField(label="Localisées", widget=forms.CheckboxInput, required=False)
    peinture_sur_toile_support_deformations_generalisees = forms.BooleanField(label="Généralisées", widget=forms.CheckboxInput, required=False)
    peinture_sur_toile_support_deformations_panneau_voile = forms.BooleanField(label="Panneau voilé", widget=forms.CheckboxInput, required=False)
    peinture_sur_toile_support_deformations_enfoncement_par_la_face = forms.BooleanField(label="Enfoncement par la face", widget=forms.CheckboxInput, required=False)
    peinture_sur_toile_support_deformations_enfoncement_au_revers = forms.BooleanField(label="Enfoncement au revers", widget=forms.CheckboxInput, required=False)
    peinture_sur_toile_support_deformations_panneau_aminci = forms.BooleanField(label="Panneau aminci", widget=forms.CheckboxInput, required=False)


    #chassis

    ##
    #fields of caracteristiques
    ##
    peinture_sur_toile_chassis_caracteristiques_revers_inaccessible = forms.BooleanField(label="Revers inaccessible", widget=forms.CheckboxInput, required=False)
    peinture_sur_toile_chassis_caracteristiques_neuf = forms.BooleanField(label="Neuf", widget=forms.CheckboxInput, required=False)
    peinture_sur_toile_chassis_caracteristiques_bon_etat = forms.BooleanField(label="Bon état", widget=forms.CheckboxInput, required=False)
    peinture_sur_toile_chassis_caracteristiques_mauvais_etat = forms.BooleanField(label="Mauvais état", widget=forms.CheckboxInput, required=False)
    peinture_sur_toile_chassis_caracteristiques_d_origine = forms.BooleanField(label="D'origine", widget=forms.CheckboxInput, required=False)
    peinture_sur_toile_chassis_caracteristiques_chanfreine = forms.BooleanField(label="Chanfreiné", widget=forms.CheckboxInput, required=False)
    peinture_sur_toile_chassis_caracteristiques_renforts_d_angles = forms.BooleanField(label="Renforts d'angles", widget=forms.CheckboxInput, required=False)
    peinture_sur_toile_chassis_caracteristiques_fendu = forms.BooleanField(label="Fendu", widget=forms.CheckboxInput, required=False)
    peinture_sur_toile_chassis_caracteristiques_ouvert = forms.BooleanField(label="Ouvert", widget=forms.CheckboxInput, required=False)
    peinture_sur_toile_chassis_caracteristiques_vermoulu = forms.BooleanField(label="Vermoulu", widget=forms.CheckboxInput, required=False)
    peinture_sur_toile_chassis_caracteristiques_traverses_horizontales = forms.BooleanField(label="Traverses horizontales", widget=forms.CheckboxInput, required=False)
    peinture_sur_toile_chassis_caracteristiques_nombre_traverses_horizontales = forms.IntegerField(label="Nombre : ", required=False)
    peinture_sur_toile_chassis_caracteristiques_traverses_verticales = forms.BooleanField(label="Traverses verticales", widget=forms.CheckboxInput, required=False)
    peinture_sur_toile_chassis_caracteristiques_nombre_traverses_verticales = forms.IntegerField(label="Nombre : ", required=False)    
    peinture_sur_toile_chassis_caracteristiques_trous_de_pitons = forms.BooleanField(label="Trous de pitons", widget=forms.CheckboxInput, required=False)
    peinture_sur_toile_chassis_caracteristiques_etiquettes = forms.BooleanField(label="Etiquettes", widget=forms.CheckboxInput, required=False)
    peinture_sur_toile_chassis_caracteristiques_marques = forms.BooleanField(label="Marques", widget=forms.CheckboxInput, required=False)
    peinture_sur_toile_chassis_caracteristiques_caisson_climatique = forms.BooleanField(label="Caisson climatique", widget=forms.CheckboxInput, required=False)
    peinture_sur_toile_chassis_caracteristiques_protection_arriere = forms.BooleanField(label="Protection arrière", widget=forms.CheckboxInput, required=False)
    peinture_sur_toile_chassis_caracteristiques_nature_protection_arriere = forms.CharField(label="Nature : ", required=False)
    peinture_sur_toile_chassis_caracteristiques_poignees_sur_montants = forms.BooleanField(label="Poignées sur montants", widget=forms.CheckboxInput, required=False)
    peinture_sur_toile_chassis_caracteristiques_nature_poignees_sur_montants = forms.CharField(label="Nature : ", required=False)
    peinture_sur_toile_chassis_caracteristiques_nombre_poignees_sur_montants = forms.IntegerField(label="Nombre : ", required=False)

    ##
    #fields of Assemblage
    ##
    peinture_sur_toile_chassis_assemblage_correct = forms.BooleanField(label="Correct", widget=forms.CheckboxInput, required=False)
    peinture_sur_toile_chassis_assemblage_faible = forms.BooleanField(label="Faible", widget=forms.CheckboxInput, required=False)
    peinture_sur_toile_chassis_assemblage_disjoint = forms.BooleanField(label="Disjoint", widget=forms.CheckboxInput, required=False)

    ##
    #fields of cles
    ##
    peinture_sur_toile_chassis_cles_chassis_fixe = forms.BooleanField(label="Châssis fixe", widget=forms.CheckboxInput, required=False)
    peinture_sur_toile_chassis_cles_chassis_a_cles = forms.BooleanField(label="Châssis à clés", widget=forms.CheckboxInput, required=False)
    peinture_sur_toile_chassis_cles_nombre_cles_presentes = forms.IntegerField(label="Nombre de clés présentes : ", required=False)
    peinture_sur_toile_chassis_cles_manquantes = forms.BooleanField(label="Manquantes", widget=forms.CheckboxInput, required=False)
    peinture_sur_toile_chassis_cles_nombre_manquantes = forms.IntegerField(label="nombre : ", required=False)
    peinture_sur_toile_chassis_cles_cassees = forms.BooleanField(label="Cassées", widget=forms.CheckboxInput, required=False)
    peinture_sur_toile_chassis_cles_nombre_cassees = forms.IntegerField(label="nombre : ", required=False)
    peinture_sur_toile_chassis_cles_vermoules = forms.BooleanField(label="Vermoules", widget=forms.CheckboxInput, required=False)
    peinture_sur_toile_chassis_cles_nombre_vermoules = forms.IntegerField(label="nombre : ", required=False)
    peinture_sur_toile_chassis_cles_attachees = forms.BooleanField(label="Attachées", widget=forms.CheckboxInput, required=False)
    peinture_sur_toile_chassis_cles_nombre_attachees = forms.IntegerField(label="nombre : ", required=False)    

    ##
    #fields of Tranche
    ##
    peinture_sur_toile_chassis_tranche_invisible = forms.BooleanField(label="Invisible", widget=forms.CheckboxInput, required=False)
    peinture_sur_toile_chassis_tranche_papier_de_bordage = forms.BooleanField(label="Papier de bordage", widget=forms.CheckboxInput, required=False)
    peinture_sur_toile_chassis_tranche_etat = forms.CharField(label="Etat : ", required=False)

    ##
    #fields of Semence
    ##
    peinture_sur_toile_chassis_semence_d_origine = forms.BooleanField(label="D'origine", widget=forms.CheckboxInput, required=False)
    peinture_sur_toile_chassis_semence_ajoutees = forms.BooleanField(label="Ajoutées", widget=forms.CheckboxInput, required=False)
    peinture_sur_toile_chassis_semence_agrafes = forms.BooleanField(label="Agrafes", widget=forms.CheckboxInput, required=False)
    peinture_sur_toile_chassis_semence_guirlande_de_tension = forms.BooleanField(label="Guirlande de tension", widget=forms.CheckboxInput, required=False)
    peinture_sur_toile_chassis_semence_corrosion = forms.BooleanField(label="Corrosion", widget=forms.CheckboxInput, required=False)
    peinture_sur_toile_chassis_semence_manques = forms.BooleanField(label="Manques", widget=forms.CheckboxInput, required=False)


class FormSearchArtWork(forms.Form):

    ART_GRAPHIQUE = 'art_graphique'
    PEINTURE_SUR_TOILE = 'peinture_sur_toile'
    PEINTURE_SUR_BOIS = 'peinture_sur_bois'

    ART_TYPE = [
        (ART_GRAPHIQUE, 'Art graphique'),
        (PEINTURE_SUR_TOILE, 'Peinture sur toile'),
        (PEINTURE_SUR_BOIS, 'Peinture sur bois')
    ]

    SEARCH_BY = [
        ('title', 'Titre'),
        ('inventory_number', 'Numéro d\'inventaire'),
    ]

    art_type = forms.ChoiceField(
        choices=ART_TYPE,
        required=True
    )

    search_by = forms.ChoiceField(
        choices=SEARCH_BY,
        required=True
    )

    query = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'name': 'id',
                'placeholder': 'Art...',
                'type': 'text',
            }
        )
    )
