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


def interface_port_channel_ipv6_hide_vrrpv3_holder_vrrpv3_track_interface_interface_type(**kwargs):
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
            
    ipv6 = ET.SubElement(port_channel, "ipv6")
    if kwargs.pop('delete_ipv6', False) is True:
        delete_ipv6 = config.find('.//*ipv6')
        delete_ipv6.set('operation', 'delete')
        
    hide_vrrpv3_holder = ET.SubElement(ipv6, "hide-vrrpv3-holder", xmlns="urn:brocade.com:mgmt:brocade-vrrpv3")
    if kwargs.pop('delete_hide_vrrpv3_holder', False) is True:
        delete_hide_vrrpv3_holder = config.find('.//*hide-vrrpv3-holder')
        delete_hide_vrrpv3_holder.set('operation', 'delete')
        
    vrrpv3 = ET.SubElement(hide_vrrpv3_holder, "vrrpv3")
    if kwargs.pop('delete_vrrpv3', False) is True:
        delete_vrrpv3 = config.find('.//*vrrpv3')
        delete_vrrpv3.set('operation', 'delete')
        
    vrid_key = ET.SubElement(vrrpv3, "vrid")
    vrid_key.text = kwargs.pop('vrid')
    if kwargs.pop('delete_vrid', False) is True:
        delete_vrid = config.find('.//*vrid')
        delete_vrid.set('operation', 'delete')
            
    track = ET.SubElement(vrrpv3, "track")
    if kwargs.pop('delete_track', False) is True:
        delete_track = config.find('.//*track')
        delete_track.set('operation', 'delete')
        
    interface = ET.SubElement(track, "interface")
    if kwargs.pop('delete_interface', False) is True:
        delete_interface = config.find('.//*interface')
        delete_interface.set('operation', 'delete')
        
    interface_name_key = ET.SubElement(interface, "interface-name")
    interface_name_key.text = kwargs.pop('interface_name')
    if kwargs.pop('delete_interface_name', False) is True:
        delete_interface_name = config.find('.//*interface-name')
        delete_interface_name.set('operation', 'delete')
            
    interface_type = ET.SubElement(interface, "interface-type")
    if kwargs.pop('delete_interface_type', False) is True:
        delete_interface_type = config.find('.//*interface-type')
        delete_interface_type.set('operation', 'delete')
        
    interface_type.text = kwargs.pop('interface_type')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class interface_port_channel_ipv6_hide_vrrpv3_holder_vrrpv3_track_interface_interface_type_act(Action):
    def run(self, delete_interface_name, name, delete_vrid, interface_type, vrid, delete_interface_type, delete_port_channel, delete_interface, delete_name, interface_name, delete_track, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        interface_port_channel_ipv6_hide_vrrpv3_holder_vrrpv3_track_interface_interface_type(delete_vrid=delete_vrid, name=name, delete_name=delete_name, delete_track=delete_track, interface_name=interface_name, delete_port_channel=delete_port_channel, delete_interface_type=delete_interface_type, delete_interface_name=delete_interface_name, vrid=vrid, interface_type=interface_type, host=host, delete_interface=delete_interface, username=username, password=password, callback=_callback, mgr=mgr)
        return 0
    