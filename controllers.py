# -*- coding: utf-8 -*-
from models import models
from openerp import http
import json


class IntefaceData(http.Controller):
    @http.route('/room_data/', type='http', auth='public', methods=['POST'])
    def index(self, **post):
        datas = {}
        if post:
            room_id = post['id']
            room = http.request.env['cmdb.base_type'].sudo().search([('id', '=', room_id)],limit=1)
            if room:
                datas['roomName'] = room.type_name
                datas['cabinet'] = []
                cabinets = http.request.env['cmdb.cabinet'].sudo().search([('lab.id', '=', room_id)])
                if cabinets:
                    for cabinet in cabinets:
                        datas['cabinet'].append({'id':cabinet.id, 'cab_num':cabinet.cab_num})
        return json.dumps(datas)


