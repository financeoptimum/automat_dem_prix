import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import tkinter as tk
from tkinter import ttk, messagebox

def envoyer_mail_DTD(nom_prospect, volume, code_postal, ville_depart, ville_destination, pays_destination, date_echeance, poe_destination, adresse_mail_destinateur, mdp_adresse_mail_destinateur, noms_transitaires, adresses_mail_destinataires_transitaires, noms_agents_livraison, adresses_mail_destinataires_agents_livraison, noms_rates_request_ds, adresses_mail_rates_request_ds, notes_Dem_Emb_Export, notes_Dem_Export_Mer, notes_rates_request_ds):
   
    try:
        # Recover the container size 
        if float(volume) <= 31 : 
            container = "20ft" 
        else : 
            container = "40ft"
    except Exception as e:
        print(f"Une erreur s'est produite lors de la connexion à la boite mail {adresse_mail_destinateur}: {e}")
        messagebox.showinfo("Erreur lors de la saisie d'informations", 
                        f'''
UNE ERREUR S'EST PRODUITE. PAS D'INQUIETUDE. 

Suivez ces étapes :   
1) Rassurez-vous que la valeur du volume est bien entrée SANS unité et SANS toutes autres lettres. 
2) Rassurez-vous que les adresses mail destinataires sont bien entrés avec des ';'. 
3) Rassurez-vous que les champs obligatoires sont remplis (champs marqués par un '*').  
4) Fermer cette fenetre et reessayer. 
''')

    
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
    '''
    # affichage de la liste des fournisseurs avec leur nom
    destinataires_dem_emb_export = "\n".join([f" {i+1}. {nom_agent_livraison} EMAIL : {email}" for i, (email, nom_agent_livraison) in enumerate(zip(adresses_mail_destinataires_agents_livraison,noms_agents_livraison))])
    destinataires_dem_export_mer = "\n".join([f" {i+1}. {noms_transitaires} EMAIL : {email}" for i, email in enumerate(zip(adresses_mail_destinataires_transitaires, noms_transitaires))])
    destinataires_rates_request_destination_service = "\n".join([f" {i+1}. {noms_rates_request_ds} EMAIL : {email}" for i, email in enumerate(zip(adresses_mail_rates_request_ds, noms_rates_request_ds))])
    '''
    
    # affichage de la liste des fournisseurs 
    destinataires_dem_emb_export = "\n".join([f" {i+1}. {email}" for i, email in enumerate(adresses_mail_destinataires_agents_livraison)])
    destinataires_dem_export_mer = "\n".join([f" {i+1}. {email}" for i, email in enumerate(adresses_mail_destinataires_transitaires)])
    destinataires_rates_request_destination_service = "\n".join([f" {i+1}. {email}" for i, email in enumerate(adresses_mail_rates_request_ds)])
    

    # Corps des mails modele
    body_mail_Dem_Emb_Export = f'''
<html>
  <body>
    <p>Bonjour,</p>
    <p>Pouvez-vous nous donner votre prix pour le <strong>service d'emballage maritime</strong> suivant chez le client:</p>
    <ul>
      <li><b>Volume : {volume} m3</b></li>
      <li><b>Ville d'emballage & chargement du container:  {code_postal} {ville_depart}</b></li>
      <li>Accès Simple, 2e étage maximum supposé</li>
      <li><b>Date ou Période: {date_echeance} </b></li>

      <li><b>Service :</b></li>
      <ul>
        <li>Emballage EXPORT en CATEGORIE 2 sauf précision contraire</li>
        <li>Emballage des effets fragiles et meubles uniquement</li>
        <li>Démontage des meubles simples</li>
        <li>Étiqueter / numéroter tous les colis et remplir la liste de colisage</li>
        <li>Charger et caler les effets dans container maritime</li>
      </ul>
      <li><b>Spécial : </b></li>
      <li><b>Notes</b> : {notes_Dem_Emb_Export}</li>
    </ul>
    <p>Merci de votre retour.</p>
    <p>Cordialement,</p>
    <br>

    <p><b>Rates Department</b></p>
    <br>
    <div style="margin-top: 10px;">
        <p>OPTIMUM MOBILITY<br> Global Mobility Solutions</p>
        <p>Phone: (+33) 09 67 24 16 14</p>
        <p>Email: <a href="mailto:rates@optimum-mobility.com">rates@optimum-mobility.com</a></p>
    </div>
  </body>
</html>
'''
    
    body_mail_Dem_Export_Mer = f'''
<html>
  <body>
    <p>Bonjour,</p>
    <p>Pouvez-vous nous donner votre prix pour le posit, douane export et fret suivant:</p>
    <ul>
      <li><b>Container : {container} </b></li>
      <li><b>Origine : {code_postal} {ville_depart}</b></li>
      <li><b>Destination POE : {poe_destination}</b></li>
      <li><b>Ville de destination : {ville_destination} </b></li> 
      <li><b>Pays de destination : {pays_destination} </b></li>
      <li><b>Notes</b>: {notes_Dem_Export_Mer}</li>
    </ul>
    <p>Veuillez préciser Transit time, compagnie, validité fret, surcharges cas échéant, DTHC en option.</p>
    <p>Je vous remercie.</p>
    <p>Cordialement,</p>
    <p><b>Rates Department</b></p>
    <br>
        <p>OPTIMUM MOBILITY<br> Global Mobility Solutions</p>
        <p>Phone: (+33) 09 67 24 16 14</p>
        <p>Email: <a href="mailto:rates@optimum-mobility.com">rates@optimum-mobility.com</a></p>
    </div>
  </body>
</html>
'''
    
    body_mail_rates_request_destination_service = f'''
<html>
  <body>
    <p>Dear Colleague,</p>
    <p>We hope that our mail finds you well.</p>
    <p>Please send your best <b>DESTINATION SERVICE</b> rate for the below shipment :</p>
    <ul>
      <li><b>Volume : {volume} cbm in {container} </b></li>
      <li><b>From Best POE</b> : please advise</li>
      <li><b>To Client Residence : {ville_destination}, {pays_destination}</b></li>
      <li><b>Notes</b>: {notes_rates_request_ds}</li>
    </ul>
    <p>Service required for Destination service:</p>
    <ul>
      <li>Customs clearance</li>
      <li>Transport container to client residence</li>
      <li>Unloading, unpacking fragile items & furniture, normal & simple reassembly, removing the debris</li>
      <li>Transport container back to port or terminal</li>
      <li>Special : NONE</li>
    </ul>
    <p>Please advise besides your rate for Destination Service:</p>
    <ul>
      <li>Needed documents for clearance and customs process</li>
      <li>Restricted / forbidden items</li>
      <li>Additional charges if applicable:</li>
      <ul>
        <li>Mandatory if any expected : ISF filling, chassis, parking permit, port due,</li>
        <li>Other possible : DTHC, physical inspection, duties & taxes,... etc.</li>
      </ul>
    </ul>
    <p>Thank you for your reply.</p>
    <p>Cordialement,</p>
    <br>
    <p>Best regards,</p>
    <p><b>Rates Department</b></p>
    <br>
    <div style="margin-top: 10px;">
        <p>OPTIMUM MOBILITY<br> Global Mobility Solutions</p>
        <p>Phone: (+33) 09 67 24 16 14</p>
        <p>Email: <a href="mailto:rates@optimum-mobility.com">rates@optimum-mobility.com</a></p>
    </div>
  </body>
</html>'''

    try : 
        messagebox.showinfo("Recapitulatif des informations", 
                        f'''
RECAPITULATIF Demande de tarif DTD : 

NOM DU PROSPECT : {nom_prospect}

Pour les mails DEM_EMB_EXPORT :
==============================
Volume en m3 : {volume}
Code postal : {code_postal}
Ville de départ : {ville_depart}
Date / Période : {date_echeance}
Notes : {notes_Dem_Emb_Export}
Liste des destinataires : \n {destinataires_dem_emb_export}

Pour les mails DEM_EXPORT_MER :
==============================
container : {container}
Origine : {code_postal} {ville_depart}
Destination POE : {poe_destination}
Ville de destination : {ville_destination}
Pays de destination : {pays_destination}
Notes : {notes_Dem_Export_Mer}
Liste des destinataires : \n {destinataires_dem_export_mer}

Pour les mails Rates Request Destination Service :
==============================
Volume en m3 : {volume}
Ville de destination : {ville_destination}
Pays de destination : {pays_destination}
Notes : {notes_rates_request_ds}
Liste des destinataires : \n {destinataires_rates_request_destination_service}
''')
        
        # Configuration du serveur SMTP
        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls() # Sécurisation de la connexion
        server.login(adresse_mail_destinateur, mdp_adresse_mail_destinateur)

        
        if(adresses_mail_destinataires_agents_livraison != ['']):
          # Envoi du mail à chaque agent livraison FR (DEM_EMB_EXPORT)
          for adresse_mail_destinataire_agent_livraison in adresses_mail_destinataires_agents_livraison:
              # Création du message
              message = MIMEMultipart()
              message['From'] = adresse_mail_destinateur
              message['To'] = adresse_mail_destinataire_agent_livraison
              message['Subject'] = f''' Ref. {nom_prospect} / {ville_depart} / Demande de Prix Emballage Maritime'''
              message.attach(MIMEText(body_mail_Dem_Emb_Export, 'html'))
              server.sendmail(adresse_mail_destinateur, adresse_mail_destinataire_agent_livraison, message.as_string())
              print(f"Email envoyé à {adresse_mail_destinataire_agent_livraison}")

        if(adresses_mail_destinataires_transitaires != ['']):
          # Envoi du mail aux transitaires (Dem_Export_Mer : Demande Fret Export 20ft OU 40ft)
          for adresse_mail_destinataire_transitaire in adresses_mail_destinataires_transitaires:
              # Création du message
              message = MIMEMultipart()
              message['From'] = adresse_mail_destinateur
              message['To'] = adresse_mail_destinataire_transitaire
              message['Subject'] = f''' Ref. {nom_prospect} / Demande Fret Export {container} : de {code_postal} {ville_depart}'''
              message.attach(MIMEText(body_mail_Dem_Export_Mer, 'html'))
              server.sendmail(adresse_mail_destinateur, adresse_mail_destinataire_transitaire, message.as_string())
              print(f"Email envoyé à {adresse_mail_destinataire_transitaire}")

        
        # Envoi de mail aux agents rates requests ds (Rate request : Destination Service)
        for adresse_mail_rates_request_ds in adresses_mail_rates_request_ds:
            # Création du message
            message = MIMEMultipart()
            message['From'] = adresse_mail_destinateur
            message['To'] = adresse_mail_rates_request_ds
            message['Subject'] = f'''{nom_prospect} / {ville_destination} / Optimum Mobility Rate request : Destination Service'''
            message.attach(MIMEText(body_mail_rates_request_destination_service, 'html'))
            server.sendmail(adresse_mail_destinateur, adresse_mail_rates_request_ds, message.as_string())
            print(f"Email envoyé à {adresse_mail_rates_request_ds}")

        # Fermeture de la connexion
        server.quit()
        print("Tous les emails ont été envoyés avec succès.")
        # Affichage d'un message avec les informations saisies
        messagebox.showinfo("", f"Tous les emails ont été envoyés avec succès.")


    except Exception as e:
        print(f"Une erreur s'est produite lors de la connexion à la boite mail {adresse_mail_destinateur}: {e}")
        messagebox.showinfo("Erreur lors de la saisie d'informations", 
                        f'''
UNE ERREUR S'EST PRODUITE. PAS D'INQUIETUDE. 

Suivez ces étapes :   
1) Rassurez-vous que la valeur du volume est bien entrée SANS unité et SANS toutes autres lettres. 
2) Rassurez-vous que les adresses mail destinataires sont bien entrés avec des ';'. 
3) Rassurez-vous que les champs obligatoires sont remplis (champs marqués par un '*').  
4) Fermer cette fenetre et reessayer. 
''')


