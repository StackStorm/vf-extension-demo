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


def rbridge_id_router_router_bgp_address_family_l2vpn_evpn_neighbor_evpn_neighbor_ipv4_allowas_in(**kwargs):
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
        
    address_family = ET.SubElement(router_bgp, "address-family")
    if kwargs.pop('delete_address_family', False) is True:
        delete_address_family = config.find('.//*address-family')
        delete_address_family.set('operation', 'delete')
        
    l2vpn = ET.SubElement(address_family, "l2vpn")
    if kwargs.pop('delete_l2vpn', False) is True:
        delete_l2vpn = config.find('.//*l2vpn')
        delete_l2vpn.set('operation', 'delete')
        
    evpn = ET.SubElement(l2vpn, "evpn")
    if kwargs.pop('delete_evpn', False) is True:
        delete_evpn = config.find('.//*evpn')
        delete_evpn.set('operation', 'delete')
        
    neighbor = ET.SubElement(evpn, "neighbor")
    if kwargs.pop('delete_neighbor', False) is True:
        delete_neighbor = config.find('.//*neighbor')
        delete_neighbor.set('operation', 'delete')
        
    evpn_neighbor_ipv4 = ET.SubElement(neighbor, "evpn-neighbor-ipv4")
    if kwargs.pop('delete_evpn_neighbor_ipv4', False) is True:
        delete_evpn_neighbor_ipv4 = config.find('.//*evpn-neighbor-ipv4')
        delete_evpn_neighbor_ipv4.set('operation', 'delete')
        
    evpn_neighbor_ipv4_address_key = ET.SubElement(evpn_neighbor_ipv4, "evpn-neighbor-ipv4-address")
    evpn_neighbor_ipv4_address_key.text = kwargs.pop('evpn_neighbor_ipv4_address')
    if kwargs.pop('delete_evpn_neighbor_ipv4_address', False) is True:
        delete_evpn_neighbor_ipv4_address = config.find('.//*evpn-neighbor-ipv4-address')
        delete_evpn_neighbor_ipv4_address.set('operation', 'delete')
            
    allowas_in = ET.SubElement(evpn_neighbor_ipv4, "allowas-in")
    if kwargs.pop('delete_allowas_in', False) is True:
        delete_allowas_in = config.find('.//*allowas-in')
        delete_allowas_in.set('operation', 'delete')
        
    allowas_in.text = kwargs.pop('allowas_in')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class rbridge_id_router_router_bgp_address_family_l2vpn_evpn_neighbor_evpn_neighbor_ipv4_allowas_in_act(Action):
    def run(self, delete_address_family, delete_router_bgp, rbridge_id, allowas_in, delete_evpn, delete_allowas_in, delete_rbridge_id, delete_neighbor, delete_router, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        rbridge_id_router_router_bgp_address_family_l2vpn_evpn_neighbor_evpn_neighbor_ipv4_allowas_in(delete_router_bgp=delete_router_bgp, delete_evpn=delete_evpn, username=username, rbridge_id=rbridge_id, delete_router=delete_router, delete_neighbor=delete_neighbor, delete_allowas_in=delete_allowas_in, host=host, delete_address_family=delete_address_family, allowas_in=allowas_in, delete_rbridge_id=delete_rbridge_id, password=password, callback=_callback, mgr=mgr)
        return 0
    