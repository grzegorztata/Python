import pandas as pd

data = pd.read_html('https://pl.wikipedia.org/wiki/Miasta_w_Polsce', header=0)

# Pierwsza tabela (pod względem liczby ludności)
print(data[0])

# Druga tabela (pod względem powierzchni)
print(data[1])