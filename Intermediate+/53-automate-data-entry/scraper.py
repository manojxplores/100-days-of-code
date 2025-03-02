from bs4 import BeautifulSoup


class ScrapeData(BeautifulSoup):
    def __init__(self, content):
        super().__init__(content, "html.parser")
        self.price_list = []
        self.address_list = []
        self.a_list = []
        self.data = {}

    def get_data(self):
        div_wrapper = self.find(name="ul", class_="List-c11n-8-84-3-photo-cards")
        items = div_wrapper.find_all(name="li", class_="ListItem-c11n-8-84-3-StyledListCardWrapper")

        for idx, i in enumerate(items):
            price = i.find(name="span", class_="PropertyCardWrapper__StyledPriceLine")
            address = i.find(name="a", class_="StyledPropertyCardDataArea-anchor")
            self.address_list.append(address.get_text().strip())
            self.price_list.append(price.get_text())
            self.a_list.append(address["href"])

