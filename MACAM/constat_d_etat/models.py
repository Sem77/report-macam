from django.db import models
from django.db.models.deletion import CASCADE


class PhotoSignificative(models.Model):
    nature_alteration = models.CharField(max_length=255, null=True)
    face = models.BooleanField(default=True)

    class Meta():
        abstract = True


##
#
##
#class linked to Emballage
class ProtectionSimpleEmballageOeuvre(models.Model):
    tamponnage = models.BooleanField(default=False)
    elastoc = models.BooleanField(default=False)
    fibrenap = models.BooleanField(default=False)
    papier_kraft = models.BooleanField(default=False)
    papier_de_soie = models.BooleanField(default=False)
    film_polyester = models.BooleanField(default=False)
    papier_cristal = models.BooleanField(default=False)
    intisse = models.BooleanField(default=False)
    carton_cannele = models.BooleanField(default=False)
    plaque_de_polypropene = models.BooleanField(default=False)
    bullkraft = models.BooleanField(default=False)
    bullpack = models.BooleanField(default=False)


#class linked to Emballage
class CaisseEmballageOeuvre(models.Model):
    simple = models.BooleanField(default=False)
    double = models.BooleanField(default=False)
    isotherme = models.BooleanField(default=False)
    climatique = models.BooleanField(default=False)
    film_pare_vapeur = models.BooleanField(default=False)
    mousses = models.BooleanField(default=False)
    polystylene = models.BooleanField(default=False)
    tableau_face_dessus = models.BooleanField(default=False)
    tableau_face_dessous = models.BooleanField(default=False)
    indicateur_de_renversement = models.BooleanField(default=False)
    gel_de_silice = models.BooleanField(default=False)
    thermohygrometre = models.BooleanField(default=False)
    indicateur_de_choc = models.BooleanField(default=False)
    

#class linked to OeuvreDArt
class EmballageOeuvre(models.Model):
    caisse = models.ForeignKey(CaisseEmballageOeuvre, on_delete= CASCADE, null=True)
    protection_simple = models.ForeignKey(ProtectionSimpleEmballageOeuvre, on_delete=CASCADE, null=True)




##
#
##
#class linked to Cadre
class CaracteristiquesCadreOeuvre(models.Model):
    ancien = models.BooleanField(default=False)
    moderne = models.BooleanField(default=False)
    cadre_d_origine = models.BooleanField(default=False)
    bois_dore = models.BooleanField(default=False)
    platre_dore = models.BooleanField(default=False)
    bois_peint = models.BooleanField(default=False)
    feuillure_garnie_de_feutrine = models.BooleanField(default=False)
    verre_antireflet = models.BooleanField(default=False)
    tampons_de_calage = models.BooleanField(default=False)    


#class linked to Cadre
class AlterationCadreOeuvre(models.Model): # A revoir
    dispoint_aux_angles = models.BooleanField(default=False)
    fissures_aux_angles = models.BooleanField(default=False)
    fissures_sur_les_bords = models.BooleanField(default=False)
    cadre_voile = models.BooleanField(default=False)
    encrassement= models.BooleanField(default=False)
    decor_fragilise = models.BooleanField(default=False)
    lacunes_de_bois = models.BooleanField(default=False)
    lacunes_de_platre = models.BooleanField(default=False)
    platre_pulverilent = models.BooleanField(default=False)
    peinture_ecaillee = models.BooleanField(default=False)
    trous_d_envol = models.BooleanField(default=False)
    galeries_d_insectes = models.BooleanField(default=False)
    

#class linked to Cadre
class MontageCadreOeuvre(models.Model):
    trous_de_pitons = models.BooleanField(default=False)
    trous_de_cartels = models.BooleanField(default=False)
    cartel = models.BooleanField(default=False)
    etiquettes = models.BooleanField(default=False)
    encadrement_flottant = models.BooleanField(default=False)
    fixation_au_cadre = models.BooleanField(default=False)
    ressorts = models.BooleanField(default=False)
    clous = models.BooleanField(default=False)
    pattes = models.BooleanField(default=False)
    poignees_sur_les_montants = models.BooleanField(default=False)
    etat_poignees_sur_les_montants = models.CharField(max_length=255)
    nombre_poignees_sur_les_montants = models.IntegerField(default=0)


#class linked to Cadre
class DorureCadreOeuvre(models.Model):
    bon_etat = models.BooleanField(default=False)
    bronzine = models.BooleanField(default=False)
    dorure_mixte = models.BooleanField(default=False)
    piqures = models.BooleanField(default=False)
    lacunes = models.BooleanField(default=False)
    usures = models.BooleanField(default=False)
    maquillage = models.BooleanField(default=False)
    taches = models.BooleanField(default=False)


