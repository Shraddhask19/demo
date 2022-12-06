# Importing Required Library

import pandas as pd
import numpy as np
from itertools import combinations

# Reading Excel file 
bread = pd.read_csv('D:\\DM\\Bakery.csv')

bread = bread.drop_duplicates()

bread = bread.drop('DateTime', axis=1)
print(len(set(bread['Items'])))
print(bread.head(10))

transaction = pd.crosstab(index= bread['TransactionNo'], columns= bread['Items'])
# print(transaction)


def apriori(data, min_support=0.1,  max_length = 4):
    # Step 1:
    # Creating a dictionary to stored support of an itemset.
    support = {} 
    L = list(data.columns)
    
    # Step 2: 
    #generating combination of items with len i in ith iteration
    for i in range(1, max_length+1):
        c = set(combinations(L,i))
        
    # Reset "L" for next ith iteration
        L =set()     
    # Step 3: 
        #iterate through each item in "c"
        for j in list(c):
            #print(j)
            sup = data.loc[:,j].product(axis=1).sum()/len(data.index)
            if sup > min_support:
                #print(sup, j)
                support[j] = sup
                
                # Appending frequent itemset in list "L", already reset list "L" 
                L = list(set(L) | set(j))
        
    # Step 4: data frame with cols "items", 'support'
    result = pd.DataFrame(list(support.items()), columns = ["Items", "Support"])
    return(result)

## finding frequent itemset with min support = 4%
Freq_itemset = apriori(transaction, 0.04, 5)
Freq_itemset.sort_values(by = 'Support', ascending = False)

print(Freq_itemset)

def Association_Rule(df, min_threshold=0.5):
    import pandas as pd
    from itertools import permutations
    
    # STEP 1:
    #creating required varaible
    support = pd.Series(df.Support.values, index=df.Items).to_dict()
    data = []
    L= df.Items.values
    
    # Step 2:
    #generating rule using permutation
    p = list(permutations(L, 2))
    
    # Iterating through each rule
    for i in p:
        
        # If LHS(Antecedent) of rule is subset of RHS then valid rule.
        if set(i[0]).issubset(i[1]):
            conf = support[i[1]]/support[i[0]]
            #print(i, conf)
            if conf > min_threshold:
                #print(i, conf)
                j = i[1][not i[1].index(i[0][0])]
                lift = support[i[1]]/(support[i[0]]* support[(j,)])
                
                convection = (1 - support[(j,)])/(1- conf)
                data.append([i[0], (j,), support[i[0]], conf, lift,  convection])

         
    # STEP 3:
    result = pd.DataFrame(data, columns = ["antecedents", "consequents","support", "confidence", "Lift",  "Convection"])
    return(result)

## Rule with minimun confidence = 10%
AssoRule = Association_Rule(Freq_itemset, 0.1)
print(AssoRule)