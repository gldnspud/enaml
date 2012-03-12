import math

from wpyf.visibility import Visibility
from wpyf.canvas import Canvas as Panel

from .wpf_base_widget_component import WPFBaseWidgetComponent

from ...components.widget_component import AbstractTkWidgetComponent
from ...layout.geometry import Rect, Size, Pos


class WPFWidgetComponent(WPFBaseWidgetComponent, AbstractTkWidgetComponent):
    """ A WPF implementation of WidgetComponent.

    """
    def create(self, parent):
        """ Creates the underlying WPF widget.

        """
        print "Create a widget component"
        self.widget = Panel()
        self.add_to_parent(parent)


    def enable_updates(self):
        """ Enable rendering updates for the underlying WPF widget.

        """
        #self.widget.set_updates_enabled(True)
        raise NotImplementedError

    def disable_updates(self):
        """ Disable rendering updates for the underlying WPF widget.

        """
        #self.widget.set_updates_enabled(False)
        raise NotImplementedError

    def set_visible(self, visible):
        """ Show or hide the widget.

        """
        if visible:
            self.widget.Visibility = Visibility.Visible
        else:
            self.widget.Visibility = Visibility.Collapsed

    def size_hint(self):
        """ Returns a (width, height) tuple of integers which represent
        the suggested size of the widget for its current state, ignoring
        any windowing decorations. This value is used by the layout
        manager to determine how much space to allocate the widget.

        """
        print "size_hint: ",self
        self.widget.Measure((float('inf'), float('inf')))
        width, height = self.widget.DesiredSize
        # Round to integral values.
        print "  returned hint is: ", width, height
        return Size(width=width, height=height)

    def layout_geometry(self):
        """ Returns the (x, y, width, height) to of layout geometry
        info for the internal toolkit widget. This should ignore any
        windowing decorations, and may be different than the value
        returned by geometry() if the widget's effective layout rect
        is different from its paintable rect.

        """
        widget = self.widget
        pos = self.pos()
        width = widget.ActualWidth
        height = widget.ActualHeight
        rect = Rect(pos.x, pos.y, width, height)
        print "Widget's {} effective geometry is {}".format(self.widget, rect)
        return rect

    def set_layout_geometry(self, rect):
        """ Sets the layout geometry of the internal widget to the
        given x, y, width, and height values. The parameters passed
        are equivalent semantics to layout_geometry().

        """
        print "Setting effective geometry of {} to {}".format(self.widget, rect)
        self.set_geometry(rect)

    def geometry(self):
        """ Returns an (x, y, width, height) tuple of geometry info
        for the internal toolkit widget, ignoring any windowing
        decorations.

        """
        pos = self.pos()
        size = self.size()
        rect = Rect(pos.x, pos.y, size.width, size.height)
        print "The geometry of {} is {}".format(self.widget, rect)
        return rect

    def set_geometry(self, rect):
        """ Sets the geometry of the internal widget to the given
        x, y, width, and height values, ignoring any windowing
        decorations.

        """
        print "Set geometry of {} to {}".format(self.widget, rect)
        self.move(rect.pos)
        self.resize(rect.size)

    def min_size(self):
        """ Returns the hard minimum (width, height) of the widget,
        ignoring any windowing decorations. A widget will not be able
        to be resized smaller than this value

        """
        size = Size(self.widget.MinWidth, self.widget.MinHeight)
        print "MinSize of {} is {}".format(self.widget, size)
        return size

    def set_min_size(self, size):
        """ Set the hard minimum width and height of the widget, ignoring
        any windowing decorations. A widget will not be able to be resized
        smaller than this value.

        """
        print "set_min_size: ", self, size
        size = Size(*size)
        self.widget.MinWidth = size.width
        self.widget.MinHeight = size.height

    def max_size(self):
        """ Returns the hard maximum (width, height) of the widget,
        ignoring any windowing decorations. A widget will not be able
        to be resized larger than this value

        """
        size = Size(self.widget.MaxWidth, self.widget.MaxHeight)
        print "MaxSize of {} is {}".format(self.widget, size)
        return size

    def set_max_size(self, size):
        """ Set the hard maximum width and height of the widget, ignoring
        any windowing decorations. A widget will not be able to be resized
        larger than this value.

        """
        print "set_max_size: ", self, size
        size = Size(*size)
        self.widget.MaxWidth = size.width
        self.widget.MaxHeight = size.height

    def size(self):
        """ Returns the size of the internal toolkit widget, ignoring any
        windowing decorations, as a (width, height) tuple of integers.

        """
        widget = self.widget
        width = -1 if math.isnan(widget.Width) else widget.Width
        height = -1 if math.isnan(widget.Height) else widget.Height
        print "The size of the {} widget is {}".format(widget, (width, height))
        return Size(width, height)

    def resize(self, size):
        """ Resizes the internal toolkit widget according the given
        width and height integers, ignoring any windowing decorations.

        """
        print "Resize: ",self, size
        size = Size(*size)
        self.widget.Width = size.width
        self.widget.Height = size.height

    def pos(self):
        """ Returns the position of the internal toolkit widget as an
        (x, y) tuple of integers, including any windowing decorations.
        The coordinates should be relative to the origin of the widget's
        parent, or to the screen if the widget is toplevel.

        """
        left = Panel.GetLeft(self.widget)
        top = Panel.GetTop(self.widget)
        print "Widget is at {}".format((left, top))
        return Pos(left, top)

    def move(self, pos):
        """ Moves the internal toolkit widget according to the given
        x and y integers which are relative to the origin of the
        widget's parent and includes any windowing decorations.

        """
        widget = self.widget
        Panel.SetLeft(widget, pos.x)
        Panel.SetTop(widget, pos.y)
        print "The new position of the {} widget is {}".format(widget, pos)

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
