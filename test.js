var asteroidVertices = [];

asteroidVertices.push({x:-1, y:2});
asteroidVertices.push({x:3, y:1});
asteroidVertices.push({x:4, y:-2});
asteroidVertices.push({x:0, y:-3});
asteroidVertices.push({x:-3, y:-2});


var ast0x = -1;
var ast0y = 2;

var ast1x = 3;
var ast1y = 1;

var yShipMinusAst0 = 0 - ast0y;
var xAst1MinusAst0 = ast1x - ast0x;

var xShipMinusAst0 = 0 - ast0x;
var yAst1MinusAst0 = ast1y - ast0y;

var leftSide = yShipMinusAst0*xAst1MinusAst0
var rightSide = xShipMinusAst0*yAst1MinusAst0

var leftMinusRight = leftSide-rightSide;

var pointCompToLine = ((0 - ast0y)*(ast1x - ast0x))-((0 - ast0x)*(ast1y - ast0y));