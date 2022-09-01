
""" documentazione  Modulo  generale  """
class clspersona ():
    """ Variabile statica"""
    specializzazione_loc_static="ND"
    """ documentazione  ctor """
    def __init__(self,nome,specializzazione="generico"):
        self.name = nome
        self.specializzazione_interna=specializzazione
        self.cognome=self.name.split()[-1]

    def __del__(self):
        print("chiusura")

        
    def __str__(self):
        return " classe clsPersona"  + self.name
    def Get_specialization(self):
        return self.specializzazione_interna
    
    """" commento Cognome  """
    def GetCognome(self):
        return self.cognome
    """ set  variabile  statica """
    @staticmethod
    def Set_static_specializzazione(varspec):
        clspersona.specializzazione_loc_static=varspec
    @staticmethod    
    def Get_static_specializzazione():
        return clspersona.specializzazione_loc_static


""" documentazione  develop """
class clsDevelop(clspersona):
    ''' documentazione  Develop Ctor. '''
    def __init__(self, nome):
        clspersona.__init__(self, nome,specializzazione="Develop")
    # def Get_specialization(self)