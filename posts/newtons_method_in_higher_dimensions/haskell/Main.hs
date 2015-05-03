
type R = Double

type R2 = (R, R)

type M_2x2 = ((R, R),
              (R, R))

-- | vector subtraction
(<->) :: R2 -> R2 -> R2
(<->) (a,b) (c,d) = (a-c, b-d)

-- | matrix vector multiplication
(<@>) :: M_2x2 -> R2 -> R2
(<@>) ((a, b), (c, d)) (x, y) = ( a*x + b*y, c*x + d*y )

-- | multiply a scalar by each component of a matrix
(<**>) :: R -> M_2x2 -> M_2x2
(<**>) s ((a, b), (c, d)) = ((s * a, s * b), (s * c, s * d))

-- | task is to solve this system of equations
-- a) x^2 + y^2 - 10 = 0
-- b) 2x  + y   - 1  = 0

f1 :: R2 -> R
f1 (x, y) = x**2 + y**2 - 10

f2 :: R2 -> R
f2 (x, y) = 2*x + y - 1

-- | partial derivatives of f1 and f2
f1_x :: R2 -> R
f1_x (x, y) = 2*x

f1_y :: R2 -> R
f1_y (x, y) = 2*y

f2_x :: R2 -> R
f2_x (x, y) = 2

f2_y :: R2 -> R
f2_y (x, y) = 1

-- | we can package these two equations into a new function
f :: R2 -> R2
f a = (f1 a,
       f2 a)

-- |  determinate of 2x2 matrix
det :: M_2x2 -> R
det ((a, b), (c, d)) = (a*d) - (b*c)

-- | adjuct of 2x2 matrix
adj :: M_2x2 -> M_2x2
adj ((a, b), (c, d)) = ((d, - b), (- c, a))

-- | jacobi matrix at (x,y)
jacobi :: R2 -> M_2x2
jacobi a = ((f1_x a, f1_y a),
            (f2_x a, f2_y a))

-- | inverse of jacobi matrix at (x,y)
jacobi_inv :: R2 -> M_2x2
jacobi_inv a = (1 / det j) <**> adj j
  where j = jacobi a

newton :: R2 -> R2
newton n = n <-> ( jacobi_inv n <@> f n )


go :: R2 -> IO R2
go guess = go2 guess

go2 :: R2 -> IO R2
go2 g = do
  putStrLn $ show g
  let np1 = newton g
  pk <- getLine
  go2 np1
