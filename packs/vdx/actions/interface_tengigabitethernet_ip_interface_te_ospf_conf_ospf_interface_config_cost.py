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


def interface_tengigabitethernet_ip_interface_te_ospf_conf_ospf_interface_config_cost(**kwargs):
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
            
    ip = ET.SubElement(tengigabitethernet, "ip")
    if kwargs.pop('delete_ip', False) is True:
        delete_ip = config.find('.//*ip')
        delete_ip.set('operation', 'delete')
        
    interface_te_ospf_conf = ET.SubElement(ip, "interface-te-ospf-conf", xmlns="urn:brocade.com:mgmt:brocade-ospf")
    if kwargs.pop('delete_interface_te_ospf_conf', False) is True:
        delete_interface_te_ospf_conf = config.find('.//*interface-te-ospf-conf')
        delete_interface_te_ospf_conf.set('operation', 'delete')
        
    ospf_interface_config = ET.SubElement(interface_te_ospf_conf, "ospf-interface-config")
    if kwargs.pop('delete_ospf_interface_config', False) is True:
        delete_ospf_interface_config = config.find('.//*ospf-interface-config')
        delete_ospf_interface_config.set('operation', 'delete')
        
    cost = ET.SubElement(ospf_interface_config, "cost")
    if kwargs.pop('delete_cost', False) is True:
        delete_cost = config.find('.//*cost')
        delete_cost.set('operation', 'delete')
        
    cost.text = kwargs.pop('cost')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class interface_tengigabitethernet_ip_interface_te_ospf_conf_ospf_interface_config_cost_act(Action):
    def run(self, delete_interface_te_ospf_conf, name, delete_ip, delete_cost, cost, delete_interface, delete_name, delete_tengigabitethernet, delete_ospf_interface_config, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        interface_tengigabitethernet_ip_interface_te_ospf_conf_ospf_interface_config_cost(delete_cost=delete_cost, name=name, delete_name=delete_name, username=username, delete_ip=delete_ip, delete_ospf_interface_config=delete_ospf_interface_config, delete_tengigabitethernet=delete_tengigabitethernet, cost=cost, host=host, delete_interface=delete_interface, delete_interface_te_ospf_conf=delete_interface_te_ospf_conf, password=password, callback=_callback, mgr=mgr)
        return 0
    