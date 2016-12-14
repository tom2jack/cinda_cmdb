{
# The human-readable name of your module, displayed in the interface
        'name' : "cmdb" ,
# A more extensive description
        'description' : """
        """ ,
        'author': "Nantian",
        'website': "http://nantian.com.cn",
        
# Which modules must be installed for this one to work
        'depends' : ['base'],
        'category': 'cmdb',
# data files which are always installed
        'data': [
                'views/cmdb_view.xml',
                'views/cmdb_menu.xml',
                'views/cmdb_link.xml',
                #"security/cmdb_security.xml",
                #"security/ir.model.access.csv",
                ],
# data files which are only installed in "demonstration mode"
        'demo': ['demo.xml',
        ],
        'application': True,
        'installable': True,
        'qweb':[
            'static/src/xml/cmdb.xml',
        ],
}
