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


def rbridge_id_ipv6_router_ospf_redistribute_redistribute_static_redistribute_static_metric_type(**kwargs):
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
        
    router = ET.SubElement(ipv6, "router")
    if kwargs.pop('delete_router', False) is True:
        delete_router = config.find('.//*router')
        delete_router.set('operation', 'delete')
        
    ospf = ET.SubElement(router, "ospf", xmlns="urn:brocade.com:mgmt:brocade-ospfv3")
    if kwargs.pop('delete_ospf', False) is True:
        delete_ospf = config.find('.//*ospf')
        delete_ospf.set('operation', 'delete')
        
    vrf_key = ET.SubElement(ospf, "vrf")
    vrf_key.text = kwargs.pop('vrf')
    if kwargs.pop('delete_vrf', False) is True:
        delete_vrf = config.find('.//*vrf')
        delete_vrf.set('operation', 'delete')
            
    redistribute = ET.SubElement(ospf, "redistribute")
    if kwargs.pop('delete_redistribute', False) is True:
        delete_redistribute = config.find('.//*redistribute')
        delete_redistribute.set('operation', 'delete')
        
    redistribute_static = ET.SubElement(redistribute, "redistribute-static")
    if kwargs.pop('delete_redistribute_static', False) is True:
        delete_redistribute_static = config.find('.//*redistribute-static')
        delete_redistribute_static.set('operation', 'delete')
        
    redistribute_static_metric_type = ET.SubElement(redistribute_static, "redistribute-static-metric-type")
    if kwargs.pop('delete_redistribute_static_metric_type', False) is True:
        delete_redistribute_static_metric_type = config.find('.//*redistribute-static-metric-type')
        delete_redistribute_static_metric_type.set('operation', 'delete')
        
    redistribute_static_metric_type.text = kwargs.pop('redistribute_static_metric_type')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class rbridge_id_ipv6_router_ospf_redistribute_redistribute_static_redistribute_static_metric_type_act(Action):
    def run(self, delete_redistribute_static, rbridge_id, delete_ospf, delete_vrf, delete_redistribute, redistribute_static_metric_type, vrf, delete_rbridge_id, delete_router, delete_redistribute_static_metric_type, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        rbridge_id_ipv6_router_ospf_redistribute_redistribute_static_redistribute_static_metric_type(delete_redistribute_static=delete_redistribute_static, username=username, delete_redistribute=delete_redistribute, rbridge_id=rbridge_id, delete_vrf=delete_vrf, delete_redistribute_static_metric_type=delete_redistribute_static_metric_type, vrf=vrf, delete_router=delete_router, delete_ospf=delete_ospf, redistribute_static_metric_type=redistribute_static_metric_type, host=host, delete_rbridge_id=delete_rbridge_id, password=password, callback=_callback, mgr=mgr)
        return 0
    