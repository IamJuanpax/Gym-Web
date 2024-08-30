import reflex as rx
from Web_StarGym.styles.styles import Size
from Web_StarGym.styles import styles
from Web_StarGym.styles.colors import Color, Color_Text

# Botón personalizado
def navbar_button(title: str, url: str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.vstack(
                rx.text(title, style=styles.button_title_style),
                align_items="start",
                spacing="10px",
                _hover={"text_decoration": "underline"}  # Subraya el texto al pasar el cursor
            ),
            style=styles.navbar_button_style
        ),
        href=url,
        is_external=True,
        width="auto",  # Ajusta el ancho del enlace al tamaño del botón
        style={"display": "inline-block"},  # Asegura que el enlace se ajuste al tamaño del botón
    )


