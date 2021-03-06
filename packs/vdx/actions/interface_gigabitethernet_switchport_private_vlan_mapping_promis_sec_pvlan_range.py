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


def interface_gigabitethernet_switchport_private_vlan_mapping_promis_sec_pvlan_range(**kwargs):
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
            
    switchport = ET.SubElement(gigabitethernet, "switchport")
    if kwargs.pop('delete_switchport', False) is True:
        delete_switchport = config.find('.//*switchport')
        delete_switchport.set('operation', 'delete')
        
    private_vlan = ET.SubElement(switchport, "private-vlan")
    if kwargs.pop('delete_private_vlan', False) is True:
        delete_private_vlan = config.find('.//*private-vlan')
        delete_private_vlan.set('operation', 'delete')
        
    mapping = ET.SubElement(private_vlan, "mapping")
    if kwargs.pop('delete_mapping', False) is True:
        delete_mapping = config.find('.//*mapping')
        delete_mapping.set('operation', 'delete')
        
    promis_pri_pvlan_key = ET.SubElement(mapping, "promis-pri-pvlan")
    promis_pri_pvlan_key.text = kwargs.pop('promis_pri_pvlan')
    if kwargs.pop('delete_promis_pri_pvlan', False) is True:
        delete_promis_pri_pvlan = config.find('.//*promis-pri-pvlan')
        delete_promis_pri_pvlan.set('operation', 'delete')
            
    promis_sec_pvlan_range = ET.SubElement(mapping, "promis-sec-pvlan-range")
    if kwargs.pop('delete_promis_sec_pvlan_range', False) is True:
        delete_promis_sec_pvlan_range = config.find('.//*promis-sec-pvlan-range')
        delete_promis_sec_pvlan_range.set('operation', 'delete')
        
    promis_sec_pvlan_range.text = kwargs.pop('promis_sec_pvlan_range')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class interface_gigabitethernet_switchport_private_vlan_mapping_promis_sec_pvlan_range_act(Action):
    def run(self, delete_switchport, delete_mapping, name, delete_promis_pri_pvlan, promis_sec_pvlan_range, delete_private_vlan, delete_interface, delete_name, promis_pri_pvlan, delete_promis_sec_pvlan_range, delete_gigabitethernet, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        interface_gigabitethernet_switchport_private_vlan_mapping_promis_sec_pvlan_range(name=name, delete_name=delete_name, delete_switchport=delete_switchport, delete_promis_sec_pvlan_range=delete_promis_sec_pvlan_range, delete_mapping=delete_mapping, delete_promis_pri_pvlan=delete_promis_pri_pvlan, delete_gigabitethernet=delete_gigabitethernet, promis_sec_pvlan_range=promis_sec_pvlan_range, host=host, delete_private_vlan=delete_private_vlan, promis_pri_pvlan=promis_pri_pvlan, delete_interface=delete_interface, username=username, password=password, callback=_callback, mgr=mgr)
        return 0
    