#class linked to Cadre
class SystemeDAccrochageCadreOeuvre(models.Model):
    attelles = models.BooleanField(default=False)
    pitons = models.BooleanField(default=False)
    systeme_antivol = models.BooleanField(default=False)
    type_systeme_antivol = models.CharField(max_length=255)
    prete = models.BooleanField(default=False)
    nombre_pretee = models.IntegerField(default=0)
    retire = models.BooleanField(default=False)


#class linked to OeuvreDArt
class CadreOeuvre(models.Model):
    etat_satisfaisant = models.BooleanField(default=False)

    caracteristiques_cadre = models.ForeignKey(CaracteristiquesCadreOeuvre,on_delete=CASCADE, null=True)
    alteration = models.ForeignKey(AlterationCadreOeuvre, on_delete=CASCADE, null=True)
    montage = models.ForeignKey(MontageCadreOeuvre, on_delete=CASCADE, null=True)
    dorure = models.ForeignKey(DorureCadreOeuvre,on_delete=CASCADE, null=True)
    systeme_d_accrochage = models.ForeignKey(SystemeDAccrochageCadreOeuvre, on_delete=CASCADE, null=True)
    

#class linked to Cadre
class PhotoSignificativeCadreOeuvre(PhotoSignificative):
    photo = models.ImageField(null=True, upload_to='photos_significatives_cadre')
    photo_avec_emplacement = models.ImageField(null=True, upload_to='photos_significatives_cadre')
    cadre = models.ForeignKey(CadreOeuvre, on_delete=CASCADE, null=True)






##
#class OeuvreDArt
##
class OeuvreDArt(models.Model):
    numero_inventaire = models.CharField(max_length=10, null=True, unique=True)    
    ville = models.CharField(max_length=255, null=True)
    institution = models.CharField(max_length=255, null=True)    
    titre = models.CharField(max_length=255, null=True)
    auteur = models.CharField(max_length=255, null=True)    
    format_oeuvre = models.CharField(max_length=255, null=True)
    hauteur_avec_cadre = models.FloatField(null=True, default=0.0)
    hauteur_sans_cadre = models.FloatField(null=True)
    largeur_avec_cadre = models.FloatField(null=True, default=0.0)
    largeur_sans_cadre = models.FloatField(null=True)
    epaisseur_avec_cadre = models.FloatField(null=True, default=0.0)
    epaisseur_sans_cadre = models.FloatField(null=True)        

    class Meta():
        abstract = True






##
#
##
#class linked to CouchePicturale
class AlterationsOptiquesCouchePicturalePeinture(models.Model):
    usures = models.BooleanField(default=False)
    griffures = models.BooleanField(default=False)
    impression_de_texture = models.BooleanField(default=False)
    marques_de_chassis = models.BooleanField(default=False)
    trous_d_envol = models.BooleanField(default=False)
    dejections_d_insectes = models.BooleanField(default=False)
    transparences_accrues = models.BooleanField(default=False)
    repeints_alteres = models.BooleanField(default=False)
    mastics_debordants = models.BooleanField(default=False)
    traces_de_dorure = models.BooleanField(default=False)
    projections = models.BooleanField(default=False)
    ecrasement_de_matiere = models.BooleanField(default=False)


#class linked to CouchePicturale
class VernisCouchePicturalePeinture(models.Model):
    homogeneite_satisfaisante = models.BooleanField(default=False)
    jaunissement = models.BooleanField(default=False)
    encrassement = models.BooleanField(default=False)
    chancis = models.BooleanField(default=False)
    coulures = models.BooleanField(default=False)
    inegalite_de_surface = models.BooleanField(default=False)
    lacunes = models.BooleanField(default=False)
    soulevements = models.BooleanField(default=False)
    chevauchement_d_ecaillement = models.BooleanField(default=False)


#class linked to CouchePicturale
class AdhesionCouchePicturalePeinture(models.Model):
    satisfaisante = models.BooleanField(default=False)
    deplacage = models.BooleanField(default=False)
    epidermage = models.BooleanField(default=False)
    cloque = models.BooleanField(default=False)
    deplacement_d_ecailles = models.BooleanField(default=False)
    zones_pulverilentes = models.BooleanField(default=False)
    transposition = models.BooleanField(default=False)
    brulures = models.BooleanField(default=False)
    lacunes = models.BooleanField(default=False)
    soulevements = models.BooleanField(default=False)
    chevauchement_d_ecailles = models.BooleanField(default=False)


