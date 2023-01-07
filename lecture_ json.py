import json
import os
import time
# ce script met en forme un fichier json en utilisant la bibliotheque json
# le fichier est ainsi traité en tant que dictionnaire, ce qui facilite la lecture et l'extraction des données utiles
# les fichiers sources doivent être rangés dans un dossier EXEMPLE5/fichiers_source/
# le dossier EXEMPLE5 doit également contenir des sous-dossiers fichiers_detail et fichiers_entete pour l'écriture des résultats


start_time = time.time()
repertoireSource=os.getcwd() + '/EXEMPLE5/fichiers_source'
repertoireSortieDT = os.getcwd() + '/EXEMPLE5/fichiers_detail'
repertoireSortieET = os.getcwd() + '/EXEMPLE5/fichiers_entete'
for filename in os.listdir(repertoireSource):
    with open(os.path.join(repertoireSource, filename), 'r', encoding='UTF-8') as fileread:
        filewriteET = open(os.path.join(repertoireSortieET, filename.split(".")[0] + "_et1.csv"), 'w')
        filewriteDT = open(os.path.join(repertoireSortieDT, filename.split(".")[0] + "_dt1.csv"), 'w')
        d = json.loads(fileread.read())
        listTickets = d['EntreesJournalDeVente']
        for ticket in listTickets:
            if ticket['type']=='TRANSACTION_DE_VENTE':
                entete = ticket['EnTeteTicket']
                E_IdentifiantTicket = entete['IdentifiantTicket']
                E_NumeroDeCaisse = str(entete['NumeroDeCaisse'])
                E_DateHeureTicket = entete['DateHeureTicket']
                E_TypeOperation = entete['TypeOperation']
                listLignes = ticket['EnregistrementDetailDesArticlesVendus']
                for lig in listLignes:
                    D_CodeProduit = str(lig['CodeProduit'])
                    D_LibelleProduit = lig['LibelleProduit']
                    D_Quantite = "{:.2f}".format(lig['Quantite'])
                    D_TauxTVA = "{:.4f}".format(lig['TauxTVA'])
                    D_PrixUnitaireTTC = "{:.2f}".format(lig['PrixUnitaireTTC'])
                    D_MontantRemise = "0.00" if lig['MontantRemise'] == None\
                            else "{:.2f}".format(lig['MontantRemise'])
                    D_MontantLigneTTC = "{:.2f}".format(lig['MontantLigneTTC'])
                    ligneAEcrireArticle = E_IdentifiantTicket + "|" + E_NumeroDeCaisse + "|" + E_DateHeureTicket + "|" + \
                                          E_TypeOperation + "|" + \
                                          D_CodeProduit + "|" + D_LibelleProduit + "|" + \
                                          D_Quantite + "|" + D_TauxTVA + "|" + D_PrixUnitaireTTC + "|" + \
                                          D_MontantRemise + "|" + D_MontantLigneTTC

                    filewriteDT.write(ligneAEcrireArticle + "\n")
                ligneAEcrireTicket = E_IdentifiantTicket + "|" + E_NumeroDeCaisse + "|" + E_DateHeureTicket + "|" + \
                                          E_TypeOperation + "|"
                filewriteET.write(ligneAEcrireTicket + "\n")
        filewriteET.close()
        filewriteDT.close()
print("--- %s seconds ---" % (time.time() - start_time))




