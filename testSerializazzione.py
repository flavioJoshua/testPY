import pickle


def  DeSerializzazione():
    with open("pickser","rb") as _file:
        _classe=pickle.load(_file)
    return _classe


_cls=DeSerializzazione()
print(_cls)