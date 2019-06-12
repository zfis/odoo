import logging

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    def _default_ghu_doctoral_application_fee_product(self):
        return self.env.ref('ghu.ghu_doctoral_application_fee').id

    ghu_doctoral_application_fee_product = fields.Many2one(
        'product.product',
        string='Doctoral Application Fee Product',
        help='This is the initial application fee product for the automated invoice.',
        required=True,
        default=_default_ghu_doctoral_application_fee_product,
        config_parameter='ghu.doctoral_application_fee_product',
    )

    ghu_transferwise_api_key = fields.Char(
        string='Transferwise API Key',
        help='The Transferwise API key is needed to automatically handle incoming payments.',
        required=True,
        default='1234',
        config_parameter='ghu.transferwise_api_key',
    )

    ghu_documents_advisor_general = fields.Char(
        string=u'General Information for advisor folders',
        config_parameter='ghu.documents_advisor_general',
    )

    def _default_ghu_automated_invoice_bank_account(self):
        return self.env['res.partner.bank'].search([])[0]

    ghu_automated_invoice_bank_account = fields.Many2one(
        'res.partner.bank',
        string='Automated Invoice Partner Bank',
        required=True,
        default=_default_ghu_automated_invoice_bank_account,
        config_parameter='ghu.automated_invoice_bank_account'
    )

    @api.model
    def get_values(self):
        return super(ResConfigSettings, self).get_values()

    @api.multi
    def set_values(self):
        super(ResConfigSettings, self).set_values()
