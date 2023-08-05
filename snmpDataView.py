from pysnmp.hlapi import *

def get_snmp_data(ip, community='public', port=161):
    errorIndication, errorStatus, errorIndex, varBinds = next(
        getCmd(SnmpEngine(),
               CommunityData(community),
               UdpTransportTarget((ip, port)),
               ContextData(),
               ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0)),
               ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysName', 0)),
               ObjectType(ObjectIdentity('IF-MIB', 'ifNumber', 0)))
    )

    if errorIndication:
        print(f"SNMP error: {errorIndication}")
    elif errorStatus:
        print(f"SNMP error: {errorStatus.prettyPrint()} at {errorIndex and varBinds[int(errorIndex) - 1][0] or '?'}")
    else:
        for varBind in varBinds:
            print(f"{varBind[0]} = {varBind[1]}")

if __name__ == "__main__":
    # Replace 'your_device_ip' with the actual IP address of your SNMP device
    device_ip = '192.168.127.254'

    # Replace 'public' with the appropriate SNMP community string for your device
    community_string = 'public'

    # Optionally, you can specify a different SNMP port if necessary
    snmp_port = 161

    get_snmp_data(device_ip, community_string, snmp_port)
