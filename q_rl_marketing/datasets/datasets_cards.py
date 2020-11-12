from q_rl_marketing.config import *
from q_rl_marketing.q_utils import *
import pandas as pd


def card_people(df: pd.DataFrame) -> ui.FormCard:
    card = ui.form_card(
        box=box_main,
        items=[
            ui_table_from_df(df)
        ]
    )

    return card
