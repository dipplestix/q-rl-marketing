from h2o_wave import listen
from q_rl_marketing.run import main

print('----------------------------------------')
print(' Welcome to the H2O wave rl-marketing App!')
print('')
print(' Go to http://localhost:55555/')
print('----------------------------------------')

if __name__  == "__main__":
	listen('/', main)

