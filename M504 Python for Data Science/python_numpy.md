# Python NumPy Fundamentals for Data Science Masters

## Task 1: Array Creation and Basic Operations

**Learning Objectives:** Array creation, indexing, slicing, basic operations

### Example: Understanding NumPy Array Fundamentals

```python
import numpy as np

# Different ways to create arrays
zeros_array = np.zeros((3, 4))
ones_array = np.ones((2, 3, 4))
identity_matrix = np.eye(5)
random_array = np.random.random((3, 3))
range_array = np.arange(0, 20, 2)
linspace_array = np.linspace(0, 1, 11)

print("Zeros array shape:", zeros_array.shape)
print("Random array:\n", random_array)
```

### Your Tasks:

#### Part A: Array Creation

```python
# TODO: Create the following arrays
def create_arrays():
    """
    Create:
    1. A 4x4 array filled with the value 7
    2. A 1D array with values from 10 to 50 (step of 5)
    3. A 3x3 diagonal matrix with values [1, 4, 9]
    4. A 2x6 array with random integers between 1 and 100
    5. A 3D array of shape (2, 3, 4) filled with sequential numbers
    """
  
    # Your code here
    array_7s = # Fill with 7s
    array_range = # Range array
    diagonal_matrix = # Diagonal matrix
    random_ints = # Random integers
    array_3d = # 3D sequential array
  
    return array_7s, array_range, diagonal_matrix, random_ints, array_3d

# Test your functions
arrays = create_arrays()
for i, arr in enumerate(arrays):
    print(f"Array {i+1}:\n{arr}\nShape: {arr.shape}\n")
```

#### Part B: Array Indexing and Slicing

```python
# Sample data for practice
sales_data = np.array([[120, 135, 98, 164, 142],
                       [88, 92, 108, 95, 103],
                       [156, 178, 134, 167, 145],
                       [92, 87, 76, 89, 94]])

print("Sales data shape:", sales_data.shape)
print("Sales data:\n", sales_data)

# TODO: Extract specific information
def analyze_sales_indexing(data):
    """
    Extract:
    1. Sales for the first quarter (first 3 months) for all stores
    2. Sales for store 2 (index 1) for all months
    3. The highest sales value and its position
    4. Sales for the last 2 stores in the last 2 months
    5. Every other month's sales for store 3
    """
  
    # Your solutions here
    first_quarter = 
    store_2_sales = 
    max_sales = 
    max_position = 
    last_stores_months = 
    store_3_alternate = 
  
    return (first_quarter, store_2_sales, max_sales, 
            max_position, last_stores_months, store_3_alternate)

results = analyze_sales_indexing(sales_data)
```

#### Part C: Array Operations

```python
# TODO: Perform array operations
def array_operations():
    """
    Create two 3x3 arrays and perform:
    1. Element-wise addition, subtraction, multiplication
    2. Matrix multiplication
    3. Element-wise comparison operations
    4. Broadcasting operations with a scalar
    """
  
    # Create test arrays
    array_a = np.random.randint(1, 10, (3, 3))
    array_b = np.random.randint(1, 10, (3, 3))
  
    # Your operations here
    addition = 
    subtraction = 
    element_mult = 
    matrix_mult = 
    comparison = 
    broadcast_op = 
  
    return array_a, array_b, addition, subtraction, element_mult, matrix_mult, comparison, broadcast_op
```

---

## Task 2: Statistical Operations and Data Analysis

**Learning Objectives:** Statistical functions, aggregations, axis operations

### Example: Statistical Analysis with NumPy

```python
# Student grades dataset
students = 50
subjects = 5
grades = np.random.normal(75, 15, (students, subjects))
grades = np.clip(grades, 0, 100)  # Ensure grades are between 0-100

print("Grades shape:", grades.shape)
print("Sample grades:\n", grades[:5])

# Basic statistics
mean_per_student = np.mean(grades, axis=1)
mean_per_subject = np.mean(grades, axis=0)
overall_mean = np.mean(grades)

print(f"Overall mean: {overall_mean:.2f}")
```

### Your Tasks:

#### Part A: Comprehensive Statistical Analysis

