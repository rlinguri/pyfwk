#!/usr/bin/env python

"""
  currency.py: All currency values need to be stored and acted upon as integer.
"""

# ----------------------------CURRENCY-UTILITY----------------------------#
class Currency:
    @staticmethod
    def dollars_to_cents(dollars):
        if (dollars is not None):
            if (float(dollars) is not None):
                cents = float(dollars) * 100
                return int(cents)
            else:
                return None
        else:
            return None

    @staticmethod
    def cents_to_dollars(cents):
        if (cents is not None):
            if (isinstance(cents, int)):
                dollars = float(cents) / 100
                return dollars
            else:
                return None
        else:
            return None

# ---------------------------------EXPORT---------------------------------#
__all__ = ['Currency']


# ----------------------------------MAIN----------------------------------#
def main():
    pass


if __name__ == '__main__':
    main()
