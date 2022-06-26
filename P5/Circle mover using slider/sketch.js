let sliderX;
let sliderY;
let coord;

function setup() {
  createCanvas(400, 400);
  sliderX = createSlider(-200, 200, 0);
  sliderY = createSlider(-200, 200, 0);
}

function draw() {
  coord = createVector(sliderX.value(), sliderY.value())
  frameRate(60);
  translate(width / 2, height / 2);
  background(255);
  fill(0);

  ellipse(coord.x, coord.y, 64);
}
