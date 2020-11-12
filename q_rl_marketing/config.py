from pathlib import Path


box_title = '1 1 2 1'
box_nav_bar = '3 1 6 1'
box_sidebar = '1 2 2 7'
box_main = '3 2 6 7'

droppable_cards = [
    'people',
    'error',
    'reward',
    'finished',
    'assignment_table',
    'assignments',
    'add_people'
]

companies = [
    'Aisin Seiki Co., Ltd.',
    'Ascend Learning',
        # 'Banco Votorantim',
        # 'Bloomingdale\'s',
        # 'CEZ',
        # 'Commonwealth Bank of Australia',
        # 'Coca-Cola Bottlers Japan',
        # 'Mututal Fintech',
        # 'TARJETA NARANJA S.A.',
        # 'Underwrite.ai'
]

marketing_options = [
    'Send Newsletter',
    'Send email invite to upcoming webinar',
    'Add to email Nurture campaigns',
    'Invite to Driverless AI free trial',
    'Send email with Analyst Report',
    'None'
]

reward_options = [
    'Started DAI trial',
    'Attended Webinar',
    'Opened e-mail'
]

rewards = {
    'Started DAI trial': 20,
    'Attended Webinar': 10,
    'Opened e-mail': 5
}

path_data = Path('data')
