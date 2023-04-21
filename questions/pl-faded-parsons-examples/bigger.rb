"""
This is an example of a larger project. <br />
<br />
There is a number of files that need to be populated. <br />
<br />
The current approach is to specify each of those files in the source
"""

class GiftCard #0given
  attr_reader :balance, :error #1given
  def initialize(balance) #1given
    if balance ?< 0?
      raise ArgumentError.new("New gift card cannot have negative balance")
    end
    @balance = balance
    @error = nil
  end #1given



## setup_code ##
  def withdraw(amount)
    if @balance >= amount
      @balance -= amount
    else
      @error = "Insufficient balance"
    end
  end
end
## setup_code ##

## tests/app/customer.rb ##
class Customer
  attr_accessor :name, :gift_card
  def initialize(name, gift_card=nil)
    @gift_card = gift_card
    @name = name
  end
  def pay(amount)
    if gift_card.withdraw(amount)
      self.notify("payment successful")
    else
      self.notify("purchase cannot be completed")
    end
  end
end

## tests/app/customer.rb ##

## test ##
describe GiftCard do
    
    it 'fails with negative balance' do
      expect { GiftCard.new(-1) }.to raise_error(ArgumentError)
    end

    it 'succeeds with positive balance' do
      gift_card = GiftCard.new(20)
      expect(gift_card.balance).to eq(20)
    end

    it 'has a test that trivially passes' do
    end

end
## test ##