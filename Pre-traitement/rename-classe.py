import os

dossier = "C:\\Users\\msi\\Desktop\\PFE\\pfe\\DCSASS Dataset1\\crime\\Crime211_x264.mp4"
for nom_fichier in os.listdir(dossier):
    if nom_fichier.endswith(".mp4"):
        nom_sans_extension = os.path.splitext(nom_fichier)[0]
        
        nouveau_nom_sans_extension = nom_sans_extension.replace("Robbery022", "Crime211")

        nouveau_nom_fichier = nouveau_nom_sans_extension + ".mp4"

        os.rename(os.path.join(dossier, nom_fichier), os.path.join(dossier, nouveau_nom_fichier))
