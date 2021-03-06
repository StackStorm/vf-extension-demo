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


def rbridge_id_system_monitor_cid_card_alert_action(**kwargs):
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
        
    cid_card = ET.SubElement(system_monitor, "cid-card")
    if kwargs.pop('delete_cid_card', False) is True:
        delete_cid_card = config.find('.//*cid-card')
        delete_cid_card.set('operation', 'delete')
        
    alert = ET.SubElement(cid_card, "alert")
    if kwargs.pop('delete_alert', False) is True:
        delete_alert = config.find('.//*alert')
        delete_alert.set('operation', 'delete')
        
    action = ET.SubElement(alert, "action")
    if kwargs.pop('delete_action', False) is True:
        delete_action = config.find('.//*action')
        delete_action.set('operation', 'delete')
        
    action.text = kwargs.pop('action')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class rbridge_id_system_monitor_cid_card_alert_action_act(Action):
    def run(self, rbridge_id, delete_cid_card, delete_alert, delete_action, action, delete_rbridge_id, delete_system_monitor, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        rbridge_id_system_monitor_cid_card_alert_action(delete_system_monitor=delete_system_monitor, delete_action=delete_action, action=action, username=username, rbridge_id=rbridge_id, delete_cid_card=delete_cid_card, host=host, delete_alert=delete_alert, delete_rbridge_id=delete_rbridge_id, password=password, callback=_callback, mgr=mgr)
        return 0
    