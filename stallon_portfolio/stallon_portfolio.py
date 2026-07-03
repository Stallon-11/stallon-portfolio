import reflex as rx

# Apple's native system font stack
APPLE_FONT = "-apple-system, BlinkMacSystemFont, 'SF Pro Display', 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"

class NavState(rx.State):
    """Tracks the currently selected tab for the sliding highlight."""
    active_tab: int = 0

    def set_tab(self, index: int):
        self.active_tab = index

def nav_icon(icon_name: str, index: int, tooltip: str) -> rx.Component:
    """Helper to generate consistent navigation icons."""
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
            # Clicking updates the state AND smoothly scrolls the page to the corresponding section
            on_click=[
                NavState.set_tab(index), 
                rx.call_script(f"document.getElementById('section-{index}').scrollIntoView({{behavior: 'smooth'}})")
            ],
        ),
        content=tooltip,
    )

def toolbar() -> rx.Component:
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
        box_shadow="0 10px 30px rgba(0,0,0,0.5), inset 0 0 0 1px rgba(255, 255, 255, 0.05)",
    )

def scroll_triggers() -> rx.Component:
    """Hidden buttons that the JavaScript IntersectionObserver will click to update state."""
    return rx.box(
        rx.button(id="btn-tab-0", on_click=NavState.set_tab(0), display="none"),
        rx.button(id="btn-tab-1", on_click=NavState.set_tab(1), display="none"),
        rx.button(id="btn-tab-2", on_click=NavState.set_tab(2), display="none"),
        rx.button(id="btn-tab-3", on_click=NavState.set_tab(3), display="none"),
        rx.button(id="btn-tab-4", on_click=NavState.set_tab(4), display="none"),
    )

def section_container(index: int, title: str, content: rx.Component) -> rx.Component:
    """A full-height section wrapper that acts as a scroll waypoint."""
    return rx.vstack(
        rx.heading(title, size="8", color="#FFFFFF", margin_bottom="2rem"),
        content,
        id=f"section-{index}",
        class_name="scroll-section",
        min_height="100vh", # Forces each section to take up a full screen height
        width="100%",
        max_width="800px",
        padding_top="10rem", # Pushes content down so it isn't hidden behind the fixed toolbar
        align_items="start",
    )

def page_content() -> rx.Component:
    """The actual CV data divided into our five monitored sections."""
    return rx.vstack(
        section_container(0, "About Me", rx.text("AI & Machine Learning Engineer pursuing an MSci in Artificial Intelligence at King's College London.", color="#86868B", size="5")),
        section_container(1, "Projects", rx.vstack(
            rx.text("• Sympto Medical Diagnosis Assistant", color="#86868B", size="5"),
            rx.text("• TfL Knowledge Graph Architecture", color="#86868B", size="5"),
        )),
        section_container(2, "Experience", rx.vstack(
            rx.text("• Exams Invigilator - Cardinal Wiseman School", color="#86868B", size="5"),
            rx.text("• Retail Assistant - Primark", color="#86868B", size="5"),
        )),
        section_container(3, "Publications", rx.text("Currently exploring research opportunities in local LLM deployment and microservice architectures for Year 3.", color="#86868B", size="5")),
        section_container(4, "Contact Me", rx.text("Based in London. Reach out for collaboration.", color="#86868B", size="5")),
        width="100%",
        align_items="center",
    )

# The client-side logic: It detects when a section takes up 50% of the screen 
# and silently fires the corresponding hidden button to sync the server state.
scrollspy_script = """
setTimeout(() => {
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const index = entry.target.id.split('-')[1];
                const btn = document.getElementById('btn-tab-' + index);
                if (btn) {
                    btn.click();
                }
            }
        });
    }, { threshold: 0.5 }); // Triggers when section is 50% visible

    document.querySelectorAll('.scroll-section').forEach(sec => {
        observer.observe(sec);
    });
}, 1000); 
"""

def index() -> rx.Component:
    return rx.box(
        rx.script(scrollspy_script),
        scroll_triggers(),
        rx.center(
            toolbar(),
            position="fixed",
            top="2rem",
            width="100%",
            z_index="100",
        ),
        page_content(),
        background_color="#121212", 
        font_family=APPLE_FONT,
        width="100%",
        # Enables smooth CSS scrolling natively
        style={"scrollBehavior": "smooth"}, 
    )

app = rx.App(
    theme=rx.theme(
        appearance="dark",
        has_background=True,
    )
)
app.add_page(index)