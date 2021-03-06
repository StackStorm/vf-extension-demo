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


def rbridge_id_http_server_http_vrf_cont_use_vrf_http_vrf_shutdown(**kwargs):
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
            
    http = ET.SubElement(rbridge_id, "http", xmlns="urn:brocade.com:mgmt:brocade-http")
    if kwargs.pop('delete_http', False) is True:
        delete_http = config.find('.//*http')
        delete_http.set('operation', 'delete')
        
    server = ET.SubElement(http, "server")
    if kwargs.pop('delete_server', False) is True:
        delete_server = config.find('.//*server')
        delete_server.set('operation', 'delete')
        
    http_vrf_cont = ET.SubElement(server, "http-vrf-cont")
    if kwargs.pop('delete_http_vrf_cont', False) is True:
        delete_http_vrf_cont = config.find('.//*http-vrf-cont')
        delete_http_vrf_cont.set('operation', 'delete')
        
    use_vrf = ET.SubElement(http_vrf_cont, "use-vrf")
    if kwargs.pop('delete_use_vrf', False) is True:
        delete_use_vrf = config.find('.//*use-vrf')
        delete_use_vrf.set('operation', 'delete')
        
    use_vrf_name_key = ET.SubElement(use_vrf, "use-vrf-name")
    use_vrf_name_key.text = kwargs.pop('use_vrf_name')
    if kwargs.pop('delete_use_vrf_name', False) is True:
        delete_use_vrf_name = config.find('.//*use-vrf-name')
        delete_use_vrf_name.set('operation', 'delete')
            
    http_vrf_shutdown = ET.SubElement(use_vrf, "http-vrf-shutdown")
    if kwargs.pop('delete_http_vrf_shutdown', False) is True:
        delete_http_vrf_shutdown = config.find('.//*http-vrf-shutdown')
        delete_http_vrf_shutdown.set('operation', 'delete')
        

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class rbridge_id_http_server_http_vrf_cont_use_vrf_http_vrf_shutdown_act(Action):
    def run(self, delete_use_vrf, use_vrf_name, rbridge_id, delete_http_vrf_cont, delete_use_vrf_name, delete_server, delete_rbridge_id, delete_http_vrf_shutdown, delete_http, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        rbridge_id_http_server_http_vrf_cont_use_vrf_http_vrf_shutdown(delete_http_vrf_shutdown=delete_http_vrf_shutdown, delete_server=delete_server, delete_use_vrf=delete_use_vrf, username=username, delete_http=delete_http, delete_rbridge_id=delete_rbridge_id, rbridge_id=rbridge_id, delete_use_vrf_name=delete_use_vrf_name, host=host, use_vrf_name=use_vrf_name, delete_http_vrf_cont=delete_http_vrf_cont, password=password, callback=_callback, mgr=mgr)
        return 0
    