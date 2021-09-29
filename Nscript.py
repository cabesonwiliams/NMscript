import os
import colorama
import time
from colorama import Fore
import sys
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

############### Banner ###############
banner2 =  Fore.BLUE + """

▄████▄   ▄▄▄       ▄▄▄▄   ▓█████   ██████  ▒█████   ███▄    █      ██████  ██▓ ███▄    █    ▒███████▒
▒██▀ ▀█  ▒████▄    ▓█████▄ ▓█   ▀ ▒██    ▒ ▒██▒  ██▒ ██ ▀█   █    ▒██    ▒ ▓██▒ ██ ▀█   █    ▒ ▒ ▒ ▄▀░
▒▓█    ▄ ▒██  ▀█▄  ▒██▒ ▄██▒███   ░ ▓██▄   ▒██░  ██▒▓██  ▀█ ██▒   ░ ▓██▄   ▒██▒▓██  ▀█ ██▒   ░ ▒ ▄▀▒░
▒▓▓▄ ▄██▒░██▄▄▄▄██ ▒██░█▀  ▒▓█  ▄   ▒   ██▒▒██   ██░▓██▒  ▐▌██▒     ▒   ██▒░██░▓██▒  ▐▌██▒     ▄▀▒   ░
▒ ▓███▀ ░ ▓█   ▓██▒░▓█  ▀█▓░▒████▒▒██████▒▒░ ████▓▒░▒██░   ▓██░   ▒██████▒▒░██░▒██░   ▓██░   ▒███████▒
░ ░▒ ▒  ░ ▒▒   ▓▒█░░▒▓███▀▒░░ ▒░ ░▒ ▒▓▒ ▒ ░░ ▒░▒░▒░ ░ ▒░   ▒ ▒    ▒ ▒▓▒ ▒ ░░▓  ░ ▒░   ▒ ▒    ░▒▒ ▓░▒░▒
  ░  ▒     ▒   ▒▒ ░▒░▒   ░  ░ ░  ░░ ░▒  ░ ░  ░ ▒ ▒░ ░ ░░   ░ ▒░   ░ ░▒  ░ ░ ▒ ░░ ░░   ░ ▒░   ░░▒ ▒ ░ ▒
░          ░   ▒    ░    ░    ░   ░  ░  ░  ░ ░ ░ ▒     ░   ░ ░    ░  ░  ░   ▒ ░   ░   ░ ░    ░ ░ ░ ░ ░
░ ░            ░  ░ ░         ░  ░      ░      ░ ░           ░          ░   ░           ░      ░ ░
░                        ░                                                                   ░


 """
banner = Fore.BLUE + """

                            ,                                            
                                    *#    @                                     
                                      @/   @&                                   
                                       @@%  %@&                                 
                         (@@&.  @@@     (@@@ .@@@                               
                   @@@@@@@@@@@@@@@@@@@@#. @@@@.%@@@.                            
                .*%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#                          
             .@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@/                       
            ,@@@@@@@@@@@&*           .%@@@@@@@@@@@@@@@@@@@@.                    
         @@@@@@@@@@@@*                     %@@@@@@@@@@@@@@@@@/                  
           (@@@@@@@#                          /@@@@@@@@@@@.@@@@                 
         .@@@@@@@@#                              @@@@@@@@@@(,@@@%               
        @@@@@@@@@@,                                @@@@@@@@@@@@@@@.             
           @@@@@@@#                                  @@@@@@@@@@@@@,             
          /@@@@@@@@%                                    (@@@@@@@@@@.            
          @%.&@@@@@@@.                                      &@@@@@@@@/          
              @@@@@@@@@*                                       @@@@@@@@@%       
              *@@#@@@@@@@@,                                      @@@@@@@@*      
                    (@@@@@@@@&                                    @@@@@@        
                        (@@@@@@@@@/                              ,@@@.          
                            .&@@@@@@@@@%                                        
                                  *@@@@@@@@@*                                   
                                        %@@@@@@&                                
                                            .@@@@@%                             
                                                (@@@&                           
                                                   @@@.                         
                                                     @@/                        
                                                      &@                        
                                                       &                        
                                                       .      
 __________________________________________________________________________________________ 
 |                                                                                        |
 | [0] Coded By cabeson sin z                                                         [0] | 
 | [0] Youtube - cabeson sin z - https://youtube.com/channel/UCyxot7tzc9MO10KUjtZLEVA [0] |
 | [0] Github  - https://github.com/cabesonwiliams                                    [0] |
 |________________________________________________________________________________________|
"""

