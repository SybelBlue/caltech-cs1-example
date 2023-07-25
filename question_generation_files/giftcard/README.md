# Instructor info: Faded Parsons sequence for Gift Card Spec 

This multipart exercise starts by having the student develop simple unit
tests for pure leaf functions (constructor & public method of a very
simple GiftCard class), then proceeds to introduce test doubles to
develop unit tests for a Customer class that depends on the GiftCard
class to make a purchase.

`lib/` and `spec/` contain the complete, runnable code and tests
(i.e. effectively a reference solution). You   can verify the tests run
by doing `rspec -fd spec` in their common parent directory.  

When the question is presented, it's done in 5 parts:

1. Write tests for the `GiftCard` constructor that verify successful
creation (nonnegative balance) and failed creation (negative
balance).  **Learning objective (LO):** write simple specs that test a
single behavior each.

2. Add tests that verify a successful withdrawal returns success,
changes the card balance, and does not produce an error message.
**LO:** understand why it's necessary to use braces to create a
callable for `it` for a test that would otherwise raise an exception.

3. DRY out by grouping common preconditions for the existing specs.
**LO:** use a `before` block to group common precondition setup for
multiple specs.

4. Test a method `Customer#pay` that depends on `GiftCard#withdraw`,
but without relying on the implementation of the latter. **LO:** Use a
method double to force a return value from a helper method in a test,
rather than calling the actual implementation of the helper method.

5. Finish the sad path for `Customer#pay`, and again group common
preconditions using `before` blocks.

The `infoAssessment.json` sequences these parts in fixed order and
requires the student to get 100% on each part before going on to the
next.  At each step, work completed in previous steps becomes part of the
static code displayed on the screen, and the student develops new code in a
vertically-laid-out FPP panel that is correctly inlined/interleaved
with that static code.

## Reference SUT and solution - will not be part of the student-visible scaffolding:

* system under test: [GiftCard](lib/gift_card.rb) and [Customer](lib/customer.rb)
* reference specs: [GiftCard](spec/gift_card_spec.rb) and [Customer](spec/customer_spec.rb)

I'm using names like `gift_card_spec.1.rb`, `gift_card_spec.2.rb`, etc
to show what i hope the UX looks like in each phase.  In those files,
I separate into "regions" the parts that should be static text
displayed to the student vs the part that should be the FPP panel.
The end-of-line comment `## SC` means scaffolding (starter code, ie
this line is given in its correct place in the FPP panel).

# STUDENT-FACING INSTRUCTIONS START HERE

## Intro to Test Writing Using RSpec

This assignment introduces unit testing with RSpec.  

In ESaaS, we normally promote test-driven development (TDD), in
which you first write failing tests and then write the code to make
tests pass.  In this exercise, we'll do it the other way
around---giving you existing code that works correctly, and asking you
to construct tests for it---because the goal is to get you familiar
with the mechanics of test 
writing using RSpec.

Rather than
writing test code from scratch, you will solve Faded Parsons Problems, in
which you rearrange scrambled lines of code, possibly filling  in
blanks in some of the lines, to create necessary test cases.

1) You will first create some simple _examples_ (unit tests for
specific behaviors)  that illustrate the basic
pattern that all unit tests follow: Arrange, 
Act, Assert (AAA).  These first few tests will exercise a pure leaf
function: it has no side effects and relies on no other external
functions to do its work.

2) You will then create some more complex examples
 in which additional actions are required as part of the
Arrange part of the AAA pattern.
In particular, you will create some tests that use _test doubles_ such as
mock objects or method stubs 
to isolate the code being tested from its dependencies.

3) You will learn how grouping related tests together using 
`describe` blocks lets them 
share common Arrange steps such as setting up test doubles.

## Learning Goals

When you finish this assignment, you should be able to:

* Explain how the Arrange-Act-Assert programming pattern 
forms the underlying structure of all unit tests.

* Explain the basic mechanisms involved in realizing the
Arrange-Act-Assert steps in unit tests: expectations,
mock objects (object doubles), method stubs (method doubles).

* Recognize which of these mechanisms are necessary in a particular
unit testing scenario.

* Write unit tests for Ruby and Rails code using the RSpec testing
framework's facilities that provide these mechanisms.

* Use `describe` blocks to group together related examples that share
Arrange and/or Act steps.

# Part 0: Preparation and background

In addition to solid Ruby knowledge, you should have read at least
sections 8.1--8.3 of _ESaaS_ (2nd 
edition) and/or watched the accompanying video segments.

