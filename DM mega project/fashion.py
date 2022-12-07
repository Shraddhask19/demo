from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import csv
from bs4 import BeautifulSoup
import requests
from lxml import etree
import requests 
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu

def app():
    options = Options()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.minimize_window()
    defImg = "https://img.freepik.com/free-vector/error-404-concept-illustration_114360-1811.jpg?w=740&t=st=1668856568~exp=1668857168~hmac=7be8c25442362062a5064d946f8066c12ecf8b9fb2301c5be828f95dfbdc4b9e"
    
    st.header("Explore Fashion Product")
    search = st.text_input("Enter product name")
    pname = search
    # search = "uspa sweatshirt"

    if st.button("Search"):
        minPrice = 100000000000
        prefsite = "Amazon"
        st.subheader("Myntra")
        # st.write('#')
        mynUrl = f"https://www.myntra.com/{search}"
        driver.get(mynUrl)
        with st.container():
            c1,c2 = st.columns((1,2))
            with c2:

                try:
                    title = driver.find_element(By.XPATH, "/html/body/div[2]/div/main/div[3]/div[2]/div/div[2]/section/ul/li[2]/a/div[2]/h3").text
                    description = driver.find_element(By.XPATH, "/html/body/div[2]/div/main/div[3]/div[2]/div/div[2]/section/ul/li[2]/a/div[2]/h4[1]").text
                    price = driver.find_element(By.XPATH, "/html/body/div[2]/div/main/div[3]/div[2]/div/div[2]/section/ul/li[2]/a/div[2]/div[1]/span[1]/span[1]").text
                    rating = driver.find_element(By.XPATH, "/html/body/div[2]/div/main/div[3]/div[2]/div/div[2]/section/ul/li[2]/div[2]/span[1]").text
                    price1 = price.replace('₹', '')
                    price1 = price1.replace(',','')
                    if minPrice > int(price1):
                        minPrice = int(price1)
                        prefsite = "Myntra"
                except:
                    title="Not found"
                    description="NA"
                    price="NA"
                    rating="NA"
                st.write("Name: ",title)

                st.write("Description: " ,description)

                st.write("Price: " ,price)

                st.write("Rating: " ,rating)

            with c1:
                try:
                    image = driver.find_element(By.XPATH, "/html/body/div[2]/div/main/div[3]/div[2]/div/div[2]/section/ul/li[1]/a/div[1]/div/div[1]/div/picture/img").get_attribute('src')
                except:
                    image=defImg
                st.image(image, width=150)
            
        st.write('---')
        
        st.subheader("AJIO")
        ajioUrl = f"https://www.ajio.com/search/?text={search}"
        driver.get(ajioUrl)
        with st.container():
            c1,c2 = st.columns((1,2))
            with c2:
               
                try:
                    title = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/div/div[2]/div[2]/div[3]/div[1]/div/div[1]/a/div/div[2]/div[1]").text
                    description = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/div/div[2]/div[2]/div[3]/div[1]/div/div[1]/a/div/div[2]/div[2]").text
                    price = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/div/div[2]/div[2]/div[3]/div[1]/div/div[1]/a/div/div[2]/div[3]/span").text
                    price1 = price.replace('₹', '')
                    price1 = price1.replace(',','')
                    if minPrice > int(price1):
                        minPrice = int(price1)
                        prefsite = "Ajio"
                except:
                    title="Not found"
                    description="NA"
                    price="NA"
                    rating="NA"

                st.write("Name: ",title)

                st.write("Description: " ,description)

                st.write("Price: " ,price)

                rating = 4
                st.write("Rating: " ,rating)

            with c1:
                try:
                    image = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/div/div[2]/div[2]/div[3]/div[1]/div/div[1]/a/div/div[1]/div[1]/img").get_attribute('src')
                except:
                    image=defImg
                st.image(image, width=150)
        
        st.subheader("Flipkart")
        flip_url = 'https://www.flipkart.com/search?q={}'.format(pname)
        page = requests.get(flip_url)
        soup = BeautifulSoup(page.content, 'html.parser')
        name=soup.find('div',class_="_4rR01T")
        if name is not None:
            # st.write(name.text)
            name = name.text

            #get rating of a product
            rating=soup.find('div',class_="_3LWZlK").text
            # st.write(rating)
            image = soup.find('img', class_= "_396cs4 _3exPp9")
            
            #get price of the product
            price=soup.find('div',class_='_30jeq3 _1_WHN1').text
            price1 = price.replace('₹', '')
            price1 = price1.replace(',','')
            if minPrice > int(price1):
                minPrice = int(price1)
                prefsite = "Flipkart"
        else:
            try:
                name=soup.find('a',class_="s1Q9rs").text
                rating = soup.find('div',class_="_3LWZlK").text
                price = soup.find('div',class_='_30jeq3').text # _30jeq3
                image = soup.find('img', class_= "_396cs4 _3exPp9")
                price1 = price.replace('₹', '')
                price1 = price1.replace(',','')
                if minPrice > int(price1):
                    minPrice = int(price1)
                    prefsite = "Flipkart"
            except:
                title="Not found"
                description="NA"
                price="NA"
                rating="NA"
                image = dict()
                image['src']=defImg
        result = (image['src'], name, price, rating, flip_url)

        with st.container():
            image_col, text_col= st.columns((1,2))
            with image_col:
                st.image(f"{result[0]}", width=150, use_column_width=False)

            with text_col:
                st.write("Name:",result[1])
                st.write("Price:",result[2])
                st.write("Rating:",result[3])
                st.markdown(f"[Read more...]({result[4]})")


        st.subheader("Amazon")
        amazon_url = 'https://www.amazon.in/s?k={}&ref=nb_sb_noss_1'.format(pname)

        driver.get(amazon_url)

        soup = BeautifulSoup(driver.page_source, 'html.parser')
        results  = soup.find_all('div',{'data-component-type':'s-search-result'})

        # st.write(len(results))

        item = results[1]

        atag = item.h2.a
        description = atag.text.strip()
        amazon_url = 'https://www.amazon.in/' + atag.get('href')

        try:
            # price
            price_parent = item.find('span', 'a-price')
            price = price_parent.find('span', 'a-offscreen').text
            # //rank and rating
            rating = str(item.i.text)[0]
            image = item.find('img','s-image')
            price1 = price.replace('₹', '')
            price1 = price1.replace(',','')
            if minPrice > int(price1):
                minPrice = int(price1)
                prefsite = "Amazon"
        except AttributeError:
            title="Not found"
            description="NA"
            price="NA"
            rating="NA"
            image = dict()
            image['src']=defImg
            
        result = (image['src'],description, price, rating, amazon_url)

        with st.container():
            image_col, text_col= st.columns((1,2))
            with image_col:
                st.image(f"{result[0]}", width=150, use_column_width=False)

            with text_col:
                st.write("Name:",result[1])
                st.write("Price:",result[2])
                st.write("Rating:",result[3])
                st.markdown(f"[Read more...]({result[4]})")
        
        st.subheader(f"Buying at {prefsite} is best for you!!")
    driver.close()

