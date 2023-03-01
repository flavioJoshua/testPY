# main.py
import os
import gettext
# _ = gettext.gettext

def print_some_strings():
    print(_("Hello world"))
    print(_("This is a translatable string"))


el = gettext.translation('file', localedir='locales', languages=['us'])
el.install()
_ = el.gettext # Greek
if __name__=='__main__':
    print_some_strings()
