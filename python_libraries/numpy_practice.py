import numpy as np

print("="*60)
print("NUMPY FOR DATA ANALYSIS")
print("="*60)

# ---------------------------------------------------
# 1. ARRAY CREATION
# ---------------------------------------------------

print("\n1. ARRAY CREATION")

a = np.array([10,20,30,40,50])
print("array():",a)

print("zeros():")
print(np.zeros((2,3)))

print("ones():")
print(np.ones((2,3)))

print("full():")
print(np.full((2,2),7))

print("eye():")
print(np.eye(3))

print("arange():")
print(np.arange(1,11,2))

print("linspace():")
print(np.linspace(0,100,5))

# ---------------------------------------------------
# 2. RANDOM NUMBERS
# ---------------------------------------------------

print("\n2. RANDOM")

np.random.seed(42)

print(np.random.rand(3,3))

print(np.random.randint(1,100,(3,4)))

print(np.random.randn(2,3))

# ---------------------------------------------------
# 3. ARRAY INFORMATION
# ---------------------------------------------------

print("\n3. ARRAY INFORMATION")

arr=np.array([[1,2,3],[4,5,6]])

print("Shape :",arr.shape)
print("Dimensions :",arr.ndim)
print("Size :",arr.size)
print("Datatype :",arr.dtype)
print("Item Size :",arr.itemsize)

# ---------------------------------------------------
# 4. INDEXING
# ---------------------------------------------------

print("\n4. INDEXING")

print(arr)

print(arr[0])
print(arr[1])

print(arr[0,2])

print(arr[:,1])

print(arr[1,:])

# ---------------------------------------------------
# 5. SLICING
# ---------------------------------------------------

print("\n5. SLICING")

a=np.arange(1,11)

print(a)

print(a[2:7])

print(a[:5])

print(a[5:])

print(a[::-1])

# ---------------------------------------------------
# 6. RESHAPE
# ---------------------------------------------------

print("\n6. RESHAPE")

a=np.arange(12)

print(a)

print(a.reshape(3,4))

print(a.reshape(2,6))

# ---------------------------------------------------
# 7. FLATTEN
# ---------------------------------------------------

print("\n7. FLATTEN")

b=np.array([[1,2],[3,4]])

print(b.flatten())

print(b.ravel())

print(b.T)

# ---------------------------------------------------
# 8. MATHEMATICAL OPERATIONS
# ---------------------------------------------------

print("\n8. MATHEMATICAL OPERATIONS")

x=np.array([1,2,3])

y=np.array([4,5,6])

print(x+y)

print(x-y)

print(x*y)

print(x/y)

print(x**2)

print(np.sqrt(x))

print(np.power(x,3))

print(np.abs([-5,-2,3]))

# ---------------------------------------------------
# 9. STATISTICAL FUNCTIONS
# ---------------------------------------------------

print("\n9. STATISTICS")

data=np.array([10,20,30,40,50])

print("Sum :",np.sum(data))

print("Mean :",np.mean(data))

print("Median :",np.median(data))

print("Min :",np.min(data))

print("Max :",np.max(data))

print("Standard Deviation :",np.std(data))

print("Variance :",np.var(data))

print("Percentile :",np.percentile(data,75))

print("Product :",np.prod(data))

# ---------------------------------------------------
# 10. AXIS FUNCTIONS
# ---------------------------------------------------

print("\n10. AXIS")

matrix=np.array([[1,2,3],[4,5,6]])

print(matrix)

print("Column Sum")

print(np.sum(matrix,axis=0))

print("Row Sum")

print(np.sum(matrix,axis=1))

print("Column Mean")

print(np.mean(matrix,axis=0))

print("Row Mean")

print(np.mean(matrix,axis=1))

# ---------------------------------------------------
# 11. SORTING
# ---------------------------------------------------

print("\n11. SORTING")

a=np.array([7,3,9,1,5])

print(np.sort(a))

print(np.argsort(a))

# ---------------------------------------------------
# 12. SEARCHING
# ---------------------------------------------------

print("\n12. SEARCHING")

print(np.argmax(a))

print(np.argmin(a))

print(np.where(a>4))

# ---------------------------------------------------
# 13. BOOLEAN FILTERING
# ---------------------------------------------------

print("\n13. BOOLEAN FILTER")

print(a>4)

print(a[a>4])

print(a[(a>2)&(a<8)])

# ---------------------------------------------------
# 14. UNIQUE
# ---------------------------------------------------

print("\n14. UNIQUE")

a=np.array([1,2,2,3,3,4,5])

print(np.unique(a))

# ---------------------------------------------------
# 15. INSERT DELETE APPEND
# ---------------------------------------------------

print("\n15. INSERT DELETE")

a=np.array([1,2,3,4])

print(np.insert(a,2,100))

print(np.delete(a,1))

print(np.append(a,10))

# ---------------------------------------------------
# 16. COMBINE ARRAYS
# ---------------------------------------------------

print("\n16. COMBINE")

a=np.array([1,2])

b=np.array([3,4])

print(np.concatenate((a,b)))

print(np.vstack((a,b)))

print(np.hstack((a,b)))

print(np.stack((a,b)))

# ---------------------------------------------------
# 17. SPLIT
# ---------------------------------------------------

print("\n17. SPLIT")

a=np.arange(10)

print(np.split(a,2))

# ---------------------------------------------------
# 18. MATRIX OPERATIONS
# ---------------------------------------------------

print("\n18. MATRIX")

A=np.array([[1,2],[3,4]])

B=np.array([[5,6],[7,8]])

print("Dot Product")

print(np.dot(A,B))

print("Matrix Multiplication")

print(A@B)

print("Determinant")

print(np.linalg.det(A))

print("Inverse")

print(np.linalg.inv(A))

# ---------------------------------------------------
# 19. CUMULATIVE FUNCTIONS
# ---------------------------------------------------

print("\n19. CUMULATIVE")

a=np.array([1,2,3,4,5])

print(np.cumsum(a))

print(np.cumprod(a))

# ---------------------------------------------------
# 20. ROUNDING
# ---------------------------------------------------

print("\n20. ROUNDING")

a=np.array([2.34,4.89,6.45])

print(np.round(a))

print(np.floor(a))

print(np.ceil(a))

# ---------------------------------------------------
# 21. LOG & EXP
# ---------------------------------------------------

print("\n21. LOG & EXP")

a=np.array([1,2,3])

print(np.exp(a))

print(np.log(a))

print(np.log10(a))

# ---------------------------------------------------
# 22. TRIGONOMETRY
# ---------------------------------------------------

print("\n22. TRIGONOMETRY")

angle=np.array([0,np.pi/2,np.pi])

print(np.sin(angle))

print(np.cos(angle))

print(np.tan(angle))

# ---------------------------------------------------
# 23. COPY & VIEW
# ---------------------------------------------------

print("\n23. COPY & VIEW")

a=np.array([1,2,3])

copy=a.copy()

view=a.view()

view[0]=100

print("Original :",a)

print("Copy :",copy)

print("View :",view)

# ---------------------------------------------------
# 24. SAVE & LOAD
# ---------------------------------------------------

print("\n24. SAVE & LOAD")

np.save("sample.npy",a)

loaded=np.load("sample.npy")

print(loaded)

print("\nCompleted Successfully!")