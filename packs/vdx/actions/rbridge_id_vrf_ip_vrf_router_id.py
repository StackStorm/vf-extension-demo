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


def rbridge_id_vrf_ip_vrf_router_id(**kwargs):
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
            
    vrf = ET.SubElement(rbridge_id, "vrf", xmlns="urn:brocade.com:mgmt:brocade-vrf")
    if kwargs.pop('delete_vrf', False) is True:
        delete_vrf = config.find('.//*vrf')
        delete_vrf.set('operation', 'delete')
        
    vrf_name_key = ET.SubElement(vrf, "vrf-name")
    vrf_name_key.text = kwargs.pop('vrf_name')
    if kwargs.pop('delete_vrf_name', False) is True:
        delete_vrf_name = config.find('.//*vrf-name')
        delete_vrf_name.set('operation', 'delete')
            
    ip = ET.SubElement(vrf, "ip")
    if kwargs.pop('delete_ip', False) is True:
        delete_ip = config.find('.//*ip')
        delete_ip.set('operation', 'delete')
        
    vrf_router_id = ET.SubElement(ip, "vrf-router-id")
    if kwargs.pop('delete_vrf_router_id', False) is True:
        delete_vrf_router_id = config.find('.//*vrf-router-id')
        delete_vrf_router_id.set('operation', 'delete')
        
    vrf_router_id.text = kwargs.pop('vrf_router_id')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class rbridge_id_vrf_ip_vrf_router_id_act(Action):
    def run(self, rbridge_id, delete_ip, delete_vrf, vrf_name, delete_rbridge_id, vrf_router_id, delete_vrf_router_id, delete_vrf_name, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        rbridge_id_vrf_ip_vrf_router_id(vrf_name=vrf_name, username=username, delete_rbridge_id=delete_rbridge_id, rbridge_id=rbridge_id, delete_vrf=delete_vrf, delete_vrf_router_id=delete_vrf_router_id, delete_vrf_name=delete_vrf_name, host=host, delete_ip=delete_ip, vrf_router_id=vrf_router_id, password=password, callback=_callback, mgr=mgr)
        return 0
    