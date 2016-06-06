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


def protocol_edge_loop_detection_shutdown_time(**kwargs):
    """Auto Generated Code
    """
    config = ET.Element("config")
    protocol = ET.SubElement(config, "protocol", xmlns="urn:brocade.com:mgmt:brocade-interface")
    if kwargs.pop('delete_protocol', False) is True:
        delete_protocol = config.find('.//*protocol')
        delete_protocol.set('operation', 'delete')
        
    edge_loop_detection = ET.SubElement(protocol, "edge-loop-detection", xmlns="urn:brocade.com:mgmt:brocade-eld")
    if kwargs.pop('delete_edge_loop_detection', False) is True:
        delete_edge_loop_detection = config.find('.//*edge-loop-detection')
        delete_edge_loop_detection.set('operation', 'delete')
        
    shutdown_time = ET.SubElement(edge_loop_detection, "shutdown-time")
    if kwargs.pop('delete_shutdown_time', False) is True:
        delete_shutdown_time = config.find('.//*shutdown-time')
        delete_shutdown_time.set('operation', 'delete')
        
    shutdown_time.text = kwargs.pop('shutdown_time')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class protocol_edge_loop_detection_shutdown_time_act(Action):
    def run(self, delete_shutdown_time, shutdown_time, delete_edge_loop_detection, delete_protocol, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        protocol_edge_loop_detection_shutdown_time(username=username, delete_edge_loop_detection=delete_edge_loop_detection, delete_protocol=delete_protocol, shutdown_time=shutdown_time, host=host, delete_shutdown_time=delete_shutdown_time, password=password, callback=_callback, mgr=mgr)
        return 0
    