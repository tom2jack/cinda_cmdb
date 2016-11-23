{
# The human-readable name of your module, displayed in the interface
        'name' : "cmdb" ,
# A more extensive description
        'description' : """
        """ ,
        
# Which modules must be installed for this one to work
        'depends' : ['base'],
        'category': 'cmdb',
# data files which are always installed
        'data': [
                'views/cmdb_view.xml',
                'views/cmdb_menu.xml',
                #"security/cmdb_security.xml",
                #"security/ir.model.access.csv",
                ],
# data files which are only installed in "demonstration mode"
        'demo': ['demo.xml',
        ],
        'application': True,
        'installable': True,

}
