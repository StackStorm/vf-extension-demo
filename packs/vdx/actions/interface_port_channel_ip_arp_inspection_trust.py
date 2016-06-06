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


def interface_port_channel_ip_arp_inspection_trust(**kwargs):
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
            
    ip = ET.SubElement(port_channel, "ip")
    if kwargs.pop('delete_ip', False) is True:
        delete_ip = config.find('.//*ip')
        delete_ip.set('operation', 'delete')
        
    arp = ET.SubElement(ip, "arp", xmlns="urn:brocade.com:mgmt:brocade-dai")
    if kwargs.pop('delete_arp', False) is True:
        delete_arp = config.find('.//*arp')
        delete_arp.set('operation', 'delete')
        
    inspection = ET.SubElement(arp, "inspection")
    if kwargs.pop('delete_inspection', False) is True:
        delete_inspection = config.find('.//*inspection')
        delete_inspection.set('operation', 'delete')
        
    trust = ET.SubElement(inspection, "trust")
    if kwargs.pop('delete_trust', False) is True:
        delete_trust = config.find('.//*trust')
        delete_trust.set('operation', 'delete')
        

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class interface_port_channel_ip_arp_inspection_trust_act(Action):
    def run(self, delete_inspection, name, delete_ip, delete_trust, delete_port_channel, delete_arp, delete_name, delete_interface, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        interface_port_channel_ip_arp_inspection_trust(name=name, delete_name=delete_name, delete_inspection=delete_inspection, delete_trust=delete_trust, delete_arp=delete_arp, delete_ip=delete_ip, delete_port_channel=delete_port_channel, host=host, delete_interface=delete_interface, username=username, password=password, callback=_callback, mgr=mgr)
        return 0
    