import requests
from bs4 import BeautifulSoup

def download_profile_image(u):
    url = "https://www.drupal.org/u/" + u

    page = requests.get(url)
    content = page.content

    soup = BeautifulSoup(content, "lxml")
    images = soup.find_all("img")

    for image in images:
        if u in image.attrs['alt']:
            src = image.attrs['src']
            pos = src.find('?itok=')
            img_url = src[:pos]
            image_response = requests.get(img_url)
            if image_response.status_code == 200:
                if img_url.endswith('.jpg'):
                    file_name = u + '.jpg'
                if img_url.endswith('.png'):
                    file_name = u + '.png'
            with open(file_name, 'wb') as image_file:
                for chunk in image_response.iter_content(1024):
                    image_file.write(chunk)

# download_profile_image("aboros")
# download_profile_image("ajayvi")
# download_profile_image("akosh")
# download_profile_image("Amber-Himes Matz")
# download_profile_image("andreupav")
# download_profile_image("AnnGreazel")
# download_profile_image("anprok")
# download_profile_image("avanraaphorst")
# download_profile_image("balagan")
# download_profile_image("Balu-Ertl")
# download_profile_image("batigolix")
# download_profile_image("bemery987")
# download_profile_image("billimarie")
# download_profile_image("bsnodgrass")
# download_profile_image("bwinett")
# download_profile_image("camhoward")
# download_profile_image("chishah92")
# download_profile_image("Chris-Dart")
# download_profile_image("ckrina")
# download_profile_image("cleverington")
# download_profile_image("dalin")
# download_profile_image("davidlee55")
# download_profile_image("dgorton")
# download_profile_image("diana.lakatos")
# download_profile_image("dimaro")
# download_profile_image("drumm")
# download_profile_image("eelkeblok")
# download_profile_image("eojthebrave")
# download_profile_image("francescbassas")
# download_profile_image("gdunham")
# download_profile_image("gisle")
# download_profile_image("HaloFX")
# download_profile_image("hey_germano")
# download_profile_image("hgoto")
# download_profile_image("ifrik")
# download_profile_image("JackProbst")
# download_profile_image("jerseycheese")
# download_profile_image("jfmacdonald")
# download_profile_image("jgrubb")
# download_profile_image("jhodgdon")
# download_profile_image("jojyja")
# download_profile_image("jpraco")
# download_profile_image("jredding")
# download_profile_image("juanolalla")
# download_profile_image("jungle")
# download_profile_image("kabetani")
# download_profile_image("kamalkantpansari")
# download_profile_image("KarlKedrovsky")
# download_profile_image("ken_taguchi")
# download_profile_image("kvantomme")
# download_profile_image("Les-Lim")
# download_profile_image("lluvigne")
# download_profile_image("lolk")
# download_profile_image("Mark-LaCroix")
# download_profile_image("mericamps")
# download_profile_image("metzlerd")
# download_profile_image("michaellenahan")
# download_profile_image("mistake")
# download_profile_image("mndonx")
# download_profile_image("novid")
# download_profile_image("Pandelon")
# download_profile_image("petycomp")
# download_profile_image("Pixiekiss")
# download_profile_image("podarok")
# download_profile_image("rvilar")
# download_profile_image("SebCorbin")
# download_profile_image("spuky")
# download_profile_image("Sree")
# download_profile_image("supriyarajgopal")
# download_profile_image("surendramohan")
# download_profile_image("Takafumi")
download_profile_image("th_tushar")
download_profile_image("Tomotsugu-Kaneko")
download_profile_image("vanessakovalsky")
download_profile_image("vegantriathlete")
download_profile_image("wturrell")
download_profile_image("yrvyn")
download_profile_image("zsofi.major")
