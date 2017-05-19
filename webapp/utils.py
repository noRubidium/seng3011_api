"""
    Whatever needed mate
"""


class RetailInfo:
    def __init__(self, id, name, alias, details, thumbnail=None):
        self.id = id
        self.name = name
        self.alias = alias
        self.details = details
        self.thumbnail = thumbnail


class RetailDetails:
    def __init__(self, id, name, alias, url, info=None, categories=None, share_links=None, thumbnail=None):
        self.id = id
        self.name = name
        self.alias = alias
        self.url = url
        self.info = info
        self.categories = categories
        self.share_links = []
        self.thumbnail = thumbnail

info = dict()
info['WES.AX'] = RetailInfo('WES.AX', 'Wesfarmers Ltd', 'wesfarmers', 'This is Wesfarmers')
info['WOW.AX'] = RetailInfo('WOW.AX', 'Woolworths Supermarkets', 'woolworths', 'This is Woolies')
info['MYR.AX'] = RetailInfo('MYR.AX', 'MYER', 'myer', 'This is MYER')
info['DMP.AX'] = RetailInfo('DMP.AX', 'Domino\'s Pizza Enterprises', 'dominos', 'This is Dominos')
info['JBH.AX'] = RetailInfo('JBH.AX', 'JB Hi-Fi Limited', 'jbhifi', 'This is JB Hi-Fi')
info['HVN.AX'] = RetailInfo('HVN.AX', 'Harvey Norman Holdings Limited', 'harveynorman', 'This is Harvey Norman')
info['TRS.AX'] = RetailInfo('TRS.AX', 'Reject Shop Ltd', 'rejectshop', 'This is The Reject Shop')
info['KGN.AX'] = RetailInfo('KGN.AX', 'Kogan.Com Limited', 'kogan', 'This is Kogan')

companies_info = [info[x].__dict__ for x in sorted(info)]

categories = dict()
categories['WES.AX'] = ['Food', 'HouseholdGood', 'ClothingFootwareAndPersonalAccessory', 'DepartmentStores', 'Other', 'Total']
categories['WOW.AX'] = ['Food', 'HouseholdGood', 'ClothingFootwareAndPersonalAccessory', 'DepartmentStores', 'Other', 'Total']
categories['MYR.AX'] = ['ClothingFootwareAndPersonalAccessory', 'HouseholdGood', 'DepartmentStores', 'Other', 'Total']
categories['DMP.AX'] = ['Food', 'CafesRestaurantsAndTakeawayFood', 'Total']
categories['JBH.AX'] = ['HouseholdGood', 'DepartmentStores', 'Other', 'Total']
categories['HVN.AX'] = ['HouseholdGood', 'Other', 'Total']
categories['TRS.AX'] = ['Food', 'HouseholdGood', 'ClothingFootwareAndPersonalAccessory', 'Other', 'Total']
categories['KGN.AX'] = ['HouseholdGood', 'Other', 'Total']

data = dict()
data['WES.AX']      = RetailDetails('WES.AX',
                                    'Wesfarmers Ltd',
                                    'wesfarmers',
                                    'www.wesfarmers.com.au/',
                                    'Wesfarmers Limited is an Australian conglomerate, which owns Coles, Kmart and Target, with great interest predominantly in Australian and New Zealand retail.',
                                    categories['WES.AX'])
data['WOW.AX']      = RetailDetails('WOW.AX',
                                    'Woolworths Supermarkets',
                                    'woolworths',
                                    'www.woolworths.com.au',
                                    'Woolworths Limited is a major Australian company with extensive retail interest throughout Australia and New Zealand.',
                                    categories['WOW.AX'])
data['MYR.AX']      = RetailDetails('MYR.AX',
                                    'MYER',
                                    'myer',
                                    'www.myer.com.au',
                                    'MYER is an up market Australian department store chain trading in all Australian states and one of Australia\'s two self-governing territories.',
                                    categories['MYR.AX'])
data['DMP.AX']      = RetailDetails('DMP.AX',
                                    'Domino\'s Pizza Enterprises',
                                    'dominos',
                                    'www.dominos.com.au',
                                    'Domino\'s Pizza Enterprises is the largest pizza chain in Australia in terms of network store numbers and network sales, as well as the largest franchisee for the Domino\'s Pizza brand in the world.',
                                    categories['DMP.AX'])
data['JBH.AX']      = RetailDetails('JBH.AX',
                                    'JB Hi-Fi Limited',
                                    'jbhifi',
                                    'www.jbhifi.com.au',
                                    'JB Hi-Fi is an Australian and New Zealand retailer of consumer goods, specialising in video games, Blu-rays, DVDs, CDs, electronics/hardware and home appliances.',
                                    categories['JBH.AX'])
data['HVN.AX']      = RetailDetails('HVN.AX',
                                    'Harvey Norman Holdings Limited',
                                    'harveynorman',
                                    'www.harveynorman.com.au',
                                    'Harvey Norman is a large Australian-based, multi-national retailer of furniture, bedding, computers, communications and consumer electrical products.',
                                    categories['HVN.AX'])
data['TRS.AX']      = RetailDetails('TRS.AX',
                                    'Reject Shop Ltd',
                                    'rejectshop',
                                    'www.rejectshop.com.au',
                                    'The Reject Shop is an Australian discount variety store chain.',
                                    categories['TRS.AX'])
data['KGN.AX']      = RetailDetails('KGN.AX',
                                    'Kogan.Com Limited',
                                    'kogan',
                                    'www.kogan.com/au',
                                    'Kogan.com is the largest online department store in Australia, selling tens of thousands of products through its online direct-to-customer store.',
                                    categories['KGN.AX'])
