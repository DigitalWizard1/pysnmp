from pysnmp.hlapi import *
from pysnmp.smi import builder, view

def load_mib(mib_file):
    # Create a MIB builder and load the MIB file
    mib_builder = builder.MibBuilder()
    mib_builder.loadModules(mib_file)
    mib_view_controller = view.MibViewController(mib_builder)

def get_snmp_value(ip, oid, community='public', port=161):
    errorIndication, errorStatus, errorIndex, varBinds = next(
        getCmd(SnmpEngine(),
               CommunityData(community),
               UdpTransportTarget((ip, port)),
               ContextData(),
               ObjectType(ObjectIdentity(oid)))
    )

    if errorIndication:
        print(f"SNMP error: {errorIndication}")
    elif errorStatus:
        print(f"SNMP error: {errorStatus.prettyPrint()} at {errorIndex and varBinds[int(errorIndex) - 1][0] or '?'}")
    else:
        for varBind in varBinds:
            print(f"{varBind[0]} = {varBind[1]}")

if __name__ == "__main__":
    # Replace 'your_mib_file.mib' with the actual path to your MIB file
    mib_file_path = 'mibs/E1240snmpinfo.txt'
    load_mib(mib_file_path)

    # Replace 'your_device_ip' and 'your_oid' with the actual IP address and OID you want to retrieve
    device_ip = '192.168.127.254'
    oid_to_retrieve = '1.3.6.1.4.1.8691.10.1240.10.4.1.4.1' #AI port 0 digital value
    oid_to_retrieve = '1.3.6.1.4.1.8691.10.1240.10.4.1.7.1' # AI port 0 analog value
    #oid_to_retrieve = '1.3.6.1.4.1.8691.10.1240.2.0' # the model number
    get_snmp_value(device_ip, oid_to_retrieve)
