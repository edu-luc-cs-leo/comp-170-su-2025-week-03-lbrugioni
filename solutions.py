def solve_quadratic(a: float, b: float, c: float) -> None:
  """Basic solution to the quadratic equation. The equation
  a*x*x + b*x + c = 0
  has solutions in the real numbers if its discriminant is not negative.
  The discriminant is the quantity b*b-4*a*c. The function below computes
  the discriminant first. It then checks its sign -- if it's negative, the
  function prints "no real solutions" and stops. If the discriminant is not
  negative, the function computes the two solutions for the equation and 
  prints them. """
  # Compute the discriminant -- it's important to determine if the equation 
  # has no real solutions
  discriminant = b * b - 4 * a * c
  # Check for real solutions
  if discriminant < 0:
    print ("no real solutions")
  else:
    # Group common operations together
    common_factor = math.sqrt(discriminant)/(2*a)
    x1 = - b + common_factor # alternative x1 = (-b + math.sqrt(discriminant))/(2*a)
    x2 = - b - common_factor # alternative x2 = (-b - math.sqrt(discriminant))/(2*a)
    print(f"{x1=}\n{x2=}")
  
# Basic testing
solve_quadratic(1,2,3)
solve_quadratic(1,5,1)
greet_friends(my_friends)
