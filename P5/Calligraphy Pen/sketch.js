function setup() {
  createCanvas(windowWidth, windowHeight);
  background(0);
}

function draw() {
  locate = mouseX;
  colorr = map(locate, 0, width, 0, 255);
  locatee = map(locate, 0, width, 1, 32);

  stroke(colorr);
  strokeWeight(locatee);
  line(mouseX, mouseY, pmouseX, pmouseY);
}
