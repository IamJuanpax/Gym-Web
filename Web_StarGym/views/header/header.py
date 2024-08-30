import reflex as rx
from Web_StarGym.styles.styles import Size, Image_Size
from Web_StarGym.styles.colors import Color
from Web_StarGym.styles import styles
from Web_StarGym.components.subtitle import subtitle
from Web_StarGym.components.title import start_title, center_title, end_title


def header() -> rx.Component:
    return rx.hstack(
        rx.vstack(
            subtitle("Bienvenidos a Star Gym"),
            center_title("Donde Tu Transformación Comienza"),
            rx.text(
                f"""
                    En Star Gym, creemos que el verdadero cambio empieza desde adentro.
                    Nuestro gimnasio está diseñado para ayudarte a alcanzar tus metas, 
                    sin importar tu nivel de experiencia. Ya sea que estés buscando mejorar 
                    tu fuerza, aumentar tu resistencia o simplemente mantenerte en forma, 
                    estamos aquí para guiarte en cada paso del camino. Únete a nuestra comunidad, 
                    donde el esfuerzo se convierte en resultados y cada entrenamiento te 
                    acerca más a la mejor versión de ti mismo.
                """,
                width="100%",
                text_align="center",
            )
        ),
        style=styles.header_style
    )