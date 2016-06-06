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


def rbridge_id_ipv6_receive_access_group_ipv6_access_list(**kwargs):
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
            
    ipv6 = ET.SubElement(rbridge_id, "ipv6")
    if kwargs.pop('delete_ipv6', False) is True:
        delete_ipv6 = config.find('.//*ipv6')
        delete_ipv6.set('operation', 'delete')
        
    receive = ET.SubElement(ipv6, "receive", xmlns="urn:brocade.com:mgmt:brocade-ipv6-access-list")
    if kwargs.pop('delete_receive', False) is True:
        delete_receive = config.find('.//*receive')
        delete_receive.set('operation', 'delete')
        
    access_group = ET.SubElement(receive, "access-group")
    if kwargs.pop('delete_access_group', False) is True:
        delete_access_group = config.find('.//*access-group')
        delete_access_group.set('operation', 'delete')
        
    ipv6_access_list = ET.SubElement(access_group, "ipv6-access-list")
    if kwargs.pop('delete_ipv6_access_list', False) is True:
        delete_ipv6_access_list = config.find('.//*ipv6-access-list')
        delete_ipv6_access_list.set('operation', 'delete')
        
    ipv6_access_list.text = kwargs.pop('ipv6_access_list')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class rbridge_id_ipv6_receive_access_group_ipv6_access_list_act(Action):
    def run(self, delete_access_group, delete_rbridge_id, rbridge_id, delete_receive, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        rbridge_id_ipv6_receive_access_group_ipv6_access_list(delete_receive=delete_receive, delete_rbridge_id=delete_rbridge_id, rbridge_id=rbridge_id, delete_access_group=delete_access_group, host=host, username=username, password=password, callback=_callback, mgr=mgr)
        return 0
    