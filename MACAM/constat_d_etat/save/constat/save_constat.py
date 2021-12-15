from constat_d_etat.models import *

class SaveConstat():

    def __init__(self, data_to_save, art_work_id):
        self.data_to_save = data_to_save
        self.art_work_id = art_work_id


    def save_caracteristiques_cadre(self,):
        caracteristiques = CaracteristiquesCadreOeuvre()
        caracteristiques.ancien = self.data_to_save['cadre_caracteristiques_ancien']
        caracteristiques.moderne = self.data_to_save['cadre_caracteristiques_moderne']
        caracteristiques.cadre_d_origine = self.data_to_save['cadre_caracteristiques_cadre_d_origine']
        caracteristiques.bois_dore = self.data_to_save['cadre_caracteristiques_bois_dore']
        caracteristiques.platre_dore = self.data_to_save['cadre_caracteristiques_platre_dore']
        caracteristiques.bois_peint = self.data_to_save['cadre_caracteristiques_bois_peint']
        caracteristiques.feuillure_garnie_de_feutrine = self.data_to_save['cadre_caracteristiques_feuillure_garnie_de_feutrine']
        caracteristiques.verre_antireflet = self.data_to_save['cadre_caracteristiques_verre_antireflet']
        caracteristiques.tampons_de_calage = self.data_to_save['cadre_caracteristiques_tampons_de_calage_cadre_ou_panneau'] 
        caracteristiques.save()

        return caracteristiques


    def save_alterations_cadre(self,):

        alteration = AlterationCadreOeuvre()
        alteration.dispoint_aux_angles = self.data_to_save['cadre_alterations_disjoint_aux_angles']
        alteration.fissures_aux_angles = self.data_to_save['cadre_alterations_fissure_aux_angles']
        alteration.fissures_sur_les_bords = self.data_to_save['cadre_alterations_fissure_sur_les_bords']
        alteration.cadre_voile = self.data_to_save['cadre_alterations_cadre_voile']
        alteration.encrassement = self.data_to_save['cadre_alterations_encrassement']
        alteration.decor_fragilise = self.data_to_save['cadre_alterations_decor_fragilise']
        alteration.lacunes_de_bois = self.data_to_save['cadre_alterations_lacunes_de_bois']
        alteration.lacunes_de_platre = self.data_to_save['cadre_alterations_lacunes_de_platre']
        alteration.platre_pulverilent = self.data_to_save['cadre_alterations_platre_pulverilent']
        alteration.peinture_ecaillee = self.data_to_save['cadre_alterations_peinture_ecaillee']
        alteration.trous_d_envol = self.data_to_save['cadre_alterations_trous_d_envol']
        alteration.galeries_d_insectes = self.data_to_save['cadre_alterations_galerie_d_insectes']
        alteration.save()

        return alteration


    def save_montage_cadre(self,):

        montage = MontageCadreOeuvre()
        montage.trous_de_pitons = self.data_to_save['cadre_montage_trous_de_pitons']
        montage.trous_de_cartels = self.data_to_save['cadre_montage_trous_de_cartels']
        montage.cartel = self.data_to_save['cadre_montage_cartel']
        montage.etiquettes = self.data_to_save['cadre_montage_ettiquettes']
        montage.encadrement_flottant = self.data_to_save['cadre_montage_encadrement_flottant']
        montage.fixation_au_cadre = self.data_to_save['cadre_montage_fixation_au_cadre']
        montage.ressorts = self.data_to_save['cadre_montage_ressorts']
        montage.clous = self.data_to_save['cadre_montage_clous']
        montage.pattes = self.data_to_save['cadre_montage_pattes']
        montage.poignees_sur_les_montants = self.data_to_save['cadre_montage_poignee_sur_les_montants']            
        
        if self.data_to_save['cadre_montage_poignee_sur_les_montants']:
            montage.etat_poignees_sur_les_montants = self.data_to_save['cadre_montage_etat_poignee_sur_les_montants']
            montage.nombre_poignees_sur_les_montants = self.data_to_save['cadre_montage_nombre_poignee_sur_les_montants']
        montage.save()

        return montage


    def save_dorure_cadre(self,):

        dorure = DorureCadreOeuvre()
        dorure.bon_etat = self.data_to_save['cadre_dorure_bon_etat']
        dorure.bronzine = self.data_to_save['cadre_dorure_bronzine']
        dorure.dorure_mixte = self.data_to_save['cadre_dorure_dorure_mixte']
        dorure.piqures = self.data_to_save['cadre_dorure_piqures']
        dorure.lacunes = self.data_to_save['cadre_dorure_lacunes']
        dorure.usures = self.data_to_save['cadre_dorure_usures']
        dorure.maquillage = self.data_to_save['cadre_dorure_maquillage']
        dorure.taches = self.data_to_save['cadre_dorure_taches']
        dorure.save()

        return dorure


    def save_systeme_d_accrochage_cadre(self,):

        systeme_d_accrochage = SystemeDAccrochageCadreOeuvre()
        systeme_d_accrochage.attelles = self.data_to_save['cadre_systeme_accrochage_attelles']
        systeme_d_accrochage.pitons = self.data_to_save['cadre_systeme_accrochage_pitons']
        systeme_d_accrochage.systeme_antivol = self.data_to_save['cadre_systeme_accrochage_systeme_antivol']
        systeme_d_accrochage.prete = self.data_to_save['cadre_systeme_accrochage_pretee']
        systeme_d_accrochage.retire = self.data_to_save['cadre_systeme_accrochage_retirees']
        
        if self.data_to_save['cadre_systeme_accrochage_systeme_antivol']:
            systeme_d_accrochage.type_systeme_antivol = self.data_to_save['cadre_systeme_accrochage_type_systeme_antivol']
        if self.data_to_save['cadre_systeme_accrochage_pretee']:
            systeme_d_accrochage.nombre_pretee = self.data_to_save['cadre_systeme_accrochage_nombre_pretee']
        systeme_d_accrochage.save()

        return systeme_d_accrochage


    def save_cadre(self):
        
        if self.data_to_save['absence_de_cadre']:
            return None

        else:          
            cadre = CadreOeuvre()
            cadre.etat_satisfaisant = self.data_to_save['absence_de_cadre']
            cadre.caracteristiques_cadre = self.save_caracteristiques_cadre()
            cadre.alteration = self.save_alterations_cadre()
            cadre.montage = self.save_montage_cadre()
            cadre.dorure = self.save_dorure_cadre()
            cadre.systeme_d_accrochage = self.save_systeme_d_accrochage_cadre()
            cadre.save()
            
        return cadre






    def save_protection_simple_emballage(self,):
        protection_simple = ProtectionSimpleEmballageOeuvre()
        protection_simple.tamponnage = self.data_to_save['emballage_protection_simple_tamponnage']
        protection_simple.elastoc = self.data_to_save['emballage_protection_simple_elastoc']
        protection_simple.fibrenap = self.data_to_save['emballage_protection_simple_fibrenap']
        protection_simple.papier_kraft = self.data_to_save['emballage_protection_simple_papier_kraft']
        protection_simple.papier_de_soie = self.data_to_save['emballage_protection_simple_papier_de_soie']
        protection_simple.film_polyester = self.data_to_save['emballage_protection_simple_film_polyester']
        protection_simple.papier_cristal = self.data_to_save['emballage_protection_simple_papier_cristal']
        protection_simple.intisse = self.data_to_save['emballage_protection_simple_intisse']
        protection_simple.carton_cannele = self.data_to_save['emballage_protection_simple_carton_cannele']
        protection_simple.plaque_de_polypropene = self.data_to_save['emballage_protection_simple_plaque_de_polypropylene']
        protection_simple.bullkraft = self.data_to_save['emballage_protection_simple_bullkraft']
        protection_simple.bullpack = self.data_to_save['emballage_protection_simple_bullpack']
        protection_simple.save()

        return protection_simple


    def save_caisse_emballage(self,):
        caisse = CaisseEmballageOeuvre()
        caisse.simple = self.data_to_save['emballage_caisse_simple']
        caisse.double = self.data_to_save['emballage_caisse_double']
        caisse.isotherme = self.data_to_save['emballage_caisse_isotherme']
        caisse.climatique = self.data_to_save['emballage_caisse_climatique']
        caisse.film_pare_vapeur = self.data_to_save['emballage_caisse_film_par_vapeur']
        caisse.mousses = self.data_to_save['emballage_caisse_mousses']
        caisse.polystylene = self.data_to_save['emballage_caisse_polystylene']
        caisse.tableau_face_dessus = self.data_to_save['emballage_caisse_tableau_face_dessus']
        caisse.tableau_face_dessous = self.data_to_save['emballage_caisse_tableau_face_dessous']
        caisse.indicateur_de_renversement = self.data_to_save['emballage_caisse_indicateur_de_renversement']
        caisse.gel_de_silice = self.data_to_save['emballage_caisse_gel_de_silice']
        caisse.thermohygrometre = self.data_to_save['emballage_caisse_thermohygrometre']
        caisse.indicateur_de_choc = self.data_to_save['emballage_caisse_indicateur_de_choc']
        caisse.save()

        return caisse


    def save_emballage(self):        

        emballage = EmballageOeuvre()
        emballage.caisse = self.save_caisse_emballage()
        emballage.protection_simple = self.save_protection_simple_emballage()
        emballage.save()        

        return emballage