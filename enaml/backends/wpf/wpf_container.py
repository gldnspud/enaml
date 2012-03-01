#------------------------------------------------------------------------------
#  Copyright (c) 2012, Enthought, Inc.
#  All rights reserved.
#------------------------------------------------------------------------------
import weakref

from wpyf.panel import Panel as _WPyFPanel

from .wpf_constraints_widget import WPFConstraintsWidget

from ...components.container import AbstractTkContainer


class WPFContainer(WPFConstraintsWidget, AbstractTkContainer):
    """ A WPF implementation of Container.

    """
    def create(self, parent):
        """ Creates the underlying WPF widget.

        """
        self.widget = _WPyFPanel()
        parent.SetContent(self.widget)

    def initialize(self):
        """ Initializes the widget.

        """
        super(WPFContainer, self).initialize()

    def bind(self):
        """ Binds the signal handlers for the widget.

        """
        super(WPFContainer, self).bind()
