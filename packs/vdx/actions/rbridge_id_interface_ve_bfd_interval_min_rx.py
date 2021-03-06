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


def rbridge_id_interface_ve_bfd_interval_min_rx(**kwargs):
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
            
    interface = ET.SubElement(rbridge_id, "interface", xmlns="urn:brocade.com:mgmt:brocade-interface")
    if kwargs.pop('delete_interface', False) is True:
        delete_interface = config.find('.//*interface')
        delete_interface.set('operation', 'delete')
        
    ve = ET.SubElement(interface, "ve")
    if kwargs.pop('delete_ve', False) is True:
        delete_ve = config.find('.//*ve')
        delete_ve.set('operation', 'delete')
        
    name_key = ET.SubElement(ve, "name")
    name_key.text = kwargs.pop('name')
    if kwargs.pop('delete_name', False) is True:
        delete_name = config.find('.//*name')
        delete_name.set('operation', 'delete')
            
    bfd = ET.SubElement(ve, "bfd")
    if kwargs.pop('delete_bfd', False) is True:
        delete_bfd = config.find('.//*bfd')
        delete_bfd.set('operation', 'delete')
        
    interval = ET.SubElement(bfd, "interval")
    if kwargs.pop('delete_interval', False) is True:
        delete_interval = config.find('.//*interval')
        delete_interval.set('operation', 'delete')
        
    min_rx = ET.SubElement(interval, "min-rx")
    if kwargs.pop('delete_min_rx', False) is True:
        delete_min_rx = config.find('.//*min-rx')
        delete_min_rx.set('operation', 'delete')
        
    min_rx.text = kwargs.pop('min_rx')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class rbridge_id_interface_ve_bfd_interval_min_rx_act(Action):
    def run(self, name, delete_interval, delete_ve, delete_interface, delete_name, delete_min_rx, delete_rbridge_id, min_rx, delete_bfd, rbridge_id, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        rbridge_id_interface_ve_bfd_interval_min_rx(delete_interval=delete_interval, delete_min_rx=delete_min_rx, name=name, delete_name=delete_name, username=username, rbridge_id=rbridge_id, delete_bfd=delete_bfd, delete_ve=delete_ve, password=password, host=host, delete_interface=delete_interface, delete_rbridge_id=delete_rbridge_id, min_rx=min_rx, callback=_callback, mgr=mgr)
        return 0
    