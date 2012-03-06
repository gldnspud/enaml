#------------------------------------------------------------------------------
#  Copyright (c) 2012, Enthought, Inc.
#  All rights reserved.
#------------------------------------------------------------------------------
from wpyf.button import Button as _WPyFButton
from .wpf_control import WPFControl

from ...components.push_button import AbstractTkPushButton


class WPFPushButton(WPFControl, AbstractTkPushButton):
    """ A WPF implementation of PushButton.

    """
    #def __init__(self, *args, **kwargs):
    #    super(WPFPushButton, self).__init__(*args, **kwargs)
    #    self._bound_methods = {}

    #--------------------------------------------------------------------------
    # Setup methods
    #--------------------------------------------------------------------------
    def create(self, parent):
        """ Creates the underlying WPF PushButton control.

        """
        shell = self.shell_obj
        self.widget = _WPyFButton()
        self.add_to_parent(parent)

    def initialize(self):
        """ Intializes the widget with the attributes of this instance.

        """
        super(WPFPushButton, self).initialize()
        self.set_label(self.shell_obj.text)

    def bind(self):
        """ Connects the event handlers for the push button.

        """
        super(WPFPushButton, self).bind()
        widget = self.widget
        widget.Click += self.on_clicked

    #--------------------------------------------------------------------------
    # Implementation
    #--------------------------------------------------------------------------
    def shell_text_changed(self, text):
        """ The change handler for the 'text' attribute.

        """
        self.set_label(text)
        # If the text of the button changes, the size hint has likely
        # change and the layout system needs to be informed.
        self.shell_obj.size_hint_updated()

    def shell_icon_changed(self, icon):
        """ The change handler for the 'icon' attribute.

        """
        pass


    def on_clicked(self):
        """ The event handler for the button's clicked event.

        """
        print 'on_clicked'
        shell = self.shell_obj
        shell._down = False
        shell.clicked()
        print 'done'

    def on_pressed(self):
        """ The event handlers for the button's pressed event.

        """
        shell = self.shell_obj
        shell._down = True
        shell.pressed()

    def on_released(self):
        """ The event handler for the button's released event.

        """
        shell = self.shell_obj
        if shell._down:
            shell._down = False
            shell.released()

    def set_label(self, label):
        """ Sets the label on the button control.

        """
        shell = self.shell_obj
        self.widget.Content = unicode(shell.text)


def on_clicked():
    print 'clicked'
