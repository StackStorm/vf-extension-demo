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


def rbridge_id_vrf_address_family_ip_unicast_ip_route_static_route_oif_vrf_static_route_next_vrf_dest(**kwargs):
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
            
    vrf = ET.SubElement(rbridge_id, "vrf", xmlns="urn:brocade.com:mgmt:brocade-vrf")
    if kwargs.pop('delete_vrf', False) is True:
        delete_vrf = config.find('.//*vrf')
        delete_vrf.set('operation', 'delete')
        
    vrf_name_key = ET.SubElement(vrf, "vrf-name")
    vrf_name_key.text = kwargs.pop('vrf_name')
    if kwargs.pop('delete_vrf_name', False) is True:
        delete_vrf_name = config.find('.//*vrf-name')
        delete_vrf_name.set('operation', 'delete')
            
    address_family = ET.SubElement(vrf, "address-family")
    if kwargs.pop('delete_address_family', False) is True:
        delete_address_family = config.find('.//*address-family')
        delete_address_family.set('operation', 'delete')
        
    ip = ET.SubElement(address_family, "ip")
    if kwargs.pop('delete_ip', False) is True:
        delete_ip = config.find('.//*ip')
        delete_ip.set('operation', 'delete')
        
    unicast = ET.SubElement(ip, "unicast")
    if kwargs.pop('delete_unicast', False) is True:
        delete_unicast = config.find('.//*unicast')
        delete_unicast.set('operation', 'delete')
        
    ip = ET.SubElement(unicast, "ip", xmlns="urn:brocade.com:mgmt:brocade-rtm")
    if kwargs.pop('delete_ip', False) is True:
        delete_ip = config.find('.//*ip')
        delete_ip.set('operation', 'delete')
        
    route = ET.SubElement(ip, "route")
    if kwargs.pop('delete_route', False) is True:
        delete_route = config.find('.//*route')
        delete_route.set('operation', 'delete')
        
    static_route_oif_vrf = ET.SubElement(route, "static-route-oif-vrf")
    if kwargs.pop('delete_static_route_oif_vrf', False) is True:
        delete_static_route_oif_vrf = config.find('.//*static-route-oif-vrf')
        delete_static_route_oif_vrf.set('operation', 'delete')
        
    next_hop_vrf_key = ET.SubElement(static_route_oif_vrf, "next-hop-vrf")
    next_hop_vrf_key.text = kwargs.pop('next_hop_vrf')
    if kwargs.pop('delete_next_hop_vrf', False) is True:
        delete_next_hop_vrf = config.find('.//*next-hop-vrf')
        delete_next_hop_vrf.set('operation', 'delete')
            
    static_route_oif_type_key = ET.SubElement(static_route_oif_vrf, "static-route-oif-type")
    static_route_oif_type_key.text = kwargs.pop('static_route_oif_type')
    if kwargs.pop('delete_static_route_oif_type', False) is True:
        delete_static_route_oif_type = config.find('.//*static-route-oif-type')
        delete_static_route_oif_type.set('operation', 'delete')
            
    static_route_oif_name_key = ET.SubElement(static_route_oif_vrf, "static-route-oif-name")
    static_route_oif_name_key.text = kwargs.pop('static_route_oif_name')
    if kwargs.pop('delete_static_route_oif_name', False) is True:
        delete_static_route_oif_name = config.find('.//*static-route-oif-name')
        delete_static_route_oif_name.set('operation', 'delete')
            
    static_route_next_vrf_dest = ET.SubElement(static_route_oif_vrf, "static-route-next-vrf-dest")
    if kwargs.pop('delete_static_route_next_vrf_dest', False) is True:
        delete_static_route_next_vrf_dest = config.find('.//*static-route-next-vrf-dest')
        delete_static_route_next_vrf_dest.set('operation', 'delete')
        
    static_route_next_vrf_dest.text = kwargs.pop('static_route_next_vrf_dest')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class rbridge_id_vrf_address_family_ip_unicast_ip_route_static_route_oif_vrf_static_route_next_vrf_dest_act(Action):
    def run(self, delete_address_family, static_route_oif_type, rbridge_id, delete_ip, delete_route, delete_vrf, delete_next_hop_vrf, delete_static_route_next_vrf_dest, static_route_next_vrf_dest, delete_static_route_oif_type, delete_static_route_oif_vrf, vrf_name, delete_static_route_oif_name, next_hop_vrf, delete_rbridge_id, delete_unicast, static_route_oif_name, delete_vrf_name, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        rbridge_id_vrf_address_family_ip_unicast_ip_route_static_route_oif_vrf_static_route_next_vrf_dest(username=username, delete_address_family=delete_address_family, delete_static_route_oif_vrf=delete_static_route_oif_vrf, delete_route=delete_route, vrf_name=vrf_name, static_route_next_vrf_dest=static_route_next_vrf_dest, delete_vrf=delete_vrf, rbridge_id=rbridge_id, delete_ip=delete_ip, delete_unicast=delete_unicast, delete_static_route_next_vrf_dest=delete_static_route_next_vrf_dest, delete_next_hop_vrf=delete_next_hop_vrf, host=host, delete_vrf_name=delete_vrf_name, static_route_oif_type=static_route_oif_type, delete_static_route_oif_type=delete_static_route_oif_type, delete_static_route_oif_name=delete_static_route_oif_name, static_route_oif_name=static_route_oif_name, delete_rbridge_id=delete_rbridge_id, next_hop_vrf=next_hop_vrf, password=password, callback=_callback, mgr=mgr)
        return 0
    