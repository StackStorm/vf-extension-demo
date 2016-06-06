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


def interface_port_channel_mac_access_group_mac_access_list(**kwargs):
    """Auto Generated Code
    """
    config = ET.Element("config")
    interface = ET.SubElement(config, "interface", xmlns="urn:brocade.com:mgmt:brocade-interface")
    if kwargs.pop('delete_interface', False) is True:
        delete_interface = config.find('.//*interface')
        delete_interface.set('operation', 'delete')
        
    port_channel = ET.SubElement(interface, "port-channel")
    if kwargs.pop('delete_port_channel', False) is True:
        delete_port_channel = config.find('.//*port-channel')
        delete_port_channel.set('operation', 'delete')
        
    name_key = ET.SubElement(port_channel, "name")
    name_key.text = kwargs.pop('name')
    if kwargs.pop('delete_name', False) is True:
        delete_name = config.find('.//*name')
        delete_name.set('operation', 'delete')
            
    mac = ET.SubElement(port_channel, "mac", xmlns="urn:brocade.com:mgmt:brocade-mac-access-list")
    if kwargs.pop('delete_mac', False) is True:
        delete_mac = config.find('.//*mac')
        delete_mac.set('operation', 'delete')
        
    access_group = ET.SubElement(mac, "access-group")
    if kwargs.pop('delete_access_group', False) is True:
        delete_access_group = config.find('.//*access-group')
        delete_access_group.set('operation', 'delete')
        
    mac_direction_key = ET.SubElement(access_group, "mac-direction")
    mac_direction_key.text = kwargs.pop('mac_direction')
    if kwargs.pop('delete_mac_direction', False) is True:
        delete_mac_direction = config.find('.//*mac-direction')
        delete_mac_direction.set('operation', 'delete')
            
    mac_access_list = ET.SubElement(access_group, "mac-access-list")
    if kwargs.pop('delete_mac_access_list', False) is True:
        delete_mac_access_list = config.find('.//*mac-access-list')
        delete_mac_access_list.set('operation', 'delete')
        
    mac_access_list.text = kwargs.pop('mac_access_list')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class interface_port_channel_mac_access_group_mac_access_list_act(Action):
    def run(self, name, mac_access_list, delete_port_channel, delete_mac_access_list, delete_access_group, delete_name, delete_interface, delete_mac_direction, mac_direction, delete_mac, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        interface_port_channel_mac_access_group_mac_access_list(name=name, mac_access_list=mac_access_list, delete_mac=delete_mac, delete_access_group=delete_access_group, delete_mac_access_list=delete_mac_access_list, delete_port_channel=delete_port_channel, mac_direction=mac_direction, host=host, delete_mac_direction=delete_mac_direction, delete_name=delete_name, delete_interface=delete_interface, username=username, password=password, callback=_callback, mgr=mgr)
        return 0
    