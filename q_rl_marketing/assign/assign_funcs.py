from q_rl_marketing.assign.assign_cards import *
import pandas as pd
from q_rl_marketing.q_utils import *
import pickle
from q_rl_marketing.rl_funcs.classes import Person


async def assign(q: Q):
    await drop_cards(q, card_names=droppable_cards)
    if q.client.pos != 'assignment':
        q.page['error'] = card_error()
        try:
            q.page['assignment_table'] = card_assignment_table(q.client.pdf)
        except:
            pass
    else:
        q.page['assignments'] = card_options()
    await q.page.save()


async def begin_assignment(q: Q):
    df = []
    col_names = ['Name', 'Action']
    for person in q.client.people:
        action = q.client.ql.get_action(person.state, q.args.choices)
        person.action(action)
        df.append([person.name, action])
    pdf = pd.DataFrame(df, columns=col_names)
    q.client.pdf = pdf
    q.page['assignment_table'] = card_assignment_table(pdf)
    del q.page['assignments']
    await q.page.save()
    path = path_data
    file_name = 'marketing.pkl'
    output = open(path/file_name, 'wb')
    pickle.dump([q.client.people, q.client.ql, 'reward'], output)
    q.client.pos = 'reward'


async def dl_frame(q: Q):
    out = path_data/'out.csv'
    q.client.pdf.to_csv(out)


async def add_people(q: Q):
    await drop_cards(q, card_names=droppable_cards)

    await drop_cards(q, card_names=droppable_cards)
    if q.client.pos != 'assignment':
        q.page['error'] = card_error_add()
    else:
        q.page['add_people'] = card_add()
    await q.page.save()


async def add_company(q: Q):
    df = pd.read_csv(path_data/'All_People.csv')
    dfc = df[df['Company Name'] == q.args.company]
    for index, row in dfc.iterrows():
        q.client.people.append(Person(
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
    path = path_data
    file_name = 'marketing.pkl'
    output = open(path/file_name, 'wb')
    pickle.dump([q.client.people, q.client.ql, 'reward'], output)
    q.page['add_people'] = card_added(q)
    await q.page.save()
