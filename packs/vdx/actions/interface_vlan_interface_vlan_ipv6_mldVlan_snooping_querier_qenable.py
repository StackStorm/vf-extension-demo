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


def interface_vlan_interface_vlan_ipv6_mldVlan_snooping_querier_qenable(**kwargs):
    """Auto Generated Code
    """
    config = ET.Element("config")
    interface_vlan = ET.SubElement(config, "interface-vlan", xmlns="urn:brocade.com:mgmt:brocade-interface")
    if kwargs.pop('delete_interface_vlan', False) is True:
        delete_interface_vlan = config.find('.//*interface-vlan')
        delete_interface_vlan.set('operation', 'delete')
        
    interface = ET.SubElement(interface_vlan, "interface")
    if kwargs.pop('delete_interface', False) is True:
        delete_interface = config.find('.//*interface')
        delete_interface.set('operation', 'delete')
        
    vlan = ET.SubElement(interface, "vlan")
    if kwargs.pop('delete_vlan', False) is True:
        delete_vlan = config.find('.//*vlan')
        delete_vlan.set('operation', 'delete')
        
    name_key = ET.SubElement(vlan, "name")
    name_key.text = kwargs.pop('name')
    if kwargs.pop('delete_name', False) is True:
        delete_name = config.find('.//*name')
        delete_name.set('operation', 'delete')
            
    ipv6 = ET.SubElement(vlan, "ipv6")
    if kwargs.pop('delete_ipv6', False) is True:
        delete_ipv6 = config.find('.//*ipv6')
        delete_ipv6.set('operation', 'delete')
        
    mldVlan = ET.SubElement(ipv6, "mldVlan", xmlns="urn:brocade.com:mgmt:brocade-mld-snooping")
    if kwargs.pop('delete_mldVlan', False) is True:
        delete_mldVlan = config.find('.//*mldVlan')
        delete_mldVlan.set('operation', 'delete')
        
    snooping = ET.SubElement(mldVlan, "snooping")
    if kwargs.pop('delete_snooping', False) is True:
        delete_snooping = config.find('.//*snooping')
        delete_snooping.set('operation', 'delete')
        
    querier = ET.SubElement(snooping, "querier")
    if kwargs.pop('delete_querier', False) is True:
        delete_querier = config.find('.//*querier')
        delete_querier.set('operation', 'delete')
        
    qenable = ET.SubElement(querier, "qenable")
    if kwargs.pop('delete_qenable', False) is True:
        delete_qenable = config.find('.//*qenable')
        delete_qenable.set('operation', 'delete')
        

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class interface_vlan_interface_vlan_ipv6_mldVlan_snooping_querier_qenable_act(Action):
    def run(self, delete_vlan, name, delete_snooping, delete_interface_vlan, delete_querier, delete_qenable, delete_mldVlan, delete_interface, delete_name, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        interface_vlan_interface_vlan_ipv6_mldVlan_snooping_querier_qenable(name=name, delete_mldVlan=delete_mldVlan, delete_querier=delete_querier, delete_vlan=delete_vlan, password=password, delete_snooping=delete_snooping, delete_interface_vlan=delete_interface_vlan, host=host, delete_name=delete_name, delete_interface=delete_interface, username=username, delete_qenable=delete_qenable, callback=_callback, mgr=mgr)
        return 0
    