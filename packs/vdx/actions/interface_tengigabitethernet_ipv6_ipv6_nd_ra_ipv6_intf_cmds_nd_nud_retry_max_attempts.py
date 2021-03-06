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


def interface_tengigabitethernet_ipv6_ipv6_nd_ra_ipv6_intf_cmds_nd_nud_retry_max_attempts(**kwargs):
    """Auto Generated Code
    """
    config = ET.Element("config")
    interface = ET.SubElement(config, "interface", xmlns="urn:brocade.com:mgmt:brocade-interface")
    if kwargs.pop('delete_interface', False) is True:
        delete_interface = config.find('.//*interface')
        delete_interface.set('operation', 'delete')
        
    tengigabitethernet = ET.SubElement(interface, "tengigabitethernet")
    if kwargs.pop('delete_tengigabitethernet', False) is True:
        delete_tengigabitethernet = config.find('.//*tengigabitethernet')
        delete_tengigabitethernet.set('operation', 'delete')
        
    name_key = ET.SubElement(tengigabitethernet, "name")
    name_key.text = kwargs.pop('name')
    if kwargs.pop('delete_name', False) is True:
        delete_name = config.find('.//*name')
        delete_name.set('operation', 'delete')
            
    ipv6 = ET.SubElement(tengigabitethernet, "ipv6")
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
        
    nud = ET.SubElement(nd, "nud")
    if kwargs.pop('delete_nud', False) is True:
        delete_nud = config.find('.//*nud')
        delete_nud.set('operation', 'delete')
        
    retry = ET.SubElement(nud, "retry")
    if kwargs.pop('delete_retry', False) is True:
        delete_retry = config.find('.//*retry')
        delete_retry.set('operation', 'delete')
        
    max_attempts = ET.SubElement(retry, "max-attempts")
    if kwargs.pop('delete_max_attempts', False) is True:
        delete_max_attempts = config.find('.//*max-attempts')
        delete_max_attempts.set('operation', 'delete')
        
    max_attempts.text = kwargs.pop('max_attempts')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class interface_tengigabitethernet_ipv6_ipv6_nd_ra_ipv6_intf_cmds_nd_nud_retry_max_attempts_act(Action):
    def run(self, name, delete_nud, delete_interface, delete_name, delete_tengigabitethernet, delete_nd, delete_max_attempts, delete_retry, max_attempts, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        interface_tengigabitethernet_ipv6_ipv6_nd_ra_ipv6_intf_cmds_nd_nud_retry_max_attempts(delete_retry=delete_retry, name=name, delete_name=delete_name, max_attempts=max_attempts, delete_nud=delete_nud, delete_max_attempts=delete_max_attempts, delete_tengigabitethernet=delete_tengigabitethernet, delete_nd=delete_nd, host=host, delete_interface=delete_interface, username=username, password=password, callback=_callback, mgr=mgr)
        return 0
    