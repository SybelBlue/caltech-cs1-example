"""Your app manages online gift cards for a soon-to-be-major e-tailer.
Customers can use the app to place orders using their card
balance. <br /><br />

We have classes that model the GiftCard and the Customer.  First you
will write tests for the GiftCard class, to verify that: <br /><br />

* a GiftCard when first created has a non-negative cash balance <br />
* a GiftCard created with a positive amount sets balance accordingly <br />
* a GiftCard created with a negative amount raises an ArgumentError <br />

System Under Test:
<pl-code language="ruby">
<![CDATA[
  class GiftCard
    attr_reader :balance, :error
    def initialize(balance)
      if @balance < 0
        raise ArgumentError.new("New gift card cannot have negative balance")
      end
      @balance = balance
      @error = nil
    end
  end
]]>
</pl-code>
"""


{"pre": "describe GiftCard do\n", "lines": "it 'fails with negative balance' do\n  expect { GiftCard.new(-1) }.to raise_error(?ArgumentError?)\nend\nit 'succeeds with positive balance' do\n  gift_card = GiftCard.new(20)\n  ?expect?(gift_card.balance).to ?eq?(20)\nend\n", "post": "end\n"}