```python
# Generate student performance data
np.random.seed(42)
n_students = 100
n_subjects = 6
subject_names = ['Math', 'Physics', 'Chemistry', 'Biology', 'English', 'History']

# Create grades with different difficulty levels
base_grades = np.random.normal(70, 12, (n_students, n_subjects))
difficulty_factors = np.array([0.9, 0.8, 0.85, 0.9, 0.95, 0.92])  # Subject difficulty
grades = base_grades * difficulty_factors
grades = np.clip(grades, 0, 100)

# TODO: Calculate comprehensive statistics
def calculate_statistics(grades, subject_names):
    """
    Calculate:
    1. Mean, median, std deviation for each subject
    2. Min and max grades for each student
    3. Percentile rankings (25th, 50th, 75th, 90th)
    4. Subject difficulty ranking based on average scores
    5. Student performance ranking
    6. Correlation between different subjects
    """
  
    # Your statistical calculations here
    subject_stats = {}
    student_stats = {}
    percentiles = {}
  
    # Calculate statistics for each subject
    for i, subject in enumerate(subject_names):
        subject_grades = grades[:, i]
        subject_stats[subject] = {
            'mean': ,
            'median': ,
            'std': ,
            'min': ,
            'max': 
        }
  
    # Calculate student statistics
    student_stats = {
        'mean_grades': ,
        'min_grades': ,
        'max_grades': ,
        'std_grades': 
    }
  
    return subject_stats, student_stats

stats = calculate_statistics(grades, subject_names)
```

#### Part B: Advanced Array Operations

```python
# TODO: Advanced analysis functions
def advanced_grade_analysis(grades):
    """
    Perform advanced analysis:
    1. Find students who failed more than 2 subjects (grade < 60)
    2. Calculate grade distribution histogram
    3. Find subject pairs with highest correlation
    4. Identify outlier students (z-score > 2 in overall performance)
    5. Calculate improvement needed for each student to reach 80% average
    """
  
    # Your advanced analysis here
    failing_threshold = 60
    target_average = 80
  
    # Find students failing multiple subjects
    failing_mask = grades < failing_threshold
    students_multiple_fails = 
  
    # Calculate histograms
    grade_bins = np.arange(0, 101, 10)
    grade_distribution = 
  
    # Find correlations between subjects
    correlation_matrix = 
  
    # Identify outliers
    student_averages = 
    z_scores = 
    outliers = 
  
    # Improvement needed
    current_averages = 
    improvement_needed = 
  
    return {
        'multiple_failures': students_multiple_fails,
        'distribution': grade_distribution,
        'correlations': correlation_matrix,
        'outliers': outliers,
        'improvement_needed': improvement_needed
    }

advanced_results = advanced_grade_analysis(grades)
```

#### Part C: Conditional Operations and Masking

```python
# TODO: Use boolean indexing and masking
def conditional_operations(grades, subject_names):
    """
    Use conditional operations to:
    1. Count students with A grades (90+) in each subject
    2. Find average grade excluding failing grades (<60)
    3. Create grade letter assignments (A: 90+, B: 80-89, C: 70-79, etc.)
    4. Identify top 10% students in each subject
    5. Calculate bonus points needed to bring all students to passing grade
    """
  
    # Your conditional operations here
    a_grade_counts = 
    average_excluding_fails = 
  
    # Grade letter assignment
    grade_letters = np.empty(grades.shape, dtype='<U2')
    # Use np.where or boolean indexing
  
    # Top 10% students per subject
    top_10_percent = 
  
    # Bonus points calculation
    passing_grade = 60
    bonus_points = 
  
    return {
        'a_grades': a_grade_counts,
        'avg_excluding_fails': average_excluding_fails,
        'letter_grades': grade_letters,
        'top_students': top_10_percent,
        'bonus_needed': bonus_points
    }
```

---

## Task 3: Array Reshaping and Broadcasting

**Learning Objectives:** Array manipulation, broadcasting rules, dimension operations

### Example: Understanding Broadcasting

```python
# Broadcasting example
array_2d = np.array([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]])

row_vector = np.array([10, 20, 30])
col_vector = np.array([[1], [2], [3]])

# Broadcasting operations
result1 = array_2d + row_vector  # Add row vector to each row
result2 = array_2d + col_vector  # Add column vector to each column

print("Original array:\n", array_2d)
print("After adding row vector:\n", result1)
print("After adding column vector:\n", result2)
```

### Your Tasks:

#### Part A: Reshaping and Dimension Manipulation

