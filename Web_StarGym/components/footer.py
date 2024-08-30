import reflex as rx
from Web_StarGym.styles.styles import Size, Image_Size
from Web_StarGym.styles.colors import Color
from Web_StarGym.styles import styles

def footer() -> rx.Component:
    return rx.hstack(
        rx.text(
            f"Star Gym es un espacio seguro para entrenar y ponerse al dia",
        ),
        style=styles.footer_style,
    )