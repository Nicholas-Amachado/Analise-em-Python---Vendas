import pandas as pd
from twilio.rest import Client


#abrindo a lista dos meses com variavel
meses=['janeiro','fevereiro','março','abril','maio','junho']
#abrindo no excel
tabelavalores=pd.read_excel("janeiro.xlsx")
#vendo se as metas foram batidas
for mes in meses:
    tabelavalores=pd.read_excel(f'{mes}.xlsx')
    #print(tabelavalores)
    #colocando a mensagem caso a meta foi batida
    if (tabelavalores['Vendas'] > 55000).any():

        vendas=tabelavalores.loc[tabelavalores['Vendas'] >55000,'Vendas'].values[0]

        vendedor=tabelavalores.loc[tabelavalores['Vendas'] >55000,'Vendedor'].values[0]

        print(f'a meta foi batida no mes de {mes} sucesso!quem fez as vendas foi o {vendedor} com o total de vendas de {vendas}')


#envio do SMS
        account_sid = "AC2385a8944863bbeaa075fc0f1644357c"
        auth_token = "5eccd506f2117e2a3a4b248860dcbe5f"

        client = Client(account_sid, auth_token)

        message = client.messages.create(
            to="+5511910302041",
            from_="+17655713446",
            body=f'no mes de {mes} o vendedor {vendedor} bateu a meta de 55000 vendas com o numero de {vendas}')

        print(message.sid)





