#------------------------------------------------------------------------------
#  Copyright (c) 2011, Enthought, Inc.
#  All rights reserved.
#------------------------------------------------------------------------------
from .wpf_widget_component import WPFWidgetComponent

from ...components.constraints_widget import AbstractTkConstraintsWidget


class WPFConstraintsWidget(WPFWidgetComponent, AbstractTkConstraintsWidget):
    """ A WPF implementation of ConstraintsWidget.

    """
    pass
