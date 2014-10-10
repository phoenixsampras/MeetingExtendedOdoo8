from openerp.osv import osv, fields

class crm_meeting(osv.Model):
    _inherit = 'calendar.event'
    _columns = {
        'location_id':fields.many2one('locations.locations','Location'),
        'company_id1':fields.many2one('res.partner','Company'),
        'product_ids':fields.one2many('products.lines','calender_id'),
        'event_id':fields.many2one('crm.event','Type of Event'),
        'place_id': fields.many2one('crm.place','Place'),
    }

class products_lines(osv.Model):
    _name = 'products.lines'
    _columns = {
        'calender_id': fields.many2one('calendar.event','Calender Event'),
        'responsibly_id':fields.many2one('res.users','Responsibly'),
        'product_id':fields.many2one('product.product', 'Product'),
        'quantity': fields.integer('Quantity'),
        'activity_id':fields.many2one('crm.activity','Activity'),
        'finish_date':fields.datetime('Finish Date Time'),
        'note':fields.text('Note'),
    }

class location_location(osv.Model): 
    _name = 'locations.locations'
    _rec_name ='name'
    _columns ={
        'name':fields.char('Location', required=True),
    }

class crm_event(osv.Model):
    _name='crm.event'
    _rec_name = 'name'
    _columns = {
        'name':fields.char('Type of Event',required=True),
    }

class crm_place(osv.Model):
    _name='crm.place'
    _rec_name = 'name'
    _columns = {
        'name':fields.char('Place',required=True),
    }

class crm_activity(osv.Model):
    _name='crm.activity'
    _rec_name = 'name'
    _columns = {
        'name':fields.char('Activity',required=True),
    }
