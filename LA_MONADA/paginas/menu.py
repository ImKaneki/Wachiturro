import reflex as rx

class State(rx.State):
    text: str = "pc store"

@rx.page(route="/menu")
def menu()->rx.Component:
    return rx.vstack(
        rx.heading("pc store"),
        rx.input(
            rx.input.slot(
                rx.icon(tag="search"),
            ),
            placeholder="Search here...",
        ), 
        rx.hstack(
            rx.menu.root(
                rx.menu.trigger(
                    rx.button("CATEGORIAS")
                ),
                rx.menu.content(
                rx.menu.item("Gamer"),
                rx.menu.item("Escritorio"),
                rx.menu.item("Notebook"),
                rx.menu.item("Netbooks"),
                rx.menu.item("Laptop"),
                
                ),
               
            ), 
            rx.menu.root(
                rx.menu.trigger(
                    rx.button("Calidad")
                ),
                rx.menu.content(
                rx.menu.item("A"),
                rx.menu.item("B"),
                rx.menu.item("C"),
                rx.menu.item("D"),
                
                ),
               
            ),  
            rx.menu.root(
                rx.menu.trigger(
                    rx.button("Componentes")
                ),
                rx.menu.content(
                rx.menu.item("Teclado"),
                rx.menu.item("Mouse"),
                rx.menu.item("Parlante"),
                rx.menu.item("Audifono"),
                rx.menu.item("Camara Web"),
                rx.menu.item("Monitor"),

                ),
               
            ), 
            rx.menu.root(
                rx.menu.trigger(
                    rx.button("PRECIO")
                ),
                rx.menu.content(
                rx.menu.item("S/50"),
                rx.menu.item("S/25"),
                rx.menu.item("S/40"),
                rx.menu.item("S/25"),
                rx.menu.item("S/60"),
                rx.menu.item("S/100"),

                ),
               
            ),
        ),
        rx.flex(
            rx.card(
                rx.image(src="https://i.blogs.es/ed843e/superpc-ap/450_1000.jpeg"),
                rx.text("Pc Gamer "), 
                size="5",
                width="45%"
            ),
            rx.card(
                rx.image(src="https://shersboutique.com/wp-content/uploads/2024/07/m.jpeg"),
                rx.text("vestido de encaje S/88"), 
                size="5",
                width="45%"
            ),
             rx.card(
                rx.image(src="https://dvicioshop.com/cdn/shop/files/WhatsAppImage2024-04-27at15.45.50_1_1.jpg?v=1714257038&width=1080"),
                rx.text("vestido romantico S/150"), 
                size="5",
                width="45%"
            ),
             rx.card(
                rx.image(src="https://i.pinimg.com/736x/08/67/64/086764ac4bd6926d4d58b8119156f09f.jpg"),
                rx.text("vestido corto S/100"), 
                size="5",
                width="45%"
            ),
            spacing="2",
            align_items="flex-start",
            flex_wrap="wrap",
        )
        
    ),