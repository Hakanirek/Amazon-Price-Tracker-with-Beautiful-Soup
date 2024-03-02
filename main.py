import requests
from bs4 import BeautifulSoup
import lxml
import smtplib
import os

product_url="https://www.amazon.com.tr/Spigen-Apple-iPhone-K%C4%B1l%C4%B1f-Liquid/dp/B0B1PCRZ7D/ref=pd_sbs_sccl_3_10/261-1859074-4590362?pd_rd_w=uUS2O&content-id=amzn1.sym.ecaac94d-e145-4eee-959b-24b8c16a14db&pf_rd_p=ecaac94d-e145-4eee-959b-24b8c16a14db&pf_rd_r=5GXAY1YHZRDSCYS9E67E&pd_rd_wg=JxOQW&pd_rd_r=8df76d9e-1a71-4a47-8742-4391b6914a0c&pd_rd_i=B0B1PCRZ7D&th=1"
TARGET_PRICE = 450
MY_EMAIL = os.environ.get("EMAIL")
MY_PASSWORD = os.environ.get("PASSWORD")

headers = {
    "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "acceptLanguage": "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7,de;q=0.6",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "requestLine":"GET / HTTP/1.1"
}
response = requests.get(product_url, headers={"User-Agent":"Defined"})

#print(response.text)

soup = BeautifulSoup(response.text, "html.parser")
price = int(soup.find(name="span",class_="a-price-whole").get_text().replace(",", ""))

print(price)

if price < TARGET_PRICE:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n The price of product you selected before decrease to {price}. You can reach the product by this link {product_url}."
        )
