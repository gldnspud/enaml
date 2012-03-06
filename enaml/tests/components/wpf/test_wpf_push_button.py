#------------------------------------------------------------------------------
#  Copyright (c) 2012, Enthought, Inc.
#  All rights reserved.
#------------------------------------------------------------------------------
from .wpf_test_assistant import WPFTestAssistant
from .. import push_button


class TestWPFPushButton(WPFTestAssistant, push_button.TestPushButton):
    """ WPFPushButton tests. """

    def button_pressed(self):
        """ Press the button programmatically.

        """
        self.Fail()

    def button_released(self):
        """ Release the button programmatically.

        """
        self.Fail()

    def button_clicked(self):
        """ Click the button programmatically.

        """
        self.Fail()
