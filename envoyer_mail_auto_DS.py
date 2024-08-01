import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import tkinter as tk
from tkinter import ttk, messagebox

def envoyer_mail_DS(volume, code_postal, ville_destination, adresse_mail_destinateur, mdp_adresse_mail_destinateur, adresses_mail_destinataires_transitaires, adresses_mail_destinataires_agents_livraison):
   
    # Recover the container size 
    if float(volume) < 30 : 
        container = "20ft" 
    else : 
        container = "40ft"
    
    # recuperer les deux premiers chiffres du cp 
    cp_ville = code_postal[:2]

    # recuperer le departement en fonction du cp 
    departements_ports = {}

    # Ajouter les données
    departements_ports["01"] = ["FOS"]
    departements_ports["02"] = ["LE HAVRE"]
    departements_ports["03"] = ["LE HAVRE"]
    departements_ports["04"] = ["FOS"]
    departements_ports["05"] = ["FOS"]
    departements_ports["06"] = ["FOS"]
    departements_ports["07"] = ["FOS"]
    departements_ports["08"] = ["LE HAVRE"]
    departements_ports["09"] = ["FOS"]
    departements_ports["10"] = ["LE HAVRE"]
    departements_ports["11"] = ["FOS"]
    departements_ports["12"] = ["FOS"]
    departements_ports["13"] = ["FOS"]
    departements_ports["14"] = ["LE HAVRE"]
    departements_ports["15"] = ["FOS"]
    departements_ports["16"] = ["LE HAVRE"]
    departements_ports["17"] = ["LE HAVRE"]
    departements_ports["18"] = ["LE HAVRE"]
    departements_ports["19"] = ["LE HAVRE"]
    departements_ports["21"] = ["LE HAVRE"]
    departements_ports["22"] = ["LE HAVRE"]
    departements_ports["23"] = ["LE HAVRE"]
    departements_ports["24"] = ["LE HAVRE"]
    departements_ports["25"] = ["LE HAVRE"]
    departements_ports["26"] = ["FOS"]
    departements_ports["27"] = ["LE HAVRE"]
    departements_ports["28"] = ["LE HAVRE"]
    departements_ports["29"] = ["LE HAVRE"]
    departements_ports["30"] = ["FOS"]
    departements_ports["31"] = ["FOS"]
    departements_ports["32"] = ["FOS"]
    departements_ports["33"] = ["LE HAVRE"]
    departements_ports["34"] = ["FOS"]
    departements_ports["35"] = ["LE HAVRE"]
    departements_ports["36"] = ["LE HAVRE"]
    departements_ports["37"] = ["LE HAVRE"]
    departements_ports["38"] = ["FOS"]
    departements_ports["39"] = ["LE HAVRE", "FOS"]
    departements_ports["40"] = ["FOS"]
    departements_ports["41"] = ["LE HAVRE"]
    departements_ports["42"] = ["FOS"]
    departements_ports["43"] = ["FOS"]
    departements_ports["44"] = ["LE HAVRE"]
    departements_ports["45"] = ["LE HAVRE"]
    departements_ports["46"] = ["FOS"]
    departements_ports["47"] = ["FOS"]
    departements_ports["48"] = ["FOS"]
    departements_ports["49"] = ["LE HAVRE"]
    departements_ports["50"] = ["LE HAVRE"]
    departements_ports["51"] = ["LE HAVRE"]
    departements_ports["52"] = ["LE HAVRE"]
    departements_ports["53"] = ["LE HAVRE"]
    departements_ports["54"] = ["LE HAVRE"]
    departements_ports["55"] = ["LE HAVRE"]
    departements_ports["56"] = ["LE HAVRE"]
    departements_ports["57"] = ["LE HAVRE"]
    departements_ports["58"] = ["LE HAVRE"]
    departements_ports["59"] = ["LE HAVRE"]
    departements_ports["60"] = ["LE HAVRE"]
    departements_ports["61"] = ["LE HAVRE"]
    departements_ports["62"] = ["LE HAVRE"]
    departements_ports["63"] = ["LE HAVRE", "FOS"]
    departements_ports["64"] = ["FOS"]
    departements_ports["65"] = ["FOS"]
    departements_ports["66"] = ["FOS"]
    departements_ports["67"] = ["LE HAVRE"]
    departements_ports["68"] = ["LE HAVRE"]
    departements_ports["69"] = ["FOS"]
    departements_ports["70"] = ["FOS"]
    departements_ports["71"] = ["FOS"]
    departements_ports["72"] = ["LE HAVRE"]
    departements_ports["73"] = ["FOS"]
    departements_ports["74"] = ["FOS"]
    departements_ports["75"] = ["LE HAVRE"]
    departements_ports["76"] = ["LE HAVRE"]
    departements_ports["77"] = ["LE HAVRE"]
    departements_ports["78"] = ["LE HAVRE"]
    departements_ports["79"] = ["LE HAVRE"]
    departements_ports["80"] = ["LE HAVRE"]
    departements_ports["81"] = ["FOS"]
    departements_ports["82"] = ["FOS"]
    departements_ports["83"] = ["FOS"]
    departements_ports["84"] = ["FOS"]
    departements_ports["85"] = ["LE HAVRE"]
    departements_ports["86"] = ["LE HAVRE"]
    departements_ports["87"] = ["LE HAVRE"]
    departements_ports["88"] = ["LE HAVRE"]
    departements_ports["89"] = ["LE HAVRE"]
    departements_ports["90"] = ["LE HAVRE"]
    departements_ports["91"] = ["LE HAVRE"]
    departements_ports["92"] = ["LE HAVRE"]
    departements_ports["93"] = ["LE HAVRE"]
    departements_ports["94"] = ["LE HAVRE"]
    departements_ports["95"] = ["LE HAVRE"]

    # Récupération des ports pour le département
    ports = departements_ports.get(cp_ville, [])

    # Affichage d'un message avec les informations saisies
    messagebox.showinfo("Informations saisies", 
                        f'''
                        Volume en m3: {volume}\n
                        Code postal: {code_postal_origine}\n
                        Résidence de destination: {residence_destination}\n
                        Ville de destination : {ville_destination}\n
                        Date ou période : {date_echeance_triglobal}\n
                        Adresses mail destinataires TRANSITAIRES: {adresses_mail_destinataires_transitaires}\n
                        Adresses mail destinataires AGENTS LIVRAISON: {adresses_mail_destinataires_agents_livraison}\n
                        Ports disponibles: {ports[0]}")
                        ''')

    # Corps du message
    body_mail_dem_20ft_40ft = f''' 
Bonjour,

Pouvez vous nous donner votre prix pour dédouaner des effets personnels et transporter le container à la résidence du client:

Container : {container} 
De POE : {ports[0]}
à résidence client : {residence_destination}
nature : effets persos

<b>Merci de préciser DTHC frais compagnie, frais de drop off éventuel si terminal inland.</b>

Cordialement,
Best regards,
Jean-Philippe BIARD

OPTIMUM MOBILITY
Global Mobility Solutions

Mobile: (+33) 06 61 79 45 00
Office: (+33) 09 67 24 16 14
jpbiard@optimum-mobility.com
Logo%2BOptimum%2BMobility.jpg
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Ce message et les pièces jointes éventuelles contiennent des informations confidentielles appartenant à l'expéditeur et sont établis à l'intention exclusive de ses destinataires.
Si vous recevez ce message par erreur, merci de le détruire et d'en avertir immédiatement l'expéditeur par e-mail.
Toute utilisation de ce message non conforme à sa destination, toute diffusion ou toute publication, totale ou partielle, est interdite, sauf autorisation expresse.
Les communications sur Internet n'étant pas sécurisées, l'expéditeur informe qu'il ne peut accepter aucune responsabilité quant au contenu de ce message.
Afin de contribuer au respect de l'environnement, merci de n'imprimer ce mail qu'en cas de nécessité.

This message and the possible attachments contain confidential information belonging to the sender and are intended solely for the addressees.
If you receive this message by mistake, please delete it and notify immediately the sender of it by e-mail.
Any use of this message not in compliance with its destination, any unauthorised disclosure, dissemination or copying, either in whole or partial, is prohibited, except express authorization.
The communications on the Internet not being secured, the sender informs that he can accept no responsibility as for the contents of this message.
To contribute to the environmental protection, thank you for printing this e-mail only in case of necessity.
    '''
    
    body_mail_dem_livraison_container = f'''
Bonjour,

Pouvez vous nous donner votre prix pour le dépotage d'un container Import et remise en place chez le client :

Lieu de Livraison chez le client: {cp_ville} {ville_destination}
Volume : {volume} m3
Container : {container}
Date / Période : {date_echeance_triglobal}

Service demandé:
Déchargement du container à résidence client en 2h pour un 20ft / 3h pour 40ft,
Pointage des colis sur la liste de colisage fournie par nos soins
Déballage des cartons fragiles et meubles,
Remontage simple des meubles (lit, étagère, armoire),
Retrait des emballages perdus
Nous vous remercions de votre réponse.



Cordialement,
Best regards,
Jean-Philippe BIARD

OPTIMUM MOBILITY
Global Mobility Solutions

Mobile: (+33) 06 61 79 45 00
Office: (+33) 09 67 24 16 14
jpbiard@optimum-mobility.com
Logo%2BOptimum%2BMobility.jpg
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Ce message et les pièces jointes éventuelles contiennent des informations confidentielles appartenant à l'expéditeur et sont établis à l'intention exclusive de ses destinataires.
Si vous recevez ce message par erreur, merci de le détruire et d'en avertir immédiatement l'expéditeur par e-mail.
Toute utilisation de ce message non conforme à sa destination, toute diffusion ou toute publication, totale ou partielle, est interdite, sauf autorisation expresse.
Les communications sur Internet n'étant pas sécurisées, l'expéditeur informe qu'il ne peut accepter aucune responsabilité quant au contenu de ce message.
Afin de contribuer au respect de l'environnement, merci de n'imprimer ce mail qu'en cas de nécessité.

This message and the possible attachments contain confidential information belonging to the sender and are intended solely for the addressees.
If you receive this message by mistake, please delete it and notify immediately the sender of it by e-mail.
Any use of this message not in compliance with its destination, any unauthorised disclosure, dissemination or copying, either in whole or partial, is prohibited, except express authorization.
The communications on the Internet not being secured, the sender informs that he can accept no responsibility as for the contents of this message.
To contribute to the environmental protection, thank you for printing this e-mail only in case of necessity.
    '''

   # try : 
    # Configuration du serveur SMTP
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls() # Sécurisation de la connexion
    server.login(adresse_mail_destinateur, mdp_adresse_mail_destinateur)

    # Envoi du mail à chaque destinataire
    for adresse_mail_destinataire_transitaire in adresses_mail_destinataires_transitaires:
        # Création du message
        message = MIMEMultipart()
        message['From'] = adresse_mail_destinateur
        message['To'] = adresse_mail_destinataire_transitaire
        message['Subject'] = f''' Demande IMPORT TC {container} de POE {ports}  à {residence_destination} '''
        message.attach(MIMEText(body_mail_dem_20ft_40ft, 'plain'))
        server.sendmail(adresse_mail_destinateur, adresse_mail_destinataire_transitaire, message.as_string())
        print(f"Email envoyé à {adresse_mail_destinataire_transitaire}")

    for adresse_mail_destinataire_transitaire_agent_livraison in adresses_mail_destinataires_agents_livraison:
        # Création du message
        message = MIMEMultipart()
        message['From'] = adresse_mail_destinateur
        message['To'] = adresse_mail_destinataire_transitaire_agent_livraison
        message['Subject'] = f''' Demande IMPORT TC {container} de POE {ports}  à {residence_destination} '''
        message.attach(MIMEText(body_mail_dem_livraison_container, 'plain'))
        server.sendmail(adresse_mail_destinateur, adresse_mail_destinataire_transitaire_agent_livraison, message.as_string())
        print(f"Email envoyé à {adresse_mail_destinataire_transitaire_agent_livraison}")

    # Fermeture de la connexion
    server.quit()
    print("Tous les emails ont été envoyés avec succès.")
    # Affichage d'un message avec les informations saisies
    messagebox.showinfo("", f"Tous les emails ont été envoyés avec succès.")


    # except Exception as e:
    #     print(f"Une erreur s'est produite lors de la connexion à la boite mail {adresse_mail_destinateur}: {e}")


