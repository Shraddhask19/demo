import requests 
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
import electronics, fashion, homeDecor, cosmetics



def app():
    def load_lottieurl(url):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()

    lottie_anim1 = load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_gwwov0zg.json")
    lottie_anim2 = load_lottieurl("https://assets7.lottiefiles.com/private_files/lf30_ecnepkno.json")     #fashion
    lottie_anim3 = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_XRm5n7XBm3.json")       #electronics    
    lottie_anim4 = load_lottieurl("https://assets3.lottiefiles.com/private_files/lf30_phcng6qv.json")     #home decor
    lottie_anim5 = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_y0fpo3em.json")          #cosmetics

    navbar = option_menu(
        menu_title = "BestProduct4U",
        # menu_title="",
        options = ["Home"],
        icons = ["house"],
        menu_icon = "cast",
        # default_index = 0,
        orientation = "horizontal"       
    )
    c1,c2 = st.columns((2,1))

    with st.container():
        with c1:
            st.title("A Product and Price Comparing Tool")
            st.write("Check out products from various E-Comerce sites and make the right choice !!")
    
        with c2:
            st_lottie(lottie_anim1, height=200, key="comapring tool")

    st.write('---')

    # st.header("Explore Categories !!")
    # st.write("Select the category you want to explore")
    # st.write('#')

    # with st.sidebar:
    selected = option_menu(
        menu_title = "Explore Categories !!",
        # menu_title="",
        options = ["Electronics", "Home Decore",  "Fashion", "Cosmetics"],
        icons = ["phone","book","envelope","house"],
        menu_icon = "cast",
        # default_index = 0,
        orientation = "horizontal"       
    )

    cl1,cl2,cl3,cl4 = st.columns(4)

    with cl1:
        # st.subheader("Electroincs")
        st_lottie(lottie_anim3, height=230, width=270, key="electronic")
    with cl2:
        # st.subheader("Home Decor")
        st_lottie(lottie_anim4, height=230, width=270, key="homedecor")
    with cl3:
        # st.subheader("Fashion")
        st_lottie(lottie_anim2, height=230, width=270, key="fashion")
    with cl4:
        # st.subheader("Cosmetics")
        st_lottie(lottie_anim5, height=230, width=270, key="cosmetics")
    
    st.write('---')

    if selected == "Electronics":
        electronics.app()
    if selected == "Fashion":
        fashion.app()
    if selected == "Home Decore":
        homeDecor.app()
    if selected == "Cosmetics":
        cosmetics.app()
        
st.set_page_config(layout="wide")
app()