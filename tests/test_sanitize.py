#-*- coding: utf-8 -*-

import unittest
from textutils import sanitize


class TestSanitize(unittest.TestCase):

  def test_sanitize_replaces_spaces(self):
    subject = u'test a e i o u á é í ó ú'
    result = sanitize(subject, allow_spaces=False, space_replacement='_')
    self.assertEqual(u'test_a_e_i_o_u_á_é_í_ó_ú', result)

  def test_sanitize_replaces_double_spaces(self):
    subject = u'test a  e    i      o       u        á      é    í ó ú'
    result = sanitize(subject, allow_spaces=False, space_replacement='_')
    self.assertEqual(u'test_a_e_i_o_u_á_é_í_ó_ú', result)

  def test_sanitize_normalizes_double_spaces(self):
    subject = u'test a  e    i      o       u        á      é    í ó ú'
    result = sanitize(subject, allow_spaces=True)
    self.assertEqual(u'test a e i o u á é í ó ú', result)

  def test_sanitize_replaces_double_dashes(self):
    subject = u'test-a--e----i------o-------u--------á------é----í-ó-ú'
    result = sanitize(subject, allow_spaces=False, space_replacement='_')
    self.assertEqual(u'test-a-e-i-o-u-á-é-í-ó-ú', result)

  def test_sanitize_replaces_double_dashes_in_ascii(self):
    subject = 'test-a--e----i------o-------u--------a------e----i-o-u'
    result = sanitize(subject, allow_spaces=False, space_replacement='_')
    self.assertEqual('test-a-e-i-o-u-a-e-i-o-u', result)

  def test_sanitize_replaces_double_underscores(self):
    subject = u'test_a__e____i______o_______u________á______é____í_ó_ú'
    result = sanitize(subject, allow_spaces=False, space_replacement=u'_')
    self.assertEqual(u'test_a_e_i_o_u_á_é_í_ó_ú', result)

  def test_sanitize_remaps_unicode(self):
    subject = u'test a e i o u á é í ó ú'
    result = sanitize(subject, remap_unicode=True)
    self.assertEqual(u'test a e i o u a e i o u', result)

  def test_sanitize_removes_spaces(self):
    subject = u'test a e i o u á é í ó ú'
    result = sanitize(subject, allow_spaces=False, space_replacement='')
    self.assertEqual(u'testaeiouáéíóú', result)

  def test_sanitize_removes_spaces_and_remaps_unicode(self):
    subject = u'test a e i o u á é í ó ú'
    result = sanitize(subject, allow_spaces=False, space_replacement='',
                      remap_unicode=True)
    self.assertEqual(u'testaeiouaeiou', result)
