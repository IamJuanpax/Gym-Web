import reflex as rx
from Web_StarGym.styles.colors import Color
from Web_StarGym.styles import styles
from Web_StarGym.styles.styles import Size
from Web_StarGym.components.navbar_button import navbar_button


def navbar() -> rx.Component:
    return rx.hstack(
        rx.image(
            src="logo_navbar.png",
            width="200px",
        ),
        navbar_button("Productos", "https://tiktok.com"),
        navbar_button("Culturistas", "https://tiktok.com"),
        navbar_button("Comunidad", "https://tiktok.com"),
        navbar_button("Contactanos", "https://tiktok.com"),
        style=styles.navbar_style
    )