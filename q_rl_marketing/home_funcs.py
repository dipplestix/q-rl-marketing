import q_rl_marketing.home_cards as home_cards
from q_rl_marketing.config import *
import q_rl_marketing.q_utils as q_utils
from q_rl_marketing.rl_funcs.qlearn import QLearn
from h2o_wave import Q, ui
import os.path
from q_rl_marketing.rl_funcs.classes import *
import pandas as pd
import pickle
import time


async def initialize_app(q: Q):
    """
    Initialize app.
    """
    path = path_data
    file_name = 'marketing.pkl'
    out_file = path/file_name
    if not os.path.exists(out_file):
        df = pd.read_csv(path_data/'All_People.csv')
        people = []
        for company in companies:
            dfc = df[df['Company Name'] == company]
            for index, row in dfc.iterrows():
                people.append(Person(
                    cid=row['Id'],
                    status=row['Status'],
                    name=row['Full Name'],
                    title=row['Job Title'],
                    company=row['Company Name'],
                    email=row['Email Address'],
                    phone=row['Phone Number'],
                    source=row['Person Source'],
                    last_contact=row['Last Interesting Moment Date'],
                ))
        ql = QLearn(actions=marketing_options)
        output = open(path/file_name, 'wb')
        pickle.dump([people, ql, 'assignment'], output)
        output.close()
    state = open(out_file, 'rb')
    q.client.people, q.client.ql, q.client.pos = pickle.load(state)
    q.page['meta'] = home_cards.card_meta()
    q.page['title'] = home_cards.card_title()
    q.page['navbar'] = home_cards.card_navbar()
    q.page['home'] = home_cards.card_home()
    q.page['side'] = home_cards.card_sidebar()
    await q.page.save()


async def setup_home(q: Q):
    """
    Setup home view.
    """
    q.page.drop()
    q.page['meta'] = home_cards.card_meta()
    q.page['title'] = home_cards.card_title()
    q.page['navbar'] = home_cards.card_navbar()
    q.page['home'] = home_cards.card_home()
    q.page['side'] = home_cards.card_sidebar()

    await q.page.save()
