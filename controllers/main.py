# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import http, _
from odoo.http import request
from odoo.tools import float_round
import datetime
from odoo.addons.hr_attendance.controllers.main import HrAttendance as HrAttendanceOdoo
class HrAttendance(HrAttendanceOdoo):
    @http.route('/hr_attendance/manual_selection', type="json", auth="public")
    def manual_selection(self, token, employee_id, pin_code):        
        company = self._get_company(token)        
        if company:
            #raise Exception(123)
            employee = request.env['hr.employee'].sudo().browse(employee_id)
            if employee.company_id == company and ((not company.attendance_kiosk_use_pin) or (employee.pin == pin_code)):
                employee.with_company(company.id).sudo()._attendance_action_change(self._get_geoip_response('kiosk'))
                return self._get_employee_info_response(employee)
        return {}