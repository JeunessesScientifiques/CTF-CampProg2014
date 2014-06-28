CTF-CampProg2014
================

Challenge de Capture de Drapeaux (CTF) pour le Camp de Programmation 2014


0. Accueil et explication du fonctionnement (python)

Thème ASCII Art: http://patorjk.com/software/taag/#p=display&f=Graffiti&t=Hello%20world
http://docs.python-requests.org/en/latest/

Liste des Challenges
---
        1. Bruteforcer le mot de passe d'un utilisateur SSH pour lire un fichier [hugo]
           - peut utiliser Python (paramiko) ou un script shell, etc...
           - le fichier contient une image ASCII
           - mot de passe dans un dictionnaire ~fourni (eg: marques de voitutures, animaux d'Afrique)
           - comment empêcher un utilisateur de bloquer le compte/changer le mdp ?
           "Lily cache un secret dans son dossier personnel sur son ordinateur. Nous n'avons pas
           accès à son compte, mais son frère, Bob, a aussi un compte sur cet ordinateur et on peut
           lire le secret de Lily depuis son compte. De plus, on sait que Bob est un grand fan d'astrologie
           et que son mot de passe est le nom d'un objet du système solaire (voir liste fournie).
        2. Injection SQL [antonin]
        3. Obtenir un mot de passe caché dans un programme binaire C (solution=ouvrir le binaire avec un éditeur) [hugo]
        4. Bruteforcer le mot de passe de protection d'un programme local (binaire C) [antonin]
           - Entrer le bon mot de passe affiche la solution à entrer sur la page web du challenge
           - Mot de passe aléatoire et assez court pour que ce soit faisable en ~1 minute de calcul
        5. Réaliser un calcul et entrer la solution sur le site du challenge dans un court délai (2 secondes) [hugo]
        6. Stéganographie ?
          - Texte dans une image ou image dans une image
        7. Code source d'un programme qui génère un code, mais est rempli d'erreurs [hugo]
          - language inconnu ? Perl / Ruby
          "Le code source de ce programme a été transmi par signaux de fumée et est rempli d'erreurs."
        8. Labyrinthe de liens (des centaines de liens chaînés) 
        9. Récupérer le mot de passe du blog de Lily à travers le compte utilisateur de son frère Dan et
           le moniteur de process en cours (argument passé au programme). Le mot de passe change souvent.
        10. Page protégée par un bête mot de passe en Javascript - contient le hash du mot de passe.
        11. Site PHP mal sécurisé, une URL affiche le site et une autre donne le code source.
            Le joueur droit trouver le mot de passe admin, se connecter et poster son nom/code sur la page via
            un formulaire réservé à l'admin (stockés dans un fichier, ajout seul). [antonin]
        12. Site mal sécurisé, une URL affiche le site et une autre donne accès pour télécharger la base de données. 
            Il faut en extraire la réponse au challenge de la base de données SQLite. [hugo]
        13. Des hackers ont volé la base de données des comptes utilisateur d'un site du camp, avec tous les mots de passe hashés en MD5. 
            Vous devez usurper l'identité d'un des utilisateurs pour obtenir le code du challenge. [hugo]
        14. Même chose que 13 mais avec un sel unique par utilisateur et du sha256. [hugo]
        15. Faire tomber un site lent (Denial of Service) révèle la solution dans la page d'erreur d'un autre site qui essaie d'y récupérer des données.
            [antonin] (fait des requetes vers un autre site qui est lent à répondre)
        16. Récupération de mot de passe par Wireshark ou TCPdump sur réseau wifi non sécurisé. [Antonin]
        17. ? Analyse de l'exécution d'un programme via strace. [hugo]
        18. Découvrir avec Nmap l'IP de la machine qui a le port XX inhabituel ouvert, puis s'y connecter avec Netcat.
            Si on a le courage, se connecter affichera un Nyancat animé avec le code. [hugo]
        19. Un zip contient un ensemble de fichiers, dont une lettre et un fichier chiffré avec une clef GPG symmétrique, qui se trouve
            ou peut être devinée à partir de la lettre et des photos jointes.
            gpg -c fichier.truc [antonin]
        20. Un service web est super sécurisé. Il demande à l'utilisateur de lui envoyer sa clef publique GPG, 
            et en retour lui fournira la solution chiffrée que seul lui peut lire. [antonin] en python
        21. Accéder à un site web caché en changeant le VirtualHost de la requête HTTP. [hugo]
        22. Page qui nécessite de modifier ses cookies pour accéder au secret [antonin]

Qui fait quoi ?
---
Antonin
0 (Accueil) ,2,4,6,8,10,11,15,16,19,20,22

Hugo
1,3,5,7,9,12,13,14,17,18,21