#class linked to CouchePicturale
class CraqueluresPrematureesCouchePicturalePeinture(models.Model):
    rides = models.BooleanField(default=False)
    gercures = models.BooleanField(default=False)
    crevasses = models.BooleanField(default=False)
    craquelures_fermees = models.BooleanField(default=False)


#class linked to CouchePicturale
class CraqueluresDAgeCouchePicturalePeinture(models.Model):
    reseau_generalise_fin = models.BooleanField(default=False)
    reseau_generalise_prononce = models.BooleanField(default=False)
    limite_a_une_zone = models.BooleanField(default=False)
    circulaire = models.BooleanField(default=False)
    diagonales = models.BooleanField(default=False)
    horizontale = models.BooleanField(default=False)
    en_echelle = models.BooleanField(default=False)
    en_escargot = models.BooleanField(default=False)
    faiencage = models.BooleanField(default=False)
    pavimenteuses = models.BooleanField(default=False)


#class linked to Peinture
class CouchePicturalePeinture(models.Model):
    alterations_optiques = models.ForeignKey(AlterationsOptiquesCouchePicturalePeinture, on_delete=CASCADE, null=True)
    vernis = models.ForeignKey(VernisCouchePicturalePeinture, on_delete=CASCADE, null=True)
    adhesion = models.ForeignKey(AdhesionCouchePicturalePeinture, on_delete=CASCADE, null=True)
    craquelure_premature = models.ForeignKey(CraqueluresPrematureesCouchePicturalePeinture, on_delete=CASCADE, null=True)
    craquelure_d_age = models.ForeignKey(CraqueluresDAgeCouchePicturalePeinture, on_delete=CASCADE, null=True)    


#class linked to CouchePicturale
class PhotoSignificativeCouchePicturalePeinture(PhotoSignificative):
    photo = models.ImageField(null=True, upload_to='photos_significatives_couche_picturale')
    photo_avec_emplacement = models.ImageField(null=True, upload_to='photos_significatives_couche_picturale')
    couche_picturale = models.ForeignKey(CouchePicturalePeinture, on_delete=CASCADE, null=True)
    





##
#
##
#class linked to Chassis
class CaracteristiquesChassisPeintureSurToile(models.Model):
    neuf = models.BooleanField(default=False)
    bon_etat = models.BooleanField(default=False)
    mauvais_etat = models.BooleanField(default=False)
    d_origine = models.BooleanField(default=False)
    chanfreine = models.BooleanField(default=False)
    renforts_d_angles = models.BooleanField(default=False)
    fendu = models.BooleanField(default=False)
    ouvert = models.BooleanField(default=False)
    vermoulu = models.BooleanField(default=False)
    traverses_horizontales = models.BooleanField(default=False)
    nombre_traverses_horizontales = models.IntegerField(default=0)
    traverses_verticales = models.BooleanField(default=False)
    nombre_traverses_verticales = models.IntegerField(default=0)
    trous_de_pitons = models.BooleanField(default=False)
    etiquettes = models.BooleanField(default=False)
    marques = models.BooleanField(default=False)
    caisson_climatique = models.BooleanField(default=False)
    protection_arriere = models.BooleanField(default=False)
    nature_protection_arriere = models.CharField(max_length=255)
    poignees_sur_montants = models.BooleanField(default=False)
    nature_poignees_sur_montants = models.CharField(max_length=255)
    nombre_poignees_sur_montants = models.IntegerField(default=0)


#class linked to Chassis
class AssemblageChassisPeintureSurToile(models.Model):
    correct = models.BooleanField(default=False)
    faible = models.BooleanField(default=False)
    disjoint = models.BooleanField(default=False)


#class linked to Chassis
class ClesChassisPeintureSurToile(models.Model):
    chassis_fixe = models.BooleanField(default=False)
    chassis_a_cle = models.BooleanField(default=False)
    nombre_de_cles_presentes_chassis_a_cle = models.IntegerField(default=0)
    manquantes = models.BooleanField(default=False)
    nombre_manquantes = models.IntegerField(default=0)
    cassees = models.BooleanField(default=False)
    nombre_cassees = models.IntegerField(default=0)
    vermoulues = models.BooleanField(default=False)
    nombre_vermoulues = models.IntegerField(default=0)
    attachees = models.BooleanField(default=False)
    nombre_attachees = models.IntegerField(default=0)


#class linked to Chassis
class TrancheChassisPeintureSurToile(models.Model):
    invisible = models.BooleanField(default=False)
    papier_de_bordage = models.BooleanField(default=False)
    etat_papier_de_bordage = models.CharField(max_length=255)


