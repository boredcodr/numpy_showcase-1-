import numpy as np

table = np.genfromtxt('spending_patterns_detailed.csv', delimiter=',', names=True, dtype=None, encoding='utf-8')

# first im creating single lined arrays for columns of interest
spent = table['Total_Spent']
methods = table['Payment_Method']
cats = table['Category']


# im creating multiple masks to isolate different payment methods
mask = (methods == 'Debit Card')
mask2 = (methods == 'Credit Card')
mask3 = (methods == 'Cash')
mask4 = (methods == 'Digital Wallet')

TotalDeC = spent[mask].sum()
TotalCC = spent[mask2].sum()
TotalCash = spent[mask3].sum()
TotalDig = spent[mask4].sum()

# im creating an array to store the total spending associated with each payment method
sumsarr = np.array([TotalCash, TotalDeC, TotalCC, TotalDig])

AvgDeC = spent[mask].mean()
AvgCC = spent[mask2].mean()
AvgCash = spent[mask3].mean()
AvgDig = spent[mask4].mean()

# im creating an array to store the average spending associated with each payment method
avgarr = np.array([AvgCash, AvgDeC, AvgCC, AvgDig])


# im finding the unique methods in methods so I can easily iterate through a forloop
diff_methods = np.unique(methods)
results = {}   # we'll store: results[payment_method] = (top_category, count)

for pm in diff_methods:
    # mask is True exactly where methods == this pm
    mask = (methods == pm)

    # cat_subset holds only the Category values for that pm
    cat_subset = cats[mask]

    # count how often each category appears
    labels, counts = np.unique(cat_subset, return_counts=True)
    #    labels[i] ↔ counts[i] gives the tally for that category

    # find which label has the highest count
    idx_max = np.argmax(counts)
    top_cat = labels[idx_max]
    top_count = counts[idx_max]

    # record it
    results[pm] = (top_cat, top_count)
    # this shows people are willing to make non-essential/personal purchases with digital wallets
for pm, (cat, cnt) in results.items():
    print(f"{pm:14s} → {cat} ({cnt} transactions)")

# Digital Wallet spending leads in both total and average spending

print("Max category " + str(sumsarr.max()))
print("Max category (avg) " + str(avgarr.max()))
