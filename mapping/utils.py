
industries = dict()

# retail

industries['A2M'] = ['ConsumerFood']
industries['BAL'] = ['ConsumerFood']
industries['BGA'] = ['ConsumerFood']
industries['CCL'] = ['ConsumerFood']

industries['WES'] = ['ConsumerFood', 'HouseholdGood', 'DepartmentStores']
industries['WOW'] = ['ConsumerFood', 'HouseholdGood', 'DepartmentStores']

industries['ADH'] = ['HouseholdGood']
industries['BLX'] = ['HouseholdGood']
industries['BRG'] = ['HouseholdGood']
industries['GFY'] = ['HouseholdGood']
industries['HVN'] = ['HouseholdGood']
industries['KGN'] = ['HouseholdGood']
industries['NCK'] = ['HouseholdGood']

industries['BBG'] = ['ClothingFootwareAndPersonalAccessory']
industries['KMD'] = ['ClothingFootwareAndPersonalAccessory']
industries['SFH'] = ['ClothingFootwareAndPersonalAccessory']
industries['SSG'] = ['ClothingFootwareAndPersonalAccessory']

industries['JBH'] = ['DepartmentStores', 'HouseholdGood']
industries['MYR'] = ['DepartmentStores', 'HouseholdGood', 'ClothingFootwareAndPersonalAccessory']
industries['TRS'] = ['DepartmentStores', 'HouseholdGood']

industries['CKF'] = ['CafesRestaurantsAndTakeawayFood']
industries['DMP'] = ['CafesRestaurantsAndTakeawayFood']
industries['RFG'] = ['CafesRestaurantsAndTakeawayFood']

# exports

industries['AAC'] = ['FoodAndAgricultureProduction']
industries['FNP'] = ['FoodAndAgricultureProduction']
industries['SHV'] = ['FoodAndAgricultureProduction']

industries['AVG'] = ['BeveragesAndTobacco']
industries['CRW'] = ['BeveragesAndTobacco']
industries['TWE'] = ['BeveragesAndTobacco']

industries['BHP'] = ['Minerals']
industries['BSL'] = ['Minerals']
industries['RIO'] = ['Minerals']

industries['ALS'] = ['Chemicals']
industries['AJX'] = ['Chemicals']



companies = dict()

companies['ConsumerFood'] = ['A2M', 'BAL', 'BGA', 'CCL', 'WES', 'WOW']
companies['HouseholdGood'] = ['ADH', 'BLX', 'BRG', 'GFY', 'HVN', 'KGN', 'NCK', 'WES', 'WOW']
companies['ClothingFootwareAndPersonalAccessory'] = ['BBG', 'KMD', 'MYR', 'SFH', 'SSG']
companies['DepartmentStores'] = ['JBH', 'MYR', 'TRS', 'WES', 'WOW']
companies['CafesRestaurantsAndTakeawayFood'] = ['CKF', 'DMP', 'RFG']
companies['FoodAndAgricultureProduction'] = ['AAC', 'FNP', 'SHV']
companies['BeveragesAndTobacco'] = ['AVG', 'CRW', 'TWE']
companies['Minerals'] = ['BHP', 'BSL', 'RIO']
companies['Chemicals'] = ['ALS', 'AJX']
