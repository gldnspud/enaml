#------------------------------------------------------------------------------
#  Copyright (c) 2012, Enthought, Inc.
#  All rights reserved.
#------------------------------------------------------------------------------
import weakref
from wpyf.canvas import Canvas as Panel

from .wpf_constraints_widget import WPFConstraintsWidget

from ...components.container import AbstractTkContainer


class _Panel(Panel):
    """ A subclass of Panel which calls back onto the shell
    Container to get the size hint. If that size hint is invalid, it
    falls back onto the WPF default.

    """
    def __init__(self, wpf_container, *args, **kwargs):
        super(_Panel, self).__init__(*args, **kwargs)
        self.wpf_container = weakref.ref(wpf_container)
        print "Custom panel"

    @property
    def DesiredSize(self):
        """ Computes the size hint from the given Container, falling
        back on the default size hint computation if the Container
        returns one that is invalid.

        """
        res = None
        print "Overriden DesiredSize"
        wpf_container = self.wpf_container()
        if wpf_container is not None:
            shell = wpf_container.shell_obj
            if shell is not None:
                sh = shell.size_hint()
                print "container sizehint is {}".format(sh)
                if sh != (-1, -1):
                    res = sh
        if res is None:
            res = super(_Panel, self).DesiredSize
        return res

    # Because the Canvas panel does not report the width and high
    # propery we have to override the normal behaviour and return the
    # ActualWidth and Height instead
    @property
    def Width(self):
        return self.ActualWidth

    @Width.setter
    def Width(self, value):
        self.Width = value

    @property
    def Height(self):
        return self.ActualHeight

    @Height.setter
    def Height(self, value):
        self.Height = value


class WPFContainer(WPFConstraintsWidget, AbstractTkContainer):
    """ A WPF implementation of Container.

    """
    def create(self, parent):
        """ Creates the underlying WPF widget.

        """
        print "Create a container component"
        self.widget = _Panel(parent)
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
        print "Size of {} has changed".format(self.widget)
        self.shell_obj.refresh()