#class linked to Chassis
class SemencesChassisPeintureSurToile(models.Model):
    d_origine = models.BooleanField(default=False)
    ajoutees = models.BooleanField(default=False)
    agrafes = models.BooleanField(default=False)
    guirlande_de_tension = models.BooleanField(default=False)
    corrosion = models.BooleanField(default=False)
    manques = models.BooleanField(default=False)


#class linked to PeintureSurToile
class ChassisPeintureSurToile(models.Model):
    revers_inaccessible = models.BooleanField(default=False)

    caracteristiquesChassis = models.ForeignKey(CaracteristiquesChassisPeintureSurToile, on_delete=CASCADE, null=True)
    cles = models.ForeignKey(ClesChassisPeintureSurToile, on_delete=CASCADE, null=True)
    tranche = models.ForeignKey(TrancheChassisPeintureSurToile, on_delete=CASCADE, null=True)
    semences = models.ForeignKey(SemencesChassisPeintureSurToile, on_delete=CASCADE, null=True)
    assemblage = models.ForeignKey(AssemblageChassisPeintureSurToile, on_delete=CASCADE, null=True)


#class linked to Chassis
class PhotoSignificativeChassisPeintureSurToile(PhotoSignificative):
    photo = models.ImageField(null=True, upload_to='photos_significatives_chassis')
    photo_avec_emplacement = models.ImageField(null=True, upload_to='photos_significatives_chassis')
    chassis = models.ForeignKey(ChassisPeintureSurToile, on_delete=CASCADE, null=True)
    






##
#
##
#class linked to SupportPeintureSurToile
class CaracteristiquesSupportPeintureSurToile(models.Model):
    bon_etat = models.BooleanField(default=False)
    mauvais_etat = models.BooleanField(default=False)
    restaure = models.BooleanField(default=False)
    fendu = models.BooleanField(default=False)
    ouvert = models.BooleanField(default=False)
    vermoulu = models.BooleanField(default=False)
    inscriptions = models.BooleanField(default=False)
    etiquettes = models.BooleanField(default=False)
    marques_ou_cachets = models.BooleanField(default=False)
    caisson_climatique = models.BooleanField(default=False)
    protection_arriere = models.BooleanField(default=False)
    nature_protection_arriere = models.CharField(max_length=255)
    trous_de_pitons_dans_les_planches = models.BooleanField(default=False)
    nombre_trous_de_pitons_dans_les_planches = models.IntegerField(default=0)
    trous_de_pitons_dans_les_traverses = models.BooleanField(default=False)
    nombre_trous_de_pitons_dans_les_traverses = models.IntegerField(default=0)
    chassis_cadre = models.BooleanField(default=False)
    poignees_fixees_au_revers = models.BooleanField(default=False)
    nombre_poignees_fixees_au_revers = models.IntegerField(default=0)
    nature_poignees_fixees_au_revers = models.CharField(max_length=255)


#class linked to SupportPeintureSurToile
class EssenceSupportPeintureSurToile(models.Model):
    chene = models.BooleanField(default=False)
    resineux = models.BooleanField(default=False)
    peuplier = models.BooleanField(default=False)
    acajou = models.BooleanField(default=False)
    autre = models.BooleanField(default=False)
    essence_autre = models.CharField(max_length=255)


#class linked to SupportPeintureSurToile
class FilDuBoisSupportPeintureSurToile(models.Model):
    horizontal = models.BooleanField(default=False)
    vertical = models.BooleanField(default=False)
    regulier = models.BooleanField(default=False)
    irregulier = models.BooleanField(default=False)


#class linked to SupportPeintureSurToile
class AssemblageSupportPeintureSurToile(models.Model):
    plats_joints = models.BooleanField(default=False)
    rainures_ou_languettes = models.BooleanField(default=False)
    tenons_ou_mortaises = models.BooleanField(default=False)
    queues_d_arondes = models.BooleanField(default=False)
    correct = models.BooleanField(default=False)
    faible = models.BooleanField(default=False)
    disjoint = models.BooleanField(default=False)
    parquetage_mobile = models.BooleanField(default=False)
    parquetage_bloque = models.BooleanField(default=False)
    panneau_contraint = models.BooleanField(default=False)
    traverses_originales = models.BooleanField(default=False)
    nombre_de_traverses = models.IntegerField(default=0)
    nombre_de_planches = models.IntegerField(default=0)


#class linked to SupportPeintureSurToile
class ReversSupportPeintureSurToile(models.Model):
    lisse = models.BooleanField(default=False)
    brut = models.BooleanField(default=False)
    enduit = models.BooleanField(default=False)


