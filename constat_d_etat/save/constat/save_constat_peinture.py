from constat_d_etat.models import *
from .save_constat import *

class SaveConstatPeinture(SaveConstat):

    def __init__(self, data_to_save, art_work_id):
        SaveConstat.__init__(self, data_to_save, art_work_id)


    def save_alterations_optiques(self,):

        alterations_optiques = AlterationsOptiquesCouchePicturalePeinture()
        alterations_optiques.usures = self.data_to_save['peinture_alterations_optiques_usures']
        alterations_optiques.griffures = self.data_to_save['peinture_alterations_optiques_griffures']
        alterations_optiques.impression_de_texture = self.data_to_save['peinture_alterations_optiques_impression_texture']
        alterations_optiques.marques_de_chassis = self.data_to_save['peinture_alterations_optiques_marques_chassis']
        alterations_optiques.trous_d_envol = self.data_to_save['peinture_alterations_optiques_trous_envol']
        alterations_optiques.dejections_d_insectes = self.data_to_save['peinture_alterations_optiques_dejections_insectes']
        alterations_optiques.transparences_accrues = self.data_to_save['peinture_alterations_optiques_transparences_accrues']
        alterations_optiques.repeints_alteres = self.data_to_save['peinture_alterations_optiques_repeints_alteres']
        alterations_optiques.mastics_debordants = self.data_to_save['peinture_alterations_optiques_matics_debordants']
        alterations_optiques.traces_de_dorure = self.data_to_save['peinture_alterations_optiques_traces_de_dorure']
        alterations_optiques.projections = self.data_to_save['peinture_alterations_optiques_projections']
        alterations_optiques.ecrasement_de_matiere = self.data_to_save['peinture_alterations_optiques_ecrasement_de_matiere']
        alterations_optiques.save()

        return alterations_optiques


    def save_vernis(self,):

        vernis = VernisCouchePicturalePeinture()
        vernis.homogeneite_satisfaisante = self.data_to_save['peinture_vernis_homogeneite_satisfaisante']
        vernis.jaunissement = self.data_to_save['peinture_vernis_jaunissement']
        vernis.encrassement = self.data_to_save['peinture_vernis_encrassement']
        vernis.chancis = self.data_to_save['peinture_vernis_chancis']
        vernis.coulures = self.data_to_save['peinture_vernis_coulures']
        vernis.inegalite_de_surface = self.data_to_save['peinture_vernis_inegalite_de_surface']
        vernis.lacunes = self.data_to_save['peinture_vernis_lacunes']
        vernis.soulevements = self.data_to_save['peinture_vernis_soulevements']
        vernis.chevauchement_d_ecaillement = self.data_to_save['peinture_vernis_chevauchement_ecaillement']
        vernis.save()

        return vernis


    def save_adhesion(self,):

        adhesion = AdhesionCouchePicturalePeinture()
        adhesion.satisfaisante = self.data_to_save['peinture_adhesion_satisfaisante']
        adhesion.deplacage = self.data_to_save['peinture_adhesion_deplacage']
        adhesion.epidermage = self.data_to_save['peinture_adhesion_epidermage']
        adhesion.cloque = self.data_to_save['peinture_adhesion_cloque']
        adhesion.deplacement_d_ecailles = self.data_to_save['peinture_adhesion_deplacement_ecailles']
        adhesion.zones_pulverilentes = self.data_to_save['peinture_adhesion_zones_pulverilentes']
        adhesion.transposition = self.data_to_save['peinture_adhesion_transposition']
        adhesion.brulures = self.data_to_save['peinture_adhesion_brulures']
        adhesion.lacunes = self.data_to_save['peinture_adhesion_lacunes']
        adhesion.soulevements = self.data_to_save['peinture_adhesion_soulevement']
        adhesion.chevauchement_d_ecailles = self.data_to_save['peinture_adhesion_chevauchement_ecailles']
        adhesion.save()

        return adhesion


    def save_craquelure_prematuree(self,):

        craquelure_prematuree = CraqueluresPrematureesCouchePicturalePeinture()
        craquelure_prematuree.rides = self.data_to_save['peinture_craquelure_prematuree_rides']
        craquelure_prematuree.gercures = self.data_to_save['peinture_craquelure_prematuree_gercures']
        craquelure_prematuree.crevasses = self.data_to_save['peinture_craquelure_prematuree_crevasses']
        craquelure_prematuree.craquelures_fermees = self.data_to_save['peinture_craquelure_prematuree_craquelures_fermees']
        craquelure_prematuree.save()

        return craquelure_prematuree


    def save_craquelure_age(self,):

        craquelure_age = CraqueluresDAgeCouchePicturalePeinture()
        craquelure_age.reseau_generalise_fin = self.data_to_save['peinture_craquelure_age_reseau_generalise_fin']
        craquelure_age.reseau_generalise_prononce = self.data_to_save['peinture_craquelure_age_reseau_generalise_prononce']
        craquelure_age.limite_a_une_zone = self.data_to_save['peinture_craquelure_age_limites_a_une_zone']
        craquelure_age.circulaire = self.data_to_save['peinture_craquelure_age_circulaire']
        craquelure_age.diagonales = self.data_to_save['peinture_craquelure_age_diagonales']
        craquelure_age.horizontale = self.data_to_save['peinture_craquelure_age_horizontales_verticales']
        craquelure_age.en_echelle = self.data_to_save['peinture_craquelure_age_en_echelle']
        craquelure_age.en_escargot = self.data_to_save['peinture_craquelure_age_en_escargot']
        craquelure_age.faiencage = self.data_to_save['peinture_craquelure_age_faiencage']
        craquelure_age.pavimenteuses = self.data_to_save['peinture_craquelure_age_pavimenteuses']
        craquelure_age.save()

        return craquelure_age


    def save_couche_picturale(self,):

        couche_picturale = CouchePicturalePeinture()
        couche_picturale.alterations_optiques = self.save_alterations_optiques()
        couche_picturale.vernis = self.save_vernis()
        couche_picturale.adhesion = self.save_adhesion()
        couche_picturale.craquelure_premature = self.save_craquelure_prematuree()
        couche_picturale.craquelure_d_age = self.save_craquelure_age()
        couche_picturale.save()

        return couche_picturale
        