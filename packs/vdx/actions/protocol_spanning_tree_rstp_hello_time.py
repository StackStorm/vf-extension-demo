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


def protocol_spanning_tree_rstp_hello_time(**kwargs):
    """Auto Generated Code
    """
    config = ET.Element("config")
    protocol = ET.SubElement(config, "protocol", xmlns="urn:brocade.com:mgmt:brocade-interface")
    if kwargs.pop('delete_protocol', False) is True:
        delete_protocol = config.find('.//*protocol')
        delete_protocol.set('operation', 'delete')
        
    spanning_tree = ET.SubElement(protocol, "spanning-tree", xmlns="urn:brocade.com:mgmt:brocade-xstp")
    if kwargs.pop('delete_spanning_tree', False) is True:
        delete_spanning_tree = config.find('.//*spanning-tree')
        delete_spanning_tree.set('operation', 'delete')
        
    rstp = ET.SubElement(spanning_tree, "rstp")
    if kwargs.pop('delete_rstp', False) is True:
        delete_rstp = config.find('.//*rstp')
        delete_rstp.set('operation', 'delete')
        
    hello_time = ET.SubElement(rstp, "hello-time")
    if kwargs.pop('delete_hello_time', False) is True:
        delete_hello_time = config.find('.//*hello-time')
        delete_hello_time.set('operation', 'delete')
        
    hello_time.text = kwargs.pop('hello_time')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class protocol_spanning_tree_rstp_hello_time_act(Action):
    def run(self, delete_hello_time, hello_time, delete_spanning_tree, delete_rstp, delete_protocol, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        protocol_spanning_tree_rstp_hello_time(delete_rstp=delete_rstp, hello_time=hello_time, delete_spanning_tree=delete_spanning_tree, delete_hello_time=delete_hello_time, delete_protocol=delete_protocol, host=host, username=username, password=password, callback=_callback, mgr=mgr)
        return 0
    