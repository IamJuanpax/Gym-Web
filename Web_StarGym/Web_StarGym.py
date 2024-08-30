import reflex as rx
from Web_StarGym.components.navbar import navbar
from Web_StarGym.components.footer import footer
from Web_StarGym.components.body import body
from Web_StarGym.views.header.header import header
from Web_StarGym.views.links.links import links
from Web_StarGym.views.sponsors.sponsors import sponsors
from Web_StarGym.styles import styles
from Web_StarGym.styles.styles import Size

from rxconfig import config

class State(rx.State):
    """The app state."""
    ...

def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.vstack(
        navbar(),
        rx.hstack(
            rx.box(
                rx.center(
                    rx.vstack(
                        header(),
                        body(),
                        links(),
                        footer(),
                        max_width=styles.MAX_WIDTH,
                        width="80%",
                        margin_y=Size.DEFAULT.value,
                        padding=Size.BIG.value,
                        spacing=Size.BIG.value
                    )
                ),
                width="80%"  # Ajusta el ancho del contenedor principal
            ),
            rx.box(
                sponsors(),
                width="20%",  # Ajusta el ancho del contenedor de sponsors2
                padding=Size.DEFAULT.value  # Añade padding si es necesario
            ),
            width="100%"  # Asegura que el hstack ocupe todo el ancho disponible
        ),
        spacing="2px"
    )

app = rx.App(
    stylesheets=styles.STYLESHEETSS,
    style=styles.BASE_STYLE
)
app.add_page(
    index,
    title="Star Gym"
)
