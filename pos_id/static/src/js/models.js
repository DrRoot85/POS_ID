odoo.define('pos_id.models', function (require) {
    "use strict";

    var models = require('point_of_sale.models');

    models.load_fields('res.partner', 'x_nat_no');




   models.load_models({
            model: '',
            fields: ['x_nat_no'],
            loaded: function (self, responsability_type) {
            self.responsability_type=responsability_type;

            },
        });



});
