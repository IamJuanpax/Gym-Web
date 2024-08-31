import reflex as rx
from Web_StarGym.styles.colors import Color
from Web_StarGym.styles import styles
from Web_StarGym.styles.styles import Size
from Web_StarGym.components.navbar_button import navbar_button
from Web_StarGym.views import constants as cs


def navbar() -> rx.Component:
    return rx.hstack(
        rx.image(
            src="logo_navbar.png",
            width="200px",
        ),
        navbar_button("Productos", cs.YOUTUBE_URL),
        navbar_button("Culturistas", cs.YOUTUBE_URL),
        navbar_button("Comunidad", cs.YOUTUBE_URL),
        navbar_button("Contactanos", cs.YOUTUBE_URL),
        style=styles.navbar_style
    )