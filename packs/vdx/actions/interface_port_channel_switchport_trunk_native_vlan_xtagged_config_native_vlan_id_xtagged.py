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


def interface_port_channel_switchport_trunk_native_vlan_xtagged_config_native_vlan_id_xtagged(**kwargs):
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
            
    switchport = ET.SubElement(port_channel, "switchport")
    if kwargs.pop('delete_switchport', False) is True:
        delete_switchport = config.find('.//*switchport')
        delete_switchport.set('operation', 'delete')
        
    trunk = ET.SubElement(switchport, "trunk")
    if kwargs.pop('delete_trunk', False) is True:
        delete_trunk = config.find('.//*trunk')
        delete_trunk.set('operation', 'delete')
        
    native_vlan_xtagged_config = ET.SubElement(trunk, "native-vlan-xtagged-config")
    if kwargs.pop('delete_native_vlan_xtagged_config', False) is True:
        delete_native_vlan_xtagged_config = config.find('.//*native-vlan-xtagged-config')
        delete_native_vlan_xtagged_config.set('operation', 'delete')
        
    native_vlan_id_xtagged = ET.SubElement(native_vlan_xtagged_config, "native-vlan-id-xtagged")
    if kwargs.pop('delete_native_vlan_id_xtagged', False) is True:
        delete_native_vlan_id_xtagged = config.find('.//*native-vlan-id-xtagged')
        delete_native_vlan_id_xtagged.set('operation', 'delete')
        
    native_vlan_id_xtagged.text = kwargs.pop('native_vlan_id_xtagged')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class interface_port_channel_switchport_trunk_native_vlan_xtagged_config_native_vlan_id_xtagged_act(Action):
    def run(self, delete_switchport, delete_native_vlan_xtagged_config, name, delete_trunk, native_vlan_id_xtagged, delete_port_channel, delete_interface, delete_name, delete_native_vlan_id_xtagged, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        interface_port_channel_switchport_trunk_native_vlan_xtagged_config_native_vlan_id_xtagged(name=name, delete_trunk=delete_trunk, delete_switchport=delete_switchport, delete_native_vlan_xtagged_config=delete_native_vlan_xtagged_config, password=password, delete_port_channel=delete_port_channel, native_vlan_id_xtagged=native_vlan_id_xtagged, host=host, delete_name=delete_name, delete_interface=delete_interface, username=username, delete_native_vlan_id_xtagged=delete_native_vlan_id_xtagged, callback=_callback, mgr=mgr)
        return 0
    