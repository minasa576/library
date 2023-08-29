from odoo import fields, models, api
from odoo.exceptions import ValidationError


class LibraryBook(models.Model):
    _name = "library.book"

    name = fields.Char(required=True, string="Book Name")
    author_id = fields.Many2one(comodel_name='library.author', required=True, string="Author")
    publishing_date = fields.Date()
    return_date = fields.Date()
    is_borrowed = fields.Boolean(string="Is Borrowed", default=False)

    def action_borrowed_button(self):
        self.write({'is_borrowed': True})

    @api.constrains('is_borrowed', 'return_date')
    def prevent_setting_return_date(self):
        for book in self:
            if book.return_date and not book.is_borrowed:
                raise ValidationError("This book is not borrowed!")
