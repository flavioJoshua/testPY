import persona,sys,os
print("il mio messaggio")

# _dict={""}
# _dict.keys()

temp=sys.stdout
try:
    sys.stdout=open("20220901_console.txt","a")


    _flavio = persona.clspersona("flavioName")
    _dev = persona.clsDevelop("flavio Develop")
    persona.clspersona.Set_static_specializzazione("nuovo valore")
    _dev.specializzazione_loc_static="test chiamata"
    _dev.Set_static_specializzazione("un valore")
    print(" il mio cognome è : {0:s}".format(  _flavio.GetCognome() ))
    print(" il mio cognome è : %s"   %  _flavio.GetCognome() )
    print(f"il mio cognome è : {_flavio.GetCognome()}")
    print(_flavio, _flavio.specializzazione_interna  , " " , _flavio.Get_specialization() ,  " statica: " , _flavio.Get_static_specializzazione())
except Exception  as ex :
    print(ex)
finally:
    sys.stdout.close()
    sys.stdout=temp
    print(_dev)
