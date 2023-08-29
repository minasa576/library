{
    'name': 'Library',
    'version': '0.1',
    'author': "Itqan Systems",
    'website': "http://www.itqansystems.com",
    'license': 'AGPL-3',
    # any module necessary for this one to work correctly
    'depends': [
        'base',
    ],

    # always loaded
    'data': [
        # Security files:
        'security/ir.model.access.csv',
        # Data files:
        'data/initial_author.xml',
        'data/initial_book.xml',

        # Root menu items files:

        # View files:

        'views/author_view.xml',
        'views/book_view.xml',

        # 'views/initial_records.xml',
        # Menu items files:


    ],
}

