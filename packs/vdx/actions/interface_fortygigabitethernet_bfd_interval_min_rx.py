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


def interface_fortygigabitethernet_bfd_interval_min_rx(**kwargs):
    """Auto Generated Code
    """
    config = ET.Element("config")
    interface = ET.SubElement(config, "interface", xmlns="urn:brocade.com:mgmt:brocade-interface")
    if kwargs.pop('delete_interface', False) is True:
        delete_interface = config.find('.//*interface')
        delete_interface.set('operation', 'delete')
        
    fortygigabitethernet = ET.SubElement(interface, "fortygigabitethernet")
    if kwargs.pop('delete_fortygigabitethernet', False) is True:
        delete_fortygigabitethernet = config.find('.//*fortygigabitethernet')
        delete_fortygigabitethernet.set('operation', 'delete')
        
    name_key = ET.SubElement(fortygigabitethernet, "name")
    name_key.text = kwargs.pop('name')
    if kwargs.pop('delete_name', False) is True:
        delete_name = config.find('.//*name')
        delete_name.set('operation', 'delete')
            
    bfd = ET.SubElement(fortygigabitethernet, "bfd")
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

class interface_fortygigabitethernet_bfd_interval_min_rx_act(Action):
    def run(self, name, delete_fortygigabitethernet, delete_interval, delete_interface, delete_name, delete_min_rx, delete_bfd, min_rx, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        interface_fortygigabitethernet_bfd_interval_min_rx(delete_interval=delete_interval, delete_min_rx=delete_min_rx, name=name, delete_name=delete_name, delete_bfd=delete_bfd, host=host, password=password, delete_fortygigabitethernet=delete_fortygigabitethernet, delete_interface=delete_interface, username=username, min_rx=min_rx, callback=_callback, mgr=mgr)
        return 0
    