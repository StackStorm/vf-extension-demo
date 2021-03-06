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


def rbridge_id_threshold_monitor_security_apply(**kwargs):
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
        
    security = ET.SubElement(threshold_monitor, "security")
    if kwargs.pop('delete_security', False) is True:
        delete_security = config.find('.//*security')
        delete_security.set('operation', 'delete')
        
    apply = ET.SubElement(security, "apply")
    if kwargs.pop('delete_apply', False) is True:
        delete_apply = config.find('.//*apply')
        delete_apply.set('operation', 'delete')
        
    apply.text = kwargs.pop('apply')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class rbridge_id_threshold_monitor_security_apply_act(Action):
    def run(self, rbridge_id, delete_security, apply, delete_threshold_monitor, delete_apply, delete_rbridge_id, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        rbridge_id_threshold_monitor_security_apply(apply=apply, username=username, delete_threshold_monitor=delete_threshold_monitor, delete_security=delete_security, rbridge_id=rbridge_id, delete_apply=delete_apply, host=host, delete_rbridge_id=delete_rbridge_id, password=password, callback=_callback, mgr=mgr)
        return 0
    