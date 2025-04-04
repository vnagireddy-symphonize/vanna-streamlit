from vanna.remote import VannaDefault


# api_key = e1f6d06b7554400a88ea52ec0d4e4877 # Your API key from https://vanna.ai/account/profile
api_key = 'ccef4a2f3fbf43039f29fe654b33f93c'
vanna_model_name = 'chinook' # Your model name from https://vanna.ai/account/profile

vn = VannaDefault(model=vanna_model_name, api_key=api_key)


# import vanna as vn
# api_key = vn.get_api_key('vnagireddy.symphonize@gmail.com')
# print(api_key)
# vn.set_api_key(api_key)
sql = vn.generate_sql(question='What are the top 10 customers by Sales?')
print(sql)
