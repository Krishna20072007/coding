let angle = 0;
let colorR, colorG, colorB;

function setup() {
  createCanvas(400, 400);
  background(0);
}

function draw() {
  colorR = floor(random(0, 255));
  colorG = floor(random(0, 255));
  colorB = floor(random(0, 255));

  colorpack = color(colorR, colorG, colorB);

  angleMode(DEGREES);
  frameRate(60000);
  smooth()
  stroke(colorpack);
  translate(width / 2, height / 2);
  rotate(angle);
  line(0, 0, 0, -height / 2);
  angle += 0.1;
  noSmooth()
}
