# -*- coding: utf-8 -*-
"""Doctests runner."""

from niteoweb.ipn.jvzoo.testing import JvzooControlPanelTestCase
from Testing import ZopeTestCase as ztc
import doctest
import unittest2 as unittest


def test_suite():
    import niteoweb.ipn.jvzoo

    return unittest.TestSuite([

        # docstring unit-tests
        doctest.DocTestSuite(niteoweb.ipn.jvzoo),

        # Test the JVZoo control panel
        ztc.ZopeDocFileSuite(
            'tests/control_panel.txt', package='niteoweb.ipn.jvzoo',
            test_class=JvzooControlPanelTestCase,
            optionflags=doctest.REPORT_ONLY_FIRST_FAILURE | doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS
        ),
    ])

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
