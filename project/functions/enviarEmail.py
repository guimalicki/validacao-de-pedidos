import smtplib
import email.message
import datetime
import pandas
import os
from dotenv import load_dotenv

class EnviarEmail:
    def sendEmail(lista):
        
        load_dotenv(override=True)
        
        if lista.empty:
            print("Nenhuma informação em 'lista'. E-mail não será enviado.")
            return
        
        # Criar a lista HTML com os valores de Nro.Nota
        notas_list = "".join(f"<li>{int(nota)}</li>" for nota in lista['Nro.Nota'])
        corpo_email = f""""
        <h2> Atencao! </h2>
        <p>As notas abaixo consta com atraso. Por favor, validar o motivo!</p>
        <h3>Notas</h3>
        <ul>
        {notas_list}
        </ul>"""

        msg = email.message.Message()
        msg['Subject'] = f"Nota(s) com atraso!!!"
        msg['From'] = os.getenv("FROM")
        msg['To'] = 'kailainy.souza@seugil.com, guilherme.barbosa@seugil.com, transporte@seugil.com'
        password = os.getenv("PASSWORD")
        msg.add_header('Content-Type', "text/html")
        msg.set_payload(corpo_email)

        # Dividir e limpar os endereços de e-mail
        destinatarios = [email.strip() for email in msg['To'].split(',')]
        s = smtplib.SMTP('smtp.gmail.com: 587')
        s.starttls()
        #Login com suas credenciais
        s.login(msg['From'], password)
        s.sendmail(msg['From'], destinatarios, msg.as_string().encode('utf-8'))
        print('Email enviado')