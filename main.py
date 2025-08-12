import flet as ft
from datetime import datetime

def main(page: ft.Page):
    page.title = "Моё первое приложение"
    
    def get_greeting(name):
        now = datetime.now()
        h = now.hour
        
        if 6 <= h < 12:
            return f"Доброе утро, {name}!"
        elif 12 <= h < 18:
            return f"Добрый день, {name}!"
        elif 18 <= h < 24:
            return f"Добрый вечер, {name}!"
        else:
            return f"Доброй ночи, {name}!"

    name_field = ft.TextField(
        label="Введите ваше имя:",
    )
    
    greeting_text = ft.Text("Введите ваше имя", size=24, weight="bold")
    
    history_col = ft.Column(scroll="auto", expand=True)
    
    def remove_item(item_to_rem):
        history_col.controls.remove(item_to_rem)
        page.update()

    def update_greeting(e):
        name = name_field.value
        if not name:
            return
        
        greeting = get_greeting(name)
        greeting_text.value = greeting
        
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        hist_item = ft.Row(
            controls=[
                ft.Text(f"{now}: {name}", expand=True),
                ft.IconButton(
                    icon="delete",
                    on_click=lambda e: remove_item(hist_item)
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        )

        history_col.controls.insert(0, hist_item)
        
        page.update()

    def clear_history(e):
        history_col.controls.clear()
        page.update()

    name_field.on_submit = update_greeting
    
    page.add(
        ft.Row(
            controls=[
                ft.TextButton("Очистить историю", on_click=clear_history),
                ft.IconButton(icon="delete", on_click=clear_history),
            ],
            alignment=ft.MainAxisAlignment.END
        ),
        greeting_text,
        name_field,
        ft.ElevatedButton("Поздороваться снова", on_click=update_greeting),
        ft.Text("История приветствий:"),
        ft.Divider(),
        history_col
    )

if __name__ == "__main__":
    ft.app(target=main, view=ft.WEB_BROWSER)
