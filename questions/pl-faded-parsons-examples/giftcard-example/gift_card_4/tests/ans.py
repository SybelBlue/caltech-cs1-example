describe Customer do
  it 'buys the item if balance covers payment' do

@loaded_gift_card = double('gift_card') #0given
allow(@loaded_gift_card).to receive(:withdraw).and_return(true)
@customer = Customer.new('Student', @fake_gift_card)
expect(@customer).to receive(:notify).with("payment successful")
@customer.pay(10)

  end
end
