from p4utils.utils.sswitch_p4runtime_API import SimpleSwitchP4RuntimeAPI
controller = SimpleSwitchP4RuntimeAPI(1, 9559, 'localhost','/shared/build/p4info.txt', '/shared/build/bmv2.json')
controller.table_clear('routing_v6_table')
controller.table_add('my_station_table','NoAction', ['00:aa:00:00:00:01'])
