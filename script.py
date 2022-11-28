
import smtplib
import email.message


def enviar_email():
    NOME = ''

    corpo_email = """
  <p> Olá {NOME}, boa tarde, tudo bem? </p> 
  <p> Gostaria de comunica-lo através desse e-mail que o(a) senhor(a)... </p> 
  """

    msg = email.message.Message()
    msg['Subject'] = "Assunto"
    msg['From'] = " e-mail de origem"
    msg['to'] = "destinatário"
    password = "código gerado no G-MAIL"
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()

    # LOGIN CREDENDIALS FOR SENDING E-MAIL
    s.login(msg['From'], password)
    s.sendmail(msg['From'], msg['To'], msg.as_string().encode('utf-8'))
    print('E-mail enviado')


if __name__ == "__main__":
    enviar_email()
