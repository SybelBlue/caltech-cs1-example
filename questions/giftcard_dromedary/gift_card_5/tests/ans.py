describe Customer do
  describe 'trying to buy' do

before(:each) do #0given
  @loaded_gift_card = double('gift_card')
  @customer = Customer.new('Student', @fake_gift_card)
end
it 'succeeds if balance covers payment' do
  allow(@loaded_gift_card).to receive(:withdraw).and_return(true)
  expect(@customer).to receive(:notify).with("payment successful")
  @customer.pay(10)
end
it 'fails if balance does not cover payment' do
  allow(@loaded_gift_card).to receive(:withdraw).and_return(nil)
  expect(@customer).to receive(:notify).with("purchase cannot be completed")
  @customer.pay(10)
end

  end
end
