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


def interface_hundredgigabitethernet_ipv6_vrrpv3_group_vrid(**kwargs):
    """Auto Generated Code
    """
    config = ET.Element("config")
    interface = ET.SubElement(config, "interface", xmlns="urn:brocade.com:mgmt:brocade-interface")
    if kwargs.pop('delete_interface', False) is True:
        delete_interface = config.find('.//*interface')
        delete_interface.set('operation', 'delete')
        
    hundredgigabitethernet = ET.SubElement(interface, "hundredgigabitethernet")
    if kwargs.pop('delete_hundredgigabitethernet', False) is True:
        delete_hundredgigabitethernet = config.find('.//*hundredgigabitethernet')
        delete_hundredgigabitethernet.set('operation', 'delete')
        
    name_key = ET.SubElement(hundredgigabitethernet, "name")
    name_key.text = kwargs.pop('name')
    if kwargs.pop('delete_name', False) is True:
        delete_name = config.find('.//*name')
        delete_name.set('operation', 'delete')
            
    ipv6 = ET.SubElement(hundredgigabitethernet, "ipv6")
    if kwargs.pop('delete_ipv6', False) is True:
        delete_ipv6 = config.find('.//*ipv6')
        delete_ipv6.set('operation', 'delete')
        
    vrrpv3_group = ET.SubElement(ipv6, "vrrpv3-group", xmlns="urn:brocade.com:mgmt:brocade-vrrpv3")
    if kwargs.pop('delete_vrrpv3_group', False) is True:
        delete_vrrpv3_group = config.find('.//*vrrpv3-group')
        delete_vrrpv3_group.set('operation', 'delete')
        
    vrid = ET.SubElement(vrrpv3_group, "vrid")
    if kwargs.pop('delete_vrid', False) is True:
        delete_vrid = config.find('.//*vrid')
        delete_vrid.set('operation', 'delete')
        
    vrid.text = kwargs.pop('vrid')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class interface_hundredgigabitethernet_ipv6_vrrpv3_group_vrid_act(Action):
    def run(self, name, delete_vrid, vrid, delete_interface, delete_name, delete_hundredgigabitethernet, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        interface_hundredgigabitethernet_ipv6_vrrpv3_group_vrid(delete_vrid=delete_vrid, name=name, delete_name=delete_name, delete_hundredgigabitethernet=delete_hundredgigabitethernet, host=host, vrid=vrid, delete_interface=delete_interface, username=username, password=password, callback=_callback, mgr=mgr)
        return 0
    