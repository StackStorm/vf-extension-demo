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


def rbridge_id_ipv6_router_ospf_distribute_list_prefix_list_distribute_list_prefix_list_name(**kwargs):
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
            
    ipv6 = ET.SubElement(rbridge_id, "ipv6")
    if kwargs.pop('delete_ipv6', False) is True:
        delete_ipv6 = config.find('.//*ipv6')
        delete_ipv6.set('operation', 'delete')
        
    router = ET.SubElement(ipv6, "router")
    if kwargs.pop('delete_router', False) is True:
        delete_router = config.find('.//*router')
        delete_router.set('operation', 'delete')
        
    ospf = ET.SubElement(router, "ospf", xmlns="urn:brocade.com:mgmt:brocade-ospfv3")
    if kwargs.pop('delete_ospf', False) is True:
        delete_ospf = config.find('.//*ospf')
        delete_ospf.set('operation', 'delete')
        
    vrf_key = ET.SubElement(ospf, "vrf")
    vrf_key.text = kwargs.pop('vrf')
    if kwargs.pop('delete_vrf', False) is True:
        delete_vrf = config.find('.//*vrf')
        delete_vrf.set('operation', 'delete')
            
    distribute_list = ET.SubElement(ospf, "distribute-list")
    if kwargs.pop('delete_distribute_list', False) is True:
        delete_distribute_list = config.find('.//*distribute-list')
        delete_distribute_list.set('operation', 'delete')
        
    prefix_list = ET.SubElement(distribute_list, "prefix-list")
    if kwargs.pop('delete_prefix_list', False) is True:
        delete_prefix_list = config.find('.//*prefix-list')
        delete_prefix_list.set('operation', 'delete')
        
    distribute_list_prefix_list_name = ET.SubElement(prefix_list, "distribute-list-prefix-list-name")
    if kwargs.pop('delete_distribute_list_prefix_list_name', False) is True:
        delete_distribute_list_prefix_list_name = config.find('.//*distribute-list-prefix-list-name')
        delete_distribute_list_prefix_list_name.set('operation', 'delete')
        
    distribute_list_prefix_list_name.text = kwargs.pop('distribute_list_prefix_list_name')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class rbridge_id_ipv6_router_ospf_distribute_list_prefix_list_distribute_list_prefix_list_name_act(Action):
    def run(self, rbridge_id, delete_ospf, delete_vrf, distribute_list_prefix_list_name, vrf, delete_distribute_list, delete_distribute_list_prefix_list_name, delete_prefix_list, delete_rbridge_id, delete_router, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        rbridge_id_ipv6_router_ospf_distribute_list_prefix_list_distribute_list_prefix_list_name(delete_prefix_list=delete_prefix_list, username=username, distribute_list_prefix_list_name=distribute_list_prefix_list_name, rbridge_id=rbridge_id, delete_vrf=delete_vrf, delete_distribute_list_prefix_list_name=delete_distribute_list_prefix_list_name, delete_distribute_list=delete_distribute_list, delete_router=delete_router, delete_ospf=delete_ospf, vrf=vrf, host=host, delete_rbridge_id=delete_rbridge_id, password=password, callback=_callback, mgr=mgr)
        return 0
    