import reflex as rx
from stallon_portfolio.components.navigation import interactive_toolbar, scroll_triggers
from stallon_portfolio.components.sections import about_me_section, standard_section

APPLE_FONT = "-apple-system, BlinkMacSystemFont, 'SF Pro Display', 'Segoe UI', Roboto, Helvetica, Arial, sans-serif"

def page_content() -> rx.Component:
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
        standard_section(3, "Publications", rx.text("Currently exploring research opportunities in local LLM deployment.", color="#1D1D1F", size="5")),
        standard_section(4, "Contact Me", rx.text("Based in London. Reach out for collaboration.", color="#1D1D1F", size="5")),
        width="100%", align_items="center",
    )

scrollspy_script = """
setTimeout(() => {
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const index = entry.target.id.split('-')[1];
                const btn = document.getElementById('btn-tab-' + index);
                if (btn) btn.click();
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
            position="fixed", top="2rem", width="100%", z_index="100",
        ),
        page_content(),
        background_color="#FFFFFF", font_family=APPLE_FONT, width="100%",
        style={"scrollBehavior": "smooth"}, 
    )