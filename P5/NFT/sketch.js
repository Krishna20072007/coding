let square_canvas = 500;

function setup() {
  createCanvas(square_canvas, square_canvas);
  strokeWeight(random(square_canvas / 100, square_canvas / 50));
  bg();
  mouth();
  eye();
  nose();
  ellipse(width / 2, height / 2, width - 50);
}

function bg() {
  background(random(255), random(255), random(255));
}

function mouth() {
  angleMode(DEGREES);
  noFill();
  arc(
    width / 2,
    height / 1.75,
    (width / 2) * 1.5,
    height / 1.75,
    random(340, 380),
    random(160, 200)
  );
}

function eye() {
  noFill();
  let eye_one = new circ(
    width / 3,
    height / 3,
    width / random(3, 5),
    height / random(3, 5)
  );
  let pupil_one = new circ(width / random(3, 5));
  let iris_one = ellipse((width * 2) / 3, height / 3, width / random(6, 11));

  let eye_two = new circ(
    (width * 2) / 3,
    height / 3,
    width / random(3, 5),
    height / random(3, 5)
  );
  let pupil_two = new circ(width / random(3, 5));
  let iris_two = ellipse(width / 3, height / 3, width / random(6, 11));

  eye_one.show();
  pupil_one.show();

  eye_two.show();
  pupil_two.show();
}

function nose() {
  line(
    width / 2,
    height / 2 + random(height / 50, height / 10),
    width / 2,
    height / 2 - random(height / 50, height / 10)
  );
}

class circ {
  constructor(x, y, w, h) {
    this.x = x;
    this.y = y;
    this.w = w;
    this.h = h;
  }

  show() {
    noFill();
    ellipse(this.x, this.y, this.w, this.h);
  }
}
