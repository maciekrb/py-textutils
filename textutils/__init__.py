# -*- coding: utf-8 -*-
import re
import uuid
import string
import random

__all__ = [
  'sanitize',
  'randomToken',
  'randomString'
]

UNICODE_MAP = {
    192: u"A",  # À
    193: u"A",  # Á
    194: u"A",  # Â
    195: u"A",  # Ã
    196: u"A",  # Ä
    197: u"A",  # Å
    199: u"C",  # à
    200: u"E",  # á
    201: u"E",  # â
    202: u"E",  # ã
    203: u"E",  # ä
    204: u"I",  # å
    205: u"I",  # Ò
    206: u"I",  # Ó
    207: u"I",  # Ô
    209: u"N",  # Õ
    210: u"O",  # Ö
    211: u"O",  # Ø
    212: u"O",  # ò
    213: u"O",  # ó
    214: u"O",  # ô
    216: u"O",  # õ
    217: u"U",  # ö
    218: u"U",  # ø
    219: u"U",  # È
    220: u"U",  # É
    224: u"a",  # Ê
    225: u"a",  # Ë
    226: u"a",  # è
    227: u"a",  # é
    228: u"a",  # ê
    229: u"a",  # ë
    231: u"c",  # Ç
    232: u"e",  # ç
    233: u"e",  # Ì
    234: u"e",  # Í
    235: u"e",  # Î
    236: u"i",  # Ï
    237: u"i",  # ì
    238: u"i",  # í
    239: u"i",  # î
    241: u"n",  # ï
    242: u"o",  # Ù
    243: u"o",  # Ú
    244: u"o",  # Û
    245: u"o",  # Ü
    246: u"o",  # ù
    248: u"o",  # ú
    249: u"u",  # û
    250: u"u",  # ü
    251: u"u",  # ÿ
    252: u"u",  # Ñ
    255: u"Y",  # ñ
}

LONEXP = u'[^a-zA-Z0-9 ÀÁÂÃÄÅàáâãäåÒÓÔÕÖØòóôõöøÈÉÊËèéêëÇçÌÍÎÏìíîïÙÚÛÜùúûüÿÑñ_-]+'
LETTER_OR_NUMBER = re.compile(LONEXP, re.UNICODE)
SEPARATORS = (u' ', u'-', u'_')
SPACES = re.compile(u'\s+')


def sanitize(subject, allow_spaces=True, space_replacement=u'-',
             remap_unicode=False):
  """
  Sanitizes a string removing all non word characters.

  Args:
    - string: unicode string to transform
    - allow_spaces: wheter remove or keep spaces
    - space_replacement: if allow_spaces is set to False, the will be replaced
      by this
    - remap_unicode: wheter transliteration should be executed
      (change áéí..aei)
  Returns
    - Sanitized string

  @TODO
    - convert string to unicode
    - accept underscores and dashes between words
  """
  subject = unicode(subject)
  subject = subject.expandtabs()

  subject = LETTER_OR_NUMBER.sub(u'', subject)
  for sep in SEPARATORS:
    subject = re.sub(u'{0}{{2,}}'.format(sep), sep, subject)

  if remap_unicode is True:
    subject = subject.translate(UNICODE_MAP)

  if allow_spaces is False:
    subject = re.sub(SPACES, space_replacement, subject)

  return subject


def randomToken():
  return str(uuid.uuid4()).replace('-', '_')


def randomString(size=32, chars="uppercase,lowercase,digits"):
  """
  Creates a random string of specified size and type

  Args:
    size: (int) Desired length of generated string
    chars : (str) Desired types to use separated by "," : (uppercase, lowercase, digits)

  Returns:
    Random generated string
  """
  opt = chars.split(",")
  use_chars = ""
  if 'uppercase' in opt:
    use_chars = use_chars + string.ascii_uppercase
  if 'lowercase' in opt:
    use_chars = use_chars + string.ascii_lowercase
  if 'digits' in opt:
    use_chars = use_chars + string.digits

  return ''.join(random.choice(use_chars) for x in range(size))

def sanitize_html(html):
  """ Removes HTML from the given content
  Args:
    - html: text containing HTML markup

  Returns
    str without HTML tags
  """

  import BeautifulSoup

  soup = BeautifulSoup(html)
  return soup.get_text(' ').replace('\n', ' ').replace('\t', '')

