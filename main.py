import imaplib

from emailparser import EmailParser
from email import policy
from email.parser import BytesParser
from credentials import Credentials
from settings import Settings
from database import Database


def read_email_from_gmail(mycredentials, mysettings, myparser, istestmode):
    listofuser = []
    mail = imaplib.IMAP4_SSL(mysettings.smtp_server)
    try:
        mail.login(mycredentials.myemail, mycredentials.mypwd)
        mail.select('inbox')

        type, data = mail.search(None, 'FROM', '"flobobca@gmail.com"')
        id_list = reversed(data[0].split())

        for num in id_list:
            rv, data = mail.fetch(num, '(RFC822)')
            if rv != 'OK':
                print("ERROR getting message", num)
                return
            msg = BytesParser(policy=policy.default).parsebytes(data[0][1])
            opres, user = myparser.parse_email(msg)
            if opres:
                listofuser.append(user)

            if istestmode:
                break
        return listofuser
    except imaplib.IMAP4.error:
        print(imaplib.IMAP4.error)


if __name__ == '__main__':
    credentials = Credentials()
    settings = Settings()
    parser = EmailParser()
    testmode = True
    listOfUserToTreat = read_email_from_gmail(credentials, settings, parser, testmode)
    if len(listOfUserToTreat) > 0:
        mydatabase = Database(listOfUserToTreat)
        mydatabase.closedb()