#class linked to SupportPeintureSurToile
class TrancheSupportPeintureSurToile(models.Model):
    invisible = models.BooleanField(default=False)
    visible = models.BooleanField(default=False)
    etat = models.CharField(max_length=255)


#class linked to SupportPeintureSurToile
class AlterationsSupportPeintureSurToile(models.Model):
    percements = models.BooleanField(default=False)
    eraflures = models.BooleanField(default=False)
    cloques = models.BooleanField(default=False)
    coulures = models.BooleanField(default=False)
    moisissures = models.BooleanField(default=False)
    poussiere = models.BooleanField(default=False)
    encrassement = models.BooleanField(default=False)
    aureoles = models.BooleanField(default=False)
    effritement = models.BooleanField(default=False)
    fendillement = models.BooleanField(default=False)
    trous_d_envol = models.BooleanField(default=False)
    galerie_d_insectes = models.BooleanField(default=False)    


#class linked to SupportPeintureSurToile
class DeformationsSupportPeintureSurToile(models.Model):
    localisees = models.BooleanField(default=False)
    generalisees = models.BooleanField(default=False)
    panneau_voile = models.BooleanField(default=False)
    enfoncement_par_la_face = models.BooleanField(default=False)
    enfoncement_au_revers = models.BooleanField(default=False)
    panneau_aminci = models.BooleanField(default=False)


#class linked to PeintureSurToile
class SupportPeintureSurToile(models.Model):
    revers_inaccessible = models.BooleanField(default=True)

    caracteristiques = models.ForeignKey(CaracteristiquesSupportPeintureSurToile, on_delete=CASCADE, null=True)
    essence = models.ForeignKey(EssenceSupportPeintureSurToile, on_delete=CASCADE, null=True)
    fil_du_bois = models.ForeignKey(FilDuBoisSupportPeintureSurToile, on_delete=CASCADE, null=True)
    assemblage = models.ForeignKey(AssemblageSupportPeintureSurToile, on_delete=CASCADE, null=True)
    revers = models.ForeignKey(ReversSupportPeintureSurToile, on_delete=CASCADE, null=True)
    tranche = models.ForeignKey(TrancheSupportPeintureSurToile, on_delete=CASCADE, null=True)
    alterations = models.ForeignKey(AlterationsSupportPeintureSurToile, on_delete=CASCADE, null=True)
    deformations = models.ForeignKey(DeformationsSupportPeintureSurToile, on_delete=CASCADE, null=True)


#class extends Peinture
class PeintureSurToile(OeuvreDArt):
    photo_face = models.ImageField(upload_to='photos_identification_peinture_sur_toile', null=True)
    photo_revers = models.ImageField(upload_to='photos_identification_peinture_sur_toile', null=True)







##
#
##
#class linked to SupportPeintureSurBois
class ConstitutionSupportPeintureSurBois(models.Model):
    armure_toile = models.BooleanField(default=False)
    armure_sergee = models.BooleanField(default=False)
    armure_satin = models.BooleanField(default=False)
    papier_maroufle = models.BooleanField(default=False)
    tissage_de_la_toile = models.BooleanField(default=False)
    lache = models.BooleanField(default=False)
    moyen = models.BooleanField(default=False)
    serre = models.BooleanField(default=False)
    toile_originale = models.BooleanField(default=False)
    rentoilage = models.BooleanField(default=False)
    doublage = models.BooleanField(default=False)
    doublage_aveugle = models.BooleanField(default=False)
    agrandissement = models.BooleanField(default=False)
    coutures = models.BooleanField(default=False)
    noeud_de_toile = models.BooleanField(default=False)
    bande_de_tension = models.BooleanField(default=False)
    transposition = models.BooleanField(default=False)
    marouflage = models.BooleanField(default=False)
    pieces = models.BooleanField(default=False)
    nombre_pieces = models.IntegerField(default=0)
    inscriptions = models.BooleanField(default=False)
    etiquettes = models.BooleanField(default=False)
    marques_ou_cachets = models.BooleanField(default=False)


#class linked to SupportPeintureSurBois
class TensionSupportPeintureSurBois(models.Model):
    tension_correcte = models.BooleanField(default=False)
    toile_tres_lache = models.BooleanField(default=False)
    toile_lache = models.BooleanField(default=False)
    toile_trop_tendue = models.BooleanField(default=False)


