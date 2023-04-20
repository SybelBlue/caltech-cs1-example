require_relative './lucky.rb'

describe 'LuckyNumber' do
    it 'should be defined' do
        expect { Lucky }.not_to raise_error
    end

    it 'should set a valid secret' do
        @lucky_number = Lucky.new(50)
        expect(@lucky_number.secret).to eq(50)
    end

    it 'should reject invalid secret' do
        expect { Lucky.new(-1) }.to raise_error(ArgumentError)
    end

    it 'can win on 42' do
        @lucky_number = Lucky.new(42)
        allow(@lucky_number).to receive(:generate).and_return(42)
        expect(@lucky_number.feeling_lucky).to be true
    end

    it 'can will lose on not 42' do
        @lucky_number = Lucky.new(42)
        allow(@lucky_number).to receive(:generate).and_return(32)
        expect(@lucky_number.feeling_lucky).to be false
    end

end