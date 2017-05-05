"""
    Whatever needed mate
"""

class RetailInfo():
    def __init__(self, id, name, details, thumbnail=None):
        self.id = id
        self.name = name
        self.details = details
        self.thumbnail = thumbnail

    @staticmethod
    def to_dict(retail):
        return dict(id=retail.id, name=retail.name, details=retail.details, thumbnail=retail.thumbnail)

info = dict()
info['coles'] = RetailInfo('coles', 'Coles Supermarkets Australia Pty Ltd', 'This is Coles')
info['woolworths'] = RetailInfo('woolworths', 'Woolworths Supermarkets', 'This is Woolies')
info['myer'] = RetailInfo('myer', 'MYER', 'This is MYER')
info['dominos'] = RetailInfo('dominos', 'Domino\'s Pizza Enterprises', 'This is Dominos')

companies_info = map(RetailInfo.to_dict, info.values())


class RetailDetails():
    def __init__(self, id, name, url, share_links=[], thumbnail=None):
        self.id = id
        self.name = name
        self.url = url
        self.share_links = []
        self.thumbnail = thumbnail

    @staticmethod
    def to_dict(retail):
        return dict(id=retail.id,
                    name=retail.name,
                    url=retail.url,
                    share_links=retail.share_links,
                    thumbnail=retail.thumbnail)

data = dict()
data['coles'] = RetailDetails('WES', 'Coles Supermarkets Australia Pty Ltd', 'www.coles.com.au')
data['woolworths'] = RetailDetails('WOW', 'Woolworths Supermarkets', 'www.woolworths.com.au')
data['myer'] = RetailDetails('MYR', 'MYER', 'www.myer.com.au')
data['dominos'] = RetailDetails('DMP', 'Domino\'s Pizza Enterprises', 'www.dominos.com.au')

categories = dict()
categories['coles'] = ['Food', 'HouseholdGood', 'ClothingFootwareAndPersonalAccessory', 'DepartmentStores', 'Other']
categories['woolworths'] = ['Food', 'HouseholdGood', 'ClothingFootwareAndPersonalAccessory', 'DepartmentStores', 'Other']
categories['myer'] = ['Food', 'HouseholdGood', 'ClothingFootwareAndPersonalAccessory', 'DepartmentStores', 'Other']
categories['dominos'] = ['Food', 'CafesRestaurantsAndTakeawayFood']