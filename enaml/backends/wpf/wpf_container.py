#------------------------------------------------------------------------------
#  Copyright (c) 2012, Enthought, Inc.
#  All rights reserved.
#------------------------------------------------------------------------------
from wpyf.panel import Panel

from .wpf_constraints_widget import WPFConstraintsWidget

from ...components.container import AbstractTkContainer


class WPFContainer(WPFConstraintsWidget, AbstractTkContainer):
    """ A WPF implementation of Container.

    """
    def create(self, parent):
        """ Creates the underlying WPF widget.

        """
        self.widget = Panel()
        self.add_to_parent(parent)

    def initialize(self):
        """ Initializes the widget.

        """
        super(WPFContainer, self).initialize()

    def bind(self):
        """ Binds the signal handlers for the widget.

        """
        super(WPFContainer, self).bind()
        self.widget.SizeChanged += self.on_resize

    def on_resize(self):
        self.shell_obj.refresh()
