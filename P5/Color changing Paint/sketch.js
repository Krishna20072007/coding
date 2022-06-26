let c;
let r = 255;
let g = 255;
let b = 255;
let a = 0;

function setup() {
  createCanvas(windowWidth, windowHeight);
  background(0);
}

function draw() {
  noStroke();
  c = color(r, g, b, a);
  fill(c);
  ellipse(mouseX, mouseY, 16);
}

function mousePressed() {
  r = floor(random(0, 255));
  g = floor(random(0, 255));
  b = floor(random(0, 255));
  //a = floor(map(mouseX, 0, width, 0, 255));
  a = floor((r + g + b) / 3) + ceil((r + g + b) / 3) / 2;

  console.log(r, g, b, a);
}
