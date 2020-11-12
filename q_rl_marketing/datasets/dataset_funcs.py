from h2o_wave import Q
from q_rl_marketing.config import *
from q_rl_marketing.datasets.datasets_cards import *


async def view_people(q: Q):
    await drop_cards(q, card_names=droppable_cards)
    col_names = ['cid', 'Name', 'Title', 'Company', 'Newsletters', 'Webinar Invites', 'DAI Invitations',
                 'Nurture Subscribed', 'Analyst Reports', 'Emails Opened', 'Webinars Attended', 'DAI User']
    data = []
    for person in q.client.people:
        row = [person.cid, person.name, person.title, person.company, person.newsletters, person.webinars_invited,
               person.dai_invites, person.nurture, person.reports, person.emails_opened, person.webinars_attended,
               person.dai_user]
        data.append(row)
    df = pd.DataFrame(data, columns=col_names)
    q.page['people'] = card_people(df)
    await q.page.save()
