"""
    Whatever needed mate
"""


class RetailInfo:
    def __init__(self, id, name, details, thumbnail=None):
        self.id = id
        self.name = name
        self.details = details
        self.thumbnail = thumbnail


class RetailDetails:
    def __init__(self, id, name, url, info=None, categories=None, share_links=None, thumbnail=None):
        self.id = id
        self.name = name
        self.url = url
        self.info = info
        self.categories = categories
        self.share_links = []
        self.thumbnail = thumbnail

info = dict()
info['WES.AX'] = RetailInfo('WES.AX', 'Wesfarmers Ltd', 'This is Wesfarmers')
info['WOW.AX'] = RetailInfo('WOW.AX', 'Woolworths Supermarkets', 'This is Woolies')
info['MYR.AX'] = RetailInfo('MYR.AX', 'MYER', 'This is MYER')
info['DMP.AX'] = RetailInfo('DMP.AX', 'Domino\'s Pizza Enterprises', 'This is Dominos')
info['JBH.AX'] = RetailInfo('JBH.AX', 'JB Hi-Fi Limited', 'This is JB Hi-Fi')
info['HVN.AX'] = RetailInfo('HVN.AX', 'Harvey Norman Holdings Limited', 'This is Harvey Norman')
info['TRS.AX'] = RetailInfo('TRS.AX', 'Reject Shop Ltd', 'This is The Reject Shop')
info['KGN.AX'] = RetailInfo('KGN.AX', 'Kogan.Com Limited', 'This is Kogan')

companies_info = [info[x].__dict__ for x in sorted(info)]

categories = dict()
categories['WES.AX'] = ['Food', 'HouseholdGood', 'ClothingFootwareAndPersonalAccessory', 'DepartmentStores', 'Other']
categories['WOW.AX'] = ['Food', 'HouseholdGood', 'ClothingFootwareAndPersonalAccessory', 'DepartmentStores', 'Other']
categories['MYR.AX'] = ['Food', 'HouseholdGood', 'ClothingFootwareAndPersonalAccessory', 'DepartmentStores', 'Other']
categories['DMP.AX'] = ['Food', 'CafesRestaurantsAndTakeawayFood']
categories['JBH.AX'] = ['HouseholdGood', 'DepartmentStores', 'Other']
categories['HVN.AX'] = ['HouseholdGood', 'Other']
categories['TRS.AX'] = ['Food', 'HouseholdGood', 'ClothingFootwareAndPersonalAccessory', 'Other']
categories['KGN.AX'] = ['HouseholdGood', 'Other']

data = dict()
data['WES.AX']      = RetailDetails('WES.AX',
                                    'Wesfarmers Ltd',
                                    'http://www.wesfarmers.com.au/',
                                    'This is Wesfarmers',
                                    categories['WES.AX'])
data['WOW.AX']      = RetailDetails('WOW.AX',
                                   'Woolworths Supermarkets',
                                   'www.woolworths.com.au',
                                   'This is Woolworths',
                                   categories['WOW.AX'])
data['MYR.AX']      = RetailDetails('MYR.AX',
                                    'MYER',
                                    'www.myer.com.au',
                                    'This is MYER',
                                    categories['MYR.AX'])
data['DMP.AX']      = RetailDetails('DMP.AX',
                                    'Domino\'s Pizza Enterprises',
                                    'www.dominos.com.au',
                                    'This is Domino\'',
                                    categories['DMP.AX'])
data['JBH.AX']      = RetailDetails('JBH.AX',
                                    'JB Hi-Fi Limited',
                                    'www.jbhifi.com.au',
                                    'This is JB Hi-Fi',
                                    categories['JBH.AX'])
data['HVN.AX']      = RetailDetails('HVN.AX',
                                    'Harvey Norman Holdings Limited',
                                    'www.harveynorman.com.au',
                                    'This is Harvey Norman',
                                    categories['HVN.AX'])
data['TRS.AX']      = RetailDetails('TRS.AX',
                                    'Reject Shop Ltd',
                                    'www.rejectshop.com.au',
                                    'This is The Reject Shop',
                                    categories['TRS.AX'])
data['KGN.AX']      = RetailDetails('KGN.AX',
                                    'Kogan.Com Limited',
                                    'www.kogan.com/au',
                                    'This is Kogan',
                                    categories['KGN.AX'])