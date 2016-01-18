import random, datetime

class TooManyMelonsError(ValueError):
    """Error when too many melons are ordered"""

    def __init__(self):
        """initialize TooManyMelonsError using init method
        from ValueError"""

        super(TooManyMelonsError, self).__init__("No more than 100 melons!")

class AbstractMelonOrder(object):
    """An abstract base class that other Melon Orders inherit from"""

    def __init__(self, species, qty, order_type, tax):
        """Initialize melon order and set species, quantity, and shipped"""

        self.species = species
        self.qty = qty
        self.order_type = order_type
        self.tax = tax
        self.shipped = False

        # qty is the argument passed in; self.qty means the instance
        # melon is set by the qty argument

        if qty > 100:
            raise TooManyMelonsError

    def get_base_price(self):
        """set base price using splurge pricing and rush hour fee"""

        now = datetime.datetime.now()

        base_price = random.randint(5, 9)

        # add surcharge to melons ordered during morning rush hour
        # Mon - Fri, 8 - 11 am

        if (now.weekday() < 5 and now.hour in range(8, 11)):
            base_price += 4

        return base_price


    def get_total(self):
        """Calculate total price, including tax."""

        base_price = self.get_base_price()

        if self.species == "Christmas melon":
            base_price *= 1.5

        total = (1 + self.tax) * self.qty * base_price

        if self.order_type == "international" and self.qty < 10:
            total += 3

        return total

    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True



class DomesticMelonOrder(AbstractMelonOrder):
    """Class for melon orders within USA"""

    def __init__(self, species, qty):
        super(DomesticMelonOrder, self).__init__(species,
                                                 qty,
                                                 "domestic",
                                                 0.08)


class GovernmentMelonOrder(AbstractMelonOrder):
    """Class for US government melon orders"""

    def __init__(self, species, qty):
        super(GovernmentMelonOrder, self).__init__(species,
                                                   qty,
                                                   "domestic",
                                                   0)
        self.passed_inspection = False

    def inspect_melon(self, passed):
        """Set value of attribute passed_inspection"""
        
        self.passed_inspection = passed


class InternationalMelonOrder(AbstractMelonOrder):
    """Class for international (non-US) melon orders"""

    # inherit parent __init__ method and add "country_code" parameter
    def __init__(self, species, qty, country_code):
        super(InternationalMelonOrder, self).__init__(species,
                                                      qty,
                                                      "international",
                                                      0.17)
        self.country_code = country_code

    def get_country_code(self):
        """Return the country code."""

        return self.country_code





