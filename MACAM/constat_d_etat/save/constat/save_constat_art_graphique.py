from constat_d_etat.models import *
from .save_constat import *

class SaveConstatArtGraphique(SaveConstat):

    def __init__(self, data_to_save, art_work_id):
        SaveConstat.__init__(self, data_to_save, art_work_id)

    
    def save_materiaux_support(self,):

        if self.data_to_save['art_graphique_materiaux_support_revers_inacessible']:
            return None

        materiaux_support = MateriauxSupportArtGraphique()
        materiaux_support.revers_inaccessible = self.data_to_save['art_graphique_materiaux_support_revers_inacessible']
        materiaux_support.carton = self.data_to_save['art_graphique_materiaux_support_carton']
        materiaux_support.velin = self.data_to_save['art_graphique_materiaux_support_velin']
        materiaux_support.papyrus = self.data_to_save['art_graphique_materiaux_support_papyrus']
        materiaux_support.ivoire = self.data_to_save['art_graphique_materiaux_support_ivoire']
        materiaux_support.cuir = self.data_to_save['art_graphique_materiaux_support_cuir']
        materiaux_support.parchemin = self.data_to_save['art_graphique_materiaux_support_parchemin']
        materiaux_support.soie = self.data_to_save['art_graphique_materiaux_support_soie']
        materiaux_support.toile = self.data_to_save['art_graphique_materiaux_support_toile']
        materiaux_support.papier = self.data_to_save['art_graphique_materiaux_support_papier']
        materiaux_support.papier_machine = self.data_to_save['art_graphique_materiaux_support_papier_machine']
        materiaux_support.papier_main = self.data_to_save['art_graphique_materiaux_support_papier_main']
        materiaux_support.papier_oriental = self.data_to_save['art_graphique_materiaux_support_papier_oriental']
        materiaux_support.papier_occidental = self.data_to_save['art_graphique_materiaux_support_papier_occidental']
        materiaux_support.papier_velin = self.data_to_save['art_graphique_materiaux_support_papier_velin']
        materiaux_support.papier_base_fibre_vegetale = self.data_to_save['art_graphique_materiaux_support_papier_base_fibre_vegetale']
        materiaux_support.papier_a_base_de_bois = self.data_to_save['art_graphique_materiaux_support_papier_a_base_de_bois']
        materiaux_support.filigrane = self.data_to_save['art_graphique_materiaux_support_filigrane']
        materiaux_support.papier_verge = self.data_to_save['art_graphique_materiaux_support_papier_verge']        
        

        try:
            materiaux_support.intervalles_des_vergeures = self.data_to_save['art_graphique_materiaux_support_nombre_intervalles_vergeures']
        except TypeError:
            pass

        try:
            materiaux_support.intervalles_de_pontuseaux = self.data_to_save['art_graphique_materiaux_support_nombre_intervalles_pontuseaux']
        except TypeError:
            pass

        materiaux_support.save()

        return materiaux_support


    def save_technique_dessin(self):

        technique_dessein = TechniqueDesseinArtGraphique()
        technique_dessein.pointe_de_metal = self.data_to_save['art_graphique_technique_dessin_stylet_pointe_metal']
        technique_dessein.stylet_ou_pierre_noire = self.data_to_save['art_graphique_technique_dessin_pierre_noire']
        technique_dessein.fusain_crayon_comte = self.data_to_save['art_graphique_technique_dessin_fusain_crayon_comte']
        technique_dessein.graphite = self.data_to_save['art_graphique_technique_dessin_graphite']
        technique_dessein.sanguine = self.data_to_save['art_graphique_technique_dessin_sanguine']
        technique_dessein.craie_blanche = self.data_to_save['art_graphique_technique_dessin_craie_blanche']
        technique_dessein.crayon_de_couleurs = self.data_to_save['art_graphique_technique_dessin_crayon_de_couleurs']
        technique_dessein.rehauts_blancs = self.data_to_save['art_graphique_technique_dessin_rehauts_blancs']
        technique_dessein.pastel = self.data_to_save['art_graphique_technique_dessin_pastel']
        technique_dessein.encre_au_carbone = self.data_to_save['art_graphique_technique_dessin_encre_au_carbone']
        technique_dessein.encre_brune = self.data_to_save['art_graphique_technique_dessin_encre_brune']
        technique_dessein.encre_metallogallique = self.data_to_save['art_graphique_technique_dessin_encre_metallogallique']
        technique_dessein.peinture_a_l_huile_et_essence_terebentine_sur_papier = self.data_to_save['art_graphique_technique_dessin_peinture_huile_et_essence_terebenthine_sur_papier']
        technique_dessein.encre_de_couleur = self.data_to_save['art_graphique_technique_dessin_encre_de_couleur']
        technique_dessein.tempera = self.data_to_save['art_graphique_technique_dessin_tempera']
        technique_dessein.gouache = self.data_to_save['art_graphique_technique_dessin_gouache']
        technique_dessein.aquarelle = self.data_to_save['art_graphique_technique_dessin_aquarelle']
        technique_dessein.autre = self.data_to_save['art_graphique_technique_dessin_autre']
        
        if self.data_to_save['art_graphique_technique_dessin_autre']:
            technique_dessein.autre_technique_dessin = self.data_to_save['art_graphique_technique_dessin_autre_technique_dessin']
        technique_dessein.save()

        return technique_dessein


    def save_technique_estampe(self):

        technique_estampe = TechniqueEstampeArtGraphique()
        technique_estampe.burin = self.data_to_save['art_graphique_technique_estampe_burin']
        technique_estampe.xylographie = self.data_to_save['art_graphique_technique_estampe_xylographie']
        technique_estampe.taille_d_epargne = self.data_to_save['art_graphique_technique_estampe_taille_epargne']
        technique_estampe.eau_forte = self.data_to_save['art_graphique_technique_estampe_eau_forte']
        technique_estampe.aquatinte = self.data_to_save['art_graphique_technique_estampe_aquatinte']
        technique_estampe.taille_douce = self.data_to_save['art_graphique_technique_estampe_taille_douce']
        technique_estampe.lithographie = self.data_to_save['art_graphique_technique_estampe_lithographie']
        technique_estampe.pointe_seche = self.data_to_save['art_graphique_technique_estampe_pointe_seche']
        technique_estampe.maniere_noire = self.data_to_save['art_graphique_technique_estampe_maniere_noire']
        technique_estampe.maniere_au_crayon = self.data_to_save['art_graphique_technique_estampe_maniere_au_crayon']
        technique_estampe.procede_au_pochoir = self.data_to_save['art_graphique_technique_estampe_procede_au_pochoir']
        technique_estampe.serigraphie = self.data_to_save['art_graphique_technique_estampe_serigraphie']
        technique_estampe.technique_combinees = self.data_to_save['art_graphique_technique_estampe_techniques_combinees']
        technique_estampe.technique_combinees_technique_estampe = self.data_to_save['art_graphique_technique_estampe_nom_techniques_combinees']
        
        if self.data_to_save['art_graphique_technique_estampe_techniques_combinees']:
            technique_estampe.technique_combinees_techniqueEstampe = self.data_to_save['art_graphique_technique_estampe_nom_techniques_combinees']
        technique_estampe.save()

        return technique_estampe


    def save_autre_technique_graphique(self):

        autre_technique_graphique = AutreTechniqueGraphiqueArtGraphique()
        autre_technique_graphique.encre_a_imprimer_a_l_eau = self.data_to_save['art_graphique_autre_technique_graphique_encre_a_imprimer_eau']
        autre_technique_graphique.encre_a_imprimer_a_l_huile = self.data_to_save['art_graphique_autre_technique_graphique_encre_a_imprimer_huile']
        
        autre_technique_graphique.save()

        return autre_technique_graphique


    def save_technique_reproduction(self):

        technique_reproduction = TechniqueReproductionArtGraphique()
        technique_reproduction.heliogravure = self.data_to_save['art_graphique_technique_reproduction_heliogravure']
        technique_reproduction.quadrichromie_offset = self.data_to_save['art_graphique_technique_reproduction_quadrichromie_offset']
        technique_reproduction.save()

        return technique_reproduction


    def save_support(self):

        support = SupportArtGraphique()
        support.amincissement = self.data_to_save['art_graphique_support_amincissement']
        support.fragilite = self.data_to_save['art_graphique_support_fragilite']
        support.trous_de_punaises = self.data_to_save['art_graphique_support_trou_de_punaises']
        support.anciennes_restauration = self.data_to_save['art_graphique_support_anciennes_restaurations']
        support.gondrolement = self.data_to_save['art_graphique_support_gondolement']
        support.trace_de_colle = self.data_to_save['art_graphique_support_trace_de_colle']
        support.brulure = self.data_to_save['art_graphique_support_brulure']
        support.pliure = self.data_to_save['art_graphique_support_pliure']
        support.residus_d_adhesif = self.data_to_save['art_graphique_support_residus_adhesifs']
        support.cassant = self.data_to_save['art_graphique_support_cassant']
        support.piqure = self.data_to_save['art_graphique_support_piqure']
        support.rouille = self.data_to_save['art_graphique_support_rouille']
        support.coupure = self.data_to_save['art_graphique_support_coupure']
        support.papier_froisse = self.data_to_save['art_graphique_support_papier_froisse']
        support.taches_claires = self.data_to_save['art_graphique_support_taches_claires']
        support.dechirure = self.data_to_save['art_graphique_support_dechirure']
        support.lacune = self.data_to_save['art_graphique_support_lacune']
        support.taches_diverses = self.data_to_save['art_graphique_support_taches_diverses']
        support.decoloration = self.data_to_save['art_graphique_support_decoloration']
        support.rigidite = self.data_to_save['art_graphique_support_rigidite']
        support.zone_brune = self.data_to_save['art_graphique_support_zone_brune']
        support.deformations = self.data_to_save['art_graphique_support_deformations']
        support.peluches = self.data_to_save['art_graphique_support_peluches']
        support.poussieres = self.data_to_save['art_graphique_support_poussieres']
        support.depot_matiere_formant_tache = self.data_to_save['art_graphique_support_depot_matiere_formant_tache']
        support.perforation = self.data_to_save['art_graphique_support_perforation']
        support.insectes = self.data_to_save['art_graphique_support_insectes']
        support.dislocation_des_fibres_cellulose = self.data_to_save['art_graphique_support_dislocation_des_fibres_cellulose']
        support.jaunissement_generalise = self.data_to_save['art_graphique_support_jaunissement_generalise']
        support.trou_d_insectes = self.data_to_save['art_graphique_support_trou_d_insectes']
        support.doublage_defectueux = self.data_to_save['art_graphique_support_doublage_defectueux']
        support.jaunissement_localise = self.data_to_save['art_graphique_support_jaunissement_localise']
        support.micro_organismes = self.data_to_save['art_graphique_support_micro_organismes']
        support.epidermages = self.data_to_save['art_graphique_support_epidermages']
        support.impregnation_d_un_produit_gras = self.data_to_save['art_graphique_support_impregnation_produit_gras']
        support.moisissures_ou_bacteries = self.data_to_save['art_graphique_support_moisissures_bacteries']
        support.save()

        return support


    def save_technique(self):

        technique = TechniqueArtGraphique()
        technique.affaiblissement_des_traits = self.data_to_save['art_graphique_technique_affaiblissement_des_traits']
        technique.craquelure = self.data_to_save['art_graphique_technique_craquelure']
        technique.fixatif_altere = self.data_to_save['art_graphique_technique_fixatif_altere']
        technique.anciennes_restaurations = self.data_to_save['art_graphique_technique_anciennes_restaurations']
        technique.decapage = self.data_to_save['art_graphique_technique_decapage']
        technique.jaunissement = self.data_to_save['art_graphique_technique_jaunissement']
        technique.corrosion_de_l_encre = self.data_to_save['art_graphique_technique_corrosion_encre']
        technique.encaillage_des_gouaches = self.data_to_save['art_graphique_technique_ecaillage_des_gouaches']
        technique.vernis_altere = self.data_to_save['art_graphique_technique_vernis_altere']
        technique.couleurs_qui_ont_fuse = self.data_to_save['art_graphique_technique_couleurs_qui_ont_fuse']
        technique.manques = self.data_to_save['art_graphique_technique_manques']
        technique.trait_degrade = self.data_to_save['art_graphique_technique_traits_degrade']
        technique.couleurs_eclaircies = self.data_to_save['art_graphique_technique_couleurs_eclaircies']
        technique.pulverulence = self.data_to_save['art_graphique_technique_pulverulence']
        technique.teintes_palies = self.data_to_save['art_graphique_technique_teintes_palies']
        technique.teintes_transformees = self.data_to_save['art_graphique_technique_teintes_transformees']
        technique.save()

        return technique


    def save_montage(self):

        montage = MontageArtGraphique()
        montage.carton_au_verso = self.data_to_save['art_graphique_montage_carton_au_verso']
        montage.colle_en_plein = self.data_to_save['art_graphique_montage_colle_en_plein']
        montage.anciennes_restauration = self.data_to_save['art_graphique_montage_anciennes_restaurations']
        montage.fenetre_au_recto = self.data_to_save['art_graphique_montage_fenetre_au_recto']
        montage.colle_par_les_bords = self.data_to_save['art_graphique_montage_colle_par_les_bords']
        montage.defaut_d_adherance = self.data_to_save['art_graphique_montage_defaut_adherence']
        montage.passepartout = self.data_to_save['art_graphique_montage_passepartout']
        montage.fausse_marge = self.data_to_save['art_graphique_montage_fausse_marge']
        montage.charniere_en_japon = self.data_to_save['art_graphique_montage_charniere_en_japon']
        montage.save()

        return montage


    def save_constat_art_graphique(self):

        constat = ConstatArtGraphique()
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
        constat.technique_dessein = self.save_technique_dessin()
        constat.technique_estampe = self.save_technique_estampe()
        constat.autre_technique_graphique = self.save_autre_technique_graphique()
        constat.technique_reproduction = self.save_technique_reproduction()
        constat.support = self.save_support()
        constat.technique = self.save_technique()
        constat.montage = self.save_montage()
        constat.art_graphique = ArtGraphique.objects.get(id=self.art_work_id)
        
        cadre = self.save_cadre()
        materiaux_support = self.save_materiaux_support()

        if cadre != None:
            constat.cadre = cadre

        if materiaux_support != None:
            constat.materiaux_support = materiaux_support

        constat.save()

        return constat


    def save_photo_significative_cadre(self):
        pass