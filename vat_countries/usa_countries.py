class USARegionVAT(object):
    """Class representing USA region VAT rules,
    allowing VAT to be calculated for the given product.
    """
    def __init__(self, product, cost):
        self.product = product
        self.cost = cost
        self.base_vat = 0.10

    def calculate_region_vat(self):
        if 'dairy' in self.product['types']:
            return self.calculate_dairy_vat()
        elif 'alcohol' in self.product['types']:
            return self.calculate_alcohol_vat()
        else:
            return self.cost * self.base_vat

    def calculate_dairy_vat(self, discount=0):
        cost = self.cost - discount
        return cost * 0.05

    def calculate_alcohol_vat(self, discount=0):
        cost = self.cost - discount
        vat = cost * self.base_vat
        vat += cost * 0.075
        return vat


class TexasVAT(USARegionVAT):
    """Class representing Texas VAT rules,
    allowing VAT to be calculated for the given product.
    """
    def __init__(self, product, cost):
        super(TexasVAT, self).__init__(product, cost)
        self.base_vat = 0.125
        self.custom_rules = {
            'bread': self.calculate_bread_vat,
            'beer': self.calculate_beer_vat
        }

    def calculate_country_vat(self):
        """Calculate the VAT for the given product, taking into
        account any special rules.
        """
        vat = 0
        special_cases = [ii for ii in self.product['types'] if ii in self.custom_rules]
        for product_type in special_cases:
            # Assume just one for now, but can be > 1?
            vat += self.custom_rules[product_type]()
            return vat

        vat += self.cost * self.base_vat
        return vat

    def calculate_bread_vat(self):
        return 0.05

    def calculate_beer_vat(self):
        vat = 0
        if self.cost > 1.00:
            vat = super(TexasVAT, self).calculate_alcohol_vat(discount=1)
        return vat


class ColoradoVAT(USARegionVAT):
    """Class representing Colorado VAT rules,
    allowing VAT to be calculated for the given product.
    """
    def __init__(self, product, cost):
        super(ColoradoVAT, self).__init__(product, cost)
        self.base_vat = 0.11
        self.custom_rules = {
            'bread': self.calculate_bread_vat,
            'milk': self.calculate_milk_vat
        }

    def calculate_country_vat(self):
        """Calculate the VAT for the given product, taking into
        account any special rules.
        """
        vat = 0
        special_cases = [ii for ii in self.product['types'] if ii in self.custom_rules]
        for product_type in special_cases:
            # Assume just one for now, but can be > 1?
            vat += self.custom_rules[product_type]()
            return vat

        vat += self.cost * self.base_vat
        return vat

    def calculate_bread_vat(self):
        return self.cost * 0.05

    def calculate_milk_vat(self):
        # Only first $2 taxable.
        taxable_amount = 2
        discount = self.cost - taxable_amount if self.cost > taxable_amount else 0
        return super(ColoradoVAT, self).calculate_dairy_vat(discount=discount)
