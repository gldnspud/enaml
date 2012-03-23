#------------------------------------------------------------------------------
#  Copyright (c) 2012, Enthought, Inc.
#  All rights reserved.
#------------------------------------------------------------------------------
import weakref

from wpyf.window import Window

from ...components.base_widget_component import AbstractTkBaseWidgetComponent


class WPFBaseWidgetComponent(AbstractTkBaseWidgetComponent):
    #: The a reference to the shell object. Will be stored as a weakref.
    _shell_obj = lambda self: None

    #: The WPF widget created by the component
    widget = None

    @property
    def toolkit_widget(self):
        """ A property that returns the toolkit specific widget for this
        component.

        """
        return self.widget

    def _get_shell_obj(self):
        """ Returns a strong reference to the shell object.

        """
        return self._shell_obj()

    def _set_shell_obj(self, obj):
        """ Stores a weak reference to the shell object.

        """
        self._shell_obj = weakref.ref(obj)

    #: A property which gets a sets a reference (stored weakly)
    #: to the shell object
    shell_obj = property(_get_shell_obj, _set_shell_obj)

    def bind(self):
        """ Bind any event handlers for the WPF Widget. By default,
        this is a no-op. Subclasses should reimplement this method as
        necessary to bind any widget event handlers or signals.

        """
        super(WPFBaseWidgetComponent, self).bind()

    def destroy(self):
        """ Destroys the underlying WPF widget.

        """
        self.widget = None

    def add_to_parent(self, parent):
        """ Add the widget to the provided parent.

        The method is used to hide the different ways of parenting in WPF.
        """
        child = self.widget
        if isinstance(parent, Window):
            parent.Content = child
        else:
            parent.Children.Add(child)

