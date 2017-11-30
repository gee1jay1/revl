class EURegionVAT(object):
    """Class representing EU region VAT rules,
    allowing VAT to be calculated for the given product.
    """
    def __init__(self, product, cost):
        self.product = product
        self.cost = cost
        self.base_vat = 0.125

    def calculate_region_vat(self):
        if 'bread' in self.product['types']:
            return self.calculate_bread_vat()
        else:
            return self.cost * self.base_vat

    def calculate_bread_vat(self):
        return 0.05


class GermanyVAT(EURegionVAT):
    """Class representing Germany VAT rules,
    allowing VAT to be calculated for the given product.
    """
    def __init__(self, product, cost):
        super(GermanyVAT, self).__init__(product, cost)
        self.base_vat = 0.15
        self.custom_rules = {
            'bread': self.calculate_bread_vat,
            'wine': self.calculate_wine_vat
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
        if self.cost > 1.00:
            return super(GermanyVAT, self).calculate_bread_vat()
        else:
            return 0

    def calculate_wine_vat(self):
        return self.cost * 0.2


class UKVAT(EURegionVAT):
    """Class representing Germany VAT rules,
    allowing VAT to be calculated for the given product.
    """
    def __init__(self, product, cost):
        super(UKVAT, self).__init__(product, cost)
        self.custom_rules = {
            'wine': self.calculate_wine_vat
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

        vat += self.calculate_vat_upto_20()
        if self.cost < 20.00:
            return vat

        vat += self.calculate_vat_upto_100()
        if self.cost < 100.00:
            return vat

        vat += self.calculate_vat_over_100()
        return vat

    def calculate_vat_upto_20(self):
        """Calculate vat on the first 20 Euros."""
        if self.cost < 20.00:
            vat = self.cost * self.base_vat
        else:
            vat = 20.00 * self.base_vat
        return vat

    def calculate_vat_upto_100(self):
        """Calculate VAT on between 20 and 100 Euros."""
        if self.cost < 100.00:
            vat = (self.cost - 20.00) * 0.15
        else:
            vat = 80.00 * 0.15
        return vat

    def calculate_vat_over_100(self):
        """Calculate VAT on anything over 100 Euros."""
        vat = (self.cost - 100.00) * 0.20
        return vat

    def calculate_wine_vat(self):
        return self.cost * 0.1