############### Banner ###############

 # coded by  cabeson sin z!

############### Nmap code ###############



def nmap():
    os.system("clear")
    print(banner2)
    time.sleep(0.30)
    os.system('cls')
    print(banner)
    time.sleep(1)
    print (Fore.BLUE + "  _________________________________________________________________________________________ ")
    print (Fore.BLUE + " | [0] Nmap help                                                                           |")
    time.sleep(0.20)
    print (Fore.BLUE + " | [1] Scanear 1000 puertos famosos                                                        |")
    time.sleep(0.20)
    print (Fore.BLUE + " | [2] Scanear todos los puertos existentes                                                |")
    time.sleep(0.20)
    print (Fore.BLUE + " | [3] Escaneo de servicios estandar                                                       |")
    time.sleep(0.20)
    print (Fore.BLUE + " | [4] Escaneo de servicios agreviso                                                       |")
    time.sleep(0.20)
    print (Fore.BLUE + " | [5] Scan Detallado                                                                      |")
    time.sleep(0.20)
    print (Fore.BLUE + " | [6] Scanear de OS                                                                       |")
    time.sleep(0.20)
    print (Fore.BLUE + " | [7] Scanear SubRed                                                                      |")
    time.sleep(0.20)
    print (Fore.BLUE + " | [8] Scanear un solo puerto                                                              |")
    time.sleep(0.20)
    print (Fore.BLUE + " | [9] Scaneo silencioso - No deja rastros en el servidor...                               |")
    time.sleep(0.20)
    print (Fore.BLUE + " | [10] Host activos en la web + trace route (RH)                                          |") 
    time.sleep(0.20)
    print (Fore.BLUE + " | [11] Host activos en una red (LH)                                                       |") 
    time.sleep(0.20)
    print (Fore.BLUE + " | [12] Identificar Ip                                                                     |")
    time.sleep(0.20)
    print (Fore.BLUE + " | [13] Confundir al firewall para que suelte datos importantes                            |") 
    time.sleep(0.20)
    print (Fore.BLUE + " | [14] Utilizar seÃ±uelos - para que un IDS no nos detecte - Host fake                    |")  
    time.sleep(0.20)
    print (Fore.BLUE + " | [15] Detectar Firewall                                                                  |")
    time.sleep(0.20)
    print (Fore.BLUE + " | [16] Deteccion de Firewall exacta                                                       |")
    time.sleep(0.20)
    print (Fore.BLUE + " | [17] Escaneo agresivo - Puede dejar rastros en el servidor                              |")
    time.sleep(0.20)
    print (Fore.BLUE + " | [18] Escanear todos los puertos - [TCP]                                                 |")
    time.sleep(0.20)
    print (Fore.BLUE + " | [19] Escanear todos los puertos - [UDP]                                                 |")
    time.sleep(0.20)
    print (Fore.BLUE + " | [20] Mandar paquetes ICMP                                                               |")
    time.sleep(0.20)
    print (Fore.BLUE + " |_________________________________________________________________________________________|")
    time.sleep(0.20)
    print (Fore.BLUE + " |                                                                                         |")
    time.sleep(0.20)
    print (Fore.BLUE + " | [001] FTP brute force  -- (Script usado para la fuerza bruta en el protocolo ftp)       |")
    time.sleep(0.20)
    print (Fore.BLUE + " | [002] Safe script nmap -- (Script que permite un escaneo silencioso)                    |")
    time.sleep(0.20)
    print (Fore.BLUE + " | [003] Vuln script --  (Script que busca vulnerabilidades)                               |")
    time.sleep(0.20)
    print (Fore.BLUE + " | [004] Dns Search --  (Script utilizado para la busqueda de subdominios)                 |")
    time.sleep(0.20)
    print (Fore.BLUE + " | [005] MySql DB -- (Script que nos permite buscar contrasenias en servicios mysql)       |")
    time.sleep(0.20)
    print (Fore.BLUE + " | [000] Salir                                                                             |")
    time.sleep(0.20)
    print (Fore.BLUE + " |_________________________________________________________________________________________|")
    time.sleep(0.20)
    print("")

  ######################## All opciones - Nmap ##########################

    opcion = input(Fore.BLUE + ' Seleciona una opcion\n >> ')
    if opcion == "1":
        os.system("clear")
        print(banner)
        normal = input(Fore.BLUE + "Que ip quieres scanear?\n>> " "")
        print(Fore.BLUE)
        os.system("nmap --top-ports 1000 " + (normal))
        time.sleep(15)
        input(Fore.BLUE + 'Presiona Cualquier Letra Para Volver Al Menu\n>> ') 
        nmap()

 ######################## Opcion 2 ##########################

    elif opcion == "2":
        os.system("clear")
        print(banner)
        psa = input(Fore.BLUE + "Introduzca una IP\n>> " "")
        os.system("nmap -p- " + (psa))
        time.sleep(15)
        input(Fore.BLUE + 'Presiona Cualquier Letra Para Volver Al Menu\n>> ') 
        nmap()

 ######################## Opcion 3 ##########################

    elif opcion == "4":
        os.system("clear")
        print(banner)
        agresivo = input(Fore.BLUE + "Introduzca una ip u pagina web ( e.j https://googlesource.com )\n>> ")
        os.system("nmap -sV -T5"+agresivo)
        time.sleep(15)
        input(Fore.BLUE + 'Presiona Cualquier Letra Para Volver Al Menu\n>> ') 
        nmap()

 ######################## Opcion 4 ##########################

    elif opcion == "3":
        os.system("clear")
        print(banner)
        normal = input(Fore.BLUE + "Introduzca una ip u pagina web ( e.j https://googlesource.com )\n>> ")      
        os.system("nmap -sV  "+normal)  
        time.sleep(15)
        input(Fore.BLUE + 'Presiona Cualquier Letra Para Volver Al Menu\n>> ') 
        nmap()

 ######################## Opcion 5 ##########################

    elif opcion == "5":
        os.system("clear")
        print(banner)
        s = input(Fore.BLUE + "Introduzca una ip\n>> ")
        os.system(f'nmap -Pn -A  {s}')
        time.sleep(15)
        input(Fore.BLUE + 'Presiona Cualquier Letra Para Volver Al Menu\n>> ') 
        nmap()

 ######################## Opcion 6 ##########################

    elif opcion == "6":
        os.system("clear")
        print(banner)
        systemx4 = input(Fore.BLUE + "Introduzca una ip u pagina web ( e.j https://googlesource.com )\n>> ")
        os.system("nmap -O "+systemx4)
        time.sleep(15)
        input(Fore.BLUE + 'Presiona Cualquier Letra Para Volver Al Menu\n>> ') 
        nmap()

 ######################## Opcion 7 ##########################

    elif opcion == "7":
        os.system("clear")
        print(banner)
        subred = input(Fore.BLUE + "Introduzca una ip\n>> ")
        puertoSub = input(Fore.BLUE + "Introduzca un puerto ( usar abajo del 32 )\n>> ")
        os.system(f'nmap -sP {subred}/{puertoSub}')
        time.sleep(15)
        input(Fore.BLUE + 'Presiona Cualquier Letra Para Volver Al Menu\n>> ') 
        nmap()

 ######################## Opcion 8 ##########################

    elif opcion == "8":
        os.system("clear")
        print(banner)
        ip = (input(Fore.BLUE + "Introduzca una Ip \n>> "))
        port = str(input(Fore.BLUE + "Introduzca un puerto \n>> "))
        os.system(f'nmap -p{port} {ip} ')
        time.sleep(15)
        input(Fore.BLUE + 'Presiona Cualquier Letra Para Volver Al Menu\n>> ') 
        nmap()

 ######################## Opcion 9 ##########################

    elif opcion == "9":
        os.system("clear")
        print(banner)
        ipyp = input(Fore.BLUE + "Introduzca una ip\n>> ")
        print(Fore.BLUE)
        os.system(f'nmap -sS -O {ipyp}')
        time.sleep(15)
        input(Fore.BLUE + 'Presiona Cualquier Letra Para Volver Al Menu\n>> ') 
        nmap() 

 ######################## Opcion 10 ##########################

    elif opcion == "10":
        os.system("clear")
        print(banner)
        slut = input(Fore.BLUE + "Introduzca una ip u pagina web ( e.j https://googlesource.com )\n>> ")
        os.system(f'nmap -sn --packet-trace --send-ip -v {slut}')
        time.sleep(15)
        input(Fore.BLUE + 'Presiona Cualquier Letra Para Volver Al Menu\n>> ') 
        nmap() 

 ######################## Opcion 11 ##########################

    elif opcion == "11":
        os.system("clear")
        print(banner)
        njs = input(Fore.BLUE + "Introduzca una ip\n>> ")         
        os.system(f'nmap -sn -v {njs}')
        time.sleep(15)
        input(Fore.BLUE + 'Presiona Cualquier Letra Para Volver Al Menu\n>> ')
        nmap()

 ######################## Opcion 12 ##########################

    elif opcion == "12":
        os.system("clear")
        print(banner)
        ping = input(Fore.BLUE + ("Introduzca una pagina web ( e.j https://googlesource.com )\n>> "))
        os.system(f'ping {ping}')
        time.sleep(15)
        input(Fore.BLUE + 'Presiona Cualquier Letra Para Volver Al Menu\n>> ')
        nmap()

 ######################## Opcion 13 ##########################

    elif opcion == "13":
        os.system("clear")
        print(banner)
        ConfundirFirewall = input(Fore.BLUE + ("Introduzca una ip\n>> "))
        os.system(f' nmap --mtu 24 -sV {ConfundirFirewall}')
        time.sleep(15)
        input(Fore.BLUE + 'Presiona Cualquier Letra Para Volver Al Menu\n>> ')
        nmap()

 ######################## Opcion 14 ##########################

    elif opcion == "14":
        os.system("clear")
        print(banner)
        senuelo = input(Fore.BLUE + ("Introduzca una ip\n>> "))
        os.system(f'nmap -n -D 172.67.131.21,104.21.3.183 {senuelo}')
        time.sleep(15)
        input(Fore.BLUE + 'Presiona Cualquier Letra Para Volver Al Menu\n>> ')
        nmap()

 ######################## Opcion 15 ##########################

    elif opcion == "15":
        os.system("clear")
        print(banner)
        senuelo = input(Fore.BLUE + ( "Introduzca una ip u pagina web ( e.j https://googlesource.com )\n>> "))
        Port = input(Fore.BLUE + ("Intoduzca los puertos que va a usar (Si no sabe cuales pruebe con 80,443)\n>> "))
        os.system(f'nmap -p{Port} --script http-waf-detect --script-args="http-waf-detect.aggro,http-waf-detect.detectBodyChanges" {senuelo}')
        time.sleep(15)
        input(Fore.BLUE + 'Presiona Cualquier Letra Para Volver Al Menu\n>> ')
        nmap()

 ######################## Opcion 16 ##########################
    elif opcion == "16":
        os.system("clear")
        print(banner)
        senuelo = input(Fore.BLUE + ( "Introduzca una ip u pagina web ( e.j https://googlesource.com )\n>> "))
        Port = input(Fore.BLUE + ("Intoduzca los puertos que va a usar (Si no sabe cuales pruebe con 80,443)\n>> "))
        os.system(f"nmap -p{Port} --script http-waf-fingerprint {senuelo}")
        time.sleep(15)
        input(Fore.BLUE + 'Presiona Cualquier Letra Para Volver Al Menu\n>> ')
        nmap()


 ######################## Opcion 17 ##########################

    elif opcion == "17":
        os.system("clear")
        print(banner)
        AgresivC = input(Fore.BLUE + ("Introduzca una ip\n>> "))
        os.system(f"nmap -sS -T insane {AgresivC}")
        time.sleep(15)
        input(Fore.BLUE + 'Presiona Cualquier Letra Para Volver Al Menu\n>> ')
        nmap()


 ######################## Opcion 18 ##########################

    elif opcion == "18": 
        os.system("clear")
        print(banner)
        tcpP = input(Fore.BLUE + ("Introduzca una ip\n>> "))
        os.system(f"nmap -n -Pn -sS -p- {tcpP}")
        time.sleep(15)
        input(Fore.BLUE + 'Presiona Cualquier Letra Para Volver Al Menu\n>> ')
        nmap()

  ######################## Opcion 19 ##########################

    elif opcion == "19": 
        os.system("clear")
        print(banner)
        Udp = input(Fore.BLUE + ("Introduzca una ip\n>> "))
        os.system(f" nmap -n -Pn -sU -p- {Udp}")
        time.sleep(15)
        input(Fore.BLUE + 'Presiona Cualquier Letra Para Volver Al Menu\n>> ')
        nmap()

  ######################## Opcion 20 ##########################   
    
    elif opcion == "20":
        os.system("clear")
        print(banner)
        icmp = input(Fore.BLUE+ ("Introduzca una ip\n>> "))
        paquetes = int(input(Fore.BLUE + ("Introduzca el numero de paquetes\n>>")))
        os.system(f"nping -c {paquetes} {icmp}") 
        time.sleep(15)
        input(Fore.BLUE + "Presiona Cualquier Letra Para Volver Al Menu\n>> ")
        nmap()  

 ######################### Nmap-Scripts ###############################
    elif opcion == "001":
        os.system('clear')
        print(banner)
        target = input(Fore.BLUE + 'Introduzca una ip\n>>')
        Port = input(Fore.BLUE + ("Intoduzca los puertos que va a usar (Si no sabe cuales pruebe con 21)\n>> "))
        os.system(f'nmap --script ftp-brute -p 21 {target}')
        time.sleep(15)
        input(Fore.BLUE + "Presiona Cualquier Letra Para Volver Al Menu\n>> ")
        nmap() 

    elif opcion == "002":
        os.system('clear')
        print(banner)
        target = input(Fore.BLUE + 'Introduzca una ip\n>>')
        os.system(f'nmap -f --script safe {target}')
        time.sleep(15)
        input(Fore.BLUE+ "Presiona Cualquier Letra Para Volver Al Menu\n>> ")
        nmap()

    elif opcion == "003":
        os.system('clear')
        print(banner)
        target = input(Fore.BLUE + 'Introduzca una ip\n>>')
        os.system(f'nmap -f --script vuln {target}')
        time.sleep(15)
        input(Fore.BLUE + "Presiona Cualquier Letra Para Volver Al Menu\n>> ")
        nmap()  

    elif opcion == "004":
        os.system('clear')
        print(banner)
        target = input(Fore.BLUE + 'Introduzca una ip\n>>')
        Port = input(Fore.BLUE + ("Intoduzca los puertos que va a usar (Si no sabe cuales pruebe con 80,443)\n>> "))
        os.system(f'nmap -p{Port} --script dns-brute {target}')
        time.sleep(15)
        input(Fore.BLUE + "Presiona Cualquier Letra Para Volver Al Menu\n>> ")
        nmap()

    elif opcion == "005":
        os.system('clear')
        print(banner)
        target = input(Fore.BLUE + 'Introduzca una ip\n>>')
        Port = input(Fore.BLUE + ("Intoduzca los puertos que va a usar (Si no sabe cuales pruebe con 3306)\n>> "))
        os.system(f'nmap -p{Port} --script mysql-empty-password {target}')
        time.sleep(15)
        input(Fore.BLUE + "Presiona Cualquier Letra Para Volver Al Menu\n>> ")
        nmap()  
    elif opcion == "000":
        os.system('clear')
        (exit())

 ######################## Panel de ayuda - Nmap ##########################

    elif opcion == "0":
        os.system('clear')
        print('Buscando Ayuda....')
        time.sleep(2)
        os.system('nmap -help')
        time.sleep(5)
        input(Fore.BLUE + 'Presiona Cualquier Letra Para Volver Al Menu\n>> ')
        nmap()
    else:
        print(Fore.BLUE + ("no has puesto una opcion correcta!"))
        print(Fore.BLUE + ("Volviendo Al Menu..."))   
        time.sleep(2)
        (nmap()) 
      

def exit():
    print('Saliendo......')
    time.sleep(1)
    os.system("clear")
    sys.exit(1)


nmap()

