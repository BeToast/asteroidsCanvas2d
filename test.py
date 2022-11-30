import plotly.graph_objects as go

xs = [-1, 3, 4, 0, -3]
ys = [2, 1, -2, -3, -2]

fig = go.Figure(go.Scatter(x=xs, y=ys, fill="toself"))

fig.show()

# setupt completed

shipX = 0
shipY = 0

for i in range(0,5):
  ast0x = xs[i]
  ast0y = ys[i]

  if(i < 4):
    j = i+1
  else:
    j = 0

  ast1x = xs[j]
  ast1y = ys[j]

  yShipMinusAst0 = shipY - ast0y
  xAst1MinusAst0 = ast1x - ast0x

  xShipMinusAst0 = shipX - ast0x
  yAst1MinusAst0 = ast1y - ast0y

  leftSide = yShipMinusAst0*xAst1MinusAst0
  rightSide = xShipMinusAst0*yAst1MinusAst0

  leftMinusRight = leftSide-rightSide

  pointCompToLine = ((shipY - ast0y)*(ast1x - ast0x))-((shipX - ast0x)*(ast1y - ast0y))
  print(pointCompToLine)

