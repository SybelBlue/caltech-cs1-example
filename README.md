This is a copy of https://github.com/ace-lab/pl-ucb-csxxx used to develop FPP questions for software testing with rspec. 

# Starting PL with autograder support

```
export HOST_JOBS_DIR=/tmp/directory/for/autograder/jobqueue
sudo docker run -it --rm \
    -p 3000:3000 \
    -v "$HOST_JOBS_DIR":"/jobs" \
    -v `pwd`:/course \
    -v /var/run/docker.sock:/var/run/docker.sock \
    prairielearn/prairielearn:latest
```
# Thoughts on gradient of test writing

## Testing a pure leaf function (single expectation per spec)

`expect(expr).to `_matcher_  (or `not_to` _matcher_):
* `eq`
* `be >`, `be <`, etc
* `be_truthy` (or falsy)

Strings: Exercise matchers for `match(/regex/)`, `start_with(string)` (or
`end_with`)

Collections: `expect(collection).to` :
*  `be_empty`
* `include(elt)`
* `match_array(['order','doesnt','matter'])`
* `have_key(key)` (for hashes)

## Testing a function that calls a helper

`allow(:object).to ` (or `expect(:object).to`):
* `receive(:method_call)`
* `receive(:method_call).and_return(expr)`

## Multiple specs that share a before-block

## Testing a side effect

`expect { operation }.to `:
* `change { expr }`
* `change { expr }.by(qty)`
* `change { expr }.from(val).to(val)`
* `raise_error(SomeError)`

## Doubles using instance_double (makes sure instance calls its private method the right way)


# Micropilot structure and thoughts

- Read/view lecture/notes
- pre-test (AF can come up with some of this)
- finger exercises (see below)
- exercise sequence (see below)
- post-test 

## Finger exercises

In Armando's ideal world, BEFORE doing the exercise sequence below,
there would be numerous "finger exercises" to practice writing very
short and focused specs for asserting return values, error raising,
etc.  Maybe some undergrads can be recruited to help with these.
Armando will reach out via CS169 GSIs to see if interest.

## Exercise sequence

(todo) Fix Wallet class so that it raises error only when constructor gets
negative value. Withdrawing too much should return falsy and capture the error somehow.

Part 1:  develop tests for Wallet 

- test happy path of leaf function `withdraw`
- test sad path - error string gets set, and balance does not change 
   - 2 specs that can share a before-block
- test for raising error in constructor


```ruby
class Wallet
  attr_reader :cash
  def initialize(amount)
    raise ArgumentError if amount < 0
    @cash = amount
  end
  def withdraw(amount)
    # raise InsufficientFundsError if amount > @cash
    #  => return nil and have an error string attribute
    @cash -= amount
    return amount
  end
end
```

Part 2: Wallet code is replaced with rdoc-like description of Wallet,
now we write tests for Customer.


attempt_delivery motivates the use of a method stub (to force a return value from
Wallet#withdraw, whose implementation is now invisible) and also checking whether
Customer#deliver_paper gets called or not.  And you can have a separate spec to then
check that Wallet#cash has changed to the right value as a result.
Or even something like
`expect { Customer.attempt_delivery(amt) }.to change { Customer.wallet.cash }.by(amount)`

```ruby
class Customer
  def initialize(wallet)
    @wallet = wallet
    @error = ''
  end
  def attempt_delivery(amount)
    if @wallet.withdraw(amount)
      self.deliver_paper
    else
      @error = "Not enough money"
    end
  end      
end
```

