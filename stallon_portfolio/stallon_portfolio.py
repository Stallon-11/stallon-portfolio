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
                # Locked to white/gray so it stays visible on the black toolbar
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

def main_island() -> rx.Component:
    """The central Dynamic Island."""
    return rx.box(
        # The Active Highlight (Stadium Shape)
        rx.box(
            position="absolute",
            top="0.375rem",
            left="0.375rem",
            width="4rem", 
            height="2.5rem", 
            border_radius="9999px", 
            background_color="#2C2C2E", # Apple Dark Gray highlight
            transition="transform 0.5s cubic-bezier(0.32, 0.72, 0, 1)",
            transform=f"translateX(calc({NavState.active_tab} * 4rem))",
            z_index="5",
        ),
        # The Icons Container
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
        background_color="#000000", # Locked to pure black
        border_radius="9999px",
        box_shadow="0 10px 30px rgba(0,0,0,0.15)",
        z_index="10", 
    )

def interactive_toolbar() -> rx.Component:
    """The proximity wrapper that houses the main island and the search mitosis logic."""
    return rx.box(
        # INNER WRAPPER: The true bounding box
        rx.box(
            main_island(),
            # The Ejecting Search Icon
            rx.center(
                rx.icon(tag="search", size=18, color="#FFFFFF"),
                id="search-bud", 
                width="3.25rem",
                height="3.25rem",
                background_color="#000000", # Locked to pure black
                border_radius="50%",
                box_shadow="0 10px 30px rgba(0,0,0,0.15)",
                position="absolute",
                top="0", 
                right="0", 
                z_index="5", 
                cursor="pointer",
                # Hardcoded baseline state to prevent style conflicts
                style={
                    "opacity": "0",
                    "transform": "translateX(0) scale(0.5)",
                    "transition": "all 0.5s cubic-bezier(0.32, 0.72, 0, 1)",
                    "pointerEvents": "none",
                }
            ),
            position="relative",
            display="flex",
        ),
        # OUTER WRAPPER: The Proximity Sensor
        padding="1rem", 
        border_radius="9999px",
        display="inline-flex", 
        justify_content="center",
        align_items="center",
        sx={
            "&:hover #search-bud": {
                # Ejected state
                "opacity": "1 !important",
                "transform": "translateX(3.75rem) scale(1) !important", 
                "pointerEvents": "auto !important",
            }
        }
    )

def scroll_triggers() -> rx.Component:
    """Hidden buttons that the JavaScript IntersectionObserver will click to update state."""
    return rx.box(
        *[rx.button(id=f"btn-tab-{i}", on_click=NavState.set_tab(i), display="none") for i in range(5)]
    )

def about_me_section() -> rx.Component:
    """The Apple Leadership styled About Me layout."""
    return rx.vstack(
        # Top Banner Area (Light Gray)
        rx.box(
            rx.hstack(
                rx.vstack(
                    rx.heading("Stallon Fernandes", size="9", color="#1D1D1F", font_weight="600"),
                    rx.text("AI & Machine Learning Engineer", size="6", color="#86868B", font_weight="400"),
                    align_items="start",
                    spacing="2",
                ),
                # Placeholder for your portrait image
                rx.center(
                    rx.icon("image", size=40, color="#86868B"),
                    width="200px",
                    height="200px",
                    background_color="#E5E5EA",
                    border_radius="1rem",
                ),
                justify="between", # Using valid Radix argument
                align_items="center",
                width="100%",
                max_width="1000px",
                margin="auto",
                padding_x="2rem",
            ),
            width="100vw",
            background_color="#F5F5F7", # Apple's signature section background
            padding_y="6rem",
            margin_bottom="4rem",
        ),
# Two-Column Text Area
        rx.box(
            rx.flex(
                # Paragraph 1
                rx.text(
                    "I am an AI & Machine Learning Engineer currently pursuing an MSci in Artificial Intelligence at King's College London. My technical focus lies in developing microservice architectures and knowledge graphs, having built systems like the Sympto Medical Diagnosis Assistant and a comprehensive TfL Knowledge Graph. I am particularly passionate about optimizing and deploying Large Language Models for local, high-performance applications.",
                    color="#1D1D1F",
                    size="4",
                    line_height="1.6",
                    flex="1",
                ),
                # Paragraph 2
                rx.text(
                    "Before focusing entirely on AI development, I built a strong foundation in communication and operations through roles in educational administration and retail. As I prepare for my third year of university, my goal is to transition into a full-time Machine Learning Engineer role, combining my academic background with hands-on experience in containerization, Python, and semantic web technologies.",
                    color="#1D1D1F",
                    size="4",
                    line_height="1.6",
                    flex="1",
                ),
                # FIX: Use Radix dictionary format for responsive breakpoints
                direction={"initial": "column", "md": "row"}, 
                spacing="8",
                width="100%",
                max_width="1000px",
                margin="auto",
                padding_x="2rem",
            ),
            width="100%",
        ),
        id="section-0",
        class_name="scroll-section",
        min_height="100vh",
        width="100%",
        align_items="center",
    )

def standard_section(index: int, title: str, content: rx.Component) -> rx.Component:
    """Template for the remaining CV sections."""
    return rx.vstack(
        rx.heading(title, size="8", color="#1D1D1F", margin_bottom="2rem"),
        content,
        id=f"section-{index}",
        class_name="scroll-section",
        min_height="100vh", 
        width="100%",
        max_width="1000px",
        padding_top="8rem", 
        padding_x="2rem",
        align_items="start",
    )

def page_content() -> rx.Component:
    """The CV data divided into five monitored sections."""
    return rx.vstack(
        about_me_section(),
        standard_section(1, "Projects", rx.vstack(
            rx.text("• Sympto Medical Diagnosis Assistant", color="#1D1D1F", size="5"),
            rx.text("• TfL Knowledge Graph Architecture", color="#1D1D1F", size="5"),
        )),
        standard_section(2, "Experience", rx.vstack(
            rx.text("• Exams Invigilator - Cardinal Wiseman School", color="#1D1D1F", size="5"),
            rx.text("• Retail Assistant - Primark", color="#1D1D1F", size="5"),
        )),
        standard_section(3, "Publications", rx.text("Currently exploring research opportunities in local LLM deployment and microservice architectures for Year 3.", color="#1D1D1F", size="5")),
        standard_section(4, "Contact Me", rx.text("Based in London. Reach out for collaboration.", color="#1D1D1F", size="5")),
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
    }, { threshold: 0.5 }); 

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
            interactive_toolbar(),
            position="fixed",
            top="2rem",
            width="100%",
            z_index="100",
        ),
        page_content(),
        background_color="#FFFFFF", # Bright white background for Apple layout
        font_family=APPLE_FONT,
        width="100%",
        style={"scrollBehavior": "smooth"}, 
    )

# App initialization without deprecated theme argument
app = rx.App()
app.add_page(index)