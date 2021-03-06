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


def rbridge_id_secpolicy_defined_policy_policies_policy(**kwargs):
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
            
    secpolicy = ET.SubElement(rbridge_id, "secpolicy", xmlns="urn:brocade.com:mgmt:brocade-fc-auth")
    if kwargs.pop('delete_secpolicy', False) is True:
        delete_secpolicy = config.find('.//*secpolicy')
        delete_secpolicy.set('operation', 'delete')
        
    defined_policy = ET.SubElement(secpolicy, "defined-policy")
    if kwargs.pop('delete_defined_policy', False) is True:
        delete_defined_policy = config.find('.//*defined-policy')
        delete_defined_policy.set('operation', 'delete')
        
    policies = ET.SubElement(defined_policy, "policies")
    if kwargs.pop('delete_policies', False) is True:
        delete_policies = config.find('.//*policies')
        delete_policies.set('operation', 'delete')
        
    policy = ET.SubElement(policies, "policy")
    if kwargs.pop('delete_policy', False) is True:
        delete_policy = config.find('.//*policy')
        delete_policy.set('operation', 'delete')
        
    policy.text = kwargs.pop('policy')

    callback = kwargs.pop('callback', _callback)
    return callback(config, mgr=kwargs.pop('mgr'))

class rbridge_id_secpolicy_defined_policy_policies_policy_act(Action):
    def run(self, delete_defined_policy, delete_policies, delete_policy, policy, delete_secpolicy, delete_rbridge_id, rbridge_id, host, username, password):
        mgr = manager.connect(host=host,
                              port=22,
                              username=username,
                              password=password,
                              hostkey_verify=False)

        mgr.agtimeout = 600
        rbridge_id_secpolicy_defined_policy_policies_policy(delete_defined_policy=delete_defined_policy, delete_secpolicy=delete_secpolicy, username=username, rbridge_id=rbridge_id, delete_policies=delete_policies, delete_policy=delete_policy, policy=policy, host=host, delete_rbridge_id=delete_rbridge_id, password=password, callback=_callback, mgr=mgr)
        return 0
    