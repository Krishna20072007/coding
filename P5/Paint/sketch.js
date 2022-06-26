let color, colorR, colorG, colorB;

function setup() {
  createCanvas(windowWidth, windowHeight);
  background(0);
  frameRate(300);
}

function draw() {
  frameRate(300000000000000000000000000);
  colorR = floor(random(0, 255));
  colorG = floor(random(0, 255));
  colorB = floor(random(0, 255));
  stroke(colorR, colorB, colorG);
  line(mouseX, mouseY, pmouseX, pmouseY);
}
