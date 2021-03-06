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


def rbridge_id_interface_ve_ip_interface_ve_dhcp_conf_dhcp_relay_servers_server_vrf_name(**kwargs):
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
            
    ip = ET.SubElement(ve, "ip", xmlns="urn:brocade.com:mgmt:brocade-ip-config")
    if kwargs.pop('delete_ip', False) is True:
        delete_ip = config.find('.//*ip')
        delete_ip.set('operation', 'delete')
        
    interface_ve_dhcp_conf = ET.SubElement(ip, "interface-ve-dhcp-conf", xmlns="urn:brocade.com:mgmt:brocade-dhcp")
    if kwargs.pop('delete_interface_ve_dhcp_conf', False) is True:
        delete_interface_ve_dhcp_conf = config.find('.//*interface-ve-dhcp-conf')
        delete_interface_ve_dhcp_conf.set('operation', 'delete')
        
    dhcp = ET.SubElement(interface_ve_dhcp_conf, "dhcp")
    if kwargs.pop('delete_dhcp', False) is True:
        delete_dhcp = config.find('.//*dhcp')
        delete_dhcp.set('operation', 'delete')
        
    relay = ET.SubElement(dhcp, "relay")
    if kwargs.pop('delete_relay', False) is True:
        delete_relay = config.find('.//*relay')
        delete_relay.set('operation', 'delete')
        
    servers = ET.SubElement(relay, "servers")
    if kwargs.pop('delete_servers', False) is True:
        delete_servers = config.find('.//*servers')
        delete_servers.set('operation', 'delete')
        
    relay_ip_addr_key = ET.SubElement(servers, "relay-ip-addr")
    relay_ip_addr_key.text = kwargs.pop('relay_ip_addr')
    if kwargs.pop('delete_relay_ip_addr', False) is True:
        delete_relay_ip_addr = config.find('.//*relay-ip-addr')
        delete_relay_ip_addr.set('operation', 'delete')
            
    server_vrf_name = ET.SubElement(servers, "server-vrf-name")
    if kwargs.pop('delete_server_vrf_name', False) is True:
        delete_server_vrf_name = config.find('.//*server-vrf-name')
        delete_server_vrf_name.set('operation', 'delete')
        
    server_vrf_name.text = kwargs.pop('server_vrf_name')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class rbridge_id_interface_ve_ip_interface_ve_dhcp_conf_dhcp_relay_servers_server_vrf_name_act(Action):
    def run(self, relay_ip_addr, name, delete_ip, delete_interface_ve_dhcp_conf, delete_dhcp, delete_server_vrf_name, delete_servers, delete_ve, delete_relay, delete_interface, delete_name, delete_rbridge_id, server_vrf_name, delete_relay_ip_addr, rbridge_id, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        rbridge_id_interface_ve_ip_interface_ve_dhcp_conf_dhcp_relay_servers_server_vrf_name(relay_ip_addr=relay_ip_addr, name=name, delete_name=delete_name, delete_relay=delete_relay, username=username, delete_dhcp=delete_dhcp, rbridge_id=rbridge_id, delete_ip=delete_ip, delete_interface_ve_dhcp_conf=delete_interface_ve_dhcp_conf, delete_ve=delete_ve, host=host, delete_relay_ip_addr=delete_relay_ip_addr, server_vrf_name=server_vrf_name, delete_server_vrf_name=delete_server_vrf_name, delete_rbridge_id=delete_rbridge_id, delete_servers=delete_servers, delete_interface=delete_interface, password=password, callback=_callback, mgr=mgr)
        return 0
    