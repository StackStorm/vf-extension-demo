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


def rbridge_id_route_map_content_match_protocol_protocol_static_container_static(**kwargs):
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
            
    route_map = ET.SubElement(rbridge_id, "route-map", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
    if kwargs.pop('delete_route_map', False) is True:
        delete_route_map = config.find('.//*route-map')
        delete_route_map.set('operation', 'delete')
        
    name_key = ET.SubElement(route_map, "name")
    name_key.text = kwargs.pop('name')
    if kwargs.pop('delete_name', False) is True:
        delete_name = config.find('.//*name')
        delete_name.set('operation', 'delete')
            
    action_rm_key = ET.SubElement(route_map, "action-rm")
    action_rm_key.text = kwargs.pop('action_rm')
    if kwargs.pop('delete_action_rm', False) is True:
        delete_action_rm = config.find('.//*action-rm')
        delete_action_rm.set('operation', 'delete')
            
    instance_key = ET.SubElement(route_map, "instance")
    instance_key.text = kwargs.pop('instance')
    if kwargs.pop('delete_instance', False) is True:
        delete_instance = config.find('.//*instance')
        delete_instance.set('operation', 'delete')
            
    content = ET.SubElement(route_map, "content")
    if kwargs.pop('delete_content', False) is True:
        delete_content = config.find('.//*content')
        delete_content.set('operation', 'delete')
        
    match = ET.SubElement(content, "match")
    if kwargs.pop('delete_match', False) is True:
        delete_match = config.find('.//*match')
        delete_match.set('operation', 'delete')
        
    protocol = ET.SubElement(match, "protocol")
    if kwargs.pop('delete_protocol', False) is True:
        delete_protocol = config.find('.//*protocol')
        delete_protocol.set('operation', 'delete')
        
    protocol_static_container = ET.SubElement(protocol, "protocol-static-container")
    if kwargs.pop('delete_protocol_static_container', False) is True:
        delete_protocol_static_container = config.find('.//*protocol-static-container')
        delete_protocol_static_container.set('operation', 'delete')
        
    static = ET.SubElement(protocol_static_container, "static")
    if kwargs.pop('delete_static', False) is True:
        delete_static = config.find('.//*static')
        delete_static.set('operation', 'delete')
        

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class rbridge_id_route_map_content_match_protocol_protocol_static_container_static_act(Action):
    def run(self, delete_protocol_static_container, delete_static, rbridge_id, delete_protocol, delete_match, delete_route_map, delete_content, instance, delete_instance, action_rm, delete_name, delete_rbridge_id, delete_action_rm, name, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        rbridge_id_route_map_content_match_protocol_protocol_static_container_static(delete_instance=delete_instance, name=name, delete_static=delete_static, delete_name=delete_name, delete_action_rm=delete_action_rm, username=username, rbridge_id=rbridge_id, delete_content=delete_content, password=password, delete_route_map=delete_route_map, delete_protocol_static_container=delete_protocol_static_container, delete_protocol=delete_protocol, host=host, delete_match=delete_match, action_rm=action_rm, delete_rbridge_id=delete_rbridge_id, instance=instance, callback=_callback, mgr=mgr)
        return 0
    