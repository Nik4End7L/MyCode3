import flet as ft


def main(page: ft.Page):
    page.title = 'My first app on flet.'
    greeting_text = ft.Text('Hello Flet!')
    name_input = ft.TextField(label = 'Write Your Name: ')

    page.add(greeting_text, name_input)



ft.app(target = main)



