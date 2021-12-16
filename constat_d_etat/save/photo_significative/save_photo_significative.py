from constat_d_etat.models import PhotoSignificativeCadreOeuvre
from constat_d_etat.models import PhotoSignificativeCouchePicturalePeinture
from constat_d_etat.models import PhotoSignificativeChassisPeintureSurToile
from constat_d_etat.models import PhotoSignificativeSupportPeintureSurBois
from constat_d_etat.models import PhotoSignificativeSupportArtGraphique

from django.core.files.storage import FileSystemStorage

class SavePhotoSignificative():

    PATH_SAVING_PHOTO_SIGN_CADRE = 'photos_significatives_cadre/'
    PATH_SAVING_PHOTO_SIGN_CP = 'photos_significatives_couche_picturale/'
    PATH_SAVING_PHOTO_SIGN_CHASSIS = 'photos_significatives_chassis/'
    PATH_SAVING_PHOTO_SIGN_SUPPORT = 'photos_significatives_support/'


    def __init__(self, request_post, request_files, constat):
        self.request_post = request_post
        self.request_files = request_files
        self.constat = constat


    def save_photo(self, photo_significative, rubrique, i, PATH_SAVING_PHOTO_SIGN):
        photo_significative.nature_alteration = self.request_post['nature-alteration-{}-photo{}'.format(rubrique, i)]

        #if the variable exists it returns its value
        #if not it returns 'face'
        face = self.request_post.get('face-emplacement-detail-{}{}'.format(rubrique, i), 'face')
        photo_significative.face = True if face == 'face' else False 

        fss = FileSystemStorage()

        if self.request_files.get('photo-zoom-{}{}'.format(rubrique, i)) != None:
            fss.save(PATH_SAVING_PHOTO_SIGN + self.request_files['photo-zoom-{}{}'.format(rubrique, i)].name, self.request_files['photo-zoom-{}{}'.format(rubrique, i)])
            photo_significative.photo = PATH_SAVING_PHOTO_SIGN + self.request_files['photo-zoom-{}{}'.format(rubrique, i)].name           
        
        if self.request_files.get('photo-zoom-detail-{}{}'.format(rubrique, i)) != None:
            fss.save(self.PATH_SAVING_PHOTO_SIGN_CADRE + self.request_files['photo-zoom-detail-{}{}'.format(rubrique, i)].name, self.request_files['photo-zoom-detail-{}{}'.format(rubrique, i)])
            photo_significative.photo_avec_emplacement = PATH_SAVING_PHOTO_SIGN + self.request_files['photo-zoom-detail-{}{}'.format(rubrique, i)].name
        
        photo_significative.save()

    

    def save_photo_significative_cadre(self):
        nb_pht_sign = int(self.request_post['nombre-photos-significatives-cadre'])
        if nb_pht_sign > 0:
            for i in range(1, nb_pht_sign + 1):                
                ph_sign = PhotoSignificativeCadreOeuvre()
                ph_sign.cadre = self.constat.cadre                
                self.save_photo(ph_sign, 'cadre', i, self.PATH_SAVING_PHOTO_SIGN_CADRE)


    def save_photo_significative_support_peinture_sur_bois(self):
        nb_pht_sign = int(self.request_post['nombre-photos-significatives-support'])
        if nb_pht_sign > 0:
            for i in range(1, nb_pht_sign + 1):
                ph_sign = PhotoSignificativeSupportPeintureSurBois()
                ph_sign.support = self.constat.support_peinture_sur_bois
                self.save_photo(ph_sign, 'support', i, self.PATH_SAVING_PHOTO_SIGN_SUPPORT)


    def save_photo_significative_couche_picturale(self):
        nb_pht_sign = int(self.request_post['nombre-photos-significatives-couche-picturale'])
        if nb_pht_sign > 0:
            for i in range(1, nb_pht_sign + 1):
                ph_sign = PhotoSignificativeCouchePicturalePeinture()
                ph_sign.couche_picturale = self.constat.couche_picturale
                self.save_photo(ph_sign, 'couche-picturale', i, self.PATH_SAVING_PHOTO_SIGN_CP)


    def save_photo_significative_chassis(self):
        nb_pht_sign = int(self.request_post['nombre-photos-significatives-chassis'])
        if nb_pht_sign > 0:
            for i in range(1, nb_pht_sign + 1):
                ph_sign = PhotoSignificativeChassisPeintureSurToile()
                ph_sign.chassis = self.constat.chassis
                self.save_photo(ph_sign, 'chassis', i, self.PATH_SAVING_PHOTO_SIGN_CHASSIS)


    def save_photo_significative_support_art_graphique(self):
        nb_pht_sign = int(self.request_post['nombre-photos-significatives-support'])
        if nb_pht_sign > 0:
            for i in range(1, nb_pht_sign + 1):
                ph_sign = PhotoSignificativeSupportArtGraphique()
                ph_sign.support = self.constat.support
                self.save_photo(ph_sign, 'support', i, self.PATH_SAVING_PHOTO_SIGN_CADRE)