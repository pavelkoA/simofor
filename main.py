import time
import ClassesDevice
from datetime import *

if __name__ == '__main__':
    HP_swich_srv = ClassesDevice.Device('belomor', '192.168.0.241', 161)
    print(HP_swich_srv.snmp_get_next('1.3.6.1.2.1.1.5.0'))
    time_up = int(HP_swich_srv.snmp_get_next('1.3.6.1.2.1.1.3.0'))
    print(timedelta(seconds=time_up))
    print(HP_swich_srv.snmp_get_next('1.3.6.1.2.1.1.1.0'))
    print(HP_swich_srv.snmp_get_next('1.3.6.1.4.1.25506.2.6.1.1.1.1.12'))
    # print(HP_swich_srv.snmp_get_next('1.3.6.1.2.1.1.3.0'))
    # print(HP_swich_srv.snmp_get_next('1.3.6.1.2.1.1.3.0'))


