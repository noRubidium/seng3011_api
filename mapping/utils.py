
industries = dict()

# retail

industries['A2M'] = ['Food']
industries['BAL'] = ['Food']
industries['BGA'] = ['Food']
industries['CCL'] = ['Food']

industries['WES'] = ['Food', 'HouseholdGood', 'DepartmentStores']
industries['WOW'] = ['Food', 'HouseholdGood', 'DepartmentStores']

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

industries['AAC'] = ['FoodAndLiveAnimals']
industries['FNP'] = ['FoodAndLiveAnimals']
industries['SHV'] = ['FoodAndLiveAnimals']

industries['AVG'] = ['BeveragesAndTobacco']
industries['TWE'] = ['BeveragesAndTobacco']

industries['BHP'] = ['MineralFuelLubricantAndRelatedMaterial']
industries['BSL'] = ['MineralFuelLubricantAndRelatedMaterial']
industries['RIO'] = ['MineralFuelLubricantAndRelatedMaterial']

industries['AJX'] = ['ChemicalsAndRelatedProducts']



companies = dict()

companies['Food'] = ['A2M', 'BAL', 'BGA', 'CCL', 'WES', 'WOW']
companies['HouseholdGood'] = ['ADH', 'BLX', 'BRG', 'GFY', 'HVN', 'KGN', 'NCK', 'WES', 'WOW']
companies['ClothingFootwareAndPersonalAccessory'] = ['BBG', 'KMD', 'MYR', 'SFH', 'SSG']
companies['DepartmentStores'] = ['JBH', 'MYR', 'TRS', 'WES', 'WOW']
companies['CafesRestaurantsAndTakeawayFood'] = ['CKF', 'DMP', 'RFG']
companies['FoodAndLiveAnimals'] = ['AAC', 'FNP', 'SHV']
companies['BeveragesAndTobacco'] = ['AVG', 'TWE']
companies['MineralFuelLubricantAndRelatedMaterial'] = ['BHP', 'BSL', 'RIO']
companies['ChemicalsAndRelatedProducts'] = ['AJX']
