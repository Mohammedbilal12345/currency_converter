import streamlit as st
import freecurrencyapi
import matplotlib.pyplot as plt
#backend

#streamlit code
#frontend
crncs={'data': {'EUR': {'symbol': '€', 'name': 'Euro', 'symbol_native': '€', 'decimal_digits': 2, 'rounding': 0, 'code': 'EUR', 'name_plural': 'Euros'}, 'USD': {'symbol': '$', 'name': 'US Dollar', 'symbol_native': '$', 'decimal_digits': 2, 'rounding': 0, 'code': 'USD', 'name_plural': 'US dollars'}, 'JPY': {'symbol': '¥', 'name': 'Japanese Yen', 'symbol_native': '￥', 'decimal_digits': 0, 'rounding': 0, 'code': 'JPY', 'name_plural': 'Japanese yen'}, 'GBP': {'symbol': '£', 'name': 'British Pound Sterling', 'symbol_native': '£', 'decimal_digits': 2, 'rounding': 0, 'code': 'GBP', 'name_plural': 'British pounds sterling'}, 'SEK': {'symbol': 'Skr', 'name': 'Swedish Krona', 'symbol_native': 'kr', 'decimal_digits': 2, 'rounding': 0, 'code': 'SEK', 'name_plural': 'Swedish kronor'}, 'CHF': {'symbol': 'CHF', 'name': 'Swiss Franc', 'symbol_native': 'CHF', 'decimal_digits': 2, 'rounding': 0, 'code': 'CHF', 'name_plural': 'Swiss francs'}, 'RUB': {'symbol': 'RUB', 'name': 'Russian Ruble', 'symbol_native': 'руб.', 'decimal_digits': 2, 'rounding': 0, 'code': 'RUB', 'name_plural': 'Russian rubles'}, 'AUD': {'symbol': 'AU$', 'name': 'Australian Dollar', 'symbol_native': '$', 'decimal_digits': 2, 'rounding': 0, 'code': 'AUD', 'name_plural': 'Australian dollars'}, 'BRL': {'symbol': 'R$', 'name': 'Brazilian Real', 'symbol_native': 'R$', 'decimal_digits': 2, 'rounding': 0, 'code': 'BRL', 'name_plural': 'Brazilian reals'}, 'CAD': {'symbol': 'CA$', 'name': 'Canadian Dollar', 'symbol_native': '$', 'decimal_digits': 2, 'rounding': 0, 'code': 'CAD', 'name_plural': 'Canadian dollars'}, 'CNY': {'symbol': 'CN¥', 'name': 'Chinese Yuan', 'symbol_native': 'CN¥', 'decimal_digits': 2, 'rounding': 0, 'code': 'CNY', 'name_plural': 'Chinese yuan'}, 'INR': {'symbol': 'Rs', 'name': 'Indian Rupee', 'symbol_native': 'টকা', 'decimal_digits': 2, 'rounding': 0, 'code': 'INR', 'name_plural': 'Indian rupees'}, 'KRW': {'symbol': '₩', 'name': 'South Korean Won', 'symbol_native': '₩', 'decimal_digits': 0, 'rounding': 0, 'code': 'KRW', 'name_plural': 'South Korean won'}, 'SGD': {'symbol': 'S$', 'name': 'Singapore Dollar', 'symbol_native': '$', 'decimal_digits': 2, 'rounding': 0, 'code': 'SGD', 'name_plural': 'Singapore dollars'}, 'ZAR': {'symbol': 'R', 'name': 'South African Rand', 'symbol_native': 'R', 'decimal_digits': 2, 'rounding': 0, 'code': 'ZAR', 'name_plural': 'South African rand'}}}
cont1=st.container()
cont2=st.container()
cont3=st.container()
cont4=st.container()
cont5=st.container()
with cont1:
    st.title('Currency Converter')
    st.markdown(
    """
    <hr style="border: none; height: 2px; background-color: green;">
    """,
    unsafe_allow_html=True
)

with cont2:
    col1,col2,col3=st.columns([2,0.6,2])
    src_cur=col1.selectbox('choose the input currency',['USD','INR','GBP','RUB','EUR','CAD','AUD','JPY','CNY','KRW','ZAR','CHF','SEK','SGD','BRL'])
    amount=col1.number_input(f'enter the amount in {src_cur}')
    col2.write('')
    col2.write('')
    col2.write('')
    with col2:
        coli,colj,colk=st.columns([1,4,1])
        btn2=colj.button('⇌   ',key='switch')
    
    
    btn1=col2.button('convert',key='convertbutton')
    
    st.markdown(
        """
        <style>
        .switch {
            display: flex;
            align-items: center;
        </style>
        """,
        unsafe_allow_html=True
    )
    cnv_cur=col3.selectbox('choose the output currency',['USD','INR','GBP','RUB','EUR','CAD','AUD','JPY','CNY','KRW','ZAR','CHF','SEK','SGD','BRL'])

#resultc=client.currencies(currencies=['EUR','CAD'])


