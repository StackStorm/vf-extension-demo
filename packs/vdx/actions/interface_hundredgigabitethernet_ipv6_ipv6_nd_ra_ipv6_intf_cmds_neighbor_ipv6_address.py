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


def interface_hundredgigabitethernet_ipv6_ipv6_nd_ra_ipv6_intf_cmds_neighbor_ipv6_address(**kwargs):
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
            
    ipv6 = ET.SubElement(hundredgigabitethernet, "ipv6")
    if kwargs.pop('delete_ipv6', False) is True:
        delete_ipv6 = config.find('.//*ipv6')
        delete_ipv6.set('operation', 'delete')
        
    ipv6_nd_ra = ET.SubElement(ipv6, "ipv6-nd-ra", xmlns="urn:brocade.com:mgmt:brocade-ipv6-nd-ra")
    if kwargs.pop('delete_ipv6_nd_ra', False) is True:
        delete_ipv6_nd_ra = config.find('.//*ipv6-nd-ra')
        delete_ipv6_nd_ra.set('operation', 'delete')
        
    ipv6_intf_cmds = ET.SubElement(ipv6_nd_ra, "ipv6-intf-cmds")
    if kwargs.pop('delete_ipv6_intf_cmds', False) is True:
        delete_ipv6_intf_cmds = config.find('.//*ipv6-intf-cmds')
        delete_ipv6_intf_cmds.set('operation', 'delete')
        
    neighbor = ET.SubElement(ipv6_intf_cmds, "neighbor")
    if kwargs.pop('delete_neighbor', False) is True:
        delete_neighbor = config.find('.//*neighbor')
        delete_neighbor.set('operation', 'delete')
        
    ipv6_address = ET.SubElement(neighbor, "ipv6-address")
    if kwargs.pop('delete_ipv6_address', False) is True:
        delete_ipv6_address = config.find('.//*ipv6-address')
        delete_ipv6_address.set('operation', 'delete')
        
    ipv6_address.text = kwargs.pop('ipv6_address')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class interface_hundredgigabitethernet_ipv6_ipv6_nd_ra_ipv6_intf_cmds_neighbor_ipv6_address_act(Action):
    def run(self, delete_neighbor, delete_hundredgigabitethernet, delete_interface, delete_name, name, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        interface_hundredgigabitethernet_ipv6_ipv6_nd_ra_ipv6_intf_cmds_neighbor_ipv6_address(name=name, delete_name=delete_name, delete_neighbor=delete_neighbor, delete_hundredgigabitethernet=delete_hundredgigabitethernet, host=host, delete_interface=delete_interface, username=username, password=password, callback=_callback, mgr=mgr)
        return 0
    