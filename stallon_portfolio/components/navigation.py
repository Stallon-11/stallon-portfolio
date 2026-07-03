import reflex as rx
from stallon_portfolio.state import NavState

def nav_icon(icon_name: str, index: int, tooltip: str) -> rx.Component:
    return rx.tooltip(
        rx.center(
            rx.icon(
                tag=icon_name,
                size=20,
                color=rx.cond(NavState.active_tab == index, "#FFFFFF", "#6E6E73"),
                transition="color 0.4s cubic-bezier(0.32, 0.72, 0, 1)",
            ),
            width="4rem",  
            height="2.5rem",
            cursor="pointer",
            z_index="10",
            on_click=[
                NavState.set_tab(index), 
                rx.call_script(f"document.getElementById('section-{index}').scrollIntoView({{behavior: 'smooth'}})")
            ],
        ),
        content=tooltip,
    )

def main_island() -> rx.Component:
    return rx.box(
        rx.box(
            position="absolute",
            top="0.375rem",
            left="0.375rem",
            width="4rem", 
            height="2.5rem", 
            border_radius="9999px", 
            background_color="#2C2C2E", 
            transition="transform 0.5s cubic-bezier(0.32, 0.72, 0, 1)",
            transform=f"translateX(calc({NavState.active_tab} * 4rem))",
            z_index="5",
        ),
        rx.hstack(
            nav_icon("user", 0, "About Me"),
            nav_icon("folder", 1, "Projects"),
            nav_icon("briefcase", 2, "Experience"),
            nav_icon("file-pen", 3, "Publications"),
            nav_icon("mail", 4, "Contact Me"),
            spacing="0", 
        ),
        position="relative",
        padding="0.375rem",
        background_color="#000000", 
        border_radius="9999px",
        box_shadow="0 10px 30px rgba(0,0,0,0.15)",
        z_index="10", 
    )

def interactive_toolbar() -> rx.Component:
    return rx.box(
        rx.box(
            main_island(),
            rx.center(
                rx.icon(tag="search", size=18, color="#FFFFFF"),
                id="search-bud", 
                width="3.25rem",
                height="3.25rem",
                background_color="#000000",
                border_radius="50%",
                box_shadow="0 10px 30px rgba(0,0,0,0.15)",
                position="absolute",
                top="0", right="0", z_index="5", cursor="pointer",
                style={
                    "opacity": "0",
                    "transform": "translateX(0) scale(0.5)",
                    "transition": "all 0.5s cubic-bezier(0.32, 0.72, 0, 1)",
                    "pointerEvents": "none",
                }
            ),
            position="relative", display="flex",
        ),
        padding="1rem", border_radius="9999px", display="inline-flex", 
        justify_content="center", align_items="center",
        sx={
            "&:hover #search-bud": {
                "opacity": "1 !important",
                "transform": "translateX(3.75rem) scale(1) !important", 
                "pointerEvents": "auto !important",
            }
        }
    )

def scroll_triggers() -> rx.Component:
    return rx.box(
        *[rx.button(id=f"btn-tab-{i}", on_click=NavState.set_tab(i), display="none") for i in range(5)]
    )