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


def rbridge_id_vrf_route_target_target_community(**kwargs):
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
            
    route_target = ET.SubElement(vrf, "route-target")
    if kwargs.pop('delete_route_target', False) is True:
        delete_route_target = config.find('.//*route-target')
        delete_route_target.set('operation', 'delete')
        
    action_key = ET.SubElement(route_target, "action")
    action_key.text = kwargs.pop('action')
    if kwargs.pop('delete_action', False) is True:
        delete_action = config.find('.//*action')
        delete_action.set('operation', 'delete')
            
    target_community = ET.SubElement(route_target, "target-community")
    if kwargs.pop('delete_target_community', False) is True:
        delete_target_community = config.find('.//*target-community')
        delete_target_community.set('operation', 'delete')
        
    target_community.text = kwargs.pop('target_community')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class rbridge_id_vrf_route_target_target_community_act(Action):
    def run(self, rbridge_id, delete_vrf, target_community, delete_target_community, vrf_name, delete_action, action, delete_rbridge_id, delete_route_target, delete_vrf_name, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        rbridge_id_vrf_route_target_target_community(delete_target_community=delete_target_community, delete_route_target=delete_route_target, username=username, action=action, delete_vrf=delete_vrf, rbridge_id=rbridge_id, vrf_name=vrf_name, delete_action=delete_action, host=host, target_community=target_community, delete_rbridge_id=delete_rbridge_id, password=password, delete_vrf_name=delete_vrf_name, callback=_callback, mgr=mgr)
        return 0
    