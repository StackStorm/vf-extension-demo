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


def interface_tengigabitethernet_ip_ip_config_unnumbered_ip_donor_interface_type(**kwargs):
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
            
    ip = ET.SubElement(tengigabitethernet, "ip")
    if kwargs.pop('delete_ip', False) is True:
        delete_ip = config.find('.//*ip')
        delete_ip.set('operation', 'delete')
        
    ip_config = ET.SubElement(ip, "ip-config", xmlns="urn:brocade.com:mgmt:brocade-ip-config")
    if kwargs.pop('delete_ip_config', False) is True:
        delete_ip_config = config.find('.//*ip-config')
        delete_ip_config.set('operation', 'delete')
        
    unnumbered = ET.SubElement(ip_config, "unnumbered")
    if kwargs.pop('delete_unnumbered', False) is True:
        delete_unnumbered = config.find('.//*unnumbered')
        delete_unnumbered.set('operation', 'delete')
        
    ip_donor_interface_type = ET.SubElement(unnumbered, "ip-donor-interface-type")
    if kwargs.pop('delete_ip_donor_interface_type', False) is True:
        delete_ip_donor_interface_type = config.find('.//*ip-donor-interface-type')
        delete_ip_donor_interface_type.set('operation', 'delete')
        
    ip_donor_interface_type.text = kwargs.pop('ip_donor_interface_type')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class interface_tengigabitethernet_ip_ip_config_unnumbered_ip_donor_interface_type_act(Action):
    def run(self, delete_ip_config, delete_ip_donor_interface_type, name, delete_ip, ip_donor_interface_type, delete_unnumbered, delete_interface, delete_name, delete_tengigabitethernet, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        interface_tengigabitethernet_ip_ip_config_unnumbered_ip_donor_interface_type(name=name, delete_unnumbered=delete_unnumbered, delete_ip_config=delete_ip_config, delete_ip=delete_ip, delete_ip_donor_interface_type=delete_ip_donor_interface_type, delete_tengigabitethernet=delete_tengigabitethernet, host=host, ip_donor_interface_type=ip_donor_interface_type, delete_name=delete_name, delete_interface=delete_interface, username=username, password=password, callback=_callback, mgr=mgr)
        return 0
    