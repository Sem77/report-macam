from constat_d_etat.models import *
from .save_constat import *
from .save_constat_peinture import *

class SaveConstatPeintureSurBois(SaveConstatPeinture):

    def __init__(self, data_to_save, art_work_id):
        SaveConstatPeinture.__init__(self, data_to_save, art_work_id)


    def save_constitution_support(self):

        constitution = ConstitutionSupportPeintureSurBois()
        constitution.armure_toile = self.data_to_save['peinture_sur_bois_constitution_armure_toile']
        constitution.armure_sergee = self.data_to_save['peinture_sur_bois_constitution_armure_sergee']
        constitution.armure_satin = self.data_to_save['peinture_sur_bois_constitution_armure_satin']
        constitution.papier_maroufle = self.data_to_save['peinture_sur_bois_constitution_papier_maroufle']
        constitution.tissage_de_la_toile = self.data_to_save['peinture_sur_bois_constitution_tissage_toile']
        constitution.lache = self.data_to_save['peinture_sur_bois_constitution_lache']
        constitution.moyen = self.data_to_save['peinture_sur_bois_constitution_moyen']
        constitution.serre = self.data_to_save['peinture_sur_bois_constitution_serre']
        constitution.toile_originale = self.data_to_save['peinture_sur_bois_constitution_toile_originale']
        constitution.rentoilage = self.data_to_save['peinture_sur_bois_constitution_rentoilage']
        constitution.doublage = self.data_to_save['peinture_sur_bois_constitution_doublage']
        constitution.doublage_aveugle = self.data_to_save['peinture_sur_bois_constitution_doublage_aveugle']
        constitution.agrandissement = self.data_to_save['peinture_sur_bois_constitution_agrandissement']
        constitution.coutures = self.data_to_save['peinture_sur_bois_constitution_coutures']
        constitution.noeud_de_toile = self.data_to_save['peinture_sur_bois_constitution_noeuds_toile']
        constitution.bande_de_tension = self.data_to_save['peinture_sur_bois_constitution_bande_tension']
        constitution.transposition = self.data_to_save['peinture_sur_bois_constitution_transposition']
        constitution.marouflage = self.data_to_save['peinture_sur_bois_constitution_marouflage']

        constitution.pieces = self.data_to_save['peinture_sur_bois_constitution_pieces']
        if self.data_to_save['peinture_sur_bois_constitution_pieces']:
            constitution.nombre_pieces = self.data_to_save['peinture_sur_bois_constitution_nombre_pieces']

        constitution.inscriptions = self.data_to_save['peinture_sur_bois_constitution_inscriptions']
        constitution.etiquettes = self.data_to_save['peinture_sur_bois_constitution_etiquettes']
        constitution.marques_ou_cachets = self.data_to_save['peinture_sur_bois_constitution_marques_cachets']

        constitution.save()

        return constitution


    def save_tension_support(self,):

        tension = TensionSupportPeintureSurBois()
        tension.tension_correcte = self.data_to_save['peinture_sur_bois_tension_tension_correcte']
        tension.toile_tres_lache = self.data_to_save['peinture_sur_bois_tension_toile_tres_lache']
        tension.toile_lache = self.data_to_save['peinture_sur_bois_tension_toile_lache']
        tension.toile_trop_tendue = self.data_to_save['peinture_sur_bois_tension_toile_trop_tendue']

        tension.save()

        return tension


    def save_alterations_support(self,):

        alterations = AlterationsSupportPeintureSurBois()
        alterations.toile_cuite = self.data_to_save['peinture_sur_bois_alterations_toile_cuite']
        alterations.toile_impregnee = self.data_to_save['peinture_sur_bois_alterations_toile_impregnee']
        alterations.aureoles = self.data_to_save['peinture_sur_bois_alterations_aureoles']
        alterations.coulures = self.data_to_save['peinture_sur_bois_alterations_coulures']
        alterations.dechirures_simples = self.data_to_save['peinture_sur_bois_alterations_dechirures_simples']
        alterations.dechirures_complexes = self.data_to_save['peinture_sur_bois_alterations_dechirures_complexes']
        alterations.coupures = self.data_to_save['peinture_sur_bois_alterations_coupure']
        alterations.lacerations = self.data_to_save['peinture_sur_bois_alterations_lacerations']
        alterations.percement = self.data_to_save['peinture_sur_bois_alterations_percement']
        alterations.eraflures = self.data_to_save['peinture_sur_bois_alterations_eraflures']
        alterations.cloques = self.data_to_save['peinture_sur_bois_alterations_cloques']
        alterations.poussiere = self.data_to_save['peinture_sur_bois_alterations_poussiere']
        alterations.encrassement = self.data_to_save['peinture_sur_bois_alterations_encrassement']
        alterations.trous_d_envol = self.data_to_save['peinture_sur_bois_alterations_trous_envol']
        alterations.moisissures = self.data_to_save['peinture_sur_bois_alterations_moisissures']
        alterations.infestation_active = self.data_to_save['peinture_sur_bois_alterations_infestation_active']

        alterations.save()

        return alterations


    def save_deformations_support(self,):

        deformations = DeformationSupportPeintureSurBois()
        deformations.localisees = self.data_to_save['peinture_sur_bois_deformations_localisees']
        deformations.generales = self.data_to_save['peinture_sur_bois_deformations_generales']
        deformations.poches = self.data_to_save['peinture_sur_bois_deformations_poche']
        deformations.en_drapeau = self.data_to_save['peinture_sur_bois_deformations_en_drapeau']
        deformations.plis = self.data_to_save['peinture_sur_bois_deformations_plis']
        deformations.plis_d_angles = self.data_to_save['peinture_sur_bois_deformations_plis_angles']
        deformations.retraits = self.data_to_save['peinture_sur_bois_deformations_retraits']
        deformations.effets_de_vagues = self.data_to_save['peinture_sur_bois_deformations_effets_vagues']
        deformations.scrupules = self.data_to_save['peinture_sur_bois_deformations_scrupules']
        deformations.enfoncement_par_la_face = self.data_to_save['peinture_sur_bois_deformations_enfoncement_par_la_face']
        deformations.enfoncement_par_le_revers = self.data_to_save['peinture_sur_bois_deformations_enfoncement_par_le_revers']

        deformations.save()

        return deformations


    def save_support(self,):

        support = SupportPeintureSurBois()
        support.constitution = self.save_constitution_support()
        support.tension = self.save_tension_support()
        support.alterations = self.save_alterations_support()
        support.deformations = self.save_deformations_support()

        support.save()

        return support


    def save_constat_peinture_sur_bois(self,):

        constat = ConstatPeintureSurBois()
        constat.absence_cadre = self.data_to_save['absence_de_cadre']
        constat.num_caisse = self.data_to_save['constat_numero_caisse']
        constat.ville = self.data_to_save['ville']
        constat.nom_transporteur = self.data_to_save['constat_nom_transporteur']
        constat.autres_ouvres_dans_la_meme_caisse = self.data_to_save['constat_autres_oeuvres_meme_caisse']
        constat.remarque = self.data_to_save['constat_remarques_notes']
        constat.photos_numeriques_realisees_au_depart = self.data_to_save['constat_photos_numeriques_realisees_au_depart']
        constat.original_constat_laisse_a_l_emprunteur = self.data_to_save['constat_original_constat_laisse_emprunteur']
        constat.copie_constat_laisse_a_l_emprunteur = self.data_to_save['constat_copie_constat_laisse_emprunteur']
        #field date but we don't really need to implement it
        constat.auteur = self.data_to_save['constat_auteur_constat']
        if self.data_to_save['signature_auteur_constat'] != None:
            constat.signature_auteur = self.data_to_save['signature_auteur_constat']
        constat.nom_convoyeur = self.data_to_save['constat_nom_convoyeur']

        constat.lieu_conservation = self.data_to_save['lieu_de_conservation']
        constat.emplacement = self.data_to_save['emplacement_oeuvre']
        
        constat.emballage = self.save_emballage()
        constat.support_peinture_sur_bois = self.save_support()
        constat.couche_picturale = self.save_couche_picturale()

        cadre = self.save_cadre()

        if cadre != None:
            constat.cadre = cadre

        constat.peinture_sur_bois = PeintureSurBois.objects.get(id=self.art_work_id)

        constat.save()

        return constat