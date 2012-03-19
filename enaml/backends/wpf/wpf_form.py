#------------------------------------------------------------------------------
#  Copyright (c) 2011, Enthought, Inc.
#  All rights reserved.
#------------------------------------------------------------------------------
from .wpf_container import WPFContainer

from ...components.form import AbstractTkForm


class WPFForm(WPFContainer, AbstractTkForm):
    """ A WPF implementation of a From container.

    """
    # The WPFContainer implementation is enough.
    pass

