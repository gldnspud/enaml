#------------------------------------------------------------------------------
#  Copyright (c) 2011, Enthought, Inc.
#  All rights reserved.
#------------------------------------------------------------------------------
from casuarius import ConstraintVariable


class BoxModel(object):
    """ Provides ConstraintVariables describing a box with margins.

    Primitive Variables:
        - left
        - top
        - width
        - height
        - right
        - bottom
        - v_center
        - h_center

    """
    def __init__(self, component):
        label = '{0}_{1:x}'.format(type(component).__name__, id(component))
        for primitive in ('left', 'top', 'width', 'height', 'right', 'bottom', 'v_center', 'h_center'):
            var = ConstraintVariable('{0}_{1}'.format(primitive, label))
            setattr(self, primitive, var) 


class MarginBoxModel(BoxModel):
    """ Provides ConstraintVariables describing a box with margins.

    Primitive Variables:
        - margin_[left|right|top|bottom]
        - contents_[left|top|right|bottom|width|height|v_center|h_center]
    
    """
    def __init__(self, component):
        super(MarginBoxModel, self).__init__(component)
        label = '{0}_{1:x}'.format(type(component).__name__, id(component))
        for primitive in ('left', 'right', 'top', 'bottom'):
           attr = 'margin_{0}'.format(primitive)
           var = ConstraintVariable('{0}_{1}'.format(attr, label))
           setattr(self, attr, var)
        for primitive in ('left', 'top', 'right', 'bottom', 'width', 'height',
            'v_center', 'h_center'):
            attr = 'contents_{0}'.format(primitive)
            var = ConstraintVariable('{0}_{1}'.format(attr, label))
            setattr(self, attr, var)

