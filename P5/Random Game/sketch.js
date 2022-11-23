let x;
let y;
let mover = 1;

function setup() {
  createCanvas(windowWidth + 1, windowHeight);
  x = width / 2;
  y = height / 2;
  col = random(0, 255);
  background(255 - col);
  stroke(col);
  fill(col);
}

function draw() {
  ellipse(x, y, 50);

  keyPressed();
  bounce();
}

function keyPressed() {
  if (key === "w") {
    y -= mover;
  } else if (key === "s") {
    y += mover;
  } else if (key === "a") {
    x -= mover;
  } else if (key === "d") {
    x += mover;
  }
}

function bounce() {
  if (y < 0) {
    y = 0;
  } else if (y > height) {
    y = height;
  } else if (x < 0) {
    x = 0;
  } else if (x > width) {
    x = width;
  }
}
