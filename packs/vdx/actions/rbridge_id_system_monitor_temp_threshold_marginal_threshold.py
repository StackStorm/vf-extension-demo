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


def rbridge_id_system_monitor_temp_threshold_marginal_threshold(**kwargs):
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
            
    system_monitor = ET.SubElement(rbridge_id, "system-monitor", xmlns="urn:brocade.com:mgmt:brocade-system-monitor")
    if kwargs.pop('delete_system_monitor', False) is True:
        delete_system_monitor = config.find('.//*system-monitor')
        delete_system_monitor.set('operation', 'delete')
        
    temp = ET.SubElement(system_monitor, "temp")
    if kwargs.pop('delete_temp', False) is True:
        delete_temp = config.find('.//*temp')
        delete_temp.set('operation', 'delete')
        
    threshold = ET.SubElement(temp, "threshold")
    if kwargs.pop('delete_threshold', False) is True:
        delete_threshold = config.find('.//*threshold')
        delete_threshold.set('operation', 'delete')
        
    marginal_threshold = ET.SubElement(threshold, "marginal-threshold")
    if kwargs.pop('delete_marginal_threshold', False) is True:
        delete_marginal_threshold = config.find('.//*marginal-threshold')
        delete_marginal_threshold.set('operation', 'delete')
        
    marginal_threshold.text = kwargs.pop('marginal_threshold')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class rbridge_id_system_monitor_temp_threshold_marginal_threshold_act(Action):
    def run(self, delete_threshold, delete_system_monitor, delete_temp, delete_marginal_threshold, delete_rbridge_id, marginal_threshold, rbridge_id, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        rbridge_id_system_monitor_temp_threshold_marginal_threshold(delete_system_monitor=delete_system_monitor, delete_marginal_threshold=delete_marginal_threshold, delete_temp=delete_temp, marginal_threshold=marginal_threshold, username=username, rbridge_id=rbridge_id, host=host, delete_threshold=delete_threshold, delete_rbridge_id=delete_rbridge_id, password=password, callback=_callback, mgr=mgr)
        return 0
    