import requests
try:
    class Cat_fact:
        def __init__(self, fact_text):
            self.fact = fact_text
        def show(self):
            print("_"*length)
            print(f"Interesting fact {self.fact}")
            print("_"*length)
    url = 'https://catfact.ninja/fact'
    with requests.Session() as session:
       data=session.get(url).json()
       length = len(data['fact'])
       my_cat_fact = Cat_fact(data['fact'])
       my_cat_fact.show()
except Exception as e:
    print(e)





