from pox.core import core
import pox.openflow.libopenflow_01 as of
import random

log = core.getLogger()

DROP_PROBABILITY = 0.3

def _handle_PacketIn(event):
    packet = event.parsed
    ip = packet.find('ipv4')

    #  RANDOM PACKET DROP (ALWAYS ACTIVE)
    if random.random() < DROP_PROBABILITY:
        log.info("Packet DROPPED")
        return

    #  BLOCK h3 → h1 (flow rule)
    if ip:
        if str(ip.srcip) == "10.0.0.3" and str(ip.dstip) == "10.0.0.1":
            log.info("Installing BLOCK rule")

            msg = of.ofp_flow_mod()
            msg.priority = 100
            msg.match.dl_type = 0x0800
            msg.match.nw_src = ip.srcip
            msg.match.nw_dst = ip.dstip
            # no action = drop

            event.connection.send(msg)
            return

    # FORWARD WITHOUT INSTALLING FLOW (IMPORTANT)
    msg = of.ofp_packet_out()
    msg.data = event.ofp
    msg.actions.append(of.ofp_action_output(port=of.OFPP_FLOOD))
    event.connection.send(msg)

def launch():
    core.openflow.addListenerByName("PacketIn", _handle_PacketIn)
