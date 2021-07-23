import pandas as pd

df = pd.read_excel('c:/scanner/OPC_Dom_spec.xlsx', header=None)
dfd = []
for item in (df.iloc(0)[0]):
    dfd.append(item)
df.columns = dfd
print(dfd)
# df.drop(0, inplace=True)
for i, item in enumerate(df.iloc(1)[2]):
    df['ChannelSpec'][i] = item.split(';')[-1].split(':')[-1].replace('"', '').replace('\'', '')
# df.to_)
df.drop(0, inplace=True)
print(df.head(10))
df.to_excel('c:/scanner/channels.xlsx')
