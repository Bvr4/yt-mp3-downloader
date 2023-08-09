# Youtube mp3 downloader

Ce script permet de télécharger la partie audio de vidéos de youtube, puis de les enregistrer au format MP3.   
Le script lit des fichiers en entrée et télécharge les audios des vidéos dont les liens y sont inscrits.  
A utiliser pour un usage personnel, merci de vous référer aux conditions d'utilisation de youtube, et aux licences d'utilisation des vidéos.

## Les fichiers en entrée sont :
- url_videos_a_telecharger.txt  
pour télécharger une ou plusieurs vidéos  
- url_playlist_a_telecharger.txt  
pour télécharger les vidéos appartenant à une ou plusieurs playlists

il faut y inscrire une URL par ligne

## prérequis :
- le module pytube doit être installé
- FFMPEG doit être installé sur l'ordinateur