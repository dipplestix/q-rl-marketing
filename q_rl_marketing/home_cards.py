from h2o_wave import Q, ui
from q_rl_marketing.config import *


def card_title() -> ui.HeaderCard:
    """
    Card for title.
    """
    card = ui.header_card(
        box=box_title,
        title='RL Marketing',
        subtitle='Targeted Marketing Solution',
        icon='Telemarketer',
        icon_color='$blue'
    )

    return card


def card_navbar() -> ui.TabCard:
    """
    Card for top navigation bar.
    """
    card = ui.tab_card(
        box=box_nav_bar,
        items=[
            ui.tab(name='#home', label='Home'),
            ui.tab(name='#data', label='People')
        ]
    )

    return card


def card_meta() -> ui.MetaCard:
    """
    Card for meta information.
    """
    card = ui.meta_card(
        box='',
        title='RL Marketing'
    )

    return card


def card_home() -> ui.FormCard:
    """
    Card for home.
    """

    card = ui.form_card(
        box=box_main,
        items=[
            ui.text_xl('Welcome to the RL Marketing App!'),
            ui.text('<img src="https://www.envision-creative.com/wp-content/uploads/2020/'
                    '07/Envision-blog-what-is-marketing-01-00_Header-scaled.jpg" width="850">')
        ]
    )

    return card


def card_sidebar() -> ui.NavCard:
    """
    Card for demo.
    """
    item_list = [
        ui.nav_group('Functions', items=[
            ui.nav_item(name='assign', label='Assign next action'),
            ui.nav_item(name='record', label='Record results'),
            ui.nav_item(name='add_people', label='Add people')
            ])
    ]
    card = ui.nav_card(
        box=box_sidebar,
        items=item_list
    )

    return card
