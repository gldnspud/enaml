from .wpf_base_widget_component import WPFBaseWidgetComponent

from ...components.widget_component import AbstractTkWidgetComponent
from ...layout.geometry import Rect, Size, Pos


class WPFWidgetComponent(WPFBaseWidgetComponent, AbstractTkWidgetComponent):
    """ A WPF implementation of WidgetComponent.

    """
    def enable_updates(self):
        """ Enable rendering updates for the underlying WPF widget.

        """
        #self.widget.set_updates_enabled(True)
        pass

    def disable_updates(self):
        """ Disable rendering updates for the underlying WPF widget.

        """
        #self.widget.set_updates_enabled(False)
        pass

    def set_visible(self, visible):
        """ Show or hide the widget.

        """
        if visible:
            self.widget.Visibility  = visibility.Visible
        else:
            self.widget.Visibility  = visibility.Collapsed

    def size_hint(self):
        """ Returns a (width, height) tuple of integers which represent
        the suggested size of the widget for its current state, ignoring
        any windowing decorations. This value is used by the layout
        manager to determine how much space to allocate the widget.

        """
        return Size(0, 0)

    def layout_geometry(self):
        """ Returns the (x, y, width, height) to of layout geometry
        info for the internal toolkit widget. This should ignore any
        windowing decorations, and may be different than the value
        returned by geometry() if the widget's effective layout rect
        is different from its paintable rect.

        """
        return self.geometry()

    def set_layout_geometry(self, rect):
        """ Sets the layout geometry of the internal widget to the
        given x, y, width, and height values. The parameters passed
        are equivalent semantics to layout_geometry().

        """
        pass

    def geometry(self):
        """ Returns an (x, y, width, height) tuple of geometry info
        for the internal toolkit widget, ignoring any windowing
        decorations.

        """
        return Rect(0, 0, 1, 1)

    def set_geometry(self, rect):
        """ Sets the geometry of the internal widget to the given
        x, y, width, and height values, ignoring any windowing
        decorations.

        """
        pass

    def min_size(self):
        """ Returns the hard minimum (width, height) of the widget,
        ignoring any windowing decorations. A widget will not be able
        to be resized smaller than this value

        """
        return Size(0, 0)

    def set_min_size(self, size):
        """ Set the hard minimum width and height of the widget, ignoring
        any windowing decorations. A widget will not be able to be resized
        smaller than this value.

        """
        pass

    def max_size(self):
        """ Returns the hard maximum (width, height) of the widget,
        ignoring any windowing decorations. A widget will not be able
        to be resized larger than this value

        """
        return Size(0, 0)

    def set_max_size(self, size):
        """ Set the hard maximum width and height of the widget, ignoring
        any windowing decorations. A widget will not be able to be resized
        larger than this value.

        """
        pass

    def size(self):
        """ Returns the size of the internal toolkit widget, ignoring any
        windowing decorations, as a (width, height) tuple of integers.

        """
        return Size(0, 0)

    def resize(self, size):
        """ Resizes the internal toolkit widget according the given
        width and height integers, ignoring any windowing decorations.

        """
        pass

    def pos(self):
        """ Returns the position of the internal toolkit widget as an
        (x, y) tuple of integers, including any windowing decorations.
        The coordinates should be relative to the origin of the widget's
        parent, or to the screen if the widget is toplevel.

        """
        return Pos(0, 0)

    def move(self, pos):
        """ Moves the internal toolkit widget according to the given
        x and y integers which are relative to the origin of the
        widget's parent and includes any windowing decorations.

        """
        pass

    def shell_enabled_changed(self, enabled):
        """ The change handler for the 'enabled' attribute on the shell
        object.

        """
        self.set_enabled(enabled)

    def shell_bgcolor_changed(self, color):
        """ The change handler for the 'bgcolor' attribute on the shell
        object. Sets the background color of the internal widget to the
        given color.

        """
        self.set_bgcolor(color)

    def shell_fgcolor_changed(self, color):
        """ The change handler for the 'fgcolor' attribute on the shell
        object. Sets the foreground color of the internal widget to the
        given color.

        """
        self.set_fgcolor(color)

    def shell_font_changed(self, font):
        """ The change handler for the 'font' attribute on the shell
        object. Sets the font of the internal widget to the given font.

        """
        self.set_font(font)
