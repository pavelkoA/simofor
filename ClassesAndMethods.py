from pysnmp.hlapi import *

class Device:
    def __init__(self, comunity, ip_address_host, port_snmp):
        self.comunity = comunity
        self.ip_address_host = ip_address_host
        self.port_snmp = port_snmp
        self.OID_sysName = '1.3.6.1.2.1.1.5.0'

    def snmp_getcmd_oid(self, OID):
        return getCmd(SnmpEngine(), CommunityData(self.comunity), UdpTransportTarget((self.ip_address_host, self.port_snmp)), ContextData(), ObjectType(ObjectIdentity(OID)))

    def snmp_get_next(self, OID):
        errorIndication, errorStatus, errorIndex, varBinds = next(self.snmp_getcmd_oid(OID))
        for name, val in varBinds:
            return (val.prettyPrint())


