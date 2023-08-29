from odoo import fields, models, api


class LibraryAuthor(models.Model):
    _name = "library.author"

    name = fields.Char(required=True, string="Author Name")
    book_ids = fields.One2many('library.book', 'author_id', string="Books")
    date_of_birth = fields.Date()
    nationality = fields.Many2one('res.country', string="Nationality")
