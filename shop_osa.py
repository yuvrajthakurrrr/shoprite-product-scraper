import requests
import json
import pandas as pd
from datetime import datetime
from database import database
import time
import pyodbc
import string
import sqlalchemy as sa
from sqlalchemy.types import NVARCHAR
import urllib
import os
from lxml import etree




cookies = {
    '_ga_GL7R6TK7S9': 'GS1.2.1728563673.3.0.1728563673.60.0.0',
    '_ga_F6CZGHNDZ7': 'GS1.1.1728565487.4.0.1728565487.0.0.0',
    '__cf_bm': 'J8FwtqBHa4UQVysWC5ZTLDxLKwLGh9ifKzVF.ufP7DE-1728977654-1.0.1.1-s7DJvCr8jEeCS1ULxq85IhvnuJo8aBZcps4ThY.D0xvA3xM45M9yBe9EcUyen8dtSbuhynX.PJ8SREGngRMW2_Q2YYNalJfqr6tPMg8vFtE',
    '__cfruid': 'b9b1d64595a4f756932516b07c58c2a993500eff-1728977654',
    'fw_utm': '{%22value%22:%22{}%22%2C%22createTime%22:%222024-10-15T07:34:13.945Z%22}',
    'fw_uid': '{%22value%22:%228ee7af37-8b45-41b2-8c44-e30f016df3cb%22%2C%22createTime%22:%222024-10-15T07:34:13.952Z%22}',
    'fw_se': '{%22value%22:%22fws2.e83187f7-ca75-47f3-94a4-6044b79e38e0.3.1728977653965%22%2C%22createTime%22:%222024-10-15T07:34:13.965Z%22}',
    'cf_clearance': 'F9dBN2GwhbPo8myLwLbT_9sMqlmW2THP7YV9U24Ez18-1728977656-1.2.1.1-IN.esjsFzVi2p5IEX_86Qt.EtRjxxXvwkEZIndHrQ.C8uSx4u_MJCbiAl7NkPS3C103CmvPZjg51S5Ti8pJZbAN9w2k2Mlko9zeIiDSadoYxnbEb3MvAJrK4ayuw0Q4ZHl5zGKxUWmhq_YhJ4d6C320Ra1PXdt4DaCg8r9DE1u79M2H5uDrPJiCIvesWHkobzy1g.y55Hl5ukgpLxr2y85.D9I4ZOcreWiBNrhuq2I6892WSURumRgR_YYzKpor0ihk32qImnCpf6QvZFzbJICau62dTUDXan2kwV.pV5SKjlBv3hBQYKmzA1KtR7Aox9SBJ1CWUl8SiwUNw46VVDKBvYeENJuEoZpXgipgsTmfElUHbgWFzbMKFouxJMNJj',
    'fw_bid': '{%22value%22:%225EK3Wg%22%2C%22createTime%22:%222024-10-15T07:34:15.672Z%22}',
    'fw_chid': '{%22value%22:%22p0en7pV%22%2C%22createTime%22:%222024-10-15T07:34:15.731Z%22}',
    '_gid': 'GA1.2.1603367120.1728977658',
    '_ga': 'GA1.2.1110087459.1728385209',
    '_ga_J7H5215LEX': 'GS1.1.1728977659.5.1.1728977807.0.0.0',
    '_gat_UA-84476771-44': '1',
}

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9',
    # 'cookie': '_ga_GL7R6TK7S9=GS1.2.1728563673.3.0.1728563673.60.0.0; _ga_F6CZGHNDZ7=GS1.1.1728565487.4.0.1728565487.0.0.0; __cf_bm=J8FwtqBHa4UQVysWC5ZTLDxLKwLGh9ifKzVF.ufP7DE-1728977654-1.0.1.1-s7DJvCr8jEeCS1ULxq85IhvnuJo8aBZcps4ThY.D0xvA3xM45M9yBe9EcUyen8dtSbuhynX.PJ8SREGngRMW2_Q2YYNalJfqr6tPMg8vFtE; __cfruid=b9b1d64595a4f756932516b07c58c2a993500eff-1728977654; fw_utm={%22value%22:%22{}%22%2C%22createTime%22:%222024-10-15T07:34:13.945Z%22}; fw_uid={%22value%22:%228ee7af37-8b45-41b2-8c44-e30f016df3cb%22%2C%22createTime%22:%222024-10-15T07:34:13.952Z%22}; fw_se={%22value%22:%22fws2.e83187f7-ca75-47f3-94a4-6044b79e38e0.3.1728977653965%22%2C%22createTime%22:%222024-10-15T07:34:13.965Z%22}; cf_clearance=F9dBN2GwhbPo8myLwLbT_9sMqlmW2THP7YV9U24Ez18-1728977656-1.2.1.1-IN.esjsFzVi2p5IEX_86Qt.EtRjxxXvwkEZIndHrQ.C8uSx4u_MJCbiAl7NkPS3C103CmvPZjg51S5Ti8pJZbAN9w2k2Mlko9zeIiDSadoYxnbEb3MvAJrK4ayuw0Q4ZHl5zGKxUWmhq_YhJ4d6C320Ra1PXdt4DaCg8r9DE1u79M2H5uDrPJiCIvesWHkobzy1g.y55Hl5ukgpLxr2y85.D9I4ZOcreWiBNrhuq2I6892WSURumRgR_YYzKpor0ihk32qImnCpf6QvZFzbJICau62dTUDXan2kwV.pV5SKjlBv3hBQYKmzA1KtR7Aox9SBJ1CWUl8SiwUNw46VVDKBvYeENJuEoZpXgipgsTmfElUHbgWFzbMKFouxJMNJj; fw_bid={%22value%22:%225EK3Wg%22%2C%22createTime%22:%222024-10-15T07:34:15.672Z%22}; fw_chid={%22value%22:%22p0en7pV%22%2C%22createTime%22:%222024-10-15T07:34:15.731Z%22}; _gid=GA1.2.1603367120.1728977658; _ga=GA1.2.1110087459.1728385209; _ga_J7H5215LEX=GS1.1.1728977659.5.1.1728977807.0.0.0; _gat_UA-84476771-44=1',
    'dnt': '1',
    'origin': 'https://www.shoprite.com',
    'priority': 'u=1, i',
    'referer': 'https://www.shoprite.com/',
    'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
    'x-correlation-id': '25da541c-2748-45ac-913f-197426cb072a',
    'x-customer-session-id': 'https://www.shoprite.com|b1529f83-2635-47bd-93fe-795bd01793aa',
    'x-shopping-mode': '11111111-1111-1111-1111-111111111111',
    'x-site-host': 'https://www.shoprite.com',
    'x-site-location': 'HeadersBuilderInterceptor',
}

