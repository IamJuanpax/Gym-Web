import reflex as rx
from Web_StarGym.styles.styles import Size, Image_Size
from Web_StarGym.styles.colors import Color

def sponsors() -> rx.Component:
    return rx.vstack(
            rx.image(
                src="patrocinio1.jpg",
                height=Image_Size.SOPONSORS.value
            ),
            rx.image(
                src="patrocinio2.jpg",
                height=Image_Size.SOPONSORS.value
            ),
        width="100%",
        bg=Color.SECONDARY.value,
        margin_top = Size.BIG.value
    )