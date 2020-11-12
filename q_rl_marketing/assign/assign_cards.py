from h2o_wave import Q, ui
from q_rl_marketing.config import *
from q_rl_marketing.q_utils import *


def card_options() -> ui.FormCard:
    """
    Card to pick which options are available.
    """
    text = ui.text('Select the available options')
    choices = choices_from_list(marketing_options)
    button = ui.button(name='begin_assignment', label='Run Assignment', primary=True)
    card = ui.form_card(
        box=box_sidebar,
        items=[text, ui.checklist(name='choices', choices=choices), button]
    )

    return card


def card_assignment_table(df) -> ui.FormCard:
    card = ui.form_card(
        box=box_main,
        items=[
            ui_table_from_df(df),
            ui.button(name='dl_frame', label='Download Frame', primary=True)
        ]
    )

    return card


def card_error() -> ui.FormCard:
    card = ui.form_card(
        box=box_sidebar,
        items=[
            ui.text('Must assign rewards before assigning next action')
        ]
    )

    return card


def card_error_add() -> ui.FormCard:
    card = ui.form_card(
        box=box_sidebar,
        items=[
            ui.text('Must assign rewards before adding new people')
        ]
    )

    return card


def card_add() -> ui.FormCard:
    company = ui.textbox(name='company', label='Company Name', required=True)
    button = ui.button(name='add_company', label='Add Company', primary=True)
    card = ui.form_card(
        box=box_sidebar,
        items=[
            company, button
        ]
    )

    return card


def card_added(q: Q) -> ui.FormCard:
    card = ui.form_card(
        box=box_sidebar,
        items=[
            ui.text(f'{q.args.company} added')
        ]
    )

    return card