[TBD: in the future there will be a few "check your understanding"
questions here from that material]


## Background: Gift cards and customers

Your app manages online gift cards for a soon-to-be-major e-tailer.
Customers can pay for orders using their card
balance. 

We have simple classes that partially model the `GiftCard` and the `Customer`.  First you
will write tests for the GiftCard class, to verify that:

* a GiftCard can only be created with a non-negative cash balance
* a withdrawal when there is enough cash returns success, and changes
the card balance
* a withdrawal when there is not enough cash returns failure, provides
an error message explaining the failure, and does not change the card balance.

Once those tests are done, the main thing we want to test for Customer is what happens when they
try to buy an item.  

* If they have enough money on their gift card, the item is bought, and their card
balance goes down
* If not, the item is not bought, a helpful error message saves the
reason why, and the card balance doesn't change.

But in testing Customer, we will "seal off" the (now well-tested) GiftCard class
and rely only on the description
of its methods and their behaviors-- not their _implementation_.
This setup mimics a common scenario where you are testing your own
code that calls some code in a library you don't control,
or calls an external API,
so you need to be able to
test your code in isolation from the implementation of the library.



# 1. testing GiftCard creation

Take a look at `gift_card.rb` to understand the code you're writing
tests for.  The first task is to test gift card creation.  When a gift
card is created with a nonnegative balance, the operation should succeed
and the gift card's balance should be set to that value.  When a gift
card is created with a negative balance, creation should fail and an
`ArgumentError` exception should be raised.

Solve FPP#1 (Faded Parsons Problem #1) to create these tests.  The
autograder will attempt validate your test cases by injecting bugs
into the GiftCard code that should cause your tests to selectively
fail.

Self-check: Why is the syntax different for `expect` in the two tests?
(Hint: how does Ruby evaluate an expression that has `{ braces }`?)

# 2. testing withdrawals

If a gift card has enough funds to handle a withdrawal, then its
`#withdraw` method should return a truthy value, and the new balance
should reflect the withdrawal.

If funds are insufficient, the balance should not change, and an error
message should be stored in the `error` attribute of the gift card
instance.

Solve FPP#2 to add these tests.  **NOTE:** remember that to test gift
card withdrawal, you have to create a gift card from which to
withdraw.  So each of your tests should include the creation of a gift
card as part of its "Arrange" phase.

In the regular TDD workflow of "red-green-refactor", red represents
tests that fail because there is no code, and green (where you are
once this step is complete) represents tests that pass because the
code is correct.  Refactoring will be next.


# 3. factoring out common code

You may have noticed in part 2 that there was code being repeated for
the Arrange phase of 3 of your tests.  In this part, solve FPP#3 to
collect this common code into a `before(:each)` block, which gets
executed before _every test in that group_.  This is the refactor
phase of "red-green-refactor", in which examples sharing common code
are grouped together and that common code is extracted and DRY'd out.

# 4. Testing customer while stubbing gift card

Take a look at `customer.rb` and the `#pay` method, which is the
subject of the next set of tests that you will construct in FPP#4.

The new challenge in testing
`#pay` is that it calls an instance method of another class
(`GiftCard#withdraw`).  In this case we know all about the behavior of
that method, and it's fairly simple.  But if
don't know the details of how it works, or even worse if it's
temporarily broken, we don't want our tests to fail just because
`#withdraw` is failing.  So we use _test doubles_ to isolate the
`Customer` tests from the behavior of `GiftCard`.

If you look at `Customer#pay`, the only behavior we really care about
regarding `#withdraw` is whether it returns a truthy or falsy value,
since that determines what happens next.  FPP#4 guides you through
building a single test case in which we construct a _test double_ for
a gift card.  The double is an object that has no built-in behaviors,
so it must be given just enough behavior to be useful
for this test case: we use `allow` to say "If the double gets a call
to `withdraw`, it should just return true".  Similarly, if `#pay` is
working correctly, the result of a successful withdrawal should be a
call to `Customer#notify` with a happy message.  Note that in this
case, `Customer#notify` _hasn't even been implemented_!  By saying
that we expect to receive a call to it with a particular argument, we
basically "short-circuit" the real method call.  This further isolates
our test case from other methods, even those in `Customer` itself.

# 5. Using the double to also test failed purchases

Finally, for FPP#5, we use the same double, but this time we instruct it to
always return a falsy value so we can test the other code path in
`#pay`.  Since setting up the double (and the `Customer` instance) are
common to both test cases, we move them into a `before` block as we
did with `GiftCard`, and group the related examples and their
before-block in a `describe`.

