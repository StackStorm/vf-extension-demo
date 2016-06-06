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


def interface_hundredgigabitethernet_openflow_interface_cfg_openflow_enable_match_profile(**kwargs):
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
            
    openflow_interface_cfg = ET.SubElement(hundredgigabitethernet, "openflow-interface-cfg", xmlns="urn:brocade.com:mgmt:brocade-openflow")
    if kwargs.pop('delete_openflow_interface_cfg', False) is True:
        delete_openflow_interface_cfg = config.find('.//*openflow-interface-cfg')
        delete_openflow_interface_cfg.set('operation', 'delete')
        
    openflow_enable = ET.SubElement(openflow_interface_cfg, "openflow-enable")
    if kwargs.pop('delete_openflow_enable', False) is True:
        delete_openflow_enable = config.find('.//*openflow-enable')
        delete_openflow_enable.set('operation', 'delete')
        
    match_profile = ET.SubElement(openflow_enable, "match-profile")
    if kwargs.pop('delete_match_profile', False) is True:
        delete_match_profile = config.find('.//*match-profile')
        delete_match_profile.set('operation', 'delete')
        
    match_profile.text = kwargs.pop('match_profile')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class interface_hundredgigabitethernet_openflow_interface_cfg_openflow_enable_match_profile_act(Action):
    def run(self, name, match_profile, delete_openflow_interface_cfg, delete_interface, delete_name, delete_openflow_enable, delete_hundredgigabitethernet, delete_match_profile, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        interface_hundredgigabitethernet_openflow_interface_cfg_openflow_enable_match_profile(name=name, delete_openflow_interface_cfg=delete_openflow_interface_cfg, delete_match_profile=delete_match_profile, delete_openflow_enable=delete_openflow_enable, delete_name=delete_name, delete_hundredgigabitethernet=delete_hundredgigabitethernet, host=host, match_profile=match_profile, delete_interface=delete_interface, username=username, password=password, callback=_callback, mgr=mgr)
        return 0
    