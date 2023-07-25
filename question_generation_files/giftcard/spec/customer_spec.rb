require_relative '../lib/gift_card.rb'
require_relative '../lib/customer.rb'
describe Customer do
  describe 'trying to buy' do
    before(:each) do  ## SC
      @loaded_gift_card = double('gift_card')
      @customer = Customer.new('Student', @loaded_gift_card)
    end ## SC
    it 'succeeds if balance covers payment' do  ## SC
      allow(@loaded_gift_card).to receive(:withdraw).and_return(true)  ## SC
      expect(@customer).to receive(:notify).with("payment successful")  ## SC
      @customer.pay(10)  ## SC
    end  ## SC
    it 'fails if balance does not cover payment' do
      allow(@loaded_gift_card).to receive(:withdraw).and_return(nil)
      expect(@customer).to receive(:notify).with( "purchase cannot be completed")  ## SC
      @customer.pay(10)  ## SC
    end
  end 
end

  
  
