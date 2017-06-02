#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_wordpress_importer
----------------------------------

Tests for `wordpress_importer` module.
"""


import sys
import unittest
from contextlib import contextmanager
from click.testing import CliRunner

from wordpress_importer import wordpress_importer
from wordpress_importer import cli



class TestWordpress_importer(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_000_something(self):
        pass

    def test_command_line_interface(self):
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'wordpress_importer.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output