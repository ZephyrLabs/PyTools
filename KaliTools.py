import os
import sys, traceback


if os.getuid() != 0:
    print( "Sorry. This script requires sudo privledges")
    sys.exit()
	
def main():
    try:
        print("~~~~~~~~")
        print("KaliTools")
        print("2019-2020")
        print("~~~~~~~~")
        infile = "/etc/apt/sources.list"
        outfile ="/etc/apt/sources.list"

        delete_list = ["# Kali linux repositories | Added by KaliTools\n", "deb http://http.kali.org/kali kali-rolling main contrib non-free\n"]
        fin = open(infile)
        os.remove("/etc/apt/sources.list")
        fout = open(outfile, "w+")
        for line in fin:
            for word in delete_list:
	line = line.replace(word, "")
            fout.write(line)
        fin.close()
        fout.close()
        cmd = os.system("apt-get update -m")
        cmd1 = os.system("apt-key adv --keyserver pool.sks-keyservers.net --recv-keys ED444FF07D8D0BF6")
        cmd2 = os.system("echo '# Kali linux repositories | Added by Katoolin\ndeb http://http.kali.org/kali kali-rolling main contrib non-free' >> /etc/apt/sources.list")
						
        cmd = os.system("apt-get install -y acccheck ace-voip amap automater braa casefile cdpsnarf cisco-torch cookie-cadger copy-router-config dmitry dnmap dnsenum dnsmap dnsrecon dnstracer dnswalk dotdotpwn enum4linux enumiax exploitdb fierce firewalk fragroute fragrouter ghost-phisher golismero goofile lbd maltego-teeth masscan metagoofil miranda nmap p0f parsero recon-ng set smtp-user-enum snmpcheck sslcaudit sslsplit sslstrip sslyze thc-ipv6 theharvester tlssled twofi urlcrazy wireshark wol-e xplico ismtp intrace hping3 && wget http://www.morningstarsecurity.com/downloads/bing-ip2hosts-0.4.tar.gz && tar -xzvf bing-ip2hosts-0.4.tar.gz && cp bing-ip2hosts-0.4/bing-ip2hosts /usr/local/bin/")
        cmd = os.system("wget http://www.morningstarsecurity.com/downloads/bing-ip2hosts-0.4.tar.gz && tar -xzvf bing-ip2hosts-0.4.tar.gz && cp bing-ip2hosts-0.4/bing-ip2hosts /usr/local/bin/")
        cmd = os.system("apt-get install -y bbqsql bed cisco-auditing-tool cisco-global-exploiter cisco-ocs cisco-torch copy-router-config doona dotdotpwn greenbone-security-assistant hexorbase jsql lynis nmap ohrwurm openvas-cli openvas-manager openvas-scanner oscanner powerfuzzer sfuzz sidguesser siparmyknife sqlmap sqlninja sqlsus thc-ipv6 tnscmd10g unix-privesc-check yersinia")
        cmd = os.system("apt-get install git && git clone https://github.com/stasinopoulos/commix.git commix && cd commix && python ./commix.py --install")
        cmd = os.system("echo 'download page : http://www.cqure.net/wp/tools/database/dbpwaudit/'")
        cmd = os.system("apt-get install git && git clone git://git.kali.org/packages/gsd.git")
        cmd = os.system("apt-get install -y aircrack-ng asleap bluelog blueranger bluesnarfer bully cowpatty crackle eapmd5pass fern-wifi-cracker ghost-phisher giskismet gqrx kalibrate-rtl killerbee kismet mdk3 mfcuk mfoc mfterm multimon-ng pixiewps reaver redfang spooftooph wifi-honey wifitap wifite")
        cmd = os.system("apt-get install git && git clone git://git.kali.org/packages/bluemaho.git")
        cmd = os.system("apt-get install git && git clone git://git.kali.org/packages/bluepot.git")
        cmd = os.system("apt-get install git && git clone git://git.kali.org/packages/gr-scan.git")
        cmd = os.system("apt-get install -y apache-users arachni bbqsql blindelephant burpsuite cutycapt davtest deblaze dirb dirbuster fimap funkload grabber jboss-autopwn joomscan jsql maltego-teeth padbuster paros parsero plecost powerfuzzer proxystrike recon-ng skipfish sqlmap sqlninja sqlsus ua-tester uniscan vega w3af webscarab websploit wfuzz wpscan xsser zaproxy")
        cmd = os.system("apt-get install git && git clone git://git.kali.org/packages/webslayer.git")
        cmd = os.system("apt-get install -y burpsuite dnschef fiked hamster-sidejack hexinject iaxflood inviteflood ismtp mitmproxy ohrwurm protos-sip rebind responder rtpbreak rtpinsertsound rtpmixsound sctpscan siparmyknife sipp sipvicious sniffjoke sslsplit sslstrip thc-ipv6 voiphopper webscarab wifi-honey wireshark xspy yersinia zaproxy")
        cmd = os.system("apt-get install git && git clone git://git.kali.org/packages/isr-evilgrade.git")
        cmd = os.system("apt-get install git && git clone https://github.com/stasinopoulos/commix.git commix && cd commix && python ./commix.py --install")          cmd = os.system("apt-get install -y cryptcat cymothoa dbd dns2tcp http-tunnel httptunnel intersect nishang polenum powersploit pwnat ridenum sbd u3-pwn webshells weevely")
        cmd = os.system("apt-get install -y casefile cutycapt dos2unix dradis keepnote magictree metagoofil nipper-ng pipal")
        cmd = os.system("apt-get install -y armitage backdoor-factory cisco-auditing-tool cisco-global-exploiter cisco-ocs cisco-torch crackle jboss-autopwn linux-exploit-suggester maltego-teeth set shellnoob sqlmap thc-ipv6 yersinia beef-xss")
        cmd = os.system("apt-get install git && git clone https://github.com/stasinopoulos/commix.git commix && cd commix && python ./commix.py --install")
        cmd = os.system("apt-get install -y binwalk bulk-extractor chntpw cuckoo dc3dd ddrescue dumpzilla extundelete foremost galleta guymager iphone-backup-analyzer p0f pdf-parser pdfid pdgmail peepdf volatility xplico")
        cmd = os.system("apt-get install git && git clone git://git.kali.org/packages/capstone.git")
        cmd = os.system("apt-get install git && git clone git://git.kali.org/packages/distorm3.git")
        cmd = os.system("apt-get install -y dhcpig funkload iaxflood inviteflood ipv6-toolkit mdk3 reaver rtpflood slowhttptest t50 termineter thc-ipv6 thc-ssl-dos")
        cmd = os.system("apt-get install git && git clone git://git.kali.org/packages/inundator.git")
        cmd = os.system("apt-get install -y acccheck burpsuite cewl chntpw cisco-auditing-tool cmospwd creddump crunch findmyhash gpp-decrypt hash-identifier hexorbase john johnny keimpx maltego-teeth maskprocessor multiforcer ncrack oclgausscrack pack patator polenum rainbowcrack rcracki-mt rsmangler statsprocessor thc-pptp-bruter truecrack webscarab wordlists zaproxy")
        cmd = os.system("apt-get install git && git clone git://git.kali.org/packages/dbpwaudit.git")
        cmd = os.system("echo 'please visit : https://www.thc.org/thc-hydra/' ")
        cmd = os.system("echo 'please visit : http://www.leidecker.info/projects/phrasendrescher/index.shtml' ")
        cmd =os.system("apt-get install -y apktool dex2jar python-diStorm3 edb-debugger jad javasnoop JD OllyDbg smali Valgrind YARA")      
        cmd = os.system("apt-get install -y android-sdk apktool arduino dex2jar sakis3g smali")
        cmd = os.system("git clone https://github.com/LionSec/wifresti.git && cp wifresti/wifresti.py /usr/bin/wifresti && chmod +x /usr/bin/wifresti && wifresti")
        cmd = os.system("apt-get install squid3")
        
    
        print("Thank you for using KaliTools")
    except KeyboardInterrupt:
    		print ("Shutdown requested...")
    except Exception:
	                    traceback.print_exc(file=sys.stdout)
    sys.exit(0)

if __name__ == "__main__":
    main()       
        
        
        
        
        

                   
        

   

   
    
