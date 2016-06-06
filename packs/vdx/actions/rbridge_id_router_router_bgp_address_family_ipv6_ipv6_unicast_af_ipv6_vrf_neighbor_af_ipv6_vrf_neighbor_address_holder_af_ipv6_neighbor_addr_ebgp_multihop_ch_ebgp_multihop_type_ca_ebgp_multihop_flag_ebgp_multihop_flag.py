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


def rbridge_id_router_router_bgp_address_family_ipv6_ipv6_unicast_af_ipv6_vrf_neighbor_af_ipv6_vrf_neighbor_address_holder_af_ipv6_neighbor_addr_ebgp_multihop_ch_ebgp_multihop_type_ca_ebgp_multihop_flag_ebgp_multihop_flag(**kwargs):
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
        
    af_ipv6_vrf = ET.SubElement(ipv6_unicast, "af-ipv6-vrf")
    if kwargs.pop('delete_af_ipv6_vrf', False) is True:
        delete_af_ipv6_vrf = config.find('.//*af-ipv6-vrf')
        delete_af_ipv6_vrf.set('operation', 'delete')
        
    af_ipv6_vrf_name_key = ET.SubElement(af_ipv6_vrf, "af-ipv6-vrf-name")
    af_ipv6_vrf_name_key.text = kwargs.pop('af_ipv6_vrf_name')
    if kwargs.pop('delete_af_ipv6_vrf_name', False) is True:
        delete_af_ipv6_vrf_name = config.find('.//*af-ipv6-vrf-name')
        delete_af_ipv6_vrf_name.set('operation', 'delete')
            
    neighbor = ET.SubElement(af_ipv6_vrf, "neighbor")
    if kwargs.pop('delete_neighbor', False) is True:
        delete_neighbor = config.find('.//*neighbor')
        delete_neighbor.set('operation', 'delete')
        
    af_ipv6_vrf_neighbor_address_holder = ET.SubElement(neighbor, "af-ipv6-vrf-neighbor-address-holder")
    if kwargs.pop('delete_af_ipv6_vrf_neighbor_address_holder', False) is True:
        delete_af_ipv6_vrf_neighbor_address_holder = config.find('.//*af-ipv6-vrf-neighbor-address-holder')
        delete_af_ipv6_vrf_neighbor_address_holder.set('operation', 'delete')
        
    af_ipv6_neighbor_addr = ET.SubElement(af_ipv6_vrf_neighbor_address_holder, "af-ipv6-neighbor-addr")
    if kwargs.pop('delete_af_ipv6_neighbor_addr', False) is True:
        delete_af_ipv6_neighbor_addr = config.find('.//*af-ipv6-neighbor-addr')
        delete_af_ipv6_neighbor_addr.set('operation', 'delete')
        
    af_ipv6_neighbor_address_key = ET.SubElement(af_ipv6_neighbor_addr, "af-ipv6-neighbor-address")
    af_ipv6_neighbor_address_key.text = kwargs.pop('af_ipv6_neighbor_address')
    if kwargs.pop('delete_af_ipv6_neighbor_address', False) is True:
        delete_af_ipv6_neighbor_address = config.find('.//*af-ipv6-neighbor-address')
        delete_af_ipv6_neighbor_address.set('operation', 'delete')
            
    ebgp_multihop = ET.SubElement(af_ipv6_neighbor_addr, "ebgp-multihop")
    if kwargs.pop('delete_ebgp_multihop', False) is True:
        delete_ebgp_multihop = config.find('.//*ebgp-multihop')
        delete_ebgp_multihop.set('operation', 'delete')
        
    ch_ebgp_multihop_type = ET.SubElement(ebgp_multihop, "ch-ebgp-multihop-type")
    if kwargs.pop('delete_ch_ebgp_multihop_type', False) is True:
        delete_ch_ebgp_multihop_type = config.find('.//*ch-ebgp-multihop-type')
        delete_ch_ebgp_multihop_type.set('operation', 'delete')
        
    ca_ebgp_multihop_flag = ET.SubElement(ch_ebgp_multihop_type, "ca-ebgp-multihop-flag")
    if kwargs.pop('delete_ca_ebgp_multihop_flag', False) is True:
        delete_ca_ebgp_multihop_flag = config.find('.//*ca-ebgp-multihop-flag')
        delete_ca_ebgp_multihop_flag.set('operation', 'delete')
        
    ebgp_multihop_flag = ET.SubElement(ca_ebgp_multihop_flag, "ebgp-multihop-flag")
    if kwargs.pop('delete_ebgp_multihop_flag', False) is True:
        delete_ebgp_multihop_flag = config.find('.//*ebgp-multihop-flag')
        delete_ebgp_multihop_flag.set('operation', 'delete')
        

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class rbridge_id_router_router_bgp_address_family_ipv6_ipv6_unicast_af_ipv6_vrf_neighbor_af_ipv6_vrf_neighbor_address_holder_af_ipv6_neighbor_addr_ebgp_multihop_ch_ebgp_multihop_type_ca_ebgp_multihop_flag_ebgp_multihop_flag_act(Action):
    def run(self, delete_address_family, delete_router_bgp, rbridge_id, delete_ch_ebgp_multihop_type, delete_ebgp_multihop, delete_ebgp_multihop_flag, delete_rbridge_id, delete_neighbor, delete_router, delete_ca_ebgp_multihop_flag, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        rbridge_id_router_router_bgp_address_family_ipv6_ipv6_unicast_af_ipv6_vrf_neighbor_af_ipv6_vrf_neighbor_address_holder_af_ipv6_neighbor_addr_ebgp_multihop_ch_ebgp_multihop_type_ca_ebgp_multihop_flag_ebgp_multihop_flag(delete_router_bgp=delete_router_bgp, delete_ebgp_multihop=delete_ebgp_multihop, username=username, delete_neighbor=delete_neighbor, delete_router=delete_router, rbridge_id=rbridge_id, delete_ch_ebgp_multihop_type=delete_ch_ebgp_multihop_type, delete_ebgp_multihop_flag=delete_ebgp_multihop_flag, host=host, password=password, delete_address_family=delete_address_family, delete_rbridge_id=delete_rbridge_id, delete_ca_ebgp_multihop_flag=delete_ca_ebgp_multihop_flag, callback=_callback, mgr=mgr)
        return 0
    