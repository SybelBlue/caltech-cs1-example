describe 'LuckyNumber' do
    it 'should be defined' do
        expect { LuckyNumber }.not_to raise_error
    end

    it 'can win on 42' do
        @lucky_number = LuckyNumber.new()
        allow(@lucky_number).to receive(:generate).and_return(42)
        expect(@lucky_number.test_my_luck).to be true
    end

    it 'can will lose on not 42' do
        @lucky_number = LuckyNumber.new()
        allow(@lucky_number).to receive(:generate).and_return(32)
        expect(@lucky_number.test_my_luck).to be false
    end

end