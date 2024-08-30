import reflex as rx
from Web_StarGym.styles.styles import Size
from Web_StarGym.styles import styles

# Boton personalizado
def link_button(title: str, image: str, url: str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.image(
                    src=image,
                    width=Size.BIG.value,  # Ajusta el tamaño de la imagen
                    height=Size.BIG.value,  # Ajusta el tamaño de la imagen
                    alt=title
                ),
                rx.vstack(
                    rx.text(title, style=styles.button_title_style),
                    align_items="start",
                    spacing="0px",
                    width="100%"  # Ajusta el ancho del contenido del botón
                ),
                align_items="center",
            ),
            style= styles.link_button_style
        ),
        href=url,
        is_external=True,
        width="auto",  # Ajusta el ancho del enlace al tamaño del botón
        style={"display": "inline-block"},  # Asegura que el enlace se ajuste al tamaño del botón
    )

