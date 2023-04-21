"""Write a function <code>det</code> that calculates the determinant of a 
2 by 2 matrix of the form,
ie, evaluate 
$$\bf M = 
    \begin{bmatrix} 
        a & b \\ 
        c & d 
    \end{bmatrix}
$$"""


def det(a, b, c, d)
  ?a * d - b * c?
end

## test ##
describe "det" do
  it "returns 0 on non-invertible matrix" do
    expect(det(1, 1, 0, 0)).to eq(0)
  end
end
## test ##

