# -*- coding: utf-8 -*-
from datetime import datetime


class LedgerEntry(object):
    def __init__(self):
        self.date = None
        self.description = None
        self.change = None

    def __lt__(self, other):
        if self.date < other.date:
            return True
        elif self.description < other.description:
            return True
        else:
            return self.change < other.change


def create_entry(date, description, change):
    entry = LedgerEntry()
    entry.date = datetime.strptime(date, '%Y-%m-%d')
    entry.description = description
    entry.change = change
    return entry


def format_entries(currency, locale, entries):
    table = create_table(locale)

    for entry in sorted(entries):
        date_fmt = format_date(entry, locale)
        desc_fmt = format_description(entry)
        change_fmt = format_change(currency, entry, locale)
        table += '\n{} | {} | {}'.format(date_fmt, desc_fmt, change_fmt)
    return table

def format_change(currency, entry, locale):
    # Write entry change to table
    currency_symbol = {'USD': '$', 'EUR': u'€'}
    change_str, change_fmt = '{:>13}', ''
    if locale == 'en_US':
        left, right = ('', ' ') if entry.change >= 0 else ('(', ')')
        change_fmt = '{}{}{:0,.2f}{}'.format(left,
                                             currency_symbol[currency],
                                             abs(entry.change/100),
                                             right)
    elif locale == 'nl_NL':
        change_fmt = '{} {:0,.2f} '.format(currency_symbol[currency],
                                           entry.change/100)
        change_fmt = change_fmt.translate(str.maketrans(',.', '.,'))
    return change_str.format(change_fmt)


def format_description(entry):
    # Write entry description to table and Truncate if necessary
    if len(entry.description) > 25:
        return  entry.description[:22] + '...'
    else:
        return  '{:<25}'.format(entry.description)


def format_date(entry, lang):
    # Write entry date to table
    if lang == 'en_US':
        return f'{entry.date.month:02}/{entry.date.day:02}/{entry.date.year:04}'
    else:
        return f'{entry.date.day:02}-{entry.date.month:02}-{entry.date.year:04}'


def create_table(locale):
    # Generate Header Row
    lang_to_table = {'en_US': ['Date', 'Description', 'Change'],
                     'nl_NL': ['Datum', 'Omschrijving', 'Verandering']}
    pattern = '{:<11}| {:<26}| {:<13}'
    table = pattern.format(*lang_to_table[locale])
    return table