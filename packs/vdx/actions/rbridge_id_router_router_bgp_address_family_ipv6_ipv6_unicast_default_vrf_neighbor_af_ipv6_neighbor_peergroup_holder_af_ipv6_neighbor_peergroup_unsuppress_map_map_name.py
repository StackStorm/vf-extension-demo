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


def rbridge_id_router_router_bgp_address_family_ipv6_ipv6_unicast_default_vrf_neighbor_af_ipv6_neighbor_peergroup_holder_af_ipv6_neighbor_peergroup_unsuppress_map_map_name(**kwargs):
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
        
    ipv6 = ET.SubElement(address_family, "ipv6")
    if kwargs.pop('delete_ipv6', False) is True:
        delete_ipv6 = config.find('.//*ipv6')
        delete_ipv6.set('operation', 'delete')
        
    ipv6_unicast = ET.SubElement(ipv6, "ipv6-unicast")
    if kwargs.pop('delete_ipv6_unicast', False) is True:
        delete_ipv6_unicast = config.find('.//*ipv6-unicast')
        delete_ipv6_unicast.set('operation', 'delete')
        
    default_vrf = ET.SubElement(ipv6_unicast, "default-vrf")
    if kwargs.pop('delete_default_vrf', False) is True:
        delete_default_vrf = config.find('.//*default-vrf')
        delete_default_vrf.set('operation', 'delete')
        
    neighbor = ET.SubElement(default_vrf, "neighbor")
    if kwargs.pop('delete_neighbor', False) is True:
        delete_neighbor = config.find('.//*neighbor')
        delete_neighbor.set('operation', 'delete')
        
    af_ipv6_neighbor_peergroup_holder = ET.SubElement(neighbor, "af-ipv6-neighbor-peergroup-holder")
    if kwargs.pop('delete_af_ipv6_neighbor_peergroup_holder', False) is True:
        delete_af_ipv6_neighbor_peergroup_holder = config.find('.//*af-ipv6-neighbor-peergroup-holder')
        delete_af_ipv6_neighbor_peergroup_holder.set('operation', 'delete')
        
    af_ipv6_neighbor_peergroup = ET.SubElement(af_ipv6_neighbor_peergroup_holder, "af-ipv6-neighbor-peergroup")
    if kwargs.pop('delete_af_ipv6_neighbor_peergroup', False) is True:
        delete_af_ipv6_neighbor_peergroup = config.find('.//*af-ipv6-neighbor-peergroup')
        delete_af_ipv6_neighbor_peergroup.set('operation', 'delete')
        
    af_ipv6_neighbor_peergroup_name_key = ET.SubElement(af_ipv6_neighbor_peergroup, "af-ipv6-neighbor-peergroup-name")
    af_ipv6_neighbor_peergroup_name_key.text = kwargs.pop('af_ipv6_neighbor_peergroup_name')
    if kwargs.pop('delete_af_ipv6_neighbor_peergroup_name', False) is True:
        delete_af_ipv6_neighbor_peergroup_name = config.find('.//*af-ipv6-neighbor-peergroup-name')
        delete_af_ipv6_neighbor_peergroup_name.set('operation', 'delete')
            
    unsuppress_map = ET.SubElement(af_ipv6_neighbor_peergroup, "unsuppress-map")
    if kwargs.pop('delete_unsuppress_map', False) is True:
        delete_unsuppress_map = config.find('.//*unsuppress-map')
        delete_unsuppress_map.set('operation', 'delete')
        
    map_name = ET.SubElement(unsuppress_map, "map-name")
    if kwargs.pop('delete_map_name', False) is True:
        delete_map_name = config.find('.//*map-name')
        delete_map_name.set('operation', 'delete')
        
    map_name.text = kwargs.pop('map_name')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class rbridge_id_router_router_bgp_address_family_ipv6_ipv6_unicast_default_vrf_neighbor_af_ipv6_neighbor_peergroup_holder_af_ipv6_neighbor_peergroup_unsuppress_map_map_name_act(Action):
    def run(self, delete_address_family, delete_map_name, delete_router_bgp, rbridge_id, delete_unsuppress_map, delete_default_vrf, map_name, delete_rbridge_id, delete_neighbor, delete_router, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        rbridge_id_router_router_bgp_address_family_ipv6_ipv6_unicast_default_vrf_neighbor_af_ipv6_neighbor_peergroup_holder_af_ipv6_neighbor_peergroup_unsuppress_map_map_name(delete_map_name=delete_map_name, username=username, map_name=map_name, delete_unsuppress_map=delete_unsuppress_map, rbridge_id=rbridge_id, delete_router=delete_router, delete_neighbor=delete_neighbor, host=host, password=password, delete_address_family=delete_address_family, delete_rbridge_id=delete_rbridge_id, delete_default_vrf=delete_default_vrf, delete_router_bgp=delete_router_bgp, callback=_callback, mgr=mgr)
        return 0
    