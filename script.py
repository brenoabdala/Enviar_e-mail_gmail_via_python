
import smtplib
import email.message


destinatario = ['email1', 'email2', 'email3']


def enviar_email(e_mail_do_destinatario):

    corpo_email = """
  <p> Olá, boa tarde, tudo bem? </p> 
  <p> Gostaria de comunica-lo através desse e-mail que o(a) senhor(a)... </p> 
  """

    msg = email.message.Message()
    msg['Subject'] = "Assunto"
    msg['From'] = ""
    msg['to'] = e_mail_do_destinatario
    password = ""
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()

    # LOGIN CREDENDIALS FOR SENDING E-MAIL
    s.login(msg['From'], password)
    s.sendmail(msg['From'], msg['To'], msg.as_string().encode('utf-8'))


if __name__ == "__main__":
    for email_ in destinatario:
        enviar_email(email_)