# PROGRAMME PRINCIPAL 

# Création de l'interface graphique
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Envoi de Mail Demande de tarif DTD")


        destinataires_dem_emb_export = "\n".join([f" {i+1}. {nom_agent_livraison} EMAIL : {email}" for i, (email, nom_agent_livraison) in enumerate(zip(adresses_mail_destinataires_agents_livraison,noms_agents_livraison))])
        destinataires_dem_export_mer = "\n".join([f" {i+1}. {noms_transitaires} EMAIL : {email}" for i, email in enumerate(zip(adresses_mail_destinataires_agents_livraison, noms_transitaires))])
        destinataires_rates_request_destination_service = "\n".join([f" {i+1}. {noms_rates_request_ds} EMAIL : {email}" for i, email in enumerate(zip(adresses_mail_destinataires_agents_livraison, noms_rates_request_ds))])


        # Nom du prospect
        ttk.Label(self, text="1) Nom du prospect :").grid(row=0, column=0, padx=10, pady=5, sticky='w')
        self.prospect_entry = ttk.Entry(self)
        self.prospect_entry.grid(row=0, column=1, padx=10, pady=5)

        # Volume
        ttk.Label(self, text="2) Volume (en m3)* :").grid(row=1, column=0, padx=10, pady=5, sticky='w')
        self.volume_entry = ttk.Entry(self)
        self.volume_entry.grid(row=1, column=1, padx=10, pady=5)
        
        # Code Postal Origine
        ttk.Label(self, text="3) Code Postal :").grid(row=2, column=0, padx=10, pady=5, sticky='w')
        self.cp_entry = ttk.Entry(self)
        self.cp_entry.grid(row=2, column=1, padx=10, pady=5)
        
        # Ville d'origine
        ttk.Label(self, text="4) Ville d'origine :").grid(row=3, column=0, padx=10, pady=5, sticky='w')
        self.ville_depart_entry = ttk.Entry(self)
        self.ville_depart_entry.grid(row=3, column=1, padx=10, pady=5)
        
        # POE
        ttk.Label(self, text="5) POE de destination (si connu) :").grid(row=4, column=0, padx=10, pady=5, sticky='w')
        self.poe_destination = ttk.Entry(self)
        self.poe_destination.grid(row=4, column=1, padx=10, pady=5) 

        # Ville de Destination
        ttk.Label(self, text="6) Ville de Destination :").grid(row=5, column=0, padx=10, pady=5, sticky='w')
        self.ville_dest_entry = ttk.Entry(self)
        self.ville_dest_entry.grid(row=5, column=1, padx=10, pady=5)

        # Pays de Destination
        ttk.Label(self, text="7) Pays de Destination :").grid(row=6, column=0, padx=10, pady=5, sticky='w')
        self.pays_dest_entry = ttk.Entry(self)
        self.pays_dest_entry.grid(row=6, column=1, padx=10, pady=5) 

        # Date d'echeance
        ttk.Label(self, text="8) Date / Periode emballage :").grid(row=7, column=0, padx=10, pady=5, sticky='w')
        self.date_echeance_entry = ttk.Entry(self)
        self.date_echeance_entry.grid(row=7, column=1, padx=10, pady=5)

        # Notes supplementaires - Dem_Emb_Export 
        ttk.Label(self, text="9) Note pour l'équipe d'emballage :").grid(row=8, column=0, padx=10, pady=5, sticky='w')
        self.notes_Dem_Emb_Export = tk.Text(self, width=25, height=1)
        self.notes_Dem_Emb_Export.grid(row=8, column=1, padx=10, pady=5)

        # Listes des adresses mails agents livraison pour Demande d'emballage Export  
        ttk.Label(self, text="10)  Liste destinataires Agent FR Emballage (séparés d'un ';') :").grid(row=9, column=0, padx=10, pady=5, sticky='w')
        self.adresses_mail_agent_livraison_entry = ttk.Entry(self, width=50)
        self.adresses_mail_agent_livraison_entry.grid(row=9, column=1, padx=10, pady=5)

