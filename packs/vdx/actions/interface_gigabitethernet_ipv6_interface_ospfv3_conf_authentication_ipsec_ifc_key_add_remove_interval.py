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


def interface_gigabitethernet_ipv6_interface_ospfv3_conf_authentication_ipsec_ifc_key_add_remove_interval(**kwargs):
    """Auto Generated Code
    """
    config = ET.Element("config")
    interface = ET.SubElement(config, "interface", xmlns="urn:brocade.com:mgmt:brocade-interface")
    if kwargs.pop('delete_interface', False) is True:
        delete_interface = config.find('.//*interface')
        delete_interface.set('operation', 'delete')
        
    gigabitethernet = ET.SubElement(interface, "gigabitethernet")
    if kwargs.pop('delete_gigabitethernet', False) is True:
        delete_gigabitethernet = config.find('.//*gigabitethernet')
        delete_gigabitethernet.set('operation', 'delete')
        
    name_key = ET.SubElement(gigabitethernet, "name")
    name_key.text = kwargs.pop('name')
    if kwargs.pop('delete_name', False) is True:
        delete_name = config.find('.//*name')
        delete_name.set('operation', 'delete')
            
    ipv6 = ET.SubElement(gigabitethernet, "ipv6")
    if kwargs.pop('delete_ipv6', False) is True:
        delete_ipv6 = config.find('.//*ipv6')
        delete_ipv6.set('operation', 'delete')
        
    interface_ospfv3_conf = ET.SubElement(ipv6, "interface-ospfv3-conf", xmlns="urn:brocade.com:mgmt:brocade-ospfv3")
    if kwargs.pop('delete_interface_ospfv3_conf', False) is True:
        delete_interface_ospfv3_conf = config.find('.//*interface-ospfv3-conf')
        delete_interface_ospfv3_conf.set('operation', 'delete')
        
    authentication = ET.SubElement(interface_ospfv3_conf, "authentication")
    if kwargs.pop('delete_authentication', False) is True:
        delete_authentication = config.find('.//*authentication')
        delete_authentication.set('operation', 'delete')
        
    ipsec = ET.SubElement(authentication, "ipsec")
    if kwargs.pop('delete_ipsec', False) is True:
        delete_ipsec = config.find('.//*ipsec')
        delete_ipsec.set('operation', 'delete')
        
    ifc_key_add_remove_interval = ET.SubElement(ipsec, "ifc-key-add-remove-interval")
    if kwargs.pop('delete_ifc_key_add_remove_interval', False) is True:
        delete_ifc_key_add_remove_interval = config.find('.//*ifc-key-add-remove-interval')
        delete_ifc_key_add_remove_interval.set('operation', 'delete')
        
    ifc_key_add_remove_interval.text = kwargs.pop('ifc_key_add_remove_interval')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class interface_gigabitethernet_ipv6_interface_ospfv3_conf_authentication_ipsec_ifc_key_add_remove_interval_act(Action):
    def run(self, name, ifc_key_add_remove_interval, delete_ifc_key_add_remove_interval, delete_ipsec, delete_authentication, delete_name, delete_gigabitethernet, delete_interface, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        interface_gigabitethernet_ipv6_interface_ospfv3_conf_authentication_ipsec_ifc_key_add_remove_interval(name=name, delete_ipsec=delete_ipsec, ifc_key_add_remove_interval=ifc_key_add_remove_interval, delete_authentication=delete_authentication, host=host, delete_gigabitethernet=delete_gigabitethernet, delete_name=delete_name, delete_ifc_key_add_remove_interval=delete_ifc_key_add_remove_interval, username=username, delete_interface=delete_interface, password=password, callback=_callback, mgr=mgr)
        return 0
    