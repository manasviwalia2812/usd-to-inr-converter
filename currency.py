import requests

url = "https://api.currencyapi.com/v3/latest?apikey=cur_live_tYuK5bz8bbv2KuXThqyoeDuWDirDBnvi7R45Ikvw"

response = requests.get(url)
#print(response)

data=response.json()
# print(data)

# for i in data.keys():
#   if i=="data":
#     currency_data=data['data']
#     for d in currency_data.keys():
#       if d=='INR':
#         value_data=data['data']['INR']
#         for x in value_data.keys():
#           if x=='value':
#             # print("{}:{}".format(x,value_data[x]))
#             inr=value_data[x]
#             break
#OR
inr=data['data']['INR']['value']
user_input=int(input("Enter the Dollars: ")) 
k=user_input*inr
print("{} when converted to inr whose current current value is {} is {}".format(user_input,inr,k))

# print(type(currency_data))