#class linked to SupportPeintureSurBois
class AlterationsSupportPeintureSurBois(models.Model):
    toile_cuite = models.BooleanField(default=False)
    toile_impregnee = models.BooleanField(default=False)
    aureoles = models.BooleanField(default=False)
    coulures = models.BooleanField(default=False)
    dechirures_simples = models.BooleanField(default=False)
    dechirures_complexes = models.BooleanField(default=False)
    coupures = models.BooleanField(default=False)
    lacerations = models.BooleanField(default=False)
    percement = models.BooleanField(default=False)
    eraflures = models.BooleanField(default=False)
    cloques = models.BooleanField(default=False)
    poussiere = models.BooleanField(default=False)
    encrassement = models.BooleanField(default=False)
    trous_d_envol = models.BooleanField(default=False)
    moisissures = models.BooleanField(default=False)
    infestation_active = models.BooleanField(default=False)


#class linked to SupportPeintureSurBois (to complete)
class DeformationSupportPeintureSurBois(models.Model):
    localisees = models.BooleanField(default=False)
    generales = models.BooleanField(default=False)
    poches = models.BooleanField(default=False)
    en_drapeau = models.BooleanField(default=False)
    plis = models.BooleanField(default=False)
    plis_d_angles = models.BooleanField(default=False)
    retraits = models.BooleanField(default=False)
    effets_de_vagues = models.BooleanField(default=False)
    scrupules = models.BooleanField(default=False)
    enfoncement_par_la_face = models.BooleanField(default=False)
    enfoncement_par_le_revers = models.BooleanField(default=False)


#class linked to PeintureSurBois
class SupportPeintureSurBois(models.Model):
    constitution = models.ForeignKey(ConstitutionSupportPeintureSurBois, on_delete=CASCADE, null=True)
    tension = models.ForeignKey(TensionSupportPeintureSurBois, on_delete=CASCADE, null=True)
    alterations = models.ForeignKey(AlterationsSupportPeintureSurBois, on_delete=CASCADE, null=True)
    deformations = models.ForeignKey(DeformationSupportPeintureSurBois, on_delete=CASCADE, null=True)    


#class linked to PeintureSurBois
class PhotoSignificativeSupportPeintureSurBois(PhotoSignificative):
    photo = models.ImageField(null=True, upload_to='photos_significatives_support')
    photo_avec_emplacement = models.ImageField(null=True, upload_to='photos_significatives_support')
    support = models.ForeignKey(SupportPeintureSurBois, on_delete=CASCADE, null=True)


#class extends Peinture
class PeintureSurBois(OeuvreDArt):
    photo_face = models.ImageField(upload_to='photos_identification_peinture_sur_bois', null=True)
    photo_revers = models.ImageField(upload_to='photos_identification_peinture_sur_bois', null=True)






#class linked to ArtGraphique
class MateriauxSupportArtGraphique(models.Model):
    revers_inaccessible = models.BooleanField(default=True)
    carton = models.BooleanField(default=False)
    velin = models.BooleanField(default=False)
    papyrus = models.BooleanField(default=False)
    ivoire = models.BooleanField(default=False)
    cuir = models.BooleanField(default=False)
    parchemin = models.BooleanField(default=False)
    soie = models.BooleanField(default=False)
    toile = models.BooleanField(default=False)
    papier = models.BooleanField(default=False)
    papier_machine = models.BooleanField(default=False)
    papier_main = models.BooleanField(default=False)
    papier_oriental = models.BooleanField(default=False)
    papier_occidental = models.BooleanField(default=False)
    papier_velin = models.BooleanField(default=False)
    papier_base_fibre_vegetale = models.BooleanField(default=False)
    papier_a_base_de_bois = models.BooleanField(default=False)
    filigrane = models.BooleanField(default=False)
    papier_verge = models.BooleanField(default=False)
    intervalles_des_vergeures = models.IntegerField(default=0, null=True)
    intervalles_de_pontuseaux = models.IntegerField(default=0, null=True)


#class linked to ArtGraphique
class TechniqueDesseinArtGraphique(models.Model):
    pointe_de_metal = models.BooleanField(default=False)
    stylet_ou_pierre_noire = models.BooleanField(default=False)
    fusain_crayon_comte = models.BooleanField(default=False)
    graphite = models.BooleanField(default=False)
    sanguine = models.BooleanField(default=False)    
    craie_blanche = models.BooleanField(default=False)
    crayon_de_couleurs = models.BooleanField(default=False)
    rehauts_blancs = models.BooleanField(default=False)
    pastel = models.BooleanField(default=False)
    encre_au_carbone = models.BooleanField(default=False)
    encre_brune = models.BooleanField(default=False)
    encre_metallogallique = models.BooleanField(default=False)
    peinture_a_l_huile_et_essence_terebentine_sur_papier = models.BooleanField(default=False)
    encre_de_couleur = models.BooleanField(default=False)
    tempera = models.BooleanField(default=False)
    gouache = models.BooleanField(default=False)
    aquarelle = models.BooleanField(default=False)
    autre = models.BooleanField(default=False)
    autre_technique_dessin = models.CharField(max_length=255)


