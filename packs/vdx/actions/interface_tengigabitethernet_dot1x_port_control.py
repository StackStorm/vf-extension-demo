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


def interface_tengigabitethernet_dot1x_port_control(**kwargs):
    """Auto Generated Code
    """
    config = ET.Element("config")
    interface = ET.SubElement(config, "interface", xmlns="urn:brocade.com:mgmt:brocade-interface")
    if kwargs.pop('delete_interface', False) is True:
        delete_interface = config.find('.//*interface')
        delete_interface.set('operation', 'delete')
        
    tengigabitethernet = ET.SubElement(interface, "tengigabitethernet")
    if kwargs.pop('delete_tengigabitethernet', False) is True:
        delete_tengigabitethernet = config.find('.//*tengigabitethernet')
        delete_tengigabitethernet.set('operation', 'delete')
        
    name_key = ET.SubElement(tengigabitethernet, "name")
    name_key.text = kwargs.pop('name')
    if kwargs.pop('delete_name', False) is True:
        delete_name = config.find('.//*name')
        delete_name.set('operation', 'delete')
            
    dot1x = ET.SubElement(tengigabitethernet, "dot1x", xmlns="urn:brocade.com:mgmt:brocade-dot1x")
    if kwargs.pop('delete_dot1x', False) is True:
        delete_dot1x = config.find('.//*dot1x')
        delete_dot1x.set('operation', 'delete')
        
    port_control = ET.SubElement(dot1x, "port-control")
    if kwargs.pop('delete_port_control', False) is True:
        delete_port_control = config.find('.//*port-control')
        delete_port_control.set('operation', 'delete')
        
    port_control.text = kwargs.pop('port_control')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class interface_tengigabitethernet_dot1x_port_control_act(Action):
    def run(self, name, delete_interface, delete_name, port_control, delete_tengigabitethernet, delete_port_control, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        interface_tengigabitethernet_dot1x_port_control(name=name, delete_name=delete_name, delete_tengigabitethernet=delete_tengigabitethernet, password=password, delete_port_control=delete_port_control, host=host, delete_interface=delete_interface, username=username, port_control=port_control, callback=_callback, mgr=mgr)
        return 0
    