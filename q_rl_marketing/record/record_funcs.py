from q_rl_marketing.record.record_cards import *
import pandas as pd
from q_rl_marketing.q_utils import *
import pickle


async def record(q: Q):
    await drop_cards(q, card_names=droppable_cards)
    if q.client.pos != 'reward':
        q.page['error'] = card_error()
    else:
        q.page['reward'] = card_options(q.client.people)
    await q.page.save()


async def submit_rewards(q: Q):
    for person in q.client.people:
        last_action = person.actions[-1]
        if last_action == 'None':
            reward = 0
        else:
            reward = -1
        results = getattr(q.args, str(person.cid))
        person.log(results)
        for result in results:
            reward += rewards[result]
        q.client.ql.update(s=person.state, a=person.actions[-1], s_=person.get_state(), r=reward)
        person.state = person.get_state()
    q.client.ql.update_policy()
    q.page['finished'] = card_complete()
    del q.page['reward']
    await q.page.save()

    path = path_data
    file_name = 'marketing.pkl'
    output = open(path/file_name, 'wb')
    pickle.dump([q.client.people, q.client.ql, 'reward'], output)
    q.client.pos = 'assignment'
