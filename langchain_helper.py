from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
from secret_key import openapi_key
import os

os.environ['OPENAI_API_KEY'] = openapi_key
llm = OpenAI(temperature=0.7)

def generate_restaurant_name_and_dessert_items(dessert):
   # Chain 1 : Restaurant Name
   prompt_template_name = PromptTemplate(
       input_variables=['dessert'],
       template="I want to open a restaurant for {dessert} food. Suggest me a great fancy one name for that."
   )
   name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key='restaurant_name')

   # Chain 2 : Food Items Name

   prompt_template_items = PromptTemplate(
       input_variables=['restaurant_name'],
       template="Suggest some dessert items for {restaurant_name}.Give me a comma seperated list."
   )

   food_items_chain = LLMChain(llm=llm, prompt=prompt_template_items, output_key='dessert_items')

   chain = SequentialChain(
       chains=[name_chain, food_items_chain],
       input_variables=['dessert'],
       output_variables=['restaurant_name', 'dessert_items']
   )

   chain({'dessert': 'Italian'})
   response = chain({'dessert':dessert})

   return response

if __name__ == "__main__":
    print(generate_restaurant_name_and_dessert_items('Italian'))