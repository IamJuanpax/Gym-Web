import reflex as rx
from Web_StarGym.components.link_button import link_button
from Web_StarGym.components.title import start_title, center_title, end_title
from Web_StarGym.styles.colors import Color
from Web_StarGym.styles.styles import Size

def links() -> rx.Component:
    return rx.vstack(
            rx.vstack(
                center_title("Seguinos en nuestras redes"),
                align_items="center",  # Centra el contenido horizontalmente
                width="100%",
            ),
            rx.hstack(
                link_button("Instagram",
                            "icons/instagram.svg",
                            "https://instagram.com"),

                link_button("Twitter",
                            "icons/twitter.svg",
                            "https://twitter.com"),

                spacing="10px",        # Espaciado entre botones
                width="100%",
                justify_content="center",
            ),
            rx.vstack(
                center_title("Segui a nuestros entrenadores"),
                align_items="center",  # Centra el contenido horizontalmente
                width="100%",
            ),
            rx.hstack(
                link_button("Sergio Ledesma",
                            "icons/instagram.svg",
                            "https://instagram.com"),

                link_button("Cesar Ledesma",
                            "icons/instagram.svg",
                            "https://twitter.com"),

                link_button("Roberto Ledesma",
                            "icons/instagram.svg",
                            "https://twitter.com"),

                spacing="10px",        # Espaciado entre botones
                width="100%",
                justify_content="center",
            ),
        width="100%",
        bg=Color.SECONDARY.value,
        align_items="center",
        padding=Size.DEFAULT.value,
        border_radius="10px"
    )
