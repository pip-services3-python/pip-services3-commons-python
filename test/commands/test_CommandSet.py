# -*- coding: utf-8 -*-
"""
    tests.config.test_CommandSet
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) Conceptual Vision Consulting LLC 2015-2016, see AUTHORS for more details.
    :license: MIT, see LICENSE for more details.
"""

import pytest

from pip_services3_commons.commands import Command
from pip_services3_commons.commands import CommandSet

from pip_services3_commons.run.IExecutable import IExecutable
from pip_services3_commons.run.Parameters import Parameters


class MyTestError(Exception):
    def __init__(self, text):
        self.txt = text


class CommandExecTest(IExecutable):
    def execute(self, correlation_id, args):
        if correlation_id == 'wrongId':
            raise MyTestError('Test error')


class TestCommandSet:

    def get_value(self, correlation_id, args):
        return args.get('value')

    def test_get_name(self):
        command = Command('name', None, CommandExecTest())
        assert command is not None
        assert command.get_name() == 'name'

    def make_echo_command(self, name):
        return Command(name, None, self.get_value)

    def test_commands(self):
        commands = CommandSet()
        commands.add_command(self.make_echo_command("command1"))
        commands.add_command(self.make_echo_command("command2"))

        result = commands.execute(None, "command1", Parameters.from_tuples("value", 123))
        assert 123 == result

        result = commands.execute(None, "command1", Parameters.from_tuples("value", "ABC"))
        assert "ABC" == result

        result = commands.execute(None, "command2", Parameters.from_tuples("value", 789))
        assert 789 == result
