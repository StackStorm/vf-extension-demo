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


def rbridge_id_interface_ve_ipv6_ipv6_config_address_ipv6_address_eui_config_eui64(**kwargs):
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
            
    interface = ET.SubElement(rbridge_id, "interface", xmlns="urn:brocade.com:mgmt:brocade-interface")
    if kwargs.pop('delete_interface', False) is True:
        delete_interface = config.find('.//*interface')
        delete_interface.set('operation', 'delete')
        
    ve = ET.SubElement(interface, "ve")
    if kwargs.pop('delete_ve', False) is True:
        delete_ve = config.find('.//*ve')
        delete_ve.set('operation', 'delete')
        
    name_key = ET.SubElement(ve, "name")
    name_key.text = kwargs.pop('name')
    if kwargs.pop('delete_name', False) is True:
        delete_name = config.find('.//*name')
        delete_name.set('operation', 'delete')
            
    ipv6 = ET.SubElement(ve, "ipv6", xmlns="urn:brocade.com:mgmt:brocade-ipv6-config")
    if kwargs.pop('delete_ipv6', False) is True:
        delete_ipv6 = config.find('.//*ipv6')
        delete_ipv6.set('operation', 'delete')
        
    ipv6_config = ET.SubElement(ipv6, "ipv6-config")
    if kwargs.pop('delete_ipv6_config', False) is True:
        delete_ipv6_config = config.find('.//*ipv6-config')
        delete_ipv6_config.set('operation', 'delete')
        
    address = ET.SubElement(ipv6_config, "address")
    if kwargs.pop('delete_address', False) is True:
        delete_address = config.find('.//*address')
        delete_address.set('operation', 'delete')
        
    ipv6_address = ET.SubElement(address, "ipv6-address")
    if kwargs.pop('delete_ipv6_address', False) is True:
        delete_ipv6_address = config.find('.//*ipv6-address')
        delete_ipv6_address.set('operation', 'delete')
        
    address_key = ET.SubElement(ipv6_address, "address")
    address_key.text = kwargs.pop('address')
    if kwargs.pop('delete_address', False) is True:
        delete_address = config.find('.//*address')
        delete_address.set('operation', 'delete')
            
    eui_config = ET.SubElement(ipv6_address, "eui-config")
    if kwargs.pop('delete_eui_config', False) is True:
        delete_eui_config = config.find('.//*eui-config')
        delete_eui_config.set('operation', 'delete')
        
    eui64 = ET.SubElement(eui_config, "eui64")
    if kwargs.pop('delete_eui64', False) is True:
        delete_eui64 = config.find('.//*eui64')
        delete_eui64.set('operation', 'delete')
        

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class rbridge_id_interface_ve_ipv6_ipv6_config_address_ipv6_address_eui_config_eui64_act(Action):
    def run(self, delete_eui_config, name, delete_ve, delete_interface, delete_name, address, delete_rbridge_id, delete_address, rbridge_id, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        rbridge_id_interface_ve_ipv6_ipv6_config_address_ipv6_address_eui_config_eui64(name=name, delete_name=delete_name, address=address, username=username, rbridge_id=rbridge_id, delete_eui_config=delete_eui_config, delete_ve=delete_ve, host=host, delete_address=delete_address, delete_interface=delete_interface, delete_rbridge_id=delete_rbridge_id, password=password, callback=_callback, mgr=mgr)
        return 0
    