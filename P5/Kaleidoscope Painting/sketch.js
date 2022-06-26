let d, sw, angle;
let num = 12;

let off = 0;

function setup() {
  createCanvas(windowWidth, windowHeight);
  background(0);
  angleMode(DEGREES);
  colorMode(HSB, 255, 255, 255);
}

function draw() {
  let hu = noise(off) * 255;
  off += 0.1;
  
  translate(width / 2, height / 2);
  
  mx = mouseX - width / 2;
  my = mouseY - height / 2;
  pmx = pmouseX - width / 2;
  pmy = pmouseY - height / 2;

  if (mouseIsPressed) {
    angle = 360 / num;
    stroke(hu, 255, 255, 100);
    for (let i = 0; i < num; i++) {
      rotate(angle);
      strokeWeight(4);
      line(mx, my, pmx, pmy);
      console.log(hu);
    }
  }
}
