import sys
from userModel import Auser


class EmailParser:

    def __init__(self):
        pass

    def get_info_from_line(self, line, keyword, myuser):
        if line.find(keyword) != -1:
            myuser.setlineparame(keyword, line[len(keyword):len(line)].strip())

    def get_all_line_info(self, line, myuser):
        self.get_info_from_line(line, 'De :', myuser)
        self.get_info_from_line(line, 'email :', myuser)
        self.get_info_from_line(line, 'Adresse :', myuser)
        self.get_info_from_line(line, 'Téléphone :', myuser)
        self.get_info_from_line(line, 'Quartier :', myuser)

    def get_activities(self, msg, startflag, endflag, myuser):
        if msg.find(startflag) != -1:
            if msg.find(endflag) != -1:
                myuser.setactivity(msg[msg.find(startflag) + len(startflag):msg.find(endflag)].strip())

    def parse_email(self, msg):
        result = False
        msgtoparse = msg.get_body()
        myuser = Auser()
        if msgtoparse['content-type'].maintype == 'text':
            if msgtoparse['content-type'].subtype == 'plain':
                self.get_activities(msgtoparse.get_content(), "Objet : Inscription Volontaires", "Note : ", myuser)
                for line in msgtoparse.get_content().splitlines():
                    self.get_all_line_info(line, myuser)
                result = True
            elif msgtoparse['content-type'].subtype == 'html':
                print("Don't know how to display - Requires extra work")
            else:
                print("Don't know how to display {}".format(msgtoparse.get_content_type()))
                sys.exit()
        else:
            print("Don't know how to display {}".format(msgtoparse.get_content_type()))
            sys.exit()
        return result, myuser
