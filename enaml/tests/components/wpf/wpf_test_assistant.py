#------------------------------------------------------------------------------
#  Copyright (c) 2011, Enthought, Inc.
#  All rights reserved.
#------------------------------------------------------------------------------
from enaml import wpf_toolkit


class WPFTestAssistant(object):
    """ Assistant class for testing WPF based components.

    This class is to be used as a mixing with the base enaml test case
    class for the components tests of the WPF backend. It sets the correct
    toolkit attribute and (in the future) provide some useful methods for
    testing WPF based components.

    """

    toolkit = wpf_toolkit()

