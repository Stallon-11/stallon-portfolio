import reflex as rx
import json
import os

# Dynamically load the JSON data
DATA_PATH = os.path.join(os.getcwd(), "data", "aboutme.json")
with open(DATA_PATH, "r", encoding="utf-8") as f:
    ABOUT_DATA = json.load(f)

def about_me_section() -> rx.Component:
    return rx.vstack(
        rx.box(
            rx.hstack(
                rx.vstack(
                    rx.heading(ABOUT_DATA["name"], size="9", color="#1D1D1F", font_weight="600"),
                    rx.text(ABOUT_DATA["title"], size="6", color="#86868B", font_weight="400"),
                    align_items="start", spacing="2",
                ),
                rx.center(
                    rx.icon("image", size=40, color="#86868B"),
                    width="200px", height="200px", background_color="#E5E5EA", border_radius="1rem",
                ),
                justify="between", align_items="center",
                width="100%", max_width="1000px", margin="auto", padding_x="2rem",
            ),
            width="100vw", background_color="#F5F5F7", padding_y="6rem", margin_bottom="4rem",
        ),
        rx.box(
            rx.flex(
                # Pulling from the JSON array
                rx.text(ABOUT_DATA["paragraphs"][0], color="#1D1D1F", size="4", line_height="1.6", flex="1"),
                rx.text(ABOUT_DATA["paragraphs"][1], color="#1D1D1F", size="4", line_height="1.6", flex="1"),
                direction={"initial": "column", "md": "row"}, spacing="8", 
                width="100%", max_width="1000px", margin="auto", padding_x="2rem",
            ),
            width="100%",
        ),
        id="section-0", class_name="scroll-section", min_height="100vh", width="100%", align_items="center",
    )

def standard_section(index: int, title: str, content: rx.Component) -> rx.Component:
    return rx.vstack(
        rx.heading(title, size="8", color="#1D1D1F", margin_bottom="2rem"),
        content,
        id=f"section-{index}", class_name="scroll-section", min_height="100vh", 
        width="100%", max_width="1000px", padding_top="8rem", padding_x="2rem", align_items="start",
    )