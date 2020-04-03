class Auser:

    def __init__(self):
        self.name = ""
        self.email = ""
        self.adresse = ""
        self.tel = ""
        self.course = False
        self.brico = False
        self.periso = False
        self.scolaire = False
        self.autre = ""
        self.quartier = ""

    def setname(self, name):
        self.name = name

    def setemail(self, email):
        self.email = email

    def seteadresse(self, adresse):
        self.adresse = adresse

    def setetel(self, tel):
        self.tel = tel

    def setquartier(self, quartier):
        self.quartier = quartier

    def setactivity(self, msg):
        if msg.find("courses") != -1:
            self.course = True

        if msg.find("bricolage") != -1:
            self.brico = True

        if msg.find("isolées") != -1:
            self.periso = True

        if msg.find("Scolaire") != -1:
            self.scolaire = True

        if msg.find("ou :") != -1:
            self.autre = msg[msg.find("ou :") + len("ou :"):len(msg)]

    def setlineparame(self, keyword, valuetoset):
        if keyword == 'De :':
            self.setname(valuetoset)
        elif keyword == 'email :':
            self.setemail(valuetoset)
        elif keyword == 'Adresse :':
            self.seteadresse(valuetoset)
        elif keyword == 'Téléphone :':
            self.setetel(valuetoset)
        elif keyword == 'Quartier :':
            self.setquartier(valuetoset)
