from openerp.report import report_sxw
from openerp.osv import osv
import datetime
import time
from openerp.tools import DEFAULT_SERVER_DATE_FORMAT, DEFAULT_SERVER_DATETIME_FORMAT

class crm_meeting_report(report_sxw.rml_parse):
    def __init__(self, cr, uid, name, context):
        super(crm_meeting_report, self).__init__(cr, uid, name, context=context)
        self.localcontext.update({
                'get_date': self.get_date,
                'get_initial_hour':self.get_initial_hour,
                'get_ending_hour':self.get_ending_hour,
        })

    def get_date(self, obj_event):
        start_date = obj_event.start_datetime
        dt = ''
        if obj_event.allday == False:
            dt = datetime.datetime.strptime(start_date, DEFAULT_SERVER_DATETIME_FORMAT).strftime('%d/%m/%Y')
        return dt

    def get_initial_hour(self, obj_event):
        initial_time = obj_event.start_datetime
        ini_time = ''
        if obj_event.allday == False:
            ini_time = datetime.datetime.strptime(initial_time, DEFAULT_SERVER_DATETIME_FORMAT).strftime('%H:%M')
        return ini_time

    def get_ending_hour(self, obj_event):
        ending_time = obj_event.stop_datetime
        end_time = ''
        if obj_event.allday == False:
            end_time = datetime.datetime.strptime(ending_time, DEFAULT_SERVER_DATETIME_FORMAT).strftime('%H:%M')
        return end_time


class crm_meeting_report_test(osv.AbstractModel):
    _name = "report.crm_meeting_extended.crm_view_meeting_tmp"
    _inherit = "report.abstract_report"
    _template = "crm_meeting_extended.crm_view_meeting_tmp"
    _wrapped_report_class = crm_meeting_report
