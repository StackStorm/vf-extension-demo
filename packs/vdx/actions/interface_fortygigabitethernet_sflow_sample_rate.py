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


def interface_fortygigabitethernet_sflow_sample_rate(**kwargs):
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
            
    sflow = ET.SubElement(fortygigabitethernet, "sflow", xmlns="urn:brocade.com:mgmt:brocade-sflow")
    if kwargs.pop('delete_sflow', False) is True:
        delete_sflow = config.find('.//*sflow')
        delete_sflow.set('operation', 'delete')
        
    sample_rate = ET.SubElement(sflow, "sample-rate")
    if kwargs.pop('delete_sample_rate', False) is True:
        delete_sample_rate = config.find('.//*sample-rate')
        delete_sample_rate.set('operation', 'delete')
        
    sample_rate.text = kwargs.pop('sample_rate')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class interface_fortygigabitethernet_sflow_sample_rate_act(Action):
    def run(self, delete_sflow, name, delete_sample_rate, delete_fortygigabitethernet, sample_rate, delete_interface, delete_name, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        interface_fortygigabitethernet_sflow_sample_rate(name=name, delete_fortygigabitethernet=delete_fortygigabitethernet, delete_sflow=delete_sflow, sample_rate=sample_rate, host=host, delete_name=delete_name, delete_sample_rate=delete_sample_rate, username=username, delete_interface=delete_interface, password=password, callback=_callback, mgr=mgr)
        return 0
    