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


def rbridge_id_ip_community_list_extended_ip_community_reg_expr(**kwargs):
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
        
    community_list = ET.SubElement(ip, "community-list", xmlns="urn:brocade.com:mgmt:brocade-ip-policy")
    if kwargs.pop('delete_community_list', False) is True:
        delete_community_list = config.find('.//*community-list')
        delete_community_list.set('operation', 'delete')
        
    extended = ET.SubElement(community_list, "extended")
    if kwargs.pop('delete_extended', False) is True:
        delete_extended = config.find('.//*extended')
        delete_extended.set('operation', 'delete')
        
    name_key = ET.SubElement(extended, "name")
    name_key.text = kwargs.pop('name')
    if kwargs.pop('delete_name', False) is True:
        delete_name = config.find('.//*name')
        delete_name.set('operation', 'delete')
            
    seq_keyword_key = ET.SubElement(extended, "seq-keyword")
    seq_keyword_key.text = kwargs.pop('seq_keyword')
    if kwargs.pop('delete_seq_keyword', False) is True:
        delete_seq_keyword = config.find('.//*seq-keyword')
        delete_seq_keyword.set('operation', 'delete')
            
    instance_key = ET.SubElement(extended, "instance")
    instance_key.text = kwargs.pop('instance')
    if kwargs.pop('delete_instance', False) is True:
        delete_instance = config.find('.//*instance')
        delete_instance.set('operation', 'delete')
            
    ip_community_reg_expr = ET.SubElement(extended, "ip-community-reg-expr")
    if kwargs.pop('delete_ip_community_reg_expr', False) is True:
        delete_ip_community_reg_expr = config.find('.//*ip-community-reg-expr')
        delete_ip_community_reg_expr.set('operation', 'delete')
        
    ip_community_reg_expr.text = kwargs.pop('ip_community_reg_expr')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class rbridge_id_ip_community_list_extended_ip_community_reg_expr_act(Action):
    def run(self, ip_community_reg_expr, name, delete_ip, delete_community_list, instance, delete_instance, delete_name, delete_extended, delete_rbridge_id, delete_seq_keyword, delete_ip_community_reg_expr, seq_keyword, rbridge_id, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        rbridge_id_ip_community_list_extended_ip_community_reg_expr(delete_instance=delete_instance, delete_extended=delete_extended, name=name, delete_community_list=delete_community_list, delete_seq_keyword=delete_seq_keyword, username=username, seq_keyword=seq_keyword, rbridge_id=rbridge_id, delete_ip=delete_ip, password=password, host=host, delete_ip_community_reg_expr=delete_ip_community_reg_expr, ip_community_reg_expr=ip_community_reg_expr, delete_name=delete_name, delete_rbridge_id=delete_rbridge_id, instance=instance, callback=_callback, mgr=mgr)
        return 0
    