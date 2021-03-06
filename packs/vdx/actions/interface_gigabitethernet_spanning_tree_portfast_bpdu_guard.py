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


def interface_gigabitethernet_spanning_tree_portfast_bpdu_guard(**kwargs):
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
            
    spanning_tree = ET.SubElement(gigabitethernet, "spanning-tree", xmlns="urn:brocade.com:mgmt:brocade-xstp")
    if kwargs.pop('delete_spanning_tree', False) is True:
        delete_spanning_tree = config.find('.//*spanning-tree')
        delete_spanning_tree.set('operation', 'delete')
        
    portfast = ET.SubElement(spanning_tree, "portfast")
    if kwargs.pop('delete_portfast', False) is True:
        delete_portfast = config.find('.//*portfast')
        delete_portfast.set('operation', 'delete')
        
    bpdu_guard = ET.SubElement(portfast, "bpdu-guard")
    if kwargs.pop('delete_bpdu_guard', False) is True:
        delete_bpdu_guard = config.find('.//*bpdu-guard')
        delete_bpdu_guard.set('operation', 'delete')
        

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class interface_gigabitethernet_spanning_tree_portfast_bpdu_guard_act(Action):
    def run(self, delete_portfast, name, delete_bpdu_guard, delete_interface, delete_name, delete_spanning_tree, delete_gigabitethernet, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        interface_gigabitethernet_spanning_tree_portfast_bpdu_guard(name=name, delete_name=delete_name, username=username, delete_spanning_tree=delete_spanning_tree, delete_gigabitethernet=delete_gigabitethernet, host=host, delete_portfast=delete_portfast, delete_interface=delete_interface, delete_bpdu_guard=delete_bpdu_guard, password=password, callback=_callback, mgr=mgr)
        return 0
    