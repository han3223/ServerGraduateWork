import logging
import smtplib
import traceback
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class EmailFactory:
    address = "vault.docs@yandex.ru"
    password = "qidgkqyiyzvqexjh"

    def __init__(self):
        pass

    def send_email(self, to_email, **kwargs):
        # Открыть и прочитать HTML-шаблон из файла
        with open('D:/Programming/NeuroApi/email_factory/code_form.html', 'r') as file:
            html_content = file.read()

        html_content = html_content.format(**kwargs)

        msg = MIMEMultipart()
        msg['From'] = self.address
        msg['To'] = to_email
        msg['Subject'] = 'Код'
        msg.attach(MIMEText(html_content))

        try:
            mailserver = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
            mailserver.set_debuglevel(False)

            mailserver.ehlo()

            mailserver.starttls()

            mailserver.ehlo()
            mailserver.login(self.address, self.password)
            mailserver.sendmail(self.address, to_email, msg.as_string())
            mailserver.quit()

            print("Письмо успешно отправлено")
        except Exception as e:
            logging.error(traceback.format_exc())
            print("Ошибка: Невозможно отправить сообщение")