def currency_conv(src_cur1,cnv_cur1):
    client=freecurrencyapi.Client('fca_live_MepLdJdr0dEkrx9Bee1oTevtrlK59Xre3McrYh18')
    print(client.status())
    resultl=client.latest(base_currency=src_cur1,currencies=['USD','INR','GBP','RUB','EUR','CAD','AUD','JPY','CNY','KRW','ZAR','CHF','SEK','SGD','BRL'])
    #resulth=client.historical('2022-02-02')
    print(resultl)
    conversion_rate=resultl['data'][cnv_cur1]
    def convert(amount,conv_rate):
        conv_amount=amount*conv_rate
        return round(conv_amount,2)
    converted_amount=convert(amount,conversion_rate)
    return conversion_rate,converted_amount 
with cont3:
    col4,col5,col6=st.columns([1,4.5,1])
    st.markdown(
    """
    <hr style="border: none; height: 2px; background-color: green;">
    """,
    unsafe_allow_html=True
    )
    bun=col4.button('graph')
    def currency_graph(src_cur1,cnv_cur1,year):
        client=freecurrencyapi.Client('fca_live_MepLdJdr0dEkrx9Bee1oTevtrlK59Xre3McrYh18')            
        resulth=client.historical(base_currency=src_cur1,currencies=['USD','INR','GBP','RUB','EUR','CAD','AUD','JPY','CNY','KRW','ZAR','CHF','SEK','SGD','BRL'],date=f'{year}-04-10')
        datah=resulth['data'][f'{year}-04-10'][cnv_cur1]
        return datah
    ratelist=[]
    if bun: 
        for i in range(2000,2024,3):   
            ratelist.append(currency_graph(src_cur,cnv_cur,i))
        x =range(2000,2024,3)
        print(ratelist)
        y=ratelist
        # Plot the data
        plt.figure(figsize=(6, 4))
        plt.plot(x, y)
        plt.xlabel('time(years)')
        plt.ylabel('exchange rate')
        plt.title(f'exchange rate trend({src_cur} to {cnv_cur})')
        # Display the plot using Streamlit
        st.pyplot(plt)

if btn1:
  col3.write('')
  col3.write('')
  col3.markdown(
    f"""
    <div style='border: 1px #282a30; padding: 10px; border-radius: 10px; background-color: #3F7F29; display: flex; justify-content: center; align-items: center; height: 45px;'>
        <p><h4>{amount} {crncs['data'][src_cur]['symbol']} = {currency_conv(src_cur,cnv_cur)[1]} {crncs['data'][cnv_cur]['symbol']}</h4></p>
        
    </div>
    """,
    unsafe_allow_html=True
    )
  col5.markdown(
    f"""
    <div style='border: 1px solid yellow; border-radius: 10px; padding: 10px; text-align: center;'>
        <p><h4>1 {crncs['data'][src_cur]['name']}={round(((currency_conv(src_cur,cnv_cur))[0]),3)} {crncs['data'][cnv_cur]['name']}</h4></p>
    </div>
    """,
    unsafe_allow_html=True
)
  cont5.write('*exchange rates update everyday automatically')


if btn2:
    col3.write('')
    col3.write('')
    col3.markdown(
    f"""
    <div style='border: 1px #282a30; padding: 20px; border-radius: 10px; background-color: #3F7F29; display: flex; justify-content: center; align-items: center; height: 45px;'>
        <p><h4>{amount} {crncs['data'][cnv_cur]['symbol']} =  {currency_conv(cnv_cur,src_cur)[1]} {crncs['data'][src_cur]['symbol']}</h4></p>
        
    </div>
    """,
    unsafe_allow_html=True
    )
    col5.markdown(
    f"""
    <div style='border: 1px solid yellow; border-radius: 10px; padding: 10px; text-align: center;'>
        <p><h4>1 {crncs['data'][cnv_cur]['name']}={round(((currency_conv(cnv_cur,src_cur))[0]),3)} {crncs['data'][src_cur]['name']}</h4></p>
    </div>
    """,
    unsafe_allow_html=True
)
    cont5.write('*exchange rates update everyday automatically')

st.write("""
    <style>
        .footer {
            position: fixed;
            bottom: 0;
            right: 0;
            width: 400px; /* Adjust the width as needed */
            
            color: white; /* Text color */
            text-align: center;
            padding: 10px;
        }
        .icon {
            display: inline-block;
            margin: 0 10px;
        }
    </style>
    <div class="footer">
        <p>Follow Karthik on <a href="https://github.com/Kart8ik" target="_blank" style="color: white;">GitHub</a></p>
        <p>Follow Chethan on <a href="https://github.com/chethans2005" target="_blank" style="color: white;">GitHub</a></p>
        <p>Follow Daneshwari on <a href="https://github.com/DMelshetty" target="_blank" style="color: white;">GitHub</a></p>
        <p>Follow Bilal on <a href="https://github.com/Mohammedbilal12345" target="_blank" style="color: white;">GitHub</a></p>
    </div>
         """, unsafe_allow_html=True)
