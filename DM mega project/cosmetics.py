from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import streamlit as st
from bs4 import BeautifulSoup
import requests



def app():
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    st.header("Explore Cosmetic Product")
    search = st.text_input("Enter product name")
    pname = search
    defImg = "https://img.freepik.com/free-vector/error-404-concept-illustration_114360-1811.jpg?w=740&t=st=1668856568~exp=1668857168~hmac=7be8c25442362062a5064d946f8066c12ecf8b9fb2301c5be828f95dfbdc4b9e"
    
    # search = "uspa sweatshirt"

    if st.button("Search"):
        minPrice = 1000000000
        prefsite = "Amazon"
        st.subheader("Myglamm")
        relUrl = f"https://www.myglamm.com/search/{search}"
        driver.get(relUrl)
        with st.container():
            c1,c2 = st.columns((1,2))
            with c2:
                # st.write('#')
                try:
                    title = driver.find_element(By.XPATH, "/html/body/div[1]/section/div[2]/div[5]/div/a/div[2]/div[1]").text
                    description = driver.find_element(By.XPATH, "/html/body/div[1]/section/div[2]/div[1]/div/a/div[2]/div[2]").text
                    price = driver.find_element(By.XPATH, "/html/body/div[1]/section/div[2]/div[1]/div/a/div[2]/span/span[2]").text
                    price1 = price.replace('₹', '')
                    price1 = price1.replace(',','')
                    if minPrice > int(price1):
                        minPrice = int(price1)
                        prefsite = "Myglamm"
                except:
                    title = "NA"
                    description = "NA"
                    price = "NA"
                    
                st.write("Name: " ,title)

                st.write("Description: " ,description)

                st.write("Price: " ,price)

                st.write("Rating: 3")
                
                st.markdown(f"[Read more...]({relUrl})")


            with c1:
                try:
                    image = driver.find_element(By.XPATH, "/html/body/div[1]/section/div[2]/div[1]/div/a/div[1]/img").get_attribute('src')
                except:
                    image = defImg
                st.image(image, width=150)

            st.write('---')

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
        result = (image['src'], name, price, rating, driver.current_url)

        with st.container():
            image_col, text_col= st.columns((1,2))
            with image_col:
                st.image(f"{result[0]}", width=150, use_column_width=False)

            with text_col:
                st.write("Name:",result[1])
                st.write("Price:",result[2])
                st.write("Rating:",result[3])
                st.markdown(f"[Read more...]({result[4]})")

        st.write('---')

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
            
        result = (image['src'],description, price, rating, driver.current_url)

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

