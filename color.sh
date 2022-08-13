
# Terminal Colors

RED="$(printf '\033[31m')"  
GREEN="$(printf '\033[32m')"  
ORANGE="$(printf '\033[33m')"  
BLUE="$(printf '\033[34m')"
MAGENTA="$(printf '\033[35m')"  
CYAN="$(printf '\033[36m')"  
WHITE="$(printf '\033[37m')" 
BLACK="$(printf '\033[30m')"


echo -e "\n${GREEN}[${BLUE}+ si vediamo ${GREEN}]${GREEN} Mip packages already installed." 
echo -e "\n${GREEN} 2 Mip packages already installed." 

# sleep 1
print "exit"
if [[ `command -v proot` ]]; then
            printf ''
        else
			echo -e "\n${GREEN}[${WHITE}+${GREEN}]${MAGENTA} Installing package : ${CYAN}proot${CYANMAGENTA}"${WHITE}
            # pkg install proot resolv-conf -y
        fi