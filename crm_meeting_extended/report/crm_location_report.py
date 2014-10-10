from openerp.report import report_sxw
from openerp.osv import osv
import datetime
import time
from openerp.tools import DEFAULT_SERVER_DATE_FORMAT, DEFAULT_SERVER_DATETIME_FORMAT


class crm_meeting_location_report(report_sxw.rml_parse):
    def __init__(self, cr, uid, name, context):
        super(crm_meeting_location_report, self).__init__(cr, uid, name, context=context)
        self.localcontext.update({
            'get_end_date': self.get_end_date,
            'get_end_time': self.get_end_time,
        })

    def get_end_date(self, obj_event):
        end_date = obj_event.finish_date
        dt = ''
        if end_date:
            dt = datetime.datetime.strptime(end_date, DEFAULT_SERVER_DATETIME_FORMAT).strftime('%d/%m/%Y')
        return dt

    def get_end_time(self, obj):
        end_time = obj.finish_date
        etime = ''
        if end_time:
            etime = datetime.datetime.strptime(end_time, DEFAULT_SERVER_DATETIME_FORMAT).strftime('%H:%M')
        return etime

class crm_meeting_report_test(osv.AbstractModel):
    _name = "report.crm_meeting_extended.crm_view_meeting_location_tmp"
    _inherit = "report.abstract_report"
    _template = "crm_meeting_extended.crm_view_meeting_location_tmp"
    _wrapped_report_class = crm_meeting_location_report