```python
# Sales data for multiple stores, products, and months
np.random.seed(123)
sales_raw = np.random.randint(50, 500, 360)  # 360 data points

# TODO: Reshape and manipulate dimensions
def reshape_sales_data(sales_raw):
    """
    Transform the 1D sales data into meaningful structures:
    1. Reshape into (5 stores, 6 products, 12 months)
    2. Transpose to get (months, products, stores)
    3. Flatten back to 1D in different order
    4. Add new axis to create (1, 5, 6, 12) shape
    5. Squeeze and expand dimensions as needed
    """
  
    # Your reshaping operations
    stores, products, months = 5, 6, 12
  
    # Reshape to 3D
    sales_3d = 
  
    # Transpose dimensions
    sales_transposed = 
  
    # Flatten in different order (Fortran vs C order)
    sales_flat_c = 
    sales_flat_f = 
  
    # Add new axis
    sales_4d = 
  
    # Advanced indexing to extract specific slices
    first_quarter = # First 3 months for all stores and products
    store_1_all = # All data for store 1
  
    return {
        'original': sales_3d,
        'transposed': sales_transposed,
        'flat_c': sales_flat_c,
        'flat_f': sales_flat_f,
        '4d': sales_4d,
        'first_quarter': first_quarter,
        'store_1': store_1_all
    }

reshape_results = reshape_sales_data(sales_raw)
```

#### Part B: Broadcasting Applications

```python
# TODO: Apply broadcasting for data normalization and analysis
def broadcasting_operations():
    """
    Create practical broadcasting examples:
    1. Normalize sales data by store averages
    2. Apply seasonal adjustments (different factor per month)
    3. Calculate percentage of total sales per store
    4. Apply discount rates (different per product)
    5. Calculate performance metrics with different baselines
    """
  
    # Create sample data
    stores, products, months = 4, 5, 12
    sales = np.random.randint(100, 1000, (stores, products, months))
  
    # Store average normalization
    store_averages = # Calculate store averages across products and months
    normalized_by_store = # Normalize using broadcasting
  
    # Seasonal adjustments
    seasonal_factors = np.array([0.8, 0.9, 1.1, 1.2, 1.3, 1.4, 
                                1.5, 1.4, 1.2, 1.0, 0.9, 0.8])
    seasonally_adjusted = # Apply seasonal factors using broadcasting
  
    # Percentage calculations
    total_sales = # Calculate total sales
    percentage_by_store = # Calculate percentage using broadcasting
  
    # Product-specific discount rates
    discount_rates = np.array([0.1, 0.05, 0.15, 0.2, 0.08])  # Different per product
    discounted_sales = # Apply discounts using broadcasting
  
    # Performance metrics with baselines
    baseline_targets = np.random.randint(200, 400, (stores, 1, 1))  # Store targets
    performance_ratio = # Calculate performance vs baseline
  
    return {
        'original': sales,
        'normalized': normalized_by_store,
        'seasonal': seasonally_adjusted,
        'percentages': percentage_by_store,
        'discounted': discounted_sales,
        'performance': performance_ratio
    }

broadcast_results = broadcasting_operations()
```

---

## Task 4: Linear Algebra Operations

**Learning Objectives:** Matrix operations, linear algebra, eigenvalues, solving systems

### Example: Basic Linear Algebra

```python
# Create matrices for demonstration
A = np.array([[2, 1], [1, 3]])
B = np.array([[1, 2], [3, 1]])
b = np.array([8, 13])

# Basic operations
matrix_mult = np.dot(A, B)  # or A @ B
determinant = np.linalg.det(A)
inverse = np.linalg.inv(A)
solution = np.linalg.solve(A, b)

print("Matrix multiplication:\n", matrix_mult)
print("Determinant:", determinant)
print("Solution to Ax=b:", solution)
```

### Your Tasks:

#### Part A: Matrix Operations for Data Analysis

