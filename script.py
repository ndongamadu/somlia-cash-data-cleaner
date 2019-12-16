import pandas as pd


# functions
# Fillna (here Unspecified) a given column in a given dataframe


def fillNa(df, col):
    df[col].fillna('Unspecified', inplace=True)
    return 0


def cleanConditionality(df):
    # clean conditionality
    print("=== Cleaning CONDITIONALITY ===")
    print("=== unique values of CONDITIONALITY before ===")
    print(df['CONDITIONALITY'].unique())
    df.loc[df['CONDITIONALITY'].isin(['Yes - Cash for work', 'Yes, Cash for work', 'Cash For Work']), 'CONDITIONALITY'] = 'Yes - cash for work'
    df.loc[df['CONDITIONALITY'].isin(['No - unconditional', 'Unconditional ', 'unconditional ', 'unconditional']), 'CONDITIONALITY'] = 'Unconditional'
    df.loc[df['CONDITIONALITY'].isin(['Conditional ', 'conditional', 'Yes', 'Restricted', 'Food for work', 'Yes - cash for training',
                                     'unskilled labour', 'skilled labour', 'Cash', 'Yes - cash for work',
                                      ' Yes- Cash for Assets', 'yes - Cash for Training',
                                      'Yes - Cash for assets', 'Yes - Cash for training', 'Yes - Cash for assets']), 'CONDITIONALITY'] = 'Conditional'
    df.loc[df['CONDITIONALITY'].isin(['yes-cash for assets', 'Cash for Assets']), 'CONDITIONALITY'] = 'Yes - Cash for assets'
    df.loc[df['CONDITIONALITY'].isin(['Yes - unspecified conditionality', 'Yes-Cash for investment']), 'CONDITIONALITY'] = 'Unspecified'
    print("=== unique values of CONDITIONALITY after ===")
    print(df['CONDITIONALITY'].unique())


def cleanDeliveryMechanism(df):
    # delivery mechanism cleaning
    print("=== Cleaning DELIVERY MECHANISM ===")
    print("=== unique values of DELIVERY MECHANISM before ===")
    print(df['DELIVERY MECHANISM'].unique())
    df.loc[df['DELIVERY MECHANISM'].isin(['Cash- Mobile ', 'through mobile transfer', 'Cash- Mobile', 'Mobile transfer',
                                         ' mobile ', 'Mobile money transfer', 'Cash Mobile', 'Mobile', 'Cash - Mobile',
                                          'mobile cash', 'Mobile Transfer', 'MMT', 'mobile', 'Mobile money']), 'DELIVERY MECHANISM'] = 'Cash - mobile'
    df.loc[df['DELIVERY MECHANISM'].isin(['Money/cash transfer', 'Deposit account', 'Cash - bank transfer', 'Food', 'in kind ',
                                         'EVC Plus', 'monthly', 'Agricultural input', 'other', 'Cash - Hawaala',
                                          'Woqooyi Galbeed', 'Togdheer', 'Sanaag', 'Through FFS']), 'DELIVERY MECHANISM'] = 'Unspecified'
    df.loc[df['DELIVERY MECHANISM'].isin(['Voucher', 'Food Vourcher ', 'Voucher - Paper', 'Voucher-Paper',
                                          'Food Voucher']), 'DELIVERY MECHANISM'] = 'Voucher - paper'
    df.loc[df['DELIVERY MECHANISM'].isin(['e-voucher', 'e-Voucher', 'E-Voucher']), 'DELIVERY MECHANISM'] = 'E-voucher'
    df.loc[df['DELIVERY MECHANISM'].isin(['Cash -  in hand', 'Cash in hand', 'cash in hand', 'Cash']), 'DELIVERY MECHANISM'] = 'Cash - In Hand'
    df.loc[df['DELIVERY MECHANISM'] == 'e-cash', 'DELIVERY MECHANISM'] = 'e-Cash'
    print("=== unique values of DELIVERY MECHANISM after ===")
    print(df['DELIVERY MECHANISM'].unique())


def cleanRestriction(df):
    # cleaning restriction
    print("=== Cleaning RESTRICTION column ===")
    print("=== unique values of RESTRICTION before ===")
    print(df['RESTRICTION'].unique())
    df.loc[df['RESTRICTION'].isin(['Vulnerable People', 'Unconditional', '1.2dollar per I metre of Soil bund',
                                  '1 dollar per I metre of Soil bund', '65 USD ', '70 USD', '75 USD',
                                   '280 USD', '40 USD']), 'RESTRICTION'] = 'Unspecified'
    df.loc[df['RESTRICTION'].isin(['restricted', 'restricted ', 'yes']), 'RESTRICTION'] = 'Restricted'
    df.loc[df['RESTRICTION'].isin(['unrestricted ', 'unrestricted', 'unrestricted', 'No', 'NO']), 'RESTRICTION'] = 'Unrestricted'
    print("=== unique values of RESTRICTION after ===")
    print(df['RESTRICTION'].unique())


