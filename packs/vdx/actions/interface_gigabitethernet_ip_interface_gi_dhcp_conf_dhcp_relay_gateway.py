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


def interface_gigabitethernet_ip_interface_gi_dhcp_conf_dhcp_relay_gateway(**kwargs):
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
            
    ip = ET.SubElement(gigabitethernet, "ip")
    if kwargs.pop('delete_ip', False) is True:
        delete_ip = config.find('.//*ip')
        delete_ip.set('operation', 'delete')
        
    interface_gi_dhcp_conf = ET.SubElement(ip, "interface-gi-dhcp-conf", xmlns="urn:brocade.com:mgmt:brocade-dhcp")
    if kwargs.pop('delete_interface_gi_dhcp_conf', False) is True:
        delete_interface_gi_dhcp_conf = config.find('.//*interface-gi-dhcp-conf')
        delete_interface_gi_dhcp_conf.set('operation', 'delete')
        
    dhcp = ET.SubElement(interface_gi_dhcp_conf, "dhcp")
    if kwargs.pop('delete_dhcp', False) is True:
        delete_dhcp = config.find('.//*dhcp')
        delete_dhcp.set('operation', 'delete')
        
    relay = ET.SubElement(dhcp, "relay")
    if kwargs.pop('delete_relay', False) is True:
        delete_relay = config.find('.//*relay')
        delete_relay.set('operation', 'delete')
        
    gateway = ET.SubElement(relay, "gateway")
    if kwargs.pop('delete_gateway', False) is True:
        delete_gateway = config.find('.//*gateway')
        delete_gateway.set('operation', 'delete')
        
    gateway.text = kwargs.pop('gateway')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class interface_gigabitethernet_ip_interface_gi_dhcp_conf_dhcp_relay_gateway_act(Action):
    def run(self, name, delete_ip, delete_dhcp, delete_relay, delete_interface, delete_name, delete_gateway, delete_interface_gi_dhcp_conf, gateway, delete_gigabitethernet, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        interface_gigabitethernet_ip_interface_gi_dhcp_conf_dhcp_relay_gateway(name=name, delete_name=delete_name, delete_relay=delete_relay, delete_ip=delete_ip, delete_dhcp=delete_dhcp, gateway=gateway, delete_interface_gi_dhcp_conf=delete_interface_gi_dhcp_conf, delete_gateway=delete_gateway, host=host, delete_interface=delete_interface, delete_gigabitethernet=delete_gigabitethernet, username=username, password=password, callback=_callback, mgr=mgr)
        return 0
    