# SDN Packet Drop Simulator using Mininet and POX

## Problem Statement

This project implements an SDN-based solution using Mininet and POX controller to simulate packet loss and traffic blocking. It demonstrates controller-switch interaction, flow rule design, and network performance analysis.

---

## Topology

* 1 Switch (s1)
* 3 Hosts (h1, h2, h3)
* Single switch topology

---

## Setup and Execution

### Start Controller

```bash
cd ~/pox
python3 pox.py openflow.of_01 --port=6653 firewall
```

### Start Mininet

```bash
sudo mn --topo single,3 --controller=remote,ip=127.0.0.1,port=6653
```

---

## Commands Used

```bash
h1 ping h2
h3 ping h1
iperf h1 h2
dpctl dump-flows
```


## Functionality

* Random packet drop (~30–50%)
* Blocking traffic from h3 to h1
* Flow rules using OpenFlow match-action


## Expected Output

* Packet loss observed in h1 to h2 communication
* h3 to h1 communication blocked
* Increased latency and reduced throughput


## Test Scenarios

1. Normal vs packet loss (h1 → h2)
2. Allowed vs blocked (h3 → h1)


## Proof of Execution

Screenshots included:

### 1. POX Controller Output
![Uploading image.png…]()


Shows the controller running and dropping packets based on firewall rules.

---

### 2. Ping Test (h1 → h2)
![Uploading image.png…]()


Indicates packet loss due to applied drop rules.

---

### 3. Flow Table Entries
![Uploading image.png…]()


Displays flow rules installed in the switch.



#References

* https://mininet.org/
* https://github.com/noxrepo/pox
* https://opennetworking.org/


 Conclusion

The project demonstrates SDN concepts including controller-based decision making, flow rule installation, packet loss simulation, and traffic control.