def cleanRuralUrban(df):
    # cleaning Rural/Urban
    print("=== Cleaning Rural/Urban column ===")
    print("=== unique values of RURAL/URBAN before ===")
    print(df['RURAL/URBAN'].unique())
    df.loc[df['RURAL/URBAN'].isin(['rural', 'Rural', 'Rural ', ' Rural', 'rURAL']), 'RURAL/URBAN'] = 'RURAL'
    df.loc[df['RURAL/URBAN'].isin(['urban', 'Urban ', 'Urban', 'urban ', 'town']), 'RURAL/URBAN'] = 'URBAN'
    df.loc[df['RURAL/URBAN'].isin(['Xayira', 'Gumays', 'ongoing', 'planned', 'completed',
                                   'TBC', 'Baki', 'Belet Xaawo', 'Baardheere', 'Kismayo']), 'RURAL/URBAN'] = 'Unspecified'
    df.loc[df['RURAL/URBAN'].isin(['Mixed', 'Mixed ', 'RURAL/idp', 'RURAL/URBAN', 'Urban/Rural']), 'RURAL/URBAN'] = 'MIXED'
    df.loc[df['RURAL/URBAN'] == 'IDP', 'RURAL/URBAN'] = 'IDPs'
    df.loc[df['RURAL/URBAN'] == 'mixed', 'RURAL/URBAN'] = 'MIXED'
    print("=== unique values of RURAL/URBAN after ===")
    print(df['RURAL/URBAN'].unique())


def fillingNA(df):
    print("=== Filling NA ===")
    for col in ['CONDITIONALITY', 'RESTRICTION', 'DELIVERY MECHANISM', 'RURAL/URBAN']:
        fillNa(df, col)


def DistrictsPcoder(df, pcodes):
    # getting districts and pcoding it
    print("=== Cleaning districts ===")
    districts = pd.DataFrame(df.DISTRICT.unique())
    districts = districts.rename(columns={0: "district_name"})
    # pcodes = pcodes[['DIST_NAME', 'DIS_CODE']]
    districts = districts.merge(pcodes, how='left', left_on='district_name', right_on='DIST_NAME')
    print("=== districts results ===")
    print(districts)
    return districts


def RegionsPcoder(df):
    # getting regions and pcoding
    print("=== Cleaning regions ===")
    regions = pd.DataFrame(df.REGION.unique())
    regions = regions.rename(columns={0: "region_name"})
    regions.loc[regions['region_name'] == 'Lower Shabelle', 'REG_CODE'] = 23
    regions.loc[regions['region_name'] == 'Mudug', 'REG_CODE'] = 18
    regions.loc[regions['region_name'] == 'Bakool', 'REG_CODE'] = 25
    regions.loc[regions['region_name'] == 'Woqooyi Galbeed', 'REG_CODE'] = 12
    regions.loc[regions['region_name'] == 'Togdheer', 'REG_CODE'] = 13
    regions.loc[regions['region_name'] == 'Banadir', 'REG_CODE'] = 22
    regions.loc[regions['region_name'] == 'Lower Juba', 'REG_CODE'] = 28
    regions.loc[regions['region_name'] == 'Bari', 'REG_CODE'] = 16
    regions.loc[regions['region_name'] == 'Gedo', 'REG_CODE'] = 26
    regions.loc[regions['region_name'] == 'Sanaag', 'REG_CODE'] = 15
    regions.loc[regions['region_name'] == 'Bay', 'REG_CODE'] = 24
    regions.loc[regions['region_name'] == 'Galgaduud', 'REG_CODE'] = 19
    regions.loc[regions['region_name'] == 'Middle Shabelle', 'REG_CODE'] = 21
    regions.loc[regions['region_name'] == 'Hiraan', 'REG_CODE'] = 20
    regions.loc[regions['region_name'] == 'Lower juba', 'REG_CODE'] = 28
    regions.loc[regions['region_name'] == 'GEDO', 'REG_CODE'] = 26
    regions.loc[regions['region_name'] == 'gedo', 'REG_CODE'] = 26
    regions.loc[regions['region_name'] == 'Sool', 'REG_CODE'] = 14
    regions.loc[regions['region_name'] == 'Awdal', 'REG_CODE'] = 11
    regions.loc[regions['region_name'] == 'Nugaal', 'REG_CODE'] = 17
    print("=== regions results ===")
    print(regions.head(10))
    return regions


