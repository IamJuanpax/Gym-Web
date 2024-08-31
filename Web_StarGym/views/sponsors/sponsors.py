import reflex as rx
from Web_StarGym.styles.styles import Size, Image_Size
from Web_StarGym.styles.colors import Color
from Web_StarGym.views import constants as cs

def sponsors() -> rx.Component:
    return rx.vstack(
        rx.link(
            rx.image(
                src="patrocinio1.jpg",
                height=Image_Size.SOPONSORS.value,
            ),
            href=cs.FACEBOOK_URL, 
            is_external=True, 
        ),
        rx.link(
            rx.image(
                src="patrocinio2.jpg",
                height=Image_Size.SOPONSORS.value,
            ),
            href=cs.FACEBOOK_URL,
            is_external=True, 
        ),
        width="100%",
        #bg=Color.SECONDARY.value,           Esto esta solo para ver el contorno del contenedor
        margin_top=Size.BIG.value,
        spacing=Size.LARGE.value
    )