#class linked to ArtGraphique
class TechniqueEstampeArtGraphique(models.Model):
    burin = models.BooleanField(default=False)
    xylographie = models.BooleanField(default=False)
    taille_d_epargne = models.BooleanField(default=False)
    eau_forte = models.BooleanField(default=False)
    aquatinte = models.BooleanField(default=False)
    taille_douce = models.BooleanField(default=False)
    lithographie = models.BooleanField(default=False)
    pointe_seche = models.BooleanField(default=False)
    maniere_noire = models.BooleanField(default=False)
    maniere_au_crayon = models.BooleanField(default=False)
    procede_au_pochoir = models.BooleanField(default=False)
    serigraphie = models.BooleanField(default=False)
    technique_combinees = models.BooleanField(default=False)
    technique_combinees_technique_estampe = models.CharField(max_length=255)


#class linked to ArtGraphique
class AutreTechniqueGraphiqueArtGraphique(models.Model):
    encre_a_imprimer_a_l_eau = models.BooleanField(default=False)
    encre_a_imprimer_a_l_huile = models.BooleanField(default=False)


#class linked to ArtGraphique
class TechniqueReproductionArtGraphique(models.Model):
    heliogravure = models.BooleanField(default=False)
    quadrichromie_offset = models.BooleanField(default=False)


#class linked to ArtGraphique
class SupportArtGraphique(models.Model):
    amincissement = models.BooleanField(default=False)
    fragilite = models.BooleanField(default=False)
    trous_de_punaises = models.BooleanField(default=False)
    anciennes_restauration = models.BooleanField(default=False)
    gondrolement = models.BooleanField(default=False)
    trace_de_colle = models.BooleanField(default=False)
    brulure = models.BooleanField(default=False)
    pliure = models.BooleanField(default=False)
    residus_d_adhesif = models.BooleanField(default=False)
    cassant = models.BooleanField(default=False)
    piqure = models.BooleanField(default=False)
    rouille = models.BooleanField(default=False)
    coupure = models.BooleanField(default=False)
    papier_froisse = models.BooleanField(default=False)
    taches_claires = models.BooleanField(default=False)
    dechirure = models.BooleanField(default=False)
    lacune = models.BooleanField(default=False)
    taches_diverses = models.BooleanField(default=False)
    decoloration = models.BooleanField(default=False)
    rigidite = models.BooleanField(default=False)
    zone_brune = models.BooleanField(default=False)
    deformations = models.BooleanField(default=False)
    peluches = models.BooleanField(default=False)
    poussieres = models.BooleanField(default=False)
    depot_matiere_formant_tache = models.BooleanField(default=False)
    perforation = models.BooleanField(default=False)
    insectes = models.BooleanField(default=False)
    dislocation_des_fibres_cellulose = models.BooleanField(default=False)
    jaunissement_generalise = models.BooleanField(default=False)
    trou_d_insectes = models.BooleanField(default=False)
    doublage_defectueux = models.BooleanField(default=False)
    jaunissement_localise = models.BooleanField(default=False)
    micro_organismes = models.BooleanField(default=False)
    epidermages = models.BooleanField(default=False)
    impregnation_d_un_produit_gras = models.BooleanField(default=False)
    moisissures_ou_bacteries = models.BooleanField(default=False)


class PhotoSignificativeSupportArtGraphique(PhotoSignificative):
    photo = models.ImageField(null=True, upload_to='photos_significatives_support')
    photo_avec_emplacement = models.ImageField(null=True, upload_to='photos_significatives_support')
    support = models.ForeignKey(SupportArtGraphique, on_delete=CASCADE, null=True)


#class linked to ArtGraphique
class TechniqueArtGraphique(models.Model):
    affaiblissement_des_traits = models.BooleanField(default=False)
    craquelure = models.BooleanField(default=False)
    fixatif_altere = models.BooleanField(default=False)
    anciennes_restaurations = models.BooleanField(default=False)
    decapage = models.BooleanField(default=False)
    jaunissement = models.BooleanField(default=False)
    corrosion_de_l_encre = models.BooleanField(default=False)
    encaillage_des_gouaches = models.BooleanField(default=False)
    vernis_altere = models.BooleanField(default=False)
    couleurs_qui_ont_fuse = models.BooleanField(default=False)
    manques = models.BooleanField(default=False)
    trait_degrade = models.BooleanField(default=False)
    couleurs_eclaircies = models.BooleanField(default=False)
    pulverulence = models.BooleanField(default=False)
    teintes_palies = models.BooleanField(default=False)
    teintes_transformees = models.BooleanField(default=False)


