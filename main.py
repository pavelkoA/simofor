import ClassesAndMethods

if __name__ == '__main__':
    HP_serve = ClassesAndMethods.Device('belomor', '192.168.0.241', 161)
    print(HP_serve.snmp_get_next('1.3.6.1.2.1.1.5.0'))


