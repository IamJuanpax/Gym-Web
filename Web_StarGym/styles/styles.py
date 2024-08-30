import reflex as rx
from enum import Enum
from .colors import Color, Color_Text
from .fonts import Font, FontWeight

# Constants
MAX_WIDTH = "1920px"

# Ponemos los estilos de fuente de texto
STYLESHEETSS = [
    "https://fonts.googleapis.com/css?family=Poppins:wght@300;500&display=swap"
]

# Sizes
class Size(Enum):
    SMALL = "0.5em"
    MEDIUM = "0.8em"
    DEFAULT = "1em"
    LARGE = "1.5em"
    BIG = "2em"
    VERY_BIG = "4em"

class Image_Size(Enum):
    SOPONSORS = "400px"
    STANDAR = "200px"
    FOOTER = "50px"
    HEADER = "25px"



# Style
BASE_STYLE={
    "font_family":Font.DEFAULT.value,
    "font_weight": FontWeight.LIGHT.value,
    "background_color":Color.BACKGROUND.value,
    #"background_image": "url(logo_provisional.jpg)",  # Aquí se define la imagen de fondo
    #"background_size": "cover",  # Asegura que la imagen cubra todo el fondo
    #"background_repeat": "no-repeat",  # Evita que la imagen se repita
    #"background_position": "center center",  # Centra la imagen
    
}

button_title_style = dict(
    font_size=Size.DEFAULT.value,
    color=Color_Text.HEADER.value,
    font_family=Font.TITLE.value,
    font_weight= FontWeight.MEDIUM.value
)


footer_style = dict(
    width=Size.DEFAULT.value,  # Ancho de la imagen
    height=Size.DEFAULT.value,  # Altura de la imagen
    margin_bottom=Size.MEDIUM.value,
    font_family=Font.DEFAULT.value
)

navbar_style = dict(
    width="100%",
    height="auto",
    position="sticky",
    bg=Color.PRIMARY.value,               # Color de fondo del navbar
    padding_x=Size.BIG.value,
    padding_y=Size.DEFAULT.value,
    z_index="999",
    top="0",
    spacing="50px",
    align_items="center"
)

navbar_button_style = dict(
    width="auto",  # Ajusta el ancho del botón al tamaño de su contenido
    align_items="center",
    justify_content="start",
    padding_x=Size.SMALL.value,  # Reduce el padding horizontal
    padding_y=Size.SMALL.value,  # Reduce el padding vertical
    bg=Color.PRIMARY.value,
    _hover={"background_color": Color_Text.LINKS.value},  # Cambia el color de fondo al pasar el cursor
    radius="full"
)

footer_style = dict(
    width="100%",
    height=Image_Size.FOOTER.value,  # Aquí ajustas la altura del footer
    margin_top=Size.SMALL.value,
    bg=Color.PRIMARY.value,
    align_items="center",
    justify_content="center"
)

header_style = dict(
    width="100%",
    margin_top=Size.SMALL.value,
    bg=Color.SECONDARY.value,
    justify_content="center",
    align_items="center",
    text_align="center",
    padding=Size.DEFAULT.value,
    border_radius="10px"
)

link_button_style = dict(
    justify_content="start",
    width="auto",  # Ajusta el ancho del botón al tamaño de su contenido
    padding_x=Size.SMALL.value,  # Reduce el padding horizontal
    padding_y=Size.SMALL.value,  # Reduce el padding vertical
    bg=Color.PRIMARY.value
)