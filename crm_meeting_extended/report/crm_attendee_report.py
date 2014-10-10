from openerp.report import report_sxw
from openerp.osv import osv
import datetime
import time
from openerp.tools import DEFAULT_SERVER_DATE_FORMAT, DEFAULT_SERVER_DATETIME_FORMAT

class crm_attendee_report(report_sxw.rml_parse):
    
    def __init__(self, cr, uid, name, context):
        super(crm_attendee_report, self).__init__(cr, uid, name, context=context)
        self.counter = 0
        self.localcontext.update({
                'get_serial_number': self.get_serial_number,
                'get_arrival_time':self.get_arrival_time,
                'get_exiting_time':self.get_exiting_time,
        })
        

    def get_serial_number(self):
        self.counter += 1
        return self.counter

    def get_arrival_time(self,obj_event):
        arri_time = obj_event.start_datetime
        arrival_time = ''
        if obj_event.allday == False:
            arrival_time = datetime.datetime.strptime(arri_time, DEFAULT_SERVER_DATETIME_FORMAT).strftime('%H:%M:%S')
        return arrival_time

    def get_exiting_time(self,obj_event):
        exit_time = obj_event.stop_datetime
        exiting_time = ''
        if obj_event.allday == False:
            exiting_time = datetime.datetime.strptime(exit_time, DEFAULT_SERVER_DATETIME_FORMAT).strftime('%H:%M:%S')
        return exiting_time

class crm_meeting_report_test(osv.AbstractModel):
    _name = "report.crm_meeting_extended.crm_attendee_list_tmp"
    _inherit = "report.abstract_report"
    _template = "crm_meeting_extended.crm_attendee_list_tmp"
    _wrapped_report_class = crm_attendee_report
