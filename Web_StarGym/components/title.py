import reflex as rx
from Web_StarGym.styles import styles
from Web_StarGym.styles.fonts import FontWeight

def start_title(text: str)  -> rx.Component:
    return rx.heading(
        text,
        size="lg",
        font_size="2xl",
        font_weight=FontWeight.MEDIUM.value,
        text_align="start",
        width="100%"
    )

def center_title(text: str) -> rx.Component:
    return rx.heading(
        text,
        size="lg",
        font_size="2xl",
        font_weight=FontWeight.MEDIUM.value,
        text_align="center",
        width="100%"
    )

def end_title(text: str) -> rx.Component:
    return rx.heading(
        text,
        size="lg",
        font_size="2xl",
        font_weight=FontWeight.MEDIUM.value,
        text_align="end",
        width="100%",
    )