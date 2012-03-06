#------------------------------------------------------------------------------
#  Copyright (c) 2012, Enthought, Inc.
#  All rights reserved.
#------------------------------------------------------------------------------
from .wpf_test_assistant import WPFTestAssistant
from .. import label

class TestLabel(WPFTestAssistant, label.TestLabel):
    """ WPFLabel tests. """

    def get_text(self, widget):
        """ Get a label's text.

        """
        return widget.Content
