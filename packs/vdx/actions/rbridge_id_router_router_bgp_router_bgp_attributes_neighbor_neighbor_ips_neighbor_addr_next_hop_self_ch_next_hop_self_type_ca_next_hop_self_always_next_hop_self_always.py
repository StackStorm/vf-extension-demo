import sys
from ncclient import manager
from ncclient import xml_
import ncclient
from st2actions.runners.pythonrunner import Action
from xml.etree import ElementTree as ET



def _callback(call, handler='edit_config', target='running', source='startup', mgr=None):
    try:
        call = ET.tostring(call)
        if handler == 'get':
            call_element = xml_.to_ele(call)
            return ET.fromstring(str(mgr.dispatch(call_element)))
        if handler == 'edit_config':
            mgr.edit_config(target=target, config=call)
        if handler == 'delete_config':
            mgr.delete_config(target=target)
        if handler == 'copy_config':
            mgr.copy_config(target=target, source=source)
    except (ncclient.transport.TransportError,
            ncclient.transport.SessionCloseError,
            ncclient.transport.SSHError,
            ncclient.transport.AuthenticationError,
            ncclient.transport.SSHUnknownHostError) as error:
        logging.error(error)
        raise DeviceCommError


def rbridge_id_router_router_bgp_router_bgp_attributes_neighbor_neighbor_ips_neighbor_addr_next_hop_self_ch_next_hop_self_type_ca_next_hop_self_always_next_hop_self_always(**kwargs):
    """Auto Generated Code
    """
    config = ET.Element("config")
    rbridge_id = ET.SubElement(config, "rbridge-id", xmlns="urn:brocade.com:mgmt:brocade-rbridge")
    if kwargs.pop('delete_rbridge_id', False) is True:
        delete_rbridge_id = config.find('.//*rbridge-id')
        delete_rbridge_id.set('operation', 'delete')
        
    rbridge_id_key = ET.SubElement(rbridge_id, "rbridge-id")
    rbridge_id_key.text = kwargs.pop('rbridge_id')
    if kwargs.pop('delete_rbridge_id', False) is True:
        delete_rbridge_id = config.find('.//*rbridge-id')
        delete_rbridge_id.set('operation', 'delete')
            
    router = ET.SubElement(rbridge_id, "router")
    if kwargs.pop('delete_router', False) is True:
        delete_router = config.find('.//*router')
        delete_router.set('operation', 'delete')
        
    router_bgp = ET.SubElement(router, "router-bgp", xmlns="urn:brocade.com:mgmt:brocade-bgp")
    if kwargs.pop('delete_router_bgp', False) is True:
        delete_router_bgp = config.find('.//*router-bgp')
        delete_router_bgp.set('operation', 'delete')
        
    router_bgp_attributes = ET.SubElement(router_bgp, "router-bgp-attributes")
    if kwargs.pop('delete_router_bgp_attributes', False) is True:
        delete_router_bgp_attributes = config.find('.//*router-bgp-attributes')
        delete_router_bgp_attributes.set('operation', 'delete')
        
    neighbor = ET.SubElement(router_bgp_attributes, "neighbor")
    if kwargs.pop('delete_neighbor', False) is True:
        delete_neighbor = config.find('.//*neighbor')
        delete_neighbor.set('operation', 'delete')
        
    neighbor_ips = ET.SubElement(neighbor, "neighbor-ips")
    if kwargs.pop('delete_neighbor_ips', False) is True:
        delete_neighbor_ips = config.find('.//*neighbor-ips')
        delete_neighbor_ips.set('operation', 'delete')
        
    neighbor_addr = ET.SubElement(neighbor_ips, "neighbor-addr")
    if kwargs.pop('delete_neighbor_addr', False) is True:
        delete_neighbor_addr = config.find('.//*neighbor-addr')
        delete_neighbor_addr.set('operation', 'delete')
        
    router_bgp_neighbor_address_key = ET.SubElement(neighbor_addr, "router-bgp-neighbor-address")
    router_bgp_neighbor_address_key.text = kwargs.pop('router_bgp_neighbor_address')
    if kwargs.pop('delete_router_bgp_neighbor_address', False) is True:
        delete_router_bgp_neighbor_address = config.find('.//*router-bgp-neighbor-address')
        delete_router_bgp_neighbor_address.set('operation', 'delete')
            
    next_hop_self = ET.SubElement(neighbor_addr, "next-hop-self")
    if kwargs.pop('delete_next_hop_self', False) is True:
        delete_next_hop_self = config.find('.//*next-hop-self')
        delete_next_hop_self.set('operation', 'delete')
        
    ch_next_hop_self_type = ET.SubElement(next_hop_self, "ch-next-hop-self-type")
    if kwargs.pop('delete_ch_next_hop_self_type', False) is True:
        delete_ch_next_hop_self_type = config.find('.//*ch-next-hop-self-type')
        delete_ch_next_hop_self_type.set('operation', 'delete')
        
    ca_next_hop_self_always = ET.SubElement(ch_next_hop_self_type, "ca-next-hop-self-always")
    if kwargs.pop('delete_ca_next_hop_self_always', False) is True:
        delete_ca_next_hop_self_always = config.find('.//*ca-next-hop-self-always')
        delete_ca_next_hop_self_always.set('operation', 'delete')
        
    next_hop_self_always = ET.SubElement(ca_next_hop_self_always, "next-hop-self-always")
    if kwargs.pop('delete_next_hop_self_always', False) is True:
        delete_next_hop_self_always = config.find('.//*next-hop-self-always')
        delete_next_hop_self_always.set('operation', 'delete')
        

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class rbridge_id_router_router_bgp_router_bgp_attributes_neighbor_neighbor_ips_neighbor_addr_next_hop_self_ch_next_hop_self_type_ca_next_hop_self_always_next_hop_self_always_act(Action):
    def run(self, router_bgp_neighbor_address, delete_router_bgp, rbridge_id, delete_neighbor_addr, delete_next_hop_self_always, delete_next_hop_self, delete_router_bgp_neighbor_address, delete_router_bgp_attributes, delete_neighbor_ips, delete_ch_next_hop_self_type, delete_rbridge_id, delete_neighbor, delete_router, delete_ca_next_hop_self_always, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        rbridge_id_router_router_bgp_router_bgp_attributes_neighbor_neighbor_ips_neighbor_addr_next_hop_self_ch_next_hop_self_type_ca_next_hop_self_always_next_hop_self_always(router_bgp_neighbor_address=router_bgp_neighbor_address, delete_next_hop_self=delete_next_hop_self, delete_router_bgp=delete_router_bgp, username=username, delete_neighbor=delete_neighbor, delete_neighbor_ips=delete_neighbor_ips, rbridge_id=rbridge_id, delete_router=delete_router, delete_ch_next_hop_self_type=delete_ch_next_hop_self_type, delete_next_hop_self_always=delete_next_hop_self_always, host=host, delete_router_bgp_attributes=delete_router_bgp_attributes, delete_router_bgp_neighbor_address=delete_router_bgp_neighbor_address, delete_rbridge_id=delete_rbridge_id, delete_neighbor_addr=delete_neighbor_addr, delete_ca_next_hop_self_always=delete_ca_next_hop_self_always, password=password, callback=_callback, mgr=mgr)
        return 0
    