import reflex as rx

class NavState(rx.State):
    """Tracks the currently selected tab for the sliding highlight."""
    active_tab: int = 0

    def set_tab(self, index: int):
        self.active_tab = index