# PROGRAMME PRINCIPAL 

# Création de l'interface graphique
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Envoi de Mail Demande de tarif DS")

        # Volume
        ttk.Label(self, text="Volume:").grid(row=0, column=0, padx=2, pady=5)
        self.volume_entry = ttk.Entry(self)
        self.volume_entry.grid(row=0, column=1, padx=10, pady=5)
        
        # Code Postal Origine
        ttk.Label(self, text="Code Postal Origine:").grid(row=1, column=0, padx=10, pady=5)
        self.cp_entry = ttk.Entry(self)
        self.cp_entry.grid(row=1, column=1, padx=10, pady=5)
        
        # Résidence de Destination
        ttk.Label(self, text="Résidence de Destination:").grid(row=2, column=0, padx=10, pady=5)
        self.residence_entry = ttk.Entry(self)
        self.residence_entry.grid(row=2, column=1, padx=10, pady=5)
        
        # Ville de Destination
        ttk.Label(self, text="Ville de Destination:").grid(row=3, column=0, padx=10, pady=5)
        self.ville_entry = ttk.Entry(self)
        self.ville_entry.grid(row=3, column=1, padx=10, pady=5) 

        # Date d'echeance
        ttk.Label(self, text="Date / Periode:").grid(row=4, column=0, padx=10, pady=5)
        self.date_echeance_entry = ttk.Entry(self)
        self.date_echeance_entry.grid(row=4, column=1, padx=10, pady=5)

        # Adresses Mail Destinataires Transitaires 
        ttk.Label(self, text="Adresses Mail Destinataires FOB (séparées par un espace):").grid(row=5, column=0, padx=10, pady=5)
        self.mail_entry_transitaires = ttk.Entry(self)
        self.mail_entry_transitaires.grid(row=5, column=1, padx=10, pady=5)
        
        # Adresses Mail Destinataires
        ttk.Label(self, text="Adresses Mail Destinataires AGENT LIVRAISON (séparées par un espace):").grid(row=6, column=0, padx=2, pady=5)
        self.mail_entry_agents_livraison = ttk.Entry(self)
        self.mail_entry_agents_livraison.grid(row=6, column=1, padx=10, pady=5)
        
        # Bouton Envoyer
        self.send_button = ttk.Button(self, text="Envoyer", command=self.send_mail)
        self.send_button.grid(row=7, column=0, columnspan=2, pady=10)
    
    def send_mail(self):
        volume = self.volume_entry.get()
        code_postal_origine = self.cp_entry.get()
        residence_destination = self.residence_entry.get()
        ville_destination = self.ville_entry.get()
        date_echeance_triglobal = self.date_echeance_entry.get()
        adresses_mail_destinataires_transitaires = self.mail_entry_transitaires.get().split(' ')
        adresses_mail_destinataires_agents_livraison = self.mail_entry_agents_livraison.get().split(' ')

        # identifiant du mail destinateur
        adresse_mail_destinateur = "finance@optimum-mobility.com"
        mdp_adresse_mail_destinateur = "OMfinance2406@"
        
        # Appeler la fonction envoyer_mail_DS_dem_import_20ft_40ft
        envoyer_mail_DS(volume, code_postal_origine, date_echeance_triglobal, residence_destination, ville_destination, adresse_mail_destinateur, mdp_adresse_mail_destinateur, adresses_mail_destinataires_transitaires, adresses_mail_destinataires_agents_livraison)
   

# Lancer l'application
app = App()
app.mainloop()
