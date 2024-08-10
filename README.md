# SRv6
Original network scenario can be found [here](https://github.com/opennetworkinglab/ngsdn-tutorial/blob/advanced/EXERCISE-6.md)

This network scenario has been adapted for Kathara Dockers, but currently is missing the SDN controller.

Each switch has its own <switch_name>/controller_p4runtime.py script, which with a use of P4Runtime configure P4 tables of a device.

The switches are prepared with a SRv6 path added bettwen hosts 2001:1:2::1 and 2001:2:4::1.

## Network Scenario

This is the network scenario topology: 

![topology](topo-v6.png)

NOTE:
Numbers on the image start from 1, but in the Kathara eth devices start from 0.
