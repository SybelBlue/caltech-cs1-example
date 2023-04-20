class lucky_number_game

    def initialize()
    end

    def test_my_luck
        return generate() == 42
    end

    def generate    
        rand(1000)
    end


end