#class linked to ArtGraphique
class MontageArtGraphique(models.Model):
    carton_au_verso = models.BooleanField(default=False)
    colle_en_plein = models.BooleanField(default=False)
    anciennes_restauration = models.BooleanField(default=False)
    fenetre_au_recto = models.BooleanField(default=False)
    colle_par_les_bords = models.BooleanField(default=False)
    defaut_d_adherance = models.BooleanField(default=False)
    passepartout = models.BooleanField(default=False)
    fausse_marge = models.BooleanField(default=False)
    charniere_en_japon = models.BooleanField(default=False)
    

#class extends OeuvreDArt
class ArtGraphique(OeuvreDArt):
    photo_face = models.ImageField(upload_to='photos_identification_art_graphique/', null=True)
    photo_revers = models.ImageField(upload_to='photos_identification_art_graphique/', null=True)







##
#class Constat
##
class Constat(models.Model):
    num_caisse = models.IntegerField(null=True)
    ville = models.CharField(max_length=255, null=True)
    nom_transporteur = models.CharField(max_length=255, null=True)
    autres_ouvres_dans_la_meme_caisse= models.BooleanField(default=False)
    remarque = models.TextField(null=True)
    photos_numeriques_realisees_au_depart = models.BooleanField(null=False, default=False)
    original_constat_laisse_a_l_emprunteur = models.BooleanField(null=False)
    copie_constat_laisse_a_l_emprunteur = models.BooleanField(null=False)
    date = models.DateField(auto_now_add=True)
    auteur = models.CharField(max_length=255, null=True)
    signature_auteur = models.ImageField(null=True)
    nom_convoyeur = models.CharField(max_length=255, null=True)
    signature_convoyeur = models.ImageField(null=True) #not implemented for now      
    absence_cadre = models.BooleanField(null=True)

    lieu_conservation = models.CharField(max_length=255, null=True)
    emplacement = models.CharField(max_length=255, null=True)    

    cadre = models.ForeignKey(CadreOeuvre, on_delete=CASCADE, null=True)
    emballage = models.ForeignKey(EmballageOeuvre, on_delete=CASCADE, null=True)

    class Meta():
        abstract = True


class ConstatPeinture(Constat):
    couche_picturale = models.ForeignKey(CouchePicturalePeinture, on_delete = CASCADE, null=True)

    class Meta():
        abstract = True


class ConstatPeintureSurToile(ConstatPeinture):    
    chassis = models.ForeignKey(ChassisPeintureSurToile, on_delete=CASCADE, null=True)
    support_peinture_sur_toile = models.ForeignKey(SupportPeintureSurToile, on_delete=CASCADE, null=True)

    peinture_sur_toile = models.ForeignKey(PeintureSurToile, on_delete=CASCADE, null=True)


class ConstatPeintureSurBois(ConstatPeinture):    
    support_peinture_sur_bois = models.ForeignKey(SupportPeintureSurBois, on_delete=CASCADE, null=True)

    peinture_sur_bois = models.ForeignKey(PeintureSurBois, on_delete=CASCADE, null=True)


class ConstatArtGraphique(Constat):
    materiaux_support = models.ForeignKey(MateriauxSupportArtGraphique, on_delete=CASCADE, null=True)
    technique_dessein = models.ForeignKey(TechniqueDesseinArtGraphique, on_delete = CASCADE, null=True)
    technique_estampe = models.ForeignKey(TechniqueEstampeArtGraphique, on_delete = CASCADE, null=True)
    autre_technique_graphique = models.ForeignKey(AutreTechniqueGraphiqueArtGraphique, on_delete=CASCADE, null=True)
    technique_reproduction = models.ForeignKey(TechniqueReproductionArtGraphique, on_delete=CASCADE, null=True)
    support = models.ForeignKey(SupportArtGraphique, on_delete = CASCADE, null=True)    
    technique = models.ForeignKey(TechniqueArtGraphique, on_delete = CASCADE, null=True)    
    montage = models.ForeignKey(MontageArtGraphique, on_delete = CASCADE, null=True)

    art_graphique = models.ForeignKey(ArtGraphique, on_delete=CASCADE, null=True)
