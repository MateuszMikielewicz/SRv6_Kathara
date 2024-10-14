from p4utils.utils.sswitch_p4runtime_API import SimpleSwitchP4RuntimeAPI
controller = SimpleSwitchP4RuntimeAPI(1, 9559, 'localhost','/shared/build/p4info.txt', '/shared/build/bmv2.json')

controller.table_add('my_station_table','NoAction', ['00:aa:00:00:00:02'])

controller.table_add('srv6_my_sid','srv6_end', ['3:102:2::/128'])

controller.table_add('routing_v6_table','set_next_hop', ['2001:2:4::/64'], ['00:00:00:00:00:40'])
controller.table_add('routing_v6_table','set_next_hop', ['2001:2:3::/64'], ['00:00:00:00:00:30'])
#controller.table_add('routing_v6_table','set_next_hop', ['2001:1:1::/64'], ['00:bb:00:00:00:02'])
#controller.table_add('routing_v6_table','set_next_hop', ['2001:1:2::/64'], ['00:bb:00:00:00:02'])
controller.table_add('routing_v6_table','set_next_hop', ['3:201:2::/128'], ['00:bb:00:00:00:01'])
controller.table_add('routing_v6_table','set_next_hop', ['3:202:2::/128'], ['00:bb:00:00:00:02'])
controller.table_add('routing_v6_table','set_next_hop', ['3:101:2::/128'], ['00:bb:00:00:00:01'])
#sdn_controller
controller.table_add('routing_v6_table','set_next_hop', ['2001:c:1::/48'], ['00:bb:00:00:00:01']) #one sdn interface
controller.table_add('routing_v6_table','set_next_hop', ['2001:c:2::/48'], ['00:cc:00:00:00:00']) #two sdn interfaces
#node_manager_ip_leaf2
controller.table_add('routing_v6_table','set_next_hop', ['3:102:c::1/48'], ['00:aa:00:00:cc:02'])

#controller.table_add('srv6_transit','srv6_t_insert_3', ['2001:1:2::1'], ['3:201:2::', '3:101:2::', '2001:1:2::1'])

controller.table_add('l2_exact_table','set_egress_port', ['00:bb:00:00:00:01'], ['1'])
controller.table_add('l2_exact_table','set_egress_port', ['00:bb:00:00:00:02'], ['2'])
controller.table_add('l2_exact_table','set_egress_port', ['00:00:00:00:00:30'], ['3'])
controller.table_add('l2_exact_table','set_egress_port', ['00:00:00:00:00:40'], ['4'])
controller.table_add('l2_exact_table','set_egress_port', ['00:cc:00:00:00:00'], ['5'])
controller.table_add('l2_exact_table','set_egress_port', ['00:aa:00:00:cc:02'], ['6'])


controller.table_add('acl_table','clone_to_cpu', ['0x0&&&0x0', '0x0&&&0x0', '0x0&&&0x0', '0x8932&&&0xffff', '0x0&&&0x0', '0x0&&&0x0', '0x0&&&0x0', '0x0&&&0x0'], ['4000'])
controller.table_add('acl_table','clone_to_cpu', ['0x0&&&0x0', '0x0&&&0x0', '0x0&&&0x0', '0x86dd&&&0xffff', '0x3a&&&0xff', '0x87&&&0xff', '0x0&&&0x0', '0x0&&&0x0'], ['4000'])
controller.table_add('acl_table','clone_to_cpu', ['0x0&&&0x0', '0x0&&&0x0', '0x0&&&0x0', '0x86dd&&&0xffff', '0x3a&&&0xff', '0x88&&&0xff', '0x0&&&0x0', '0x0&&&0x0'], ['4000'])
controller.table_add('acl_table','clone_to_cpu', ['0x0&&&0x0', '0x0&&&0x0', '0x0&&&0x0', '0x88cc&&&0xffff', '0x0&&&0x0', '0x0&&&0x0', '0x0&&&0x0', '0x0&&&0x0'], ['4000'])
controller.table_add('acl_table','clone_to_cpu', ['0x0&&&0x0', '0x0&&&0x0', '0x0&&&0x0', '0x0806&&&0xffff', '0x0&&&0x0', '0x0&&&0x0', '0x1&&&0x0', '0x0&&&0x0'], ['4000'])

controller.table_add('l2_ternary_table','set_multicast_group', ['33:33:00:00:00:00&&&0xffff00000000'], ['255', '10'])
controller.table_add('l2_ternary_table','set_multicast_group', ['ff:ff:ff:ff:ff:ff&&&0xffffffffffff'], ['255', '10'])

controller.table_add('ndp_reply_table','ndp_ns_to_na', ['2001:c:2::ff'], ['00:aa:00:00:00:02']) #two sdn interfaces
controller.table_add('ndp_reply_table','ndp_ns_to_na', ['3:102:c::ff'], ['00:aa:00:00:00:02'])
controller.table_add('ndp_reply_table','ndp_ns_to_na', ['2001:2:3::ff'], ['00:aa:00:00:00:02'])
controller.table_add('ndp_reply_table','ndp_ns_to_na', ['2001:2:4::ff'], ['00:aa:00:00:00:02'])
