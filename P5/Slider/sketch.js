let w = 0;

function setup() {
  createCanvas(400, 400);
}

function draw() {
  background(0);
  stroke(255);
  rectMode(CENTER);
  rect(width / 2, height / 2, w, 10, w);
  if (w < width / 2 - 5) {
    w++;
  }
}
