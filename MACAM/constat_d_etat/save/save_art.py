from constat_d_etat.models import *
from constat_d_etat.forms import FormArt

class SaveArt():

    def __init__(self, data_to_save):
        self.data_to_save = data_to_save

    
    def save_art_graphique(self,):

        art_graphique = ArtGraphique()
        art_graphique.numero_inventaire = self.data_to_save['numero_inventaire']
        art_graphique.institution = self.data_to_save['institution']
        art_graphique.titre = self.data_to_save['titre_oeuvre']
        art_graphique.auteur = self.data_to_save['auteur_oeuvre']        
        art_graphique.hauteur_sans_cadre = self.data_to_save['hauteur_sans_cadre']     
        art_graphique.largeur_sans_cadre = self.data_to_save['largeur_sans_cadre']    
        art_graphique.epaisseur_sans_cadre = self.data_to_save['epaisseur_sans_cadre']
        art_graphique.hauteur_avec_cadre = self.data_to_save['hauteur_avec_cadre']
        art_graphique.largeur_avec_cadre = self.data_to_save['largeur_avec_cadre']
        art_graphique.epaisseur_avec_cadre = self.data_to_save['epaisseur_avec_cadre']
        art_graphique.photo_face = self.data_to_save['photo_oeuvre_face']
        art_graphique.photo_revers = self.data_to_save['photo_oeuvre_revers']

        if self.data_to_save['format_oeuvre'] == FormArt.AUTRE:
            art_graphique.format_oeuvre = self.data_to_save['autre_format']
        else:
            art_graphique.format_oeuvre = self.data_to_save['format_oeuvre']      
        
        art_graphique.save()

        return art_graphique

    
    def save_peinture_sur_bois(self,):

        peinture_sur_bois = PeintureSurBois()
        peinture_sur_bois.numero_inventaire = self.data_to_save['numero_inventaire']
        peinture_sur_bois.institution = self.data_to_save['institution']
        peinture_sur_bois.titre = self.data_to_save['titre_oeuvre']
        peinture_sur_bois.auteur = self.data_to_save['auteur_oeuvre']        
        peinture_sur_bois.hauteur_sans_cadre = self.data_to_save['hauteur_sans_cadre']      
        peinture_sur_bois.largeur_sans_cadre = self.data_to_save['largeur_sans_cadre']   
        peinture_sur_bois.epaisseur_sans_cadre = self.data_to_save['epaisseur_sans_cadre']
        peinture_sur_bois.hauteur_avec_cadre = self.data_to_save['hauteur_avec_cadre']
        peinture_sur_bois.largeur_avec_cadre = self.data_to_save['largeur_avec_cadre']
        peinture_sur_bois.epaisseur_avec_cadre = self.data_to_save['epaisseur_avec_cadre']
        peinture_sur_bois.photo_face = self.data_to_save['photo_oeuvre_face']
        peinture_sur_bois.photo_revers = self.data_to_save['photo_oeuvre_revers']
        
        if self.data_to_save['format_oeuvre'] == FormArt.AUTRE:
            peinture_sur_bois.format_oeuvre = self.data_to_save['autre_format']
        else:
            peinture_sur_bois.format_oeuvre = self.data_to_save['format_oeuvre']            
        
        peinture_sur_bois.save()

        return peinture_sur_bois


    def save_peinture_sur_toile(self,):

        peinture_sur_toile = PeintureSurToile()
        peinture_sur_toile.numero_inventaire = self.data_to_save['numero_inventaire']
        peinture_sur_toile.institution = self.data_to_save['institution']
        peinture_sur_toile.titre = self.data_to_save['titre_oeuvre']
        peinture_sur_toile.auteur = self.data_to_save['auteur_oeuvre']        
        peinture_sur_toile.hauteur_sans_cadre = self.data_to_save['hauteur_sans_cadre']    
        peinture_sur_toile.largeur_sans_cadre = self.data_to_save['largeur_sans_cadre']   
        peinture_sur_toile.epaisseur_sans_cadre = self.data_to_save['epaisseur_sans_cadre']
        peinture_sur_toile.hauteur_avec_cadre = self.data_to_save['hauteur_avec_cadre']
        peinture_sur_toile.largeur_avec_cadre = self.data_to_save['largeur_avec_cadre']
        peinture_sur_toile.epaisseur_avec_cadre = self.data_to_save['epaisseur_avec_cadre']
        peinture_sur_toile.photo_face = self.data_to_save['photo_oeuvre_face']
        peinture_sur_toile.photo_revers = self.data_to_save['photo_oeuvre_revers']
        
        if self.data_to_save['format_oeuvre'] == FormArt.AUTRE:
            peinture_sur_toile.format_oeuvre = self.data_to_save['autre_format']
        else:
            peinture_sur_toile.format_oeuvre = self.data_to_save['format_oeuvre']            
        
        peinture_sur_toile.save()

        return peinture_sur_toile
        