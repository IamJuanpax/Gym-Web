import reflex as rx
from Web_StarGym.styles.styles import Size, Image_Size
from Web_StarGym.styles.colors import Color
from Web_StarGym.components.title import start_title, end_title, center_title

def body() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.image(
                src="hombre_entrenando.jpg",
                height=Image_Size.STANDAR.value
            ),
            rx.vstack(
                start_title("Equipamiento de Vanguardia:"),
                rx.text(
                    f"""
                    En Star Gym, contamos con una amplia
                    gama de máquinas de última generación, diseñadas para maximizar tu 
                    rendimiento. Desde cintas de correr hasta equipos de musculación, cada 
                    máquina está pensada para ofrecerte la mejor experiencia de entrenamiento
                    posible, ayudándote a alcanzar tus objetivos de forma segura y eficiente.
                    """
                )
            ),
            spacing=Size.SMALL.value,
            align_items="center",
            justify_content="center",  # Asegura que el contenido del hstack esté centrado
            width="100%",  # Ajusta el ancho del hstack
            border_radius="10px",
            padding=Size.DEFAULT.value
        ),
        rx.hstack(
            rx.vstack(
                end_title("Entrenamientos Transformadores:"),
                rx.text(
                    f"""
                    En Star Gym, te ofrecemos una variedad 
                    de rutinas de ejercicios diseñadas específicamente para generar un cambio 
                    físico real. Desde circuitos de alta intensidad hasta entrenamientos de fuerza 
                    personalizados, cada sesión está enfocada en esculpir tu cuerpo, mejorar tu 
                    resistencia, y llevarte un paso más cerca de la mejor versión de ti mismo. 
                    Con la guía de nuestros entrenadores expertos, cada ejercicio se convierte en
                    un paso firme hacia tu transformación física.
                    """
                ),
                width="100%",
            ),
            rx.image(
                src="mujer_gym.jpg",
                height=Image_Size.STANDAR.value
            ),
            spacing=Size.BIG.value,
            align_items="center",
            justify_content="center",  # Asegura que el contenido del hstack esté centrado
            width="100%",  # Ajusta el ancho del hstack
            border_radius="10px",
            padding=Size.DEFAULT.value
        ),
        rx.hstack(
            rx.image(
                src="cbum.jpg",
                height=Image_Size.STANDAR.value
            ),
            rx.vstack(
                rx.text("• El único límite es el que tú te impones, ¡Rompe barreras y crea tu mejor versión!"),
                rx.text("• Cada repetición cuenta, cada esfuerzo te acerca a tu meta"),
                rx.text("• No se trata de ser el mejor, sino de ser mejor que ayer"),
                rx.text("• No esperes a que sea fácil, lucha para que valga la pena"),
                rx.text("• El cambio comienza cuando decides dar el primer paso"),
                width="100%"
            ),
            spacing=Size.SMALL.value,
            align_items="center",
            justify_content="center",  # Asegura que el contenido del hstack esté centrado
            width="100%",  # Ajusta el ancho del hstack
            border_radius="10px",
            padding=Size.DEFAULT.value
        ),
        width="100%",  # Asegura que el vstack ocupe todo el ancho disponible
        margin_top=Size.SMALL.value,
        bg=Color.SECONDARY.value,
        align_items="center",  # Alinea los hstack al centro del vstack
        justify_content="center",  # Asegura que el contenido del vstack esté centrado
        border_radius="10px",  # Redondea los bordes del vstack
        padding=Size.DEFAULT.value
    )
