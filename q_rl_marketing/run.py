from q_rl_marketing.home_funcs import *
from q_rl_marketing.datasets.dataset_funcs import *
from q_rl_marketing.assign.assign_funcs import *
from q_rl_marketing.record.record_funcs import *


async def main(q: Q):
    """
    This file only contains information for the control flow of the app. All cards and functions defined in their own
    files
    """

    # Initialize the app
    if not q.client.app_initialized:
        await initialize_app(q)
        q.client.app_initialized = True
        await setup_home(q)

    # Return to home
    elif q.args.go_home:
        await setup_home(q)

    # navigation tabs
    elif q.args['#']:
        tab = q.args['#']
        if tab == 'home':
            await setup_home(q)
        elif tab == 'data':
            await view_people(q)

    elif q.args.assign:
        await assign(q)

    elif q.args.begin_assignment:
        await begin_assignment(q)

    elif q.args.dl_frame:
        await dl_frame(q)

    elif q.args.record:
        await record(q)

    elif q.args.submit_rewards:
        await submit_rewards(q)

    elif q.args.add_people:
        await add_people(q)

    elif q.args.add_company:
        await add_company(q)
