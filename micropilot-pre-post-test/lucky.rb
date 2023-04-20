class Lucky

    attr_accessor :secret

    def initialize(secret)
      @secret = secret
      raise ArgumentError if @secret < 0 || @secret > 999
    end

    def feeling_lucky
        generate() == @secret
    end

    def generate    
        rand(1000)
    end
end