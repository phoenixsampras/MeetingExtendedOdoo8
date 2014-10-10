from openerp.report import report_sxw
from openerp.osv import osv
import time

class crm_meeting_instruction_report(report_sxw.rml_parse):
    def __init__(self, cr, uid, name, context):
        super(crm_meeting_instruction_report, self).__init__(cr, uid, name, context=context)
        self.localcontext.update({
            'time':time,
        })


class crm_meeting_report_test(osv.AbstractModel):
    _name = "report.crm_meeting_extended.crm_view_meeting_instruction_tmp"
    _inherit = "report.abstract_report"
    _template = "crm_meeting_extended.crm_view_meeting_instruction_tmp"
    _wrapped_report_class = crm_meeting_instruction_report
