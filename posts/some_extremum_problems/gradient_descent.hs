
data DiffFnR2 = DiffFnR2 {
  fn :: (Double, Double) -> Double,
  fn_x :: (Double, Double) -> Double,
  fn_y :: (Double, Double) -> Double
}

vminus :: (Double, Double) -> (Double, Double) -> (Double, Double)
vminus (a,b) (c,d) = (a-c, b-d)

mult :: Double -> (Double, Double) -> (Double, Double)
mult s (a,b) = (s * a, s * b)

grad :: DiffFnR2 -> (Double, Double) -> (Double, Double)
grad (DiffFnR2 _ fx fy) point = (fx point, fy point)

-- x_n+1 = x_n `vminus` step_n * grad x_n
gradD :: DiffFnR2 -> Double -> (Double, Double) -> (Double, Double)
gradD f step point = point `vminus` ( step `mult` (grad f point) )


surf1 = DiffFnR2 {
    fn = \(x,y) -> 2*(x**2) + y**2 + 8*x - 6*y + 20,
    fn_x = \(x,y) -> 4*x + 8,
    fn_y = \(x,y) -> 2*y - 6
  }

go :: IO (Double, Double)
go = do
  let guess = (-4,2)
  go2 guess

go2 :: (Double, Double) -> IO (Double, Double)
go2 g = do
  putStrLn $ show g
  let np1 = gradD surf1 0.1 g
  pk <- getLine
  go2 np1


