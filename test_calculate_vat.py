import pytest

from vat_countries.countries import COUNTRIES_VAT_MAP


@pytest.mark.parametrize('product, cost, country, expected_vat', [
    ({'name': 'kingsmill', 'types': ['bread']}, 1.00, 'germany', 0.0),
    ({'name': 'kingsmill', 'types': ['bread']}, 1.25, 'germany', 0.05),
    ({'name': 'stilton', 'types': ['cheese']}, 1.25, 'germany', 0.1875),
    ({'name': 'bmw', 'types': ['car']}, 40000.00, 'germany', 6000),
    ({'name': 'merlot', 'types': ['wine']}, 120.00, 'germany', 24.0),
])
def test_calculate_vat_germany(product, cost, country, expected_vat):
    """Ensure we correctly create all the possible combinations of
    ordered words from a string.
    """
    country_vat = COUNTRIES_VAT_MAP[country](product, cost)
    test_vat = country_vat.calculate_country_vat()
    assert test_vat == expected_vat


@pytest.mark.parametrize('product, cost, country, expected_vat', [
    ({'name': 'merlot', 'types': ['wine']}, 120.00, 'uk', 12.0),
    ({'name': 'stilton', 'types': ['cheese']}, 20.00, 'uk', 2.5),
    ({'name': 'table', 'types': ['furniture']}, 65.00, 'uk', 9.25),
    ({'name': 'table', 'types': ['furniture']}, 135.00, 'uk', 21.5),
])
def test_calculate_vat_uk(product, cost, country, expected_vat):
    """Ensure we correctly create all the possible combinations of
    ordered words from a string.
    """
    country_vat = COUNTRIES_VAT_MAP[country](product, cost)
    test_vat = country_vat.calculate_country_vat()
    assert test_vat == expected_vat


@pytest.mark.parametrize('product, cost, country, expected_vat', [
    ({'name': 'Corrs', 'types': ['beer']}, 0.99, 'texas', 0.0),
    ({'name': 'Corrs', 'types': ['beer']}, 1.60, 'texas', 0.12000000000000002),
    ({'name': 'kingsmill', 'types': ['bread']}, 1.0, 'texas', 0.05),
    ({'name': 'table', 'types': ['furniture']}, 65.00, 'texas', 8.125),
    ({'name': 'table', 'types': ['furniture']}, 135.00, 'texas', 16.875),
])
def test_calculate_vat_texas(product, cost, country, expected_vat):
    """Ensure we correctly create all the possible combinations of
    ordered words from a string.
    """
    country_vat = COUNTRIES_VAT_MAP[country](product, cost)
    test_vat = country_vat.calculate_country_vat()
    assert test_vat == expected_vat


@pytest.mark.parametrize('product, cost, country, expected_vat', [
    ({'name': 'skimmed', 'types': ['milk']}, 2.50, 'colorado', 0.1),
    ({'name': 'skimmed', 'types': ['milk']}, 1.60, 'colorado', 0.08000000000000002),
    ({'name': 'kingsmill', 'types': ['bread']}, 1.0, 'colorado', 0.05),
    ({'name': 'table', 'types': ['furniture']}, 65.00, 'colorado', 7.15),
    ({'name': 'table', 'types': ['furniture']}, 135.00, 'colorado', 14.85),
])
def test_calculate_vat_colorado(product, cost, country, expected_vat):
    """Ensure we correctly create all the possible combinations of
    ordered words from a string.
    """
    country_vat = COUNTRIES_VAT_MAP[country](product, cost)
    test_vat = country_vat.calculate_country_vat()
    assert test_vat == expected_vat
