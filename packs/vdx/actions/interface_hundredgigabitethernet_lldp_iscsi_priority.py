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


def interface_hundredgigabitethernet_lldp_iscsi_priority(**kwargs):
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
            
    lldp = ET.SubElement(hundredgigabitethernet, "lldp", xmlns="urn:brocade.com:mgmt:brocade-lldp")
    if kwargs.pop('delete_lldp', False) is True:
        delete_lldp = config.find('.//*lldp')
        delete_lldp.set('operation', 'delete')
        
    iscsi_priority = ET.SubElement(lldp, "iscsi-priority")
    if kwargs.pop('delete_iscsi_priority', False) is True:
        delete_iscsi_priority = config.find('.//*iscsi-priority')
        delete_iscsi_priority.set('operation', 'delete')
        
    iscsi_priority.text = kwargs.pop('iscsi_priority')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class interface_hundredgigabitethernet_lldp_iscsi_priority_act(Action):
    def run(self, iscsi_priority, name, delete_lldp, delete_iscsi_priority, delete_interface, delete_name, delete_hundredgigabitethernet, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        interface_hundredgigabitethernet_lldp_iscsi_priority(name=name, delete_iscsi_priority=delete_iscsi_priority, delete_lldp=delete_lldp, delete_hundredgigabitethernet=delete_hundredgigabitethernet, iscsi_priority=iscsi_priority, host=host, delete_name=delete_name, delete_interface=delete_interface, username=username, password=password, callback=_callback, mgr=mgr)
        return 0
    