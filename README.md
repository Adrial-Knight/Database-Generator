# Générateur d'image jour/nuit 
Cet outils utilise le [simulateur CARLA](https://carla.org/) pour générer des paires d'image jour/nuit représentant les mêmes scènes.
<p align="middle">
     <img src="https://github.com/Adrial-Knight/Database-Generator/blob/main/fig/town10HD_day.png" width=49% height=49% title="Day">
     <img src="https://github.com/Adrial-Knight/Database-Generator/blob/main/fig/town10HD_night.png" width=49% height=49% title="Night">
</p>

## Exemples
- Un apperçu [vidéo](https://www.youtube.com/watch?v=vB3TLsy6ArY) est disponible sur YouTube.
- Une base de 2048 paires au format 1080x1920 est téléchargeable sur ce [drive](https://drive.google.com/drive/folders/1B6a4aXvoviTbAt8_RCcj-upbep7-twak?usp=share_link).

## Utilisation
Un exemple d'utilisation est donné avec le script [bash](https://github.com/Adrial-Knight/Database-Generator/blob/main/sources/main.sh) fourni.

Un équivalent [python](https://github.com/Adrial-Knight/Database-Generator/blob/main/sources/main.py) est également fourni.

Dans les deux cas, il est supposé que le simulateur CARLA puisse se lancer à partir de `/opt/carla-simulator/CarlaUE4.sh`.

## Implémentation
Des explications techniques sur le fonctionnement du simulateur CARLA, ainsi que sur la bibliothèque développée sont fournies dans le fichier [rapport.pdf](https://github.com/Adrial-Knight/Database-Generator/blob/main/rapport.pdf) à la racine de ce repo.
