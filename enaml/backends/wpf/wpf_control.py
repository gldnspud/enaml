#------------------------------------------------------------------------------
#  Copyright (c) 2012, Enthought, Inc.
#  All rights reserved.
#------------------------------------------------------------------------------
from .wpf_constraints_widget import WPFConstraintsWidget

from ...components.control import AbstractTkControl


class WPFControl(WPFConstraintsWidget, AbstractTkControl):
    pass
