import reflex as rx
from Web_StarGym.styles import styles
from Web_StarGym.styles.styles import Size
from Web_StarGym.styles.colors import Color, Color_Text
from Web_StarGym.styles.fonts import Font, FontWeight

def subtitle(text: str) -> rx.Component:
    return rx.text(
            text,
            size="lg",
            font_size="2.5em", 
            width= "100%",
            font_family=Font.TITLE.value,
            font_weight= FontWeight.LIGHT.value,
            padding_top=Size.SMALL.value,
            color=Color_Text.HEADER.value,
            text_align="center"  # Alinea el texto al centro
        ),