#         # Listes des adresses mails agents livraison pour Demande d'emballage Export  
#         ttk.Label(self, text=
#                   f'''
# 10)  Voici la liste des agents de livraison FR destinataires actuellement présents : 
# {destinataires_dem_emb_export} 
# Voulez-vous ajouter des agents de livraison FR ? 
# Si oui, remplir le champ avec leur adresse mail à chaque fois suivi d'un espace. Si non, veuillez ne pas remplir ce champ.''').grid(row=9, column=0, padx=10, pady=5, sticky='w')
#         self.notes_Dem_Emb_Export = tk.Text(self, width=50, height=1)
#         self.notes_Dem_Emb_Export.grid(row=9, column=1, padx=10, pady=5)

        
        # Notes supplementaires - Dem_Export_Mer
        ttk.Label(self, text="11) Note pour la demande au transitaire :").grid(row=10, column=0, padx=10, pady=5, sticky='w')
        self.notes_Dem_Export_Mer = tk.Text(self, width=25, height=1)
        self.notes_Dem_Export_Mer.grid(row=10, column=1, padx=10, pady=5)

        # Listes des adresses mails agents livraison pour Demande d'Export Maritime  
        ttk.Label(self, text="12) Liste destinataires transitaires (séparés d'un ';') :").grid(row=11, column=0, padx=10, pady=5, sticky='w')
        self.adresses_mail_transitaire_entry = ttk.Entry(self, width=50)
        self.adresses_mail_transitaire_entry.grid(row=11, column=1, padx=10, pady=5)

