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


def rbridge_id_threshold_monitor_Memory_high_limit(**kwargs):
    """Auto Generated Code
    """
    config = ET.Element("config")
    rbridge_id = ET.SubElement(config, "rbridge-id", xmlns="urn:brocade.com:mgmt:brocade-rbridge")
    if kwargs.pop('delete_rbridge_id', False) is True:
        delete_rbridge_id = config.find('.//*rbridge-id')
        delete_rbridge_id.set('operation', 'delete')
        
    rbridge_id_key = ET.SubElement(rbridge_id, "rbridge-id")
    rbridge_id_key.text = kwargs.pop('rbridge_id')
    if kwargs.pop('delete_rbridge_id', False) is True:
        delete_rbridge_id = config.find('.//*rbridge-id')
        delete_rbridge_id.set('operation', 'delete')
            
    threshold_monitor = ET.SubElement(rbridge_id, "threshold-monitor", xmlns="urn:brocade.com:mgmt:brocade-threshold-monitor")
    if kwargs.pop('delete_threshold_monitor', False) is True:
        delete_threshold_monitor = config.find('.//*threshold-monitor')
        delete_threshold_monitor.set('operation', 'delete')
        
    Memory = ET.SubElement(threshold_monitor, "Memory")
    if kwargs.pop('delete_Memory', False) is True:
        delete_Memory = config.find('.//*Memory')
        delete_Memory.set('operation', 'delete')
        
    high_limit = ET.SubElement(Memory, "high-limit")
    if kwargs.pop('delete_high_limit', False) is True:
        delete_high_limit = config.find('.//*high-limit')
        delete_high_limit.set('operation', 'delete')
        
    high_limit.text = kwargs.pop('high_limit')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class rbridge_id_threshold_monitor_Memory_high_limit_act(Action):
    def run(self, high_limit, rbridge_id, delete_Memory, delete_threshold_monitor, delete_rbridge_id, delete_high_limit, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        rbridge_id_threshold_monitor_Memory_high_limit(username=username, delete_threshold_monitor=delete_threshold_monitor, delete_Memory=delete_Memory, rbridge_id=rbridge_id, delete_high_limit=delete_high_limit, host=host, high_limit=high_limit, delete_rbridge_id=delete_rbridge_id, password=password, callback=_callback, mgr=mgr)
        return 0
    