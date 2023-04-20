A class representing a book, with an `ISBN` and a `price`, is defined below. The constructor accepts and sets these fields, raising an error for a blank `ISBN` or negative `price`. Getter and setter methods are generated by `attr_accessor` for `ISBN` and `price`. The `price_as_string` method returns the `price` formatted with a dollar sign and two decimal places.

## System Under Test
```ruby
class Book

  # generates getter and setter methods for ISBN and price
  attr_accessor :isbn, :price
  
  # A book must have a nonblank ISBN and a price greater than zero
  def initialize(isbn, price)
    @isbn = isbn
    @price = price
    raise ArgumentError if @isbn.empty? || @price <= 0
  end

  # Return price as a formatted string with leading $ and 2 decimal places
  def price_as_string
    sprintf "$%.2f", self.price
  end
end
```

## Write rspec unit tests for the `Book` class
Write a suite of rspec unit tests to verify the desired behavior of the `Book.new` constructor and the `price_as_string` method. A reference sheet for basic rspec syntax is provided.