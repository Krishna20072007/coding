var path = [];
var angle = 0;
var resolution = 100;
var sun;
var end;
let cansize = 1000;

function setup() {
  createCanvas(cansize, cansize);
  sun = new Orbit(width / 2, height / 2, width / 4, 0);
  var next = sun;
  for (var i = 0; i < 10; i++) {
    next = next.addChild();
  }
  end = next;
}

function draw() {
  background(0);

  for (var i = 0; i < resolution; i++) {
    var next = sun;
    while (next != null) {
      next.update();
      next = next.child;
    }
    path.push(createVector(end.x, end.y));
  }

  var next = sun;
  while (next != null) {
    next.show();
    next = next.child;
  }

  beginShape();
  stroke(255, 255, 255);
  noFill();
  for (var pos of path) {
    vertex(pos.x, pos.y);
  }
  endShape();
}
