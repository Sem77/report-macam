const btn_photos_significatives_cadre = document.getElementById('btn-photos-significatives-cadre')
const btn_photos_significatives_support = document.getElementById('btn-photos-significatives-support')
const btn_photos_significatives_couche_picturale = document.getElementById('btn-photos-significatives-couche-picturale')
const btn_photos_significatives_chassis = document.getElementById('btn-photos-significatives-chassis')

let nb_photos_significatives_cadre = {nb_photos : 0}
let nb_photos_significatives_support = {nb_photos : 0}
let nb_photos_significatives_couche_picturale = {nb_photos : 0}
let nb_photos_significatives_chassis = {nb_photos : 0}


function addElt(idTab, idHidddenInput, nbPhotos, rubrique){
    nbPhotos.nb_photos++
    document.getElementById(idTab).innerHTML +=     
    `
    <hr>
    <tr>
    <td><input type="file" accept="image/*" name="photo-zoom-${rubrique}${nbPhotos.nb_photos}" id="photo-zoom-${rubrique}${nbPhotos.nb_photos}"></td>
    <td><input type="file" accept="image/*" name="photo-zoom-detail-${rubrique}${nbPhotos.nb_photos}" id="photo-zoom-detail-${rubrique}${nbPhotos.nb_photos}"></td>
    </tr>
    
    <tr>
    <td><label>Nature de l'altération: </label><input name="nature-alteration-${rubrique}-photo${nbPhotos.nb_photos}"></td>
    <td>
    <input type="radio" name="face-emplacement-detail-${rubrique}${nbPhotos.nb_photos}" value="face" selected> <label>Face</label><br>
    <input type="radio" name="face-emplacement-detail-${rubrique}${nbPhotos.nb_photos}" value="revers"> <label>Revers</label><br>
    </td>
    </tr>
    `;

    document.getElementById(idHidddenInput).setAttribute('value', nbPhotos.nb_photos);
} 

try {
    btn_photos_significatives_cadre.addEventListener("click",()=> addElt("tab-photos-significatives-cadre", "nombre-photos-significatives-cadre", nb_photos_significatives_cadre, "cadre"))
} catch(TypeError) {}

try {
    btn_photos_significatives_support.addEventListener("click",()=> addElt("tab-photos-significatives-support", "nombre-photos-significatives-support", nb_photos_significatives_support, "support"))
} catch(TypeError) {}

try {
    btn_photos_significatives_couche_picturale.addEventListener("click",()=> addElt("tab-photos-significatives-couche-picturale", "nombre-photos-significatives-couche-picturale", nb_photos_significatives_couche_picturale, "couche-picturale"))
} catch(TypeError) {}

try {
    btn_photos_significatives_chassis.addEventListener("click",()=> addElt("tab-photos-significatives-chassis", "nombre-photos-significatives-chassis", nb_photos_significatives_chassis, "chassis"))
} catch(TypeError) {}