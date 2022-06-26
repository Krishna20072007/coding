// No Draw!!

var hue;
var rainbow = true;
var rate = 4;

function setup() {
  createCanvas(windowWidth, windowHeight);
  background(0);
  hue = 0;
}

function mouseDragged() {
  if (rainbow) {
    if (hue > 360) {
      hue = 0;
    } else {
      hue += rate;
    }
  }
  colorMode(HSL, 360);
  noStroke();
  fill(hue, 200, 200);
  ellipse(mouseX, mouseY, 25, 25);
}

function clearCanvas() {
  createCanvas(width, height);
}
