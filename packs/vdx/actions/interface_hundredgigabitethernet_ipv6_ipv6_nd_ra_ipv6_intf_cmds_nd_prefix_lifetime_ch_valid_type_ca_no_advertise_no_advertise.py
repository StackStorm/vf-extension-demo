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


def interface_hundredgigabitethernet_ipv6_ipv6_nd_ra_ipv6_intf_cmds_nd_prefix_lifetime_ch_valid_type_ca_no_advertise_no_advertise(**kwargs):
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
        
    nd = ET.SubElement(ipv6_intf_cmds, "nd")
    if kwargs.pop('delete_nd', False) is True:
        delete_nd = config.find('.//*nd')
        delete_nd.set('operation', 'delete')
        
    prefix = ET.SubElement(nd, "prefix")
    if kwargs.pop('delete_prefix', False) is True:
        delete_prefix = config.find('.//*prefix')
        delete_prefix.set('operation', 'delete')
        
    prefix_ipv6_address_key = ET.SubElement(prefix, "prefix-ipv6-address")
    prefix_ipv6_address_key.text = kwargs.pop('prefix_ipv6_address')
    if kwargs.pop('delete_prefix_ipv6_address', False) is True:
        delete_prefix_ipv6_address = config.find('.//*prefix-ipv6-address')
        delete_prefix_ipv6_address.set('operation', 'delete')
            
    lifetime = ET.SubElement(prefix, "lifetime")
    if kwargs.pop('delete_lifetime', False) is True:
        delete_lifetime = config.find('.//*lifetime')
        delete_lifetime.set('operation', 'delete')
        
    ch_valid_type = ET.SubElement(lifetime, "ch-valid-type")
    if kwargs.pop('delete_ch_valid_type', False) is True:
        delete_ch_valid_type = config.find('.//*ch-valid-type')
        delete_ch_valid_type.set('operation', 'delete')
        
    ca_no_advertise = ET.SubElement(ch_valid_type, "ca-no-advertise")
    if kwargs.pop('delete_ca_no_advertise', False) is True:
        delete_ca_no_advertise = config.find('.//*ca-no-advertise')
        delete_ca_no_advertise.set('operation', 'delete')
        
    no_advertise = ET.SubElement(ca_no_advertise, "no-advertise")
    if kwargs.pop('delete_no_advertise', False) is True:
        delete_no_advertise = config.find('.//*no-advertise')
        delete_no_advertise.set('operation', 'delete')
        

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class interface_hundredgigabitethernet_ipv6_ipv6_nd_ra_ipv6_intf_cmds_nd_prefix_lifetime_ch_valid_type_ca_no_advertise_no_advertise_act(Action):
    def run(self, delete_prefix, delete_ch_valid_type, delete_ca_no_advertise, delete_no_advertise, delete_interface, delete_name, delete_hundredgigabitethernet, delete_lifetime, delete_nd, name, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        interface_hundredgigabitethernet_ipv6_ipv6_nd_ra_ipv6_intf_cmds_nd_prefix_lifetime_ch_valid_type_ca_no_advertise_no_advertise(name=name, delete_prefix=delete_prefix, delete_hundredgigabitethernet=delete_hundredgigabitethernet, username=username, delete_lifetime=delete_lifetime, delete_nd=delete_nd, host=host, delete_no_advertise=delete_no_advertise, delete_name=delete_name, delete_ch_valid_type=delete_ch_valid_type, delete_ca_no_advertise=delete_ca_no_advertise, delete_interface=delete_interface, password=password, callback=_callback, mgr=mgr)
        return 0
    