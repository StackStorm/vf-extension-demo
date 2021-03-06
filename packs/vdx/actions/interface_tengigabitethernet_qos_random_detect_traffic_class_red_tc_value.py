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


def interface_tengigabitethernet_qos_random_detect_traffic_class_red_tc_value(**kwargs):
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
            
    qos = ET.SubElement(tengigabitethernet, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
    if kwargs.pop('delete_qos', False) is True:
        delete_qos = config.find('.//*qos')
        delete_qos.set('operation', 'delete')
        
    random_detect = ET.SubElement(qos, "random-detect")
    if kwargs.pop('delete_random_detect', False) is True:
        delete_random_detect = config.find('.//*random-detect')
        delete_random_detect.set('operation', 'delete')
        
    traffic_class = ET.SubElement(random_detect, "traffic-class")
    if kwargs.pop('delete_traffic_class', False) is True:
        delete_traffic_class = config.find('.//*traffic-class')
        delete_traffic_class.set('operation', 'delete')
        
    red_tc_value = ET.SubElement(traffic_class, "red-tc-value")
    if kwargs.pop('delete_red_tc_value', False) is True:
        delete_red_tc_value = config.find('.//*red-tc-value')
        delete_red_tc_value.set('operation', 'delete')
        
    red_tc_value.text = kwargs.pop('red_tc_value')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class interface_tengigabitethernet_qos_random_detect_traffic_class_red_tc_value_act(Action):
    def run(self, delete_qos, delete_red_tc_value, name, red_tc_value, delete_traffic_class, delete_interface, delete_name, delete_tengigabitethernet, delete_random_detect, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        interface_tengigabitethernet_qos_random_detect_traffic_class_red_tc_value(delete_qos=delete_qos, delete_traffic_class=delete_traffic_class, delete_name=delete_name, name=name, red_tc_value=red_tc_value, delete_tengigabitethernet=delete_tengigabitethernet, host=host, delete_random_detect=delete_random_detect, delete_red_tc_value=delete_red_tc_value, delete_interface=delete_interface, username=username, password=password, callback=_callback, mgr=mgr)
        return 0
    