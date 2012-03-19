#------------------------------------------------------------------------------
#  Copyright (c) 2011, Enthought, Inc.
#  All rights reserved.
#------------------------------------------------------------------------------
import warnings

from .pwf_test_assistant import WPFTestAssistant, skip_nonwindows

from .. import field


warnings.simplefilter('ignore')


@skip_nonwindows
class TestWPFField(WPFTestAssistant, field.TestField):
    """ WPFField tests.

    """
    def get_value(self, widget):
        """ Get the visible text of a field.

        """
        return widget.Text

    def edit_text(self, widget, text):
        """ Simulate typing in a field.

        """
        self.fail()

    def change_text(self, widget, text):
        """ Change text programmatically, rather than "edit" it.

        """
        widget.Text = unicode(text)

    def set_cursor_position(self, widget, index):
        """ Set the cursor at a specific position.

        """
        self.fail

    def get_cursor_position(self, widget):
        """ Get the cursor position.

        """
        self.fail

    def get_password_mode(self, widget):
        """ Get the password mode status of the widget.

        """
        self.fail

    def get_selected_text(self, widget):
        """ Get the currently-selected text from a field.

        """
        self.fail

    def press_return(self, widget):
        """ Simulate a press of the 'Return' key.

        """
        self.fail

    def gain_focus_if_needed(self, widget):
        """ Have the widget gain focus if required for the tests.

        """
        pass

