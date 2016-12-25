# -*- coding: utf-8 -*-
from models import models
from openerp import http
import json


class IntefaceData(http.Controller):
    @http.route('/cabinet_data/', type='http', auth='public', methods=['POST'])
    def cabinet_data(self, **post):
        datas = {}
        if post:
            room_id = post['id']
            room = http.request.env['cmdb.base_type'].sudo().search([('id', '=', room_id)], limit=1)
            if room:
                datas['roomName'] = room.type_name
                datas['cabinet'] = []
                cabinets = http.request.env['cmdb.cabinet'].sudo().search([('lab.id', '=', room_id)])
                if cabinets:
                    for cabinet in cabinets:
                        datas['cabinet'].append({'id': cabinet.id, 'cab_num': cabinet.cab_num})
        return json.dumps(datas)

    @http.route('/u_data/', type='http', auth='public', methods=['POST'])
    def u_data(self, **post):
        datas = {}
        if post:
            cabinet_id = post['id']
            cabinet = http.request.env['cmdb.cabinet'].sudo().search([('id', '=', cabinet_id)], limit=1)
            if cabinet:
                datas['name'] = cabinet.cab_num
                datas['device'] = []
                devices = http.request.env['cmdb.device'].sudo().search([('cab.id', '=', cabinet_id)])
                if devices:
                    for device in devices:
                        datas['device'].append({'u_pos': device.u_pos.type_name, 'u_space': device.u_space, 'host_name': device.host_name})
        return json.dumps(datas)


