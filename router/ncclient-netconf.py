from ncclient import manager
import xml.dom.minidom
import time

m=manager.connect(
    host="192.168.56.101",
    port=830,
    username="cisco",
    password="cisco123!",
    hostkey_verify=False
)
#KUMPULAN FUNGSI ATAU FILTER
def passw_router():
    a=input("Masukkan password untuk router ! : ")
    netconf_passw_router= """
    <config>
        <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
            <enable>
                <password>
                    <secret> {} </secret>
                </password>
            </enable>
        </native>
    </config>
    """.format(a)
    netconf_reply = m.edit_config(target="running",config=netconf_passw_router)
    print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())

def banner_motd():
    a=input("Masukkan pesan peringatan untuk user lain ! : ")
    netconf_banner = """
    <config>
        <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
            <banner>
                <motd>
                    <banner>{}</banner>
                </motd>
            </banner>
        </native>
    </config>
    """.format(a)
    netconf_reply = m.edit_config(target="running",config=netconf_banner)
    print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())

def set_loopback():
    a=int(input("Masukkan nomer Loopback interface yang ingin ditambahkan! : "))
    b=input("Masukkan deskripsi untuk loopback : ")
    c=input("Masukkan ip address! : ")
    d=input("Masukkan netmasknya! : ")
    netconf_interface ="""
    <config>
        <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
            <interface>
                <Loopback>
                    <name>{}</name>
                    <description>{}</description>
                    <ip>
                        <address>
                            <primary>
                                <address>{}</address>
                                <mask>{}</mask>
                            </primary>
                        </address>
                    </ip>
                </Loopback>
            </interface>
        </native>
    </config>
    """.format(a,b,c,d)
    netconf_reply = m.edit_config(target="running",config=netconf_interface)
    print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())

netconf_reply = m.get_config(source="running")
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())

while True:
    time.sleep(2)
    print("""
#####################################
Menu konfigurasi :                  #
0. Exit!                            #
1. Router Password                  #
2. Message of the Day (BANNER MOTD) #
3. Loopback                         #
#####################################
""")
    try:
        menu=int(input("PILIH PROGRAM YANG ANDA INGINKAN ! : "))
    except:
        print("Error! Wrong Input")
        continue
    if menu==0:
        break
    elif menu==1:
        passw_router()
        continue
    elif menu==2:
        banner_motd()
        continue
    elif menu==3:
        set_loopback()
        continue

netconf_reply = m.get_config(source="running")
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())



