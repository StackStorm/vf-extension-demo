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


def protocol_lldp_profile_multiplier(**kwargs):
    """Auto Generated Code
    """
    config = ET.Element("config")
    protocol = ET.SubElement(config, "protocol", xmlns="urn:brocade.com:mgmt:brocade-interface")
    if kwargs.pop('delete_protocol', False) is True:
        delete_protocol = config.find('.//*protocol')
        delete_protocol.set('operation', 'delete')
        
    lldp = ET.SubElement(protocol, "lldp", xmlns="urn:brocade.com:mgmt:brocade-lldp")
    if kwargs.pop('delete_lldp', False) is True:
        delete_lldp = config.find('.//*lldp')
        delete_lldp.set('operation', 'delete')
        
    profile = ET.SubElement(lldp, "profile")
    if kwargs.pop('delete_profile', False) is True:
        delete_profile = config.find('.//*profile')
        delete_profile.set('operation', 'delete')
        
    profile_name_key = ET.SubElement(profile, "profile-name")
    profile_name_key.text = kwargs.pop('profile_name')
    if kwargs.pop('delete_profile_name', False) is True:
        delete_profile_name = config.find('.//*profile-name')
        delete_profile_name.set('operation', 'delete')
            
    multiplier = ET.SubElement(profile, "multiplier")
    if kwargs.pop('delete_multiplier', False) is True:
        delete_multiplier = config.find('.//*multiplier')
        delete_multiplier.set('operation', 'delete')
        
    multiplier.text = kwargs.pop('multiplier')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class protocol_lldp_profile_multiplier_act(Action):
    def run(self, delete_profile_name, delete_protocol, delete_lldp, delete_multiplier, profile_name, multiplier, delete_profile, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        protocol_lldp_profile_multiplier(delete_profile_name=delete_profile_name, profile_name=profile_name, delete_lldp=delete_lldp, delete_multiplier=delete_multiplier, delete_profile=delete_profile, delete_protocol=delete_protocol, password=password, host=host, username=username, multiplier=multiplier, callback=_callback, mgr=mgr)
        return 0
    