data_list=[]
queries = pd.read_csv("queries.csv", dtype={"product_id": str})

for i, row in queries.iterrows():
    
    product_id = row['product_id']
    url = f'https://storefrontgateway.shoprite.com/api/stores/3000/products/{product_id}'
    response = requests.get(url,
        cookies=cookies,
        headers=headers,
    )

    if response.status_code == 200:
        try:
            response_data = response.json()
            item = response_data

            brand_name = item.get("brand")
            pname = item.get("name")
            sp = item.get("price")
            mrp = item.get("wasPrice")
            unitPrice = item.get("unitPrice")

            defaultasin =  item.get("sku")


            units_of_size = item.get("unitsOfSize", {})

            if units_of_size:
                weight = (
                    f"{units_of_size.get('size', '')} {units_of_size.get('abbreviation', '')}"
                )
            else:
                weight = None
            

            status_text = item.get("available")
            if status_text==True:
                status_text='Available'
            else:
                status_text='Unavailable'

            # Handling categories
            try:
                categories = item.get("categories", [])
                main_cat = categories[0]["category"] 
                last_node = categories[-1]["category"]
                category_hierarchy = categories[-1].get("categoryBreadcrumb")
            except:
                main_cat = ''
                last_node = ''
                category_hierarchy = ''


            # Handling serving size safely
            serving_size_info = item.get("servingSize")
            if serving_size_info:
                serving_size = str(serving_size_info.get("size")) + " " + serving_size_info.get("type", "")
            else:
                serving_size = None

            # Handling nutritional profile safely
            nutrition_profiles = item.get("nutritionProfiles", {}).get("nutrition", {})
            if nutrition_profiles:
                nutrition_profile = (
                    f"Calories: {nutrition_profiles.get('Calories', {}).get('size', '')} {nutrition_profiles.get('Calories', {}).get('abbreviation', '')} | "
                    f"Total Fat: {nutrition_profiles.get('Total Fat', {}).get('size', '')} {nutrition_profiles.get('Total Fat', {}).get('abbreviation', '')} | "
                    f"Total Sugars: {nutrition_profiles.get('Total Sugars', {}).get('size', '')} {nutrition_profiles.get('Total Sugars', {}).get('abbreviation', '')} | "
                    f"Sodium: {nutrition_profiles.get('Sodium', {}).get('size', '')} {nutrition_profiles.get('Sodium', {}).get('abbreviation', '')}"
                )
            else:
                nutrition_profile = None

            ingredients = item.get("ingredients")
            #prod_des = item.get("description")

            # Handling image counts
            primary_image = item.get("primaryImage", {}).get("details", [])
            additional_images = item.get("additionalImages", {}).get("details", [])
            
            # Count number of images
            no_of_img = 0
            if primary_image:
                no_of_img += 1  # Primary image exists, count as 1
            if additional_images:
                no_of_img += len(additional_images)  # Add additional image count

            # Prepare the data for CSV
            extracted_data = {
                #"rank": i + 1,
                "time_stamp": datetime.now().strftime("%Y-%m-%d"),
                "location": "",
                "region": "US",
                "brand_name": brand_name,
                "platform": 'Shoprite',
                "platform_code": product_id,
                "prod_url": f"https://www.shoprite.com/sm/pickup/rsid/3000/product/id-{product_id}",
                "pname": pname,
                "sp": sp,
                "mrp": mrp,
                "item_weight":  weight,
                #"unit_price": unitPrice,
                "status_text": status_text,
                "additional_information": serving_size,
                #"defaultasin":  defaultasin,
                "image_count": no_of_img,
                "technical_details": nutrition_profile,
                "basic_details": ingredients,
                "category_hierarchy": category_hierarchy,
                "main_cat": main_cat,
                "sub_cat": last_node
                #"prod_des": prod_des
            }

            # Append the extracted data to the list
            data_list.append(extracted_data)
        except ValueError:
            print(f"Invalid JSON for product ID: {product_id}, Response: {response.text}")
    
    else:
        print(f"Failed request for product ID: {product_id}, Status Code: {response.status_code}, Response: {response.text}")

# Convert the list to DataFrame and export to CSV
df = pd.DataFrame(data_list)
#df['platform_code'] = df['platform_code'].astype(str)

# Get the current date in the format YYYY_MM_DD
current_date = datetime.now().strftime("%Y_%m_%d")

# Define the output file name
output_file = f"output_{current_date}.xlsx"

# Save the DataFrame to CSV
df.to_excel(output_file, index=False)

print(f"Data successfully saved to {output_file}")

#Write your database_push function here

database_push(df,'Your_Table_Name')
