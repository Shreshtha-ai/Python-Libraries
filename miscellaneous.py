import numpy as np 
import matplotlib.pyplot as plt

# Data structure: [restaurant_id, 2021, 2022, 2023, 2024]
sales_data = np.array([
    [1, 150000, 180000, 220000, 250000],  # Paradise Biryani
    [2, 120000, 140000, 160000, 190000],  # Beijing Bites
    [3, 200000, 230000, 260000, 300000],  # Pizza Hub
    [4, 180000, 210000, 240000, 270000],  # Burger Point
    [5, 160000, 185000, 205000, 230000]   # Chai Point
])
print("=== Zomatao Sales Analysis ===")
print("\n Shape of sales data is :", sales_data.shape)
print("Data for first three resturants:", sales_data[0:3]) #slicing
print("sales data",sales_data[:,1:]) #prints all rows and print columns from index 1 to end

#total sales of each year

print(np.sum(sales_data,axis = 0))

yearly_total = np.sum(sales_data[:,1:],axis = 0)
print("Yearly total sales:",yearly_total)


#minimum sales of each resturant
print(np.min(sales_data[:,1:],axis = 1))

#maximum sales per year
print(np.max(sales_data[:,1:],axis = 0))

#Average sales per restaurant
print(np.mean(sales_data[:,1:],axis = 1))

cumsum = np.cumsum(sales_data[:,1:],axis = 1)
print("Cumulative sum:",cumsum)

cumsum = np.cumsum(sales_data[:, 1:], axis=1)
print(cumsum)

plt.figure(figsize=(8, 6))
plt.plot(np.mean(cumsum, axis=0))
plt.title("Average cumulative sales accross all restaurant ")
plt.xlabel("Years")
plt.ylabel("Sales")
plt.grid(True)
plt.show() 

vector1 = np.array([1,2,3,4,5,6])
vector2 = np.array([7,8,9,10,11,12])

print("Sum of vector1 and vector2:",vector1+vector2)
print("Product of vector1 and vector2:",vector1*vector2)
print("Dot product:",np.dot(vector1,vector2))
angle = np.arccos(np.dot(vector1, vector2) / (np.linalg.norm(vector1) * np.linalg.norm(vector2)))
print("Angle between vector1 and vector2:",angle)

restaurant_types = np.array(["biryani","chinese","pizza","burger","chai"])
vectorized_upper = np.vectorize(str.upper)
print("Vectorized upper:",vectorized_upper(restaurant_types))

#Broadcasting

monthly_avg = sales_data[:,1:] / 12 # here 12 is broadcasted to all the elements of the array
print("Monthly average:",monthly_avg)



 

