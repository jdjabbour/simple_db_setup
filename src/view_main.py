from datetime import datetime, date
import streamlit as st
import re

try:
    from src.data_manager import DataManager as dm
    from src.calc_manager import Calcs
except:
    from data_manager import DataManager as dm
    from calc_manager import Calcs


def view_main():
    today = date.today()
    st.markdown("<h1 style='text-align: center; color: white;'>Product List</h1>", unsafe_allow_html=True)
    st.markdown(f"<h2 style='text-align: center; color: white;'>{today}</h1>", unsafe_allow_html=True)
    st.markdown('***')

    data_list = dm().get_products()
    if 'data_list' not in st.session_state:
        st.session_state.data_list = []
        for product in data_list:
            st.session_state.data_list.append(product)
            
            


    new_prod = st.text_input("Enter a new product:")
    new_prod = new_prod.split(',')

    add_button = st.button("Add Product")
    if add_button:
        if new_prod:
            if len(new_prod) != 1:
                new_prod = [(new_prod[0], new_prod[1], new_prod[2])]
                dm().add_products(new_prod)
                st.session_state.data_list.append(new_prod)
                st.success(f"'{new_prod}' added to the list!")
                st.rerun()
            elif len(new_prod) == 1:
                new_prod = [(new_prod, '0.00', '0.00')]
                dm().add_products(new_prod)
                st.session_state.data_list.append(new_prod)
                st.success(f"'{new_prod}' added to the list!")
                st.rerun()
        else:
            st.warning("Please enter an item to add.")

    
    st.write("***")
    st.subheader("Current List:")
    if st.session_state.data_list:
        for product in data_list:
            name = product[0]
            price = product[1]
            cost = product[2]
            gp = Calcs(price, cost).gross_profit()
            gp = Calcs(price, cost).highlight_gross_profit(gp)

            # if gp < 30.00:
            #     gp = f":red[{gp}]"
            # else:
            #     gp = f":green[{gp}]"

            st.write(f"- NAME: {name}, PRICE: {price}, COST: {cost}, GROSS PROFIT: {gp}")

    else:
        st.write(f"TABLE EMPTY")    




if __name__ == "__main__":
    view_main()



