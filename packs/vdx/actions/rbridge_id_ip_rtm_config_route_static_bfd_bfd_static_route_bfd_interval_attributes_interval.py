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


def rbridge_id_ip_rtm_config_route_static_bfd_bfd_static_route_bfd_interval_attributes_interval(**kwargs):
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
            
    ip = ET.SubElement(rbridge_id, "ip")
    if kwargs.pop('delete_ip', False) is True:
        delete_ip = config.find('.//*ip')
        delete_ip.set('operation', 'delete')
        
    rtm_config = ET.SubElement(ip, "rtm-config", xmlns="urn:brocade.com:mgmt:brocade-rtm")
    if kwargs.pop('delete_rtm_config', False) is True:
        delete_rtm_config = config.find('.//*rtm-config')
        delete_rtm_config.set('operation', 'delete')
        
    route = ET.SubElement(rtm_config, "route")
    if kwargs.pop('delete_route', False) is True:
        delete_route = config.find('.//*route')
        delete_route.set('operation', 'delete')
        
    static = ET.SubElement(route, "static")
    if kwargs.pop('delete_static', False) is True:
        delete_static = config.find('.//*static')
        delete_static.set('operation', 'delete')
        
    bfd = ET.SubElement(static, "bfd")
    if kwargs.pop('delete_bfd', False) is True:
        delete_bfd = config.find('.//*bfd')
        delete_bfd.set('operation', 'delete')
        
    bfd_static_route = ET.SubElement(bfd, "bfd-static-route")
    if kwargs.pop('delete_bfd_static_route', False) is True:
        delete_bfd_static_route = config.find('.//*bfd-static-route')
        delete_bfd_static_route.set('operation', 'delete')
        
    bfd_static_route_dest_key = ET.SubElement(bfd_static_route, "bfd-static-route-dest")
    bfd_static_route_dest_key.text = kwargs.pop('bfd_static_route_dest')
    if kwargs.pop('delete_bfd_static_route_dest', False) is True:
        delete_bfd_static_route_dest = config.find('.//*bfd-static-route-dest')
        delete_bfd_static_route_dest.set('operation', 'delete')
            
    bfd_static_route_src_key = ET.SubElement(bfd_static_route, "bfd-static-route-src")
    bfd_static_route_src_key.text = kwargs.pop('bfd_static_route_src')
    if kwargs.pop('delete_bfd_static_route_src', False) is True:
        delete_bfd_static_route_src = config.find('.//*bfd-static-route-src')
        delete_bfd_static_route_src.set('operation', 'delete')
            
    bfd_interval_attributes = ET.SubElement(bfd_static_route, "bfd-interval-attributes")
    if kwargs.pop('delete_bfd_interval_attributes', False) is True:
        delete_bfd_interval_attributes = config.find('.//*bfd-interval-attributes')
        delete_bfd_interval_attributes.set('operation', 'delete')
        
    interval = ET.SubElement(bfd_interval_attributes, "interval")
    if kwargs.pop('delete_interval', False) is True:
        delete_interval = config.find('.//*interval')
        delete_interval.set('operation', 'delete')
        
    interval.text = kwargs.pop('interval')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class rbridge_id_ip_rtm_config_route_static_bfd_bfd_static_route_bfd_interval_attributes_interval_act(Action):
    def run(self, bfd_static_route_src, delete_bfd_interval_attributes, delete_bfd_static_route_src, delete_bfd_static_route, rbridge_id, delete_ip, delete_route, delete_bfd_static_route_dest, delete_static, interval, delete_interval, delete_rtm_config, delete_rbridge_id, delete_bfd, bfd_static_route_dest, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        rbridge_id_ip_rtm_config_route_static_bfd_bfd_static_route_bfd_interval_attributes_interval(delete_bfd_interval_attributes=delete_bfd_interval_attributes, delete_bfd_static_route_src=delete_bfd_static_route_src, delete_static=delete_static, delete_route=delete_route, username=username, delete_ip=delete_ip, rbridge_id=rbridge_id, bfd_static_route_src=bfd_static_route_src, interval=interval, delete_rtm_config=delete_rtm_config, delete_bfd_static_route_dest=delete_bfd_static_route_dest, host=host, password=password, delete_bfd_static_route=delete_bfd_static_route, delete_interval=delete_interval, delete_rbridge_id=delete_rbridge_id, delete_bfd=delete_bfd, bfd_static_route_dest=bfd_static_route_dest, callback=_callback, mgr=mgr)
        return 0
    