let blockImg;
let block1;
let block2;
let clack;

let count = 0;
// let digits = Math.floor(Math.random() * 11);
let digits = 10;
let timeSteps = 10 ** (digits - 3);
let countDiv;

function preload() {
  blockImg = loadImage("block.png");
  clack = loadSound("Clack.wav");
}

function setup() {
  createCanvas(windowWidth + 1, 150);
  block1 = new Block(100, 20, 1, 0, 0);
  const m2 = pow(100, digits - 1);
  block2 = new Block(200, 100, m2, -1 / timeSteps, 20);
  countDiv = createDiv(count);
  countDiv.style("font-size", "72pt");
}

function draw() {
  background(0);

  let clackSound = false;

  for (let i = 0; i < timeSteps; i++) {
    if (block1.collide(block2)) {
      const v1 = block1.bounce(block2);
      const v2 = block2.bounce(block1);
      block1.v = v1;
      block2.v = v2;
      clackSound = true;
      count++;
    }

    if (block1.hitWall()) {
      block1.reverse();
      clackSound = true;
      count++;
    }

    block1.update();
    block2.update();
  }

  if (clackSound) {
    clack.play();
  }
  block1.show();
  block2.show();

  countDiv.html(nf(count, digits));
}