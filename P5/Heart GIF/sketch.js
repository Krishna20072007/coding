const heart = [];
const totalFrames = 240;
let counter = 0;
let r = Math.random() * 256;
let g = Math.random() * 256;
let b = Math.random() * 256;
let bright = (r + g + b) / 3;

function setup() {
  createCanvas(windowWidth, windowHeight - 1);
}

function draw() {
  const percent = float(counter % totalFrames) / totalFrames;
  render(percent);
  counter++;
}

function render(percent) {
  background(bright);
  translate(width / 2, height / 2);
  stroke(256 - bright);
  strokeWeight(4);
  fill(r, g, b, 256 - bright);
  beginShape();
  for (let v of heart) {
    const a = map(percent, 0, 1, 0, TWO_PI * 4);
    const r = map(sin(a), -1, 1, height / 80, height / 40);
    vertex(r * v.x, r * v.y);
  }
  endShape();

  if (percent < 0.5) {
    const a = map(percent, 0, 0.5, 0, TWO_PI);
    const x = 16 * pow(sin(a), 3);
    const y = -(13 * cos(a) - 5 * cos(2 * a) - 2 * cos(3 * a) - cos(4 * a));
    heart.push(createVector(x, y));
  } else {
    heart.splice(0, 1);
    window.location.reload();
  }
}
