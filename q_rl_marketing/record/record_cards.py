from q_rl_marketing.config import *
from q_rl_marketing.q_utils import *


def card_options(people) -> ui.FormCard:
    """
    Card to pick which options are available.
    """
    text = ui.text('Record the result for each person')
    choices = choices_from_list(reward_options)
    button = ui.button(name='submit_rewards', label='Log Results', primary=True)
    checklists = []
    for person in people:
        checklists.append(ui.checklist(name=person.cid, choices=choices, label=person.name))
    item_list = [text]
    item_list.extend(checklists)
    item_list.append(button)
    card = ui.form_card(
        box=box_sidebar,
        items=item_list
    )

    return card


def card_error() -> ui.FormCard:
    card = ui.form_card(
        box=box_main,
        items=[
            ui.text('Must choose assignments before logging rewards')
        ]
    )

    return card


def card_complete() -> ui.FormCard:
    card = ui.form_card(
        box=box_main,
        items=[
            ui.text('Assignment complete and policy updated. Please e-mail the updated version of data/marketing.pkl to'
                    ' chris.mascioli@h2o.ai'),
            ui.button(name='go_home', label='Return Home', primary=True)
        ]
    )

    return card
