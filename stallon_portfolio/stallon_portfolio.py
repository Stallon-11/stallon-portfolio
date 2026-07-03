import reflex as rx

def index() -> rx.Component:
    return rx.container(
        rx.vstack(
            # Header Section
            rx.heading("Stallon Fernandes", size="9"),
            rx.text("AI & Machine Learning Engineer", size="5", color="gray"),
            rx.divider(margin_y="4"),
            
            # Projects Section
            rx.heading("Featured Projects", size="6"),
            rx.text("• Sympto Medical Diagnosis Assistant"),
            rx.text("• TfL Knowledge Graph Architecture"),
            
            spacing="4",
            align_items="start",
            padding="2rem",
        ),
        max_width="800px",
        margin="auto",
    )

# Explicitly disable state for static GitHub Pages deployment
app = rx.App(enable_state=False)
app.add_page(index)