#------------------------------------------------------------------------------
#  Copyright (c) 2011, Enthought, Inc.
#  All rights reserved.
#------------------------------------------------------------------------------
from abc import abstractmethod

from traits.api import Property, Int, Instance, List, cached_property

from .layout_component import LayoutComponent, AbstractTkLayoutComponent
from .layout_task_handler import LayoutTaskHandler
from .tab import Tab

from ..enums import TabPosition


class AbstractTkTabGroup(AbstractTkLayoutComponent):
    """ The abstract toolkit TabGroup interface.

    """
    @abstractmethod
    def shell_tabs_changed(self, tabs):
        """ The change handler for the 'tabs' attribute of the shell 
        object.

        """
        raise NotImplementedError

    @abstractmethod
    def shell_tab_position_changed(self, tab_position):
        """ The change handler for the 'tab_position' attribute on the 
        shell object.

        """
        raise NotImplementedError

    @abstractmethod
    def shell_selected_index_changed(self, index):
        """ The change handler for the 'selected_index' attribute on
        the shell object.

        """
        raise NotImplementedError


class TabGroup(LayoutTaskHandler, LayoutComponent):
    """ A LayoutComponent that arranges its children as a group of tabs.

    The TabGroup provides a very simple way of laying out a number of 
    children as tabs, suitable for configuration dialogs and the like. 
    It is not suitable for rich tab interfaces where the group of tabs
    is the central focus of the application. For that, use a Notebook.

    """
    #: A read-only cached property that returns the tab children
    #: of this tab group.
    tabs = Property(List(Instance(Tab)), depends_on='layout_children')

    #: A readonly property which returns the selected index. If there 
    #: are no tabs in the group, this will return -1.
    selected_index = Property(Int, depends_on='_selected_index')

    #: A readonly property which returns the selected tab. If there are 
    #: no tabs in the group, this will return None.
    selected_tab = Property(Instance(Tab), depends_on='_selected_index')

    #: A TabPosition enum value that indicate where the tabs should
    #: be drawn on the control. One of 'top', 'bottom', 'left', 'right'.
    #: The default value is 'top'.
    tab_position = TabPosition('top')

    #: How strongly a component hugs it's contents' width. A TabGroup
    #: ignores its width hug by default, so it expands freely in width.
    hug_width = 'ignore'

    #: How strongly a component hugs it's contents' height. A TabGroup
    #: ignores its height hug by default, so it expands freely in height.
    hug_height = 'ignore'

    #: The private storage for the selected tab index. This is the 
    #: attribute should be used by the toolkit implementations to 
    #: communicate the current selection. A -1 indicates no selection.
    _selected_index = Int(-1)

    #--------------------------------------------------------------------------
    # Property Getters and Setters
    #--------------------------------------------------------------------------
    @cached_property
    def _get_tabs(self):
        """ The property getter for the 'tabs' attribute.

        """
        res = []
        for child in self.layout_children:
            if not isinstance(child, Tab):
                msg = ('The children of a TabGroup must be instance of Tab. '
                       'Got %s instead.' % child)
                raise TypeError(msg)
            res.append(child)
        return res
    
    def _get_selected_tab(self):
        """ The property getter for the 'selected_tab' attribute.

        """
        idx = self._selected_index
        tabs = self.tabs
        n = len(tabs)
        if 0 <= idx < n:
            res = tabs[idx]
        elif idx == -1 and tabs:
            res = tabs[0]
        else:
            res = None
        return res
    
    def _get_selected_index(self):
        """ The property getter for the 'selected_index' attribute.

        """
        idx = self._selected_index
        if idx == -1 and self.tabs:
            idx = 0
        return idx

    #--------------------------------------------------------------------------
    # Change Handlers
    #--------------------------------------------------------------------------
    def _tab_position_changed(self):
        """ A change handler for triggering a relayout when the position
        of the tabs change.

        """
        self.request_relayout()

    def _on_layout_deps_changed(self):
        """ A change handler for triggering a relayout when any of the
        layout dependencies change. It simply requests a relayout.

        """
        self.request_relayout()

    #--------------------------------------------------------------------------
    # Overrides
    #--------------------------------------------------------------------------
    def initialize_layout(self):
        """ A reimplemented parent class method which hooks up change
        handlers for child attributes which will cause a change in 
        the layout.

        """
        self.on_trait_change(
            self._on_layout_deps_changed, (
                'selected_tab.size_hint_updated'
            )
        )

    def do_relayout(self):
        """ A reimplemented LayoutTaskHandler handler method which will
        perform necessary update activity when a relayout it requested.

        """
        self.size_hint_updated = True

