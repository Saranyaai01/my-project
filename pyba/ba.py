import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv("laptop_price.csv")


display=pd.DataFrame(data)


print(display)
print(type(display))
print(display.info())

display.plot(kind='bar',
    x='Product',
    y='Price_euros',
    color='blue')

plt.title("laptop price  Graph")
plt.show()


# data={
#     "name":["saranya","abi","lavanya"],
#     "location":["trichy","chennai","madurai"]
# }

# df=pd.DataFrame(data)

# print(df)




# data=pd.read_csv("laptop_price.csv",encoding='latin-1')

# df=pd.DataFrame(data)

# print(df.head(20).dropna().to_string())
