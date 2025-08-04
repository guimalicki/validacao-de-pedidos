from functions.lerDB import LerDB
from functions.enviarEmail import EnviarEmail

class Main():
    #Le a tabela
    tableAtrasados = LerDB.lerDatabase()
    print(tableAtrasados)
    
    #Envia o email
    EnviarEmail.sendEmail(tableAtrasados)