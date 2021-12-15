from constat_d_etat.models import *
from .save_constat import *
from .save_constat_peinture import *

class SaveConstatPeintureSurToile(SaveConstatPeinture):

    def __init__(self, data_to_save, art_work_id):
        SaveConstatPeinture.__init__(self, data_to_save, art_work_id)


    def save_caracteristiques_support(self,):

        caracteristiques_support = CaracteristiquesSupportPeintureSurToile()
        caracteristiques_support.bon_etat = self.data_to_save['peinture_sur_toile_support_caracteristiques_bon_etat']
        caracteristiques_support.mauvais_etat = self.data_to_save['peinture_sur_toile_support_caracteristiques_mauvais_etat']
        caracteristiques_support.restaure = self.data_to_save['peinture_sur_toile_support_caracteristiques_restaure']
        caracteristiques_support.fendu = self.data_to_save['peinture_sur_toile_support_caracteristiques_fendu']
        caracteristiques_support.ouvert = self.data_to_save['peinture_sur_toile_support_caracteristiques_ouvert']
        caracteristiques_support.vermoulu = self.data_to_save['peinture_sur_toile_support_caracteristiques_vermoulu']
        caracteristiques_support.inscriptions = self.data_to_save['peinture_sur_toile_support_caracteristiques_inscriptions']
        caracteristiques_support.etiquettes = self.data_to_save['peinture_sur_toile_support_caracteristiques_etiquettes']
        caracteristiques_support.marques_ou_cachets = self.data_to_save['peinture_sur_toile_support_caracteristiques_marques_cachets']
        caracteristiques_support.caisson_climatique = self.data_to_save['peinture_sur_toile_support_caracteristiques_caisson_climatique']
        
        caracteristiques_support.protection_arriere = self.data_to_save['peinture_sur_toile_support_caracteristiques_protection_arriere']
        if self.data_to_save['peinture_sur_toile_support_caracteristiques_protection_arriere']:
            caracteristiques_support.nature_protection_arriere = self.data_to_save['peinture_sur_toile_support_caracteristiques_nature_protection_arriere']
        
        caracteristiques_support.trous_de_pitons_dans_les_planches = self.data_to_save['peinture_sur_toile_support_caracteristiques_trous_de_pitons_dans_les_planches']
        if self.data_to_save['peinture_sur_toile_support_caracteristiques_trous_de_pitons_dans_les_planches']:
            caracteristiques_support.nombre_trous_de_pitons_dans_les_planches = self.data_to_save['peinture_sur_toile_support_caracteristiques_nombre_trous_de_pitons_dans_les_planches']
        
        caracteristiques_support.trous_de_pitons_dans_les_traverses = self.data_to_save['peinture_sur_toile_support_caracteristiques_trous_de_pitons_dans_les_traverses']
        if self.data_to_save['peinture_sur_toile_support_caracteristiques_trous_de_pitons_dans_les_traverses']:
            caracteristiques_support.nombre_trous_de_pitons_dans_les_traverses = self.data_to_save['peinture_sur_toile_support_caracteristiques_nombre_trous_de_pitons_dans_les_traverses']
        
        caracteristiques_support.chassis_cadre = self.data_to_save['peinture_sur_toile_support_caracteristiques_chassis_cadre']

        caracteristiques_support.poignees_fixees_au_revers = self.data_to_save['peinture_sur_toile_support_caracteristiques_poignees_fixees_au_revers']
        if self.data_to_save['peinture_sur_toile_support_caracteristiques_poignees_fixees_au_revers']:
            caracteristiques_support.nombre_poignees_fixees_au_revers = self.data_to_save['peinture_sur_toile_support_caracteristiques_nombre_poignees_fixees_au_revers']
            caracteristiques_support.nature_poignees_fixees_au_revers = self.data_to_save['peinture_sur_toile_support_caracteristiques_nature_poignees_fixees_au_revers']
        
        caracteristiques_support.save()

        return caracteristiques_support


    def save_essence_support(self,):

        essence_support = EssenceSupportPeintureSurToile()
        essence_support.chene = self.data_to_save['peinture_sur_toile_support_essence_chene']
        essence_support.resineux = self.data_to_save['peinture_sur_toile_support_essence_resineux']
        essence_support.peuplier = self.data_to_save['peinture_sur_toile_support_essence_peuplier']
        essence_support.acajou = self.data_to_save['peinture_sur_toile_support_essence_acajou']
        essence_support.autre = self.data_to_save['peinture_sur_toile_support_essence_autre']

        if self.data_to_save['peinture_sur_toile_support_essence_autre']:
            essence_support.essence_autre = self.data_to_save['peinture_sur_toile_support_essence_autre_essence']

        essence_support.save()

        return essence_support


    def save_fil_du_bois_support(self,):

        fil_du_bois = FilDuBoisSupportPeintureSurToile()
        fil_du_bois.horizontal = self.data_to_save['peinture_sur_toile_support_fil_du_bois_horizontal']
        fil_du_bois.vertical = self.data_to_save['peinture_sur_toile_support_fil_du_bois_vertical']
        fil_du_bois.regulier = self.data_to_save['peinture_sur_toile_support_fil_du_bois_regulier']
        fil_du_bois.irregulier = self.data_to_save['peinture_sur_toile_support_fil_du_bois_irregulier']

        fil_du_bois.save()

        return fil_du_bois


    def save_assemblage_support(self,):

        assemblage = AssemblageSupportPeintureSurToile()
        assemblage.plats_joints = self.data_to_save['peinture_sur_toile_support_assemblage_plats_joints']
        assemblage.rainures_ou_languettes = self.data_to_save['peinture_sur_toile_support_assemblage_rainures_languettes']
        assemblage.tenons_ou_mortaises = self.data_to_save['peinture_sur_toile_support_assemblage_tenons_mortaises']
        assemblage.queues_d_arondes = self.data_to_save['peinture_sur_toile_support_assemblage_queues_arrondes']
        assemblage.correct = self.data_to_save['peinture_sur_toile_support_assemblage_correct']
        assemblage.faible = self.data_to_save['peinture_sur_toile_support_assemblage_faible']
        assemblage.disjoint = self.data_to_save['peinture_sur_toile_support_assemblage_disjoint']
        assemblage.parquetage_mobile = self.data_to_save['peinture_sur_toile_support_assemblage_parquettage_mobile']
        assemblage.parquetage_bloque = self.data_to_save['peinture_sur_toile_support_assemblage_parquettage_bloque']
        assemblage.panneau_contraint = self.data_to_save['peinture_sur_toile_support_assemblage_panneau_contraint']
        assemblage.traverses_originales = self.data_to_save['peinture_sur_toile_support_assemblage_traverses_originales']

        if self.data_to_save['peinture_sur_toile_support_assemblage_traverses_originales']:
            assemblage.nombre_de_traverses = self.data_to_save['peinture_sur_toile_support_assemblage_nombre_de_traverses']
            assemblage.nombre_de_planches = self.data_to_save['peinture_sur_toile_support_assemblage_nombre_planches']

        assemblage.save()

        return assemblage


    def save_revers_support(self,):

        revers = ReversSupportPeintureSurToile()
        revers.lisse = self.data_to_save['peinture_sur_toile_support_revers_lisse']
        revers.brut = self.data_to_save['peinture_sur_toile_support_revers_brut']
        revers.enduit = self.data_to_save['peinture_sur_toile_support_revers_enduit']

        revers.save()

        return revers


    def save_tranche_support(self,):
        
        tranche = TrancheSupportPeintureSurToile()
        tranche.invisible = self.data_to_save['peinture_sur_toile_support_tranche_invisible']
        tranche.visible = self.data_to_save['peinture_sur_toile_support_tranche_visible']
        tranche.etat = self.data_to_save['peinture_sur_toile_support_tranche_etat']

        tranche.save()

        return tranche


    def save_alterations_support(self,):

        alterations = AlterationsSupportPeintureSurToile()
        alterations.percements = self.data_to_save['peinture_sur_toile_support_alterations_percements']
        alterations.eraflures = self.data_to_save['peinture_sur_toile_support_alterations_eraflures']
        alterations.cloques = self.data_to_save['peinture_sur_toile_support_alterations_cloques']
        alterations.coulures = self.data_to_save['peinture_sur_toile_support_alterations_coulures']
        alterations.moisissures = self.data_to_save['peinture_sur_toile_support_alterations_moisissures']
        alterations.poussiere = self.data_to_save['peinture_sur_toile_support_alterations_poussiere']
        alterations.encrassement = self.data_to_save['peinture_sur_toile_support_alterations_encrassement']
        alterations.aureoles = self.data_to_save['peinture_sur_toile_support_alterations_aureoles']
        alterations.effritement = self.data_to_save['peinture_sur_toile_support_alterations_effritement']
        alterations.fendillement = self.data_to_save['peinture_sur_toile_support_alterations_fendillement']
        alterations.trous_d_envol = self.data_to_save['peinture_sur_toile_support_alterations_trous_envol']
        alterations.galerie_d_insectes = self.data_to_save['peinture_sur_toile_support_alterations_galeries_insectes']

        alterations.save()

        return alterations


    def save_deformations_support(self,):

        deformations = DeformationsSupportPeintureSurToile()
        deformations.localisees = self.data_to_save['peinture_sur_toile_support_deformations_localisees']
        deformations.generalisees = self.data_to_save['peinture_sur_toile_support_deformations_generalisees']
        deformations.panneau_voile = self.data_to_save['peinture_sur_toile_support_deformations_panneau_voile']
        deformations.enfoncement_par_la_face = self.data_to_save['peinture_sur_toile_support_deformations_enfoncement_par_la_face']
        deformations.enfoncement_au_revers = self.data_to_save['peinture_sur_toile_support_deformations_enfoncement_au_revers']
        deformations.panneau_aminci = self.data_to_save['peinture_sur_toile_support_deformations_panneau_aminci']

        deformations.save()

        return deformations


    def save_support(self,):

        support = SupportPeintureSurToile()
        support.revers_inaccessible = self.data_to_save['peinture_sur_toile_support_caracteristiques_revers_inaccessible']
        support.caracteristiques = self.save_caracteristiques_support()
        support.essence = self.save_essence_support()
        support.fil_du_bois = self.save_fil_du_bois_support()
        support.assemblage = self.save_assemblage_support()
        support.revers = self.save_revers_support()
        support.tranche = self.save_tranche_support()
        support.alterations = self.save_alterations_support()
        support.deformations = self.save_deformations_support()

        support.save()

        return support




    def save_caracteristiques_chassis(self,):

        caracteristiques = CaracteristiquesChassisPeintureSurToile()
        caracteristiques.neuf = self.data_to_save['peinture_sur_toile_chassis_caracteristiques_neuf']
        caracteristiques.bon_etat = self.data_to_save['peinture_sur_toile_chassis_caracteristiques_bon_etat']
        caracteristiques.mauvais_etat = self.data_to_save['peinture_sur_toile_chassis_caracteristiques_mauvais_etat']
        caracteristiques.d_origine = self.data_to_save['peinture_sur_toile_chassis_caracteristiques_d_origine']
        caracteristiques.chanfreine = self.data_to_save['peinture_sur_toile_chassis_caracteristiques_chanfreine']
        caracteristiques.renforts_d_angles = self.data_to_save['peinture_sur_toile_chassis_caracteristiques_renforts_d_angles']
        caracteristiques.fendu = self.data_to_save['peinture_sur_toile_chassis_caracteristiques_fendu']
        caracteristiques.ouvert = self.data_to_save['peinture_sur_toile_chassis_caracteristiques_ouvert']
        caracteristiques.vermoulu = self.data_to_save['peinture_sur_toile_chassis_caracteristiques_vermoulu']

        caracteristiques.traverses_horizontales = self.data_to_save['peinture_sur_toile_chassis_caracteristiques_traverses_horizontales']
        if self.data_to_save['peinture_sur_toile_chassis_caracteristiques_traverses_horizontales']:
            caracteristiques.nombre_traverses_horizontales = self.data_to_save['peinture_sur_toile_chassis_caracteristiques_nombre_traverses_horizontales']

        caracteristiques.traverses_verticales = self.data_to_save['peinture_sur_toile_chassis_caracteristiques_traverses_verticales']
        if self.data_to_save['peinture_sur_toile_chassis_caracteristiques_traverses_verticales']:
            caracteristiques.nombre_traverses_verticales = self.data_to_save['peinture_sur_toile_chassis_caracteristiques_nombre_traverses_verticales']

        caracteristiques.trous_de_pitons = self.data_to_save['peinture_sur_toile_chassis_caracteristiques_trous_de_pitons']
        caracteristiques.etiquettes = self.data_to_save['peinture_sur_toile_chassis_caracteristiques_etiquettes']
        caracteristiques.marques = self.data_to_save['peinture_sur_toile_chassis_caracteristiques_marques']
        caracteristiques.caisson_climatique = self.data_to_save['peinture_sur_toile_chassis_caracteristiques_caisson_climatique']

        caracteristiques.protection_arriere = self.data_to_save['peinture_sur_toile_chassis_caracteristiques_protection_arriere']
        if self.data_to_save['peinture_sur_toile_chassis_caracteristiques_protection_arriere']:
            caracteristiques.nature_protection_arriere = self.data_to_save['peinture_sur_toile_chassis_caracteristiques_nature_protection_arriere']

        caracteristiques.poignees_sur_montants = self.data_to_save['peinture_sur_toile_chassis_caracteristiques_poignees_sur_montants']
        if self.data_to_save['peinture_sur_toile_chassis_caracteristiques_poignees_sur_montants']:
            caracteristiques.nature_poignees_sur_montants = self.data_to_save['peinture_sur_toile_chassis_caracteristiques_nature_poignees_sur_montants']
            caracteristiques.nombre_poignees_sur_montants = self.data_to_save['peinture_sur_toile_chassis_caracteristiques_nombre_poignees_sur_montants']

        caracteristiques.save()

        return caracteristiques


    def save_assemblage_chassis(self,):

        assemblage = AssemblageChassisPeintureSurToile()
        assemblage.correct = self.data_to_save['peinture_sur_toile_chassis_assemblage_correct']
        assemblage.faible = self.data_to_save['peinture_sur_toile_chassis_assemblage_faible']
        assemblage.disjoint = self.data_to_save['peinture_sur_toile_chassis_assemblage_disjoint']

        assemblage.save()

        return assemblage


    def save_cles_chassis(self,):

        cles = ClesChassisPeintureSurToile()
        cles.chassis_fixe = self.data_to_save['peinture_sur_toile_chassis_cles_chassis_fixe']

        cles.chassis_a_cle = self.data_to_save['peinture_sur_toile_chassis_cles_chassis_a_cles']
        if self.data_to_save['peinture_sur_toile_chassis_cles_chassis_a_cles']:
            cles.nombre_de_cles_presentes_chassis_a_cle = self.data_to_save['peinture_sur_toile_chassis_cles_nombre_cles_presentes']
        
        cles.manquantes = self.data_to_save['peinture_sur_toile_chassis_cles_manquantes']
        if self.data_to_save['peinture_sur_toile_chassis_cles_manquantes']:
            cles.nombre_manquantes = self.data_to_save['peinture_sur_toile_chassis_cles_nombre_manquantes']

        cles.cassees = self.data_to_save['peinture_sur_toile_chassis_cles_cassees']
        if self.data_to_save['peinture_sur_toile_chassis_cles_cassees']:
            cles.nombre_cassees = self.data_to_save['peinture_sur_toile_chassis_cles_nombre_cassees']

        cles.vermoulues = self.data_to_save['peinture_sur_toile_chassis_cles_vermoules']
        if self.data_to_save['peinture_sur_toile_chassis_cles_vermoules']:
            cles.nombre_vermoulues = self.data_to_save['peinture_sur_toile_chassis_cles_nombre_vermoules']

        cles.attachees = self.data_to_save['peinture_sur_toile_chassis_cles_attachees']
        if self.data_to_save['peinture_sur_toile_chassis_cles_attachees']:
            cles.nombre_attachees = self.data_to_save['peinture_sur_toile_chassis_cles_nombre_attachees']

        cles.save()

        return cles


    def save_tranche_chassis(self,):

        tranche = TrancheChassisPeintureSurToile()
        tranche.invisible = self.data_to_save['peinture_sur_toile_chassis_tranche_invisible']
        tranche.papier_de_bordage = self.data_to_save['peinture_sur_toile_chassis_tranche_papier_de_bordage']
        tranche.etat_papier_de_bordage = self.data_to_save['peinture_sur_toile_chassis_tranche_etat']

        tranche.save()

        return tranche


    def save_semence_chassis(self,):

        semence = SemencesChassisPeintureSurToile()
        semence.d_origine = self.data_to_save['peinture_sur_toile_chassis_semence_d_origine']
        semence.ajoutees = self.data_to_save['peinture_sur_toile_chassis_semence_ajoutees']
        semence.agrafes = self.data_to_save['peinture_sur_toile_chassis_semence_agrafes']
        semence.guirlande_de_tension = self.data_to_save['peinture_sur_toile_chassis_semence_guirlande_de_tension']
        semence.corrosion = self.data_to_save['peinture_sur_toile_chassis_semence_corrosion']
        semence.manques = self.data_to_save['peinture_sur_toile_chassis_semence_manques']

        semence.save()

        return semence


    def save_chassis(self,):

        chassis = ChassisPeintureSurToile()
        chassis.revers_inaccessible = self.data_to_save['peinture_sur_toile_chassis_caracteristiques_revers_inaccessible']
        chassis.caracteristiquesChassis = self.save_caracteristiques_chassis()
        chassis.cles = self.save_cles_chassis()
        chassis.tranche = self.save_tranche_chassis()
        chassis.semences = self.save_semence_chassis()
        chassis.assemblage = self.save_assemblage_chassis()

        chassis.save()

        return chassis




    def save_constat_peinture_sur_toile(self,):

        constat = ConstatPeintureSurToile()
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
        
        constat.couche_picturale = self.save_couche_picturale()
        constat.emballage = self.save_emballage()
        constat.chassis = self.save_chassis()
        constat.support_peinture_sur_toile = self.save_support()

        cadre = self.save_cadre()

        if cadre != None:
            constat.cadre = cadre

        constat.peinture_sur_toile = PeintureSurToile.objects.get(id=self.art_work_id)

        constat.save()

        return constat