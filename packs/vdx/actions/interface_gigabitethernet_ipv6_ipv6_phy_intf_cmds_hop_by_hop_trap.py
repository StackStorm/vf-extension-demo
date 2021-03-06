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


def interface_gigabitethernet_ipv6_ipv6_phy_intf_cmds_hop_by_hop_trap(**kwargs):
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
            
    ipv6 = ET.SubElement(gigabitethernet, "ipv6")
    if kwargs.pop('delete_ipv6', False) is True:
        delete_ipv6 = config.find('.//*ipv6')
        delete_ipv6.set('operation', 'delete')
        
    ipv6_phy_intf_cmds = ET.SubElement(ipv6, "ipv6-phy-intf-cmds", xmlns="urn:brocade.com:mgmt:brocade-mld-snooping")
    if kwargs.pop('delete_ipv6_phy_intf_cmds', False) is True:
        delete_ipv6_phy_intf_cmds = config.find('.//*ipv6-phy-intf-cmds')
        delete_ipv6_phy_intf_cmds.set('operation', 'delete')
        
    hop_by_hop_trap = ET.SubElement(ipv6_phy_intf_cmds, "hop-by-hop-trap")
    if kwargs.pop('delete_hop_by_hop_trap', False) is True:
        delete_hop_by_hop_trap = config.find('.//*hop-by-hop-trap')
        delete_hop_by_hop_trap.set('operation', 'delete')
        

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class interface_gigabitethernet_ipv6_ipv6_phy_intf_cmds_hop_by_hop_trap_act(Action):
    def run(self, delete_name, delete_hop_by_hop_trap, delete_interface, delete_gigabitethernet, name, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        interface_gigabitethernet_ipv6_ipv6_phy_intf_cmds_hop_by_hop_trap(delete_hop_by_hop_trap=delete_hop_by_hop_trap, delete_name=delete_name, name=name, host=host, delete_gigabitethernet=delete_gigabitethernet, delete_interface=delete_interface, username=username, password=password, callback=_callback, mgr=mgr)
        return 0
    