```python
# TODO: Solve real-world linear algebra problems
def portfolio_optimization():
    """
    Portfolio optimization using linear algebra:
    Given expected returns and covariance matrix, find optimal weights
    """
  
    # Expected returns for 5 assets
    expected_returns = np.array([0.12, 0.10, 0.08, 0.15, 0.06])
  
    # Covariance matrix (5x5)
    np.random.seed(42)
    L = np.random.randn(5, 5)
    covariance_matrix = L @ L.T  # Ensure positive semi-definite
  
    # TODO: Solve portfolio optimization
    # Minimize risk for target return of 10%
    target_return = 0.10
  
    # Set up constraint matrices for: sum of weights = 1, target return = 10%
    # Ax = b where x are the portfolio weights
  
    # Constraint matrix
    A_constraints = # Create constraint matrix
    b_constraints = # Create constraint vector
  
    # Solve the system
    try:
        weights = # Solve using linear algebra
        portfolio_return = # Calculate expected portfolio return
        portfolio_risk = # Calculate portfolio risk (variance)
    
        return {
            'weights': weights,
            'expected_return': portfolio_return,
            'risk': portfolio_risk,
            'valid': np.allclose(np.sum(weights), 1.0)
        }
    except np.linalg.LinAlgError:
        return {'error': 'No solution found'}

portfolio_result = portfolio_optimization()
```

#### Part B: Eigenvalue Analysis

```python
# TODO: Principal Component Analysis concepts
def pca_analysis():
    """
    Perform eigenvalue decomposition for dimensionality reduction
    """
  
    # Generate sample data (100 samples, 5 features)
    np.random.seed(123)
    n_samples, n_features = 100, 5
  
    # Create correlated data
    base_data = np.random.randn(n_samples, 2)
    # Create additional features as linear combinations
    feature_3 = base_data[:, 0] + 0.5 * base_data[:, 1] + 0.1 * np.random.randn(n_samples)
    feature_4 = 0.8 * base_data[:, 0] - 0.3 * base_data[:, 1] + 0.1 * np.random.randn(n_samples)
    feature_5 = 0.2 * base_data[:, 0] + 0.9 * base_data[:, 1] + 0.1 * np.random.randn(n_samples)
  
    data = np.column_stack([base_data, feature_3, feature_4, feature_5])
  
    # TODO: Perform PCA analysis
    # 1. Center the data
    centered_data = 
  
    # 2. Calculate covariance matrix
    cov_matrix = 
  
    # 3. Find eigenvalues and eigenvectors
    eigenvalues, eigenvectors = 
  
    # 4. Sort by eigenvalue magnitude
    sorted_indices = 
    sorted_eigenvalues = 
    sorted_eigenvectors = 
  
    # 5. Calculate explained variance ratio
    total_variance = 
    explained_variance_ratio = 
    cumulative_variance = 
  
    # 6. Transform data to principal components
    principal_components = 
  
    return {
        'eigenvalues': sorted_eigenvalues,
        'eigenvectors': sorted_eigenvectors,
        'explained_variance': explained_variance_ratio,
        'cumulative_variance': cumulative_variance,
        'transformed_data': principal_components
    }

pca_results = pca_analysis()
```

#### Part C: System of Equations

```python
# TODO: Solve business problem using linear equations
def supply_demand_equilibrium():
    """
    Find market equilibrium using system of linear equations
    Multiple products with interdependent demand
    """
  
    # System: 3 products with cross-price elasticity
    # Demand equations: Qd1 = a1 - b1*P1 + c1*P2 + d1*P3
    # Supply equations: Qs1 = e1 + f1*P1
    # At equilibrium: Qd = Qs for each product
  
    # Coefficient matrix for the system
    # Variables: [P1, P2, P3] (prices)
    coefficient_matrix = np.array([
        [15, -2, -1],   # Product 1 equilibrium equation
        [-1, 12, -2],   # Product 2 equilibrium equation
        [-2, -1, 18]    # Product 3 equilibrium equation
    ])
  
    constants = np.array([100, 150, 200])  # Market size constants
  
    # TODO: Solve for equilibrium prices
    equilibrium_prices = 
  
    # TODO: Calculate equilibrium quantities
    # Using the demand equations
    demand_coefficients = np.array([
        [10, 2, 1],  # Demand for product 1
        [1, 8, 2],   # Demand for product 2
        [2, 1, 15]   # Demand for product 3
    ])
  
    equilibrium_quantities = 
  
    # Verify equilibrium conditions
    verification = # Check if supply equals demand
  
    return {
        'prices': equilibrium_prices,
        'quantities': equilibrium_quantities,
        'verification': verification
    }

equilibrium = supply_demand_equilibrium()
```
