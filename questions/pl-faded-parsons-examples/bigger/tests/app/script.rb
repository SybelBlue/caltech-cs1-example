def withdraw(amount)
    if @balance >= amount
      @balance -= amount
    else
      @error = "Insufficient balance"
    end
  end
end