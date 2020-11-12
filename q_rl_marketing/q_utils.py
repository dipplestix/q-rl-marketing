import base64
import pandas as pd
import random
from pathlib import Path

from h2o_wave import Q, ui


async def drop_cards(q: Q, card_names: list):
    """
    Drop cards from Q page.
    """
    for card_name in card_names:
        del q.page[card_name]

    await q.page.save()


async def save_df_as_csv(df: pd.DataFrame, path: Path):
    """
    Write a dataframe to disk as csv.
    """
    df.to_csv(path, index=False)


def choices_from_list(ls: list) -> list:
    """
    List of values as list of Q ui.choice.
    """
    return [ui.choice(name=str(x), label=str(x)) for x in ls]


def column_choices_from_df(df: pd.DataFrame) -> list:
    """
    List of dataframe columns as list of Q ui.choice.
    """
    return [ui.choice(name=str(x), label=str(x)) for x in df.columns.values]


def image_card_from_image(path_image: Path, box: str, title: str, image_type: str = 'png') -> ui.image_card:
    """
    Putting an image into Q ui.image_card.
    """
    with open(Path(path_image), 'rb') as file_image:
        base64_encoded_string = base64.b64encode(file_image.read()).decode('utf8')

    card = ui.image_card(
        box=box,
        title=title,
        type=image_type,
        image=base64_encoded_string,
    )

    return card


def ui_table_from_df(
    df: pd.DataFrame,
    name: str = '',
    sortables: list = None,
    filterables: list = None,
    searchables: list = None,
    min_widths: dict = None,
    max_widths: dict = None,
    multiple: bool = False,
    link_col: str = None,
    height: str = '500px'
) -> ui.table:
    """
    Convert a dataframe into Q ui.table format.
    """
    if not sortables:
        sortables = []
    if not filterables:
        filterables = []
    if not searchables:
        searchables = []
    if not min_widths:
        min_widths = {}
    if not max_widths:
        max_widths = {}

    columns = [ui.table_column(
        name=str(x),
        label=str(x),
        sortable=True if x in sortables else False,
        filterable=True if x in filterables else False,
        searchable=True if x in searchables else False,
        min_width=min_widths[x] if x in min_widths.keys() else None,
        max_width=max_widths[x] if x in max_widths.keys() else None,
        link=True if x == link_col else False
    ) for x in df.columns.values]

    try:
        table = ui.table(
            name=name,
            columns=columns,
            rows=[
                ui.table_row(
                    name=str(i),
                    cells=[str(df[col].values[i]) for col in df.columns.values]
                ) for i in range(df.shape[0])
            ],
            multiple=multiple,
            height=height
        )
    except Exception:
        table = ui.table(
            name=name,
            columns=[ui.table_column('x', 'x')],
            rows=[ui.table_row(name='ndf', cells=[str('No data found')])]
        )

    return table


def dai_name() -> str:
    """
    Generate default name based on DriverlessAI's funny_name.
    """
    return ''.join([random.choice('aeiou' if i % 2 else 'bcdfghklmnprstvw') for i in range(8)])