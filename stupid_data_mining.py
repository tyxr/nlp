import pandas as pd
def get_id():

    food_name = list(pd.read_csv('./newlist.csv', index_col=1,encoding='utf-8').index)
    food_data = pd.read_csv('./food_id_df.csv',encoding='utf-8').iloc[:,0:2]
    ids = []
    #print(food_data.iloc[:,1].str.find("酿苦瓜"))
    
    '''food_index = list(food_data[food_data.name=="酿苦瓜"].index)[0]
    _id = food_data.iloc[food_index,0]'''
    for i in food_name:
        food_index = list(food_data[food_data.name==i].index)[0]
        _id = food_data.iloc[food_index,0]
        ids.append(_id)

    '''for i in range(len(ids)):
        ids[i]=[ids[i]]
    name=['ids']
    test=pd.DataFrame(columns=name,data=ids)

    test.to_csv('d:/ids.csv',encoding='utf-8')'''
    
    #print(len(ids))
    return ids
def get_ingre():
    
    food_ingre_df = pd.read_csv('./food_ingre_df.csv',encoding='utf-8').iloc[:,1:3]
    #print(food_ingre_df)
    

    total_ingre = []

    ids = get_id()
    for i in ids:
        ingre_index = list(food_ingre_df[food_ingre_df.billfare_info_id==i].index)
        temp = []
        for j in ingre_index:
            
            ingre_id = food_ingre_df.iloc[j,1]
            temp.append(ingre_id)
        #print(i)
        #print(temp)
        total_ingre.extend(temp)
    total_ingre = list(set(total_ingre))
    return total_ingre

    
    '''for i in range(len(total_ingre)):
        total_ingre[i]=[total_ingre[i]]
    name=['ingre_ids']
    test=pd.DataFrame(columns=name,data=total_ingre)

    test.to_csv('d:/ingre_ids.csv',encoding='utf-8')'''
def get_ingre_name():
    ingre_ids = get_ingre()
    ingre_name = []
    ingre_data = pd.read_csv('./ingre_nutri_df.csv',encoding='utf-8')

    for i in ingre_ids:
        #print(i)
        ingre_id_index = list(ingre_data[ingre_data.id==i].index)
        temp = ingre_data.loc[ingre_id_index,['name']].to_dict('list')
        #print(temp['name'][0])
        ingre_name.append(temp['name'][0])
    
    return ingre_name
def name_dict():
    names = get_ingre_name()
    
    syn_dict = pd.read_csv('./syn.csv', encoding='utf-8', index_col=False, header=None)
    syn_dict = syn_dict.set_index(0)
    syn_dict = syn_dict[1]
    result = syn_dict.to_dict()
    
    temp = []
    def get_keys(d, value):
        return [k for k,v in d.items() if v == value]
    #get_keys({'a':'001', 'b':'002'}, '001') # => ['a']

    for i in names:
        
        temp.extend(get_keys(result, i))
    names.extend(temp)
    names = set(names)


    return names
def match_ingres():
    temp = 0
    food_ingre_df = pd.read_csv('./ingre_nutri_df.csv',encoding='utf-8')
    ingre_list = list(food_ingre_df.iloc[:,2])
    names = name_dict()
    for i in names:
        if i in ingre_list:
            temp = temp+1
    print(temp)
if __name__ == '__main__':
    match_ingres()
    
