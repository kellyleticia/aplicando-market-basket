import csv
import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

with open('matriz_por_tag.csv', 'r') as f:
    reader = csv.reader(f)
    dataset = list(reader)

te = TransactionEncoder()
te_ary = te.fit(dataset).transform(dataset)
df = pd.DataFrame(te_ary, columns=te.columns_)

freq_itemsets = apriori(df, min_support=0.001, use_colnames=True)

rules = association_rules(freq_itemsets, metric="lift", min_threshold=1)
rules.to_csv('teste.csv', index=False)
print(rules)

basket = ['back-end']

rules_filtered = rules[rules['antecedents'].apply(lambda x: set(basket).issubset(set(x)))]

rules_filtered = rules_filtered.sort_values(by='lift', ascending=False)

print(rules_filtered.head(5))