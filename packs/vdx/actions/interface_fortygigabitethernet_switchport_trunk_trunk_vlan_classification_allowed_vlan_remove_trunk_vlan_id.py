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


def interface_fortygigabitethernet_switchport_trunk_trunk_vlan_classification_allowed_vlan_remove_trunk_vlan_id(**kwargs):
    """Auto Generated Code
    """
    config = ET.Element("config")
    interface = ET.SubElement(config, "interface", xmlns="urn:brocade.com:mgmt:brocade-interface")
    if kwargs.pop('delete_interface', False) is True:
        delete_interface = config.find('.//*interface')
        delete_interface.set('operation', 'delete')
        
    fortygigabitethernet = ET.SubElement(interface, "fortygigabitethernet")
    if kwargs.pop('delete_fortygigabitethernet', False) is True:
        delete_fortygigabitethernet = config.find('.//*fortygigabitethernet')
        delete_fortygigabitethernet.set('operation', 'delete')
        
    name_key = ET.SubElement(fortygigabitethernet, "name")
    name_key.text = kwargs.pop('name')
    if kwargs.pop('delete_name', False) is True:
        delete_name = config.find('.//*name')
        delete_name.set('operation', 'delete')
            
    switchport = ET.SubElement(fortygigabitethernet, "switchport")
    if kwargs.pop('delete_switchport', False) is True:
        delete_switchport = config.find('.//*switchport')
        delete_switchport.set('operation', 'delete')
        
    trunk = ET.SubElement(switchport, "trunk")
    if kwargs.pop('delete_trunk', False) is True:
        delete_trunk = config.find('.//*trunk')
        delete_trunk.set('operation', 'delete')
        
    trunk_vlan_classification = ET.SubElement(trunk, "trunk-vlan-classification")
    if kwargs.pop('delete_trunk_vlan_classification', False) is True:
        delete_trunk_vlan_classification = config.find('.//*trunk-vlan-classification')
        delete_trunk_vlan_classification.set('operation', 'delete')
        
    allowed = ET.SubElement(trunk_vlan_classification, "allowed")
    if kwargs.pop('delete_allowed', False) is True:
        delete_allowed = config.find('.//*allowed')
        delete_allowed.set('operation', 'delete')
        
    vlan = ET.SubElement(allowed, "vlan")
    if kwargs.pop('delete_vlan', False) is True:
        delete_vlan = config.find('.//*vlan')
        delete_vlan.set('operation', 'delete')
        
    remove = ET.SubElement(vlan, "remove")
    if kwargs.pop('delete_remove', False) is True:
        delete_remove = config.find('.//*remove')
        delete_remove.set('operation', 'delete')
        
    trunk_vlan_id = ET.SubElement(remove, "trunk-vlan-id")
    if kwargs.pop('delete_trunk_vlan_id', False) is True:
        delete_trunk_vlan_id = config.find('.//*trunk-vlan-id')
        delete_trunk_vlan_id.set('operation', 'delete')
        
    trunk_vlan_id.text = kwargs.pop('trunk_vlan_id')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class interface_fortygigabitethernet_switchport_trunk_trunk_vlan_classification_allowed_vlan_remove_trunk_vlan_id_act(Action):
    def run(self, delete_switchport, delete_vlan, delete_allowed, trunk_vlan_id, name, delete_trunk_vlan_classification, delete_trunk, delete_fortygigabitethernet, delete_interface, delete_name, delete_remove, delete_trunk_vlan_id, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        interface_fortygigabitethernet_switchport_trunk_trunk_vlan_classification_allowed_vlan_remove_trunk_vlan_id(name=name, delete_trunk=delete_trunk, delete_name=delete_name, username=username, delete_switchport=delete_switchport, delete_trunk_vlan_id=delete_trunk_vlan_id, delete_trunk_vlan_classification=delete_trunk_vlan_classification, delete_allowed=delete_allowed, trunk_vlan_id=trunk_vlan_id, delete_vlan=delete_vlan, host=host, delete_fortygigabitethernet=delete_fortygigabitethernet, delete_interface=delete_interface, delete_remove=delete_remove, password=password, callback=_callback, mgr=mgr)
        return 0
    