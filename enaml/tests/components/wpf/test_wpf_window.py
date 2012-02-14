#------------------------------------------------------------------------------
#  Copyright (c) 2011, Enthought, Inc.
#  All rights reserved.
#------------------------------------------------------------------------------
from .wpf_test_assistant import WPFTestAssistant
from .. import window

class TestWPFWindow(WPFTestAssistant, window.TestWindow):
    """ QtWindow tests. """

    def get_title(self, widget):
        """ Get a window's title.

        """
        return widget.GetTitle()

