#------------------------------------------------------------------------------
#  Copyright (c) 2012, Enthought, Inc.
#  All rights reserved.
#------------------------------------------------------------------------------
from wpyf.api import Window, WindowSizeHelper
from wpyf.api import Size as WPFSize

from .wpf_window import WPFWindow

from ...layout.geometry import Size
from ...components.main_window import AbstractTkMainWindow


class WPFMainWindow(WPFWindow, AbstractTkMainWindow):
    """ A WPF implementation of a MainWindow.

    """
    #--------------------------------------------------------------------------
    # Setup methods
    #--------------------------------------------------------------------------
    def create(self, parent):
        """ Creates the underlying WPFMainWindow object.

        """
        self.widget = Window()

    def initialize(self):
        """ Initialize the WPFMainWindow object.

        """
        super(WPFMainWindow, self).initialize()
        self.update_menu_bar()

    #--------------------------------------------------------------------------
    # Change Handlers
    #--------------------------------------------------------------------------
    def shell_menu_bar_changed(self, menu_bar):
        """ Update the menu bar of the window with the new value from
        the shell object.

        """
        self.update_menu_bar()

    #--------------------------------------------------------------------------
    # Abstract Implementation
    #--------------------------------------------------------------------------
    def menu_bar_height(self):
        """ Returns the height of the menu bar in pixels. If the menu
        bar does not have an effect on the height of the main window,
        this method returns Zero.

        """
        return 0

    #--------------------------------------------------------------------------
    # Widget Update Methods
    #--------------------------------------------------------------------------
    def update_menu_bar(self):
        """ Updates the menu bar in the main window with the value
        from the shell object.

        """
        pass

    def update_central_widget(self):
        """ Updates the central widget in the main window with the
        value from the shell object.

        """
        # It's possible for the central widget component to be None.
        # This must be allowed since the central widget may be generated
        # by an Include component, in which case it will not exist
        # during initialization. However, we must have a central widget
        # for the MainWindow, and in that case we just fill it with a
        # dummy widget.
        pass

    def set_visible(self, visible):
        """ Overridden from the parent class to raise the window to
        the front if it should be shown.

        """
        pass

    #--------------------------------------------------------------------------
    # Widget Component override methods
    #--------------------------------------------------------------------------

    def resize(self, size):
        """ Resize window to accomodate the required client area.
        """
        new_size = WindowSizeHelper.GetWindowSizeForClientArea(self.widget,
                                                               WPFSize(size[0],
                                                                    size[1]));
        # XXX Settig the window size like this will cause resize to fire twice.
        self.widget.Width = new_size.Width
        self.widget.Height = new_size.Height

    def size(self, size):
        """ Get window client Area.
        """
        area = WindowSizeHelper.GetWindowClientArea(self.widget)
        return Size(area.Width, area.Height)

    def set_max_size(self, size):
        """ Set max size of the window to accomodate the required max
        size client area.
        """
        new_size = WindowSizeHelper.GetWindowSizeForClientArea(self.widget,
                                                               WPFSize(size[0],
                                                                    size[1]));
        self.widget.MaxWidth = new_size.Width
        self.widget.MaxHeight = new_size.Height

    def set_min_size(self, size):
        """ Set min size of the window to accomodate the required min
        size client area.
        """
        new_size = WindowSizeHelper.GetWindowSizeForClientArea(self.widget,
                                                               WPFSize(size[0],
                                                                    size[1]));
        self.widget.MinWidth = new_size.Width
        self.widget.MinHeight = new_size.Height