#         # Listes des adresses mails agents livraison pour Demande d'emballage Export  
#         ttk.Label(self, text=
#                   f'''
# 10)  Voici la liste des agents de livraison FR destinataires actuellement présents : 
# {destinataires_dem_emb_export} 
# Voulez-vous ajouter des agents de livraison FR ? 
# Si oui, remplir le champ avec leur adresse mail à chaque fois suivi d'un espace. Si non, veuillez ne pas remplir ce champ.''').grid(row=9, column=0, padx=10, pady=5, sticky='w')
#         self.notes_Dem_Emb_Export = tk.Text(self, width=50, height=1)
#         self.notes_Dem_Emb_Export.grid(row=9, column=1, padx=10, pady=5)


        # Notes supplementaires - Rates_Request_Destination_Service
        ttk.Label(self, text="13) Note pour la demande aux agents destination :").grid(row=12, column=0, padx=10, pady=5, sticky='w')
        self.notes_Rates_Request_Destination_Service = tk.Text(self, width=25, height=1)
        self.notes_Rates_Request_Destination_Service.grid(row=12, column=1, padx=10, pady=5)

        # Listes des adresses mails agents livraison pour Demande d'Export Maritime  
        ttk.Label(self, text="14) Liste destinataires agents destination (séparés d'un ';') :").grid(row=13, column=0, padx=10, pady=5, sticky='w')
        self.adresses_mail_agent_etranger_entry = ttk.Entry(self, width=50)
        self.adresses_mail_agent_etranger_entry.grid(row=13, column=1, padx=10, pady=5)
        
        # Bouton Envoyer
        self.send_button = ttk.Button(self, text="Envoyer", command=self.send_mail)
        self.send_button.grid(row=14, column=0, columnspan=2, pady=10)
    
    def send_mail(self):

        nom_prospect = self.prospect_entry.get()
        volume = self.volume_entry.get()
        code_postal = self.cp_entry.get()
        ville_depart = self.ville_depart_entry.get()
        ville_destination = self.ville_dest_entry.get()
        pays_destination = self.pays_dest_entry.get()
        poe_destination = self.poe_destination.get()
        notes_Dem_Emb_Export = self.notes_Dem_Emb_Export.get("1.0", tk.END).strip()
        
        adresses_mail_destinataires_agents_livraison = self.adresses_mail_agent_livraison_entry.get().split(';')
        print("Les adresses agents livraison : \n", adresses_mail_destinataires_agents_livraison)
        adresses_mail_destinataires_transitaires = self.adresses_mail_transitaire_entry.get().split(';')
        print("Les adresses transitaires : \n", adresses_mail_destinataires_transitaires)

        adresses_mail_rates_request_ds = self.adresses_mail_agent_etranger_entry.get().split(';')
        
        notes_Dem_Export_Mer = self.notes_Dem_Export_Mer.get("1.0", tk.END).strip()
        notes_Rates_Request_Destination_Service = self.notes_Rates_Request_Destination_Service.get("1.0", tk.END).strip()
        date_echeance_triglobal = self.date_echeance_entry.get()

        

        # identifiant du mail destinateur
        adresse_mail_destinateur = "rates@optimum-mobility.com"
        mdp_adresse_mail_destinateur = "OM@rates@2406"
        
        # Appeler la fonction envoyer_mail_DS_dem_import_20ft_40ft
        envoyer_mail_DTD(nom_prospect, volume, code_postal, ville_depart, ville_destination, pays_destination, date_echeance_triglobal, poe_destination, adresse_mail_destinateur, mdp_adresse_mail_destinateur, noms_transitaires, adresses_mail_destinataires_transitaires, noms_agents_livraison, adresses_mail_destinataires_agents_livraison, noms_rates_request_ds, adresses_mail_rates_request_ds, notes_Dem_Emb_Export, notes_Dem_Export_Mer, notes_Rates_Request_Destination_Service)
   


# Lancer l'application
adresses_mail_destinataires_transitaires = []
noms_transitaires = ["finance", "rates"]
adresses_mail_destinataires_agents_livraison = []
noms_agents_livraison = ["finance", "rates"]
adresses_mail_rates_request_ds = []
noms_rates_request_ds = ["finance", "rates"]

app = App()
app.mainloop()
