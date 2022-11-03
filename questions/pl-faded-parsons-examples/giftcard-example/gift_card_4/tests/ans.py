{"pre": "describe Customer do\n  it 'buys the item if balance covers payment' do\n", "lines": "@loaded_gift_card = double('gift_card') #0given\nallow(@loaded_gift_card).to receive(?:withdraw?).and_return(true)\n@customer = ?Customer?.new('Student', @fake_gift_card)\nexpect(?@customer?).to receive(?:notify?).with(\"payment successful\")\n@customer.?pay?(10)\n", "post": "  end\nend\n"}

