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


def interface_gigabitethernet_qos_rcv_queue_cos_threshold_cos5_threshold(**kwargs):
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
            
    qos = ET.SubElement(gigabitethernet, "qos", xmlns="urn:brocade.com:mgmt:brocade-qos")
    if kwargs.pop('delete_qos', False) is True:
        delete_qos = config.find('.//*qos')
        delete_qos.set('operation', 'delete')
        
    rcv_queue = ET.SubElement(qos, "rcv-queue")
    if kwargs.pop('delete_rcv_queue', False) is True:
        delete_rcv_queue = config.find('.//*rcv-queue')
        delete_rcv_queue.set('operation', 'delete')
        
    cos_threshold = ET.SubElement(rcv_queue, "cos-threshold")
    if kwargs.pop('delete_cos_threshold', False) is True:
        delete_cos_threshold = config.find('.//*cos-threshold')
        delete_cos_threshold.set('operation', 'delete')
        
    cos5_threshold = ET.SubElement(cos_threshold, "cos5-threshold")
    if kwargs.pop('delete_cos5_threshold', False) is True:
        delete_cos5_threshold = config.find('.//*cos5-threshold')
        delete_cos5_threshold.set('operation', 'delete')
        
    cos5_threshold.text = kwargs.pop('cos5_threshold')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class interface_gigabitethernet_qos_rcv_queue_cos_threshold_cos5_threshold_act(Action):
    def run(self, delete_qos, name, delete_rcv_queue, delete_interface, delete_name, delete_gigabitethernet, delete_cos_threshold, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        interface_gigabitethernet_qos_rcv_queue_cos_threshold_cos5_threshold(delete_qos=delete_qos, delete_name=delete_name, name=name, host=host, password=password, delete_gigabitethernet=delete_gigabitethernet, delete_interface=delete_interface, username=username, delete_rcv_queue=delete_rcv_queue, delete_cos_threshold=delete_cos_threshold, callback=_callback, mgr=mgr)
        return 0
    