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


def interface_fortygigabitethernet_ip_pim_intf_phy_cont_pim_int_cmd_mcast_bdry_prefix_list(**kwargs):
    """Auto Generated Code
    """
    config = ET.Element("config")
    interface = ET.SubElement(config, "interface", xmlns="urn:brocade.com:mgmt:brocade-interface")
    if kwargs.pop('delete_interface', False) is True:
        delete_interface = config.find('.//*interface')
        delete_interface.set('operation', 'delete')
        
    fortygigabitethernet = ET.SubElement(interface, "fortygigabitethernet")
    if kwargs.pop('delete_fortygigabitethernet', False) is True:
        delete_fortygigabitethernet = config.find('.//*fortygigabitethernet')
        delete_fortygigabitethernet.set('operation', 'delete')
        
    name_key = ET.SubElement(fortygigabitethernet, "name")
    name_key.text = kwargs.pop('name')
    if kwargs.pop('delete_name', False) is True:
        delete_name = config.find('.//*name')
        delete_name.set('operation', 'delete')
            
    ip = ET.SubElement(fortygigabitethernet, "ip")
    if kwargs.pop('delete_ip', False) is True:
        delete_ip = config.find('.//*ip')
        delete_ip.set('operation', 'delete')
        
    pim_intf_phy_cont = ET.SubElement(ip, "pim-intf-phy-cont", xmlns="urn:brocade.com:mgmt:brocade-pim")
    if kwargs.pop('delete_pim_intf_phy_cont', False) is True:
        delete_pim_intf_phy_cont = config.find('.//*pim-intf-phy-cont')
        delete_pim_intf_phy_cont.set('operation', 'delete')
        
    pim_int_cmd = ET.SubElement(pim_intf_phy_cont, "pim-int-cmd")
    if kwargs.pop('delete_pim_int_cmd', False) is True:
        delete_pim_int_cmd = config.find('.//*pim-int-cmd')
        delete_pim_int_cmd.set('operation', 'delete')
        
    mcast_bdry_prefix_list = ET.SubElement(pim_int_cmd, "mcast-bdry-prefix-list")
    if kwargs.pop('delete_mcast_bdry_prefix_list', False) is True:
        delete_mcast_bdry_prefix_list = config.find('.//*mcast-bdry-prefix-list')
        delete_mcast_bdry_prefix_list.set('operation', 'delete')
        
    mcast_bdry_prefix_list.text = kwargs.pop('mcast_bdry_prefix_list')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class interface_fortygigabitethernet_ip_pim_intf_phy_cont_pim_int_cmd_mcast_bdry_prefix_list_act(Action):
    def run(self, delete_pim_intf_phy_cont, delete_ip, delete_mcast_bdry_prefix_list, delete_fortygigabitethernet, delete_interface, delete_name, mcast_bdry_prefix_list, delete_pim_int_cmd, name, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        interface_fortygigabitethernet_ip_pim_intf_phy_cont_pim_int_cmd_mcast_bdry_prefix_list(mcast_bdry_prefix_list=mcast_bdry_prefix_list, name=name, delete_name=delete_name, username=username, delete_ip=delete_ip, delete_pim_int_cmd=delete_pim_int_cmd, delete_pim_intf_phy_cont=delete_pim_intf_phy_cont, host=host, delete_fortygigabitethernet=delete_fortygigabitethernet, delete_interface=delete_interface, delete_mcast_bdry_prefix_list=delete_mcast_bdry_prefix_list, password=password, callback=_callback, mgr=mgr)
        